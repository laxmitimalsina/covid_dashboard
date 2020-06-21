import json
from nep_stats.covid.db.models import (Country,
                                       Province, District,
                                       Municipality, Ward, CovidCase, QuarantineInfo)
from nep_stats.utils import LoggerMixin


class DatabaseLoader(LoggerMixin):
    def __init__(self, session_scope):
        self.session_scope = session_scope

    def get_entities_from_api(self, offset, limit):
        raise NotImplementedError()

    def get_existing_entities_from_db(self):
        """Returns a list of dict"""
        return []

    def convert_to_db_model(self, entity):
        raise NotImplementedError()

    def _get_all_entities(self):
        limit = 500
        offset = 0
        output = []

        self.logger.info(f"fetching using limit {limit}, offset {offset}")
        results = self.get_entities_from_api(offset=offset, limit=limit)
        output.extend(results)

        while len(results) > 0:
            offset = offset + limit
            self.logger.info(f"fetching using limit {limit}, offset {offset}")
            results = self.get_entities_from_api(offset=offset, limit=limit)
            output.extend(results)
        return output

    def _get_new_entities(self):

        self.logger.info("Fetching entities from API")
        incoming = self._get_all_entities()
        self.logger.info(f"{len(incoming)} Entities from API fetched")

        self.logger.info("Loading existing items from db")
        existing = self.get_existing_entities_from_db()
        self.logger.info(f"{len(existing)} existing from db loaded")
        existing_ids = set(e['id'] for e in existing)

        new_entities = [i for i in incoming if i.id not in existing_ids]
        seen_ids = set()
        output = []
        for entity in new_entities:
            if entity.id in seen_ids:
                continue

            seen_ids.add(entity.id)
            output.append(entity)

        return output

    def load(self):
        with self.session_scope() as sess:
            entities = [self.convert_to_db_model(
                e) for e in self._get_new_entities()]
            sess.add_all(entities)


class CountryDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(Country)]

    def get_entities_from_api(self, offset, limit):
        resp = self.api_client.api_country_list(
            "v1", limit=limit, offset=offset)
        return resp.results

    def convert_to_db_model(self, c):
        return Country(title_en=c.title_en, title_ne=c.title_ne, id=c.id, iso=c.iso)


class ProvinceDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(Province)]

    def get_entities_from_api(self, offset, limit):
        return self.api_client.api_province_list("v1", limit=limit, offset=offset).results

    def convert_to_db_model(self, p):
        title = p.title_en if p.title_en else p.title
        centroid = json.loads(p.centroid.replace("'", '"'))
        return Province(title_en=title, id=p.id, title_ne=p.title_ne, code=p.code, centroid=centroid, bbox=p.bbox)


class DistrictDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(District)]

    def get_entities_from_api(self, offset, limit):
        return self.api_client.api_district_list("v1", limit=limit, offset=offset).results

    def convert_to_db_model(self, p):
        title = p.title_en if p.title_en else p.title
        centroid = json.loads(p.centroid.replace("'", '"'))
        return District(title_en=title, id=p.id, title_ne=p.title_ne, code=p.code, centroid=centroid, bbox=p.bbox, province_id=p.province)


class MunicipalityDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(Municipality)]

    def get_entities_from_api(self, offset, limit):
        return self.api_client.api_municipality_list("v1", limit=limit, offset=offset).results

    def convert_to_db_model(self, m):
        title = m.title_en if m.title_en else m.title
        centroid = json.loads(m.centroid.replace("'", '"'))
        return Municipality(title_en=title, district_id=m.district, type=m.type, id=m.id,
                            title_ne=m.title_ne, code=m.code, centroid=centroid, bbox=m.bbox)


class WardDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(Ward)]

    def get_entities_from_api(self, offset, limit):
        return self.api_client.api_ward_list("v1", limit=limit, offset=offset).results

    def convert_to_db_model(self, w):
        centroid = json.loads(w.centroid.replace("'", '"'))
        return Ward(title_en=w.title, municipality_id=w.municipality, title_ne=w.title, id=w.id, centroid=centroid, bbox=w.bbox, )


class CovidCaseDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(CovidCase)]

    def get_entities_from_api(self, offset, limit):
        return self.api_client.api_covid19_case_list("v1", limit=limit, offset=offset).results

    def convert_to_db_model(self, c):
        case = CovidCase(id=c.id, country_id=c.nationality, province_id=c.province, district_id=c.district,
                         municipality_id=c.municipality, ward_id=c.ward, created_on=c.created_on,
                         modified_on=c.modified_on, reported_on=c.reported_on, label=c.label, gender=c.gender,
                         age=c.age, point=c.point, occupation=c.occupation, recovered_on=c.recovered_on,
                         death_on=c.death_on, current_state=c.current_state, is_reinfected=c.is_reinfected,
                         source=c.source, comment=c.comment, type=c.type, related_to=c.related_to)

        return case


class QuarantineInfoDatabaseLoader(DatabaseLoader):
    def __init__(self, session_scope, api_client):
        super().__init__(session_scope=session_scope)
        self.api_client = api_client

    def get_existing_entities_from_db(self):
        with self.session_scope() as sess:
            return [r._asdict() for r in sess.query(QuarantineInfo)]

    def get_entities_from_api(self, offset, limit):
        resp = self.api_client.api_covid19_quarantineinfo_list(
            "v1", limit=limit, offset=offset)
        return resp.results

    def convert_to_db_model(self, c):
        return QuarantineInfo(id=c.id,
                              province_id=c.province,
                              district_id=c.district,
                              tested_count=c.tested_count,
                              tested_today_count=c.tested_today_count,
                              released_count=c.released_count,
                              ambulance_count=c.ambulance_count,
                              quarantine_bed_count=c.quarantine_bed_count,
                              has_quarantined_sick_food_service=c.has_quarantined_sick_food_service,
                              quarantined_count=c.quarantined_count,
                              quarantined_male_count=c.quarantined_male_count,
                              quarantined_female_count=c.quarantined_female_count,
                              quarantined_sick_count=c.quarantined_sick_count,
                              quarantined_release_count=c.quarantined_release_count,
                              isolated_bed_count=c.isolated_bed_count,
                              isolated_count=c.isolated_count,
                              isolated_male_count=c.isolated_male_count,
                              isolated_female_count=c.isolated_female_count,
                              isolated_sick_count=c.isolated_sick_count,
                              isolated_release_count=c.isolated_release_count,
                              swab_collected_count=c.swab_collected_count,
                              swab_tested_count=c.swab_tested_count,
                              ppe_count=c.ppe_count,
                              relief_provided_count=c.relief_provided_count,
                              relief_provided_today_count=c.relief_provided_today_count,
                              remarks=c.remarks,
                              is_verified=c.is_verified,
                              created_on=c.created_on,
                              modified_on=c.modified_on,
                              reported_on=c.reported_on)
