import enum
import os
import datetime
from sqlalchemy import (
    Table,
    Column,
    String,
    Numeric,
    Boolean,
    Integer,
    JSON,
    select,
    func,
    DDL,
    event,
    Index,
    DateTime,
    MetaData,
    ForeignKey,
    ForeignKeyConstraint,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship, foreign, remote
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.dialects.postgresql as pg

Base = declarative_base()


class Country(Base):

    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, nullable=False)
    iso = Column(String, nullable=True)
    title_en = Column(String, nullable=False)
    title_ne = Column(String, nullable=True)

    def __init__(self, title_en, iso=None, id=None, title_ne=None):
        self.id = id
        self.iso = iso
        self.title_en = title_en
        self.title_ne = title_ne

    def _asdict(self):
        return {
            "id": self.id,
            "iso": self.iso,
            "title_en": self.title_en,
            "title_ne": self.title_ne
        }


class Province(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, nullable=False)
    title_en = Column(String, nullable=False)
    title_ne = Column(String, nullable=True)
    code = Column(String, nullable=True)
    centroid = Column(JSONB, nullable=True)
    bbox = Column(JSONB, nullable=True)

    def __init__(self, title_en, id=None, title_ne=None, code=None, centroid=None, bbox=None):
        self.id = id
        self.title_en = title_en
        self.title_ne = title_ne
        self.code = code
        self.centroid = centroid
        self.bbox = bbox

    def _asdict(self):
        return {
            'id': self.id,
            'title_en': self.title_en,
            'title_ne': self.title_ne,
            'code': self.code,
            'centroid': self.centroid,
            'bbox': self.bbox
        }


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, nullable=False)
    title_en = Column(String, nullable=False)
    title_ne = Column(String, nullable=True)
    code = Column(String, nullable=True)
    centroid = Column(JSONB, nullable=True)
    bbox = Column(JSONB, nullable=True)
    province_id = Column(Integer, ForeignKey(
        "provinces.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)

    def __init__(self, title_en, province_id, id=None, title_ne=None, code=None, centroid=None, bbox=None):
        self.id = id
        self.province_id = province_id
        self.title_en = title_en
        self.title_ne = title_ne
        self.code = code
        self.centroid = centroid
        self.bbox = bbox

    def _asdict(self):
        return {
            'id': self.id,
            'title_en': self.title_en,
            'title_ne': self.title_ne,
            'code': self.code,
            'centroid': self.centroid,
            'bbox': self.bbox,
            'province_id': self.province_id
        }


class Municipality(Base):
    __tablename__ = "municipalities"

    id = Column(Integer, primary_key=True, nullable=False)
    title_en = Column(String, nullable=False)
    title_ne = Column(String, nullable=True)
    code = Column(String, nullable=True)
    centroid = Column(JSONB, nullable=True)
    bbox = Column(JSONB, nullable=True)

    district_id = Column(Integer, ForeignKey(
        "districts.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
    type = Column(String, nullable=False)

    def __init__(self, title_en: str, district_id: int, type: str, id=None, title_ne=None, code=None, centroid=None, bbox=None):
        self.id = id
        self.title_en = title_en
        self.district_id = district_id
        self.type = type
        self.title_ne = title_ne
        self.code = code
        self.centroid = centroid
        self.bbox = bbox

    def _asdict(self):
        return {
            'id': self.id,
            'title_en': self.title_en,
            'title_ne': self.title_ne,
            'code': self.code,
            'centroid': self.centroid,
            'bbox': self.bbox,
            'district_id': self.district_id,
            'type': self.type,
        }


class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True, nullable=False)
    title_en = Column(String, nullable=False)
    title_ne = Column(String, nullable=True)
    centroid = Column(JSONB, nullable=True)
    bbox = Column(JSONB, nullable=True)

    municipality_id = Column(Integer, ForeignKey(
        "municipalities.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)

    def __init__(self, title_en, municipality_id, id=None, title_ne=None, centroid=None, bbox=None):
        self.title_en = title_en
        self.municipality_id = municipality_id
        self.id = id
        self.title_ne = title_ne
        self.centroid = centroid
        self.bbox = bbox

    def _asdict(self):
        return {
            'id': self.id,
            'title_en': self.title_en,
            'title_ne': self.title_ne,
            'centroid': self.centroid,
            'bbox': self.bbox,
            'municipality_id': self.municipality_id
        }


class CovidCase(Base):
    __tablename__ = "covid_cases"

    id = Column(Integer, primary_key=True, nullable=False)
    province_id = Column(Integer, ForeignKey(
        "provinces.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
    district_id = Column(Integer, ForeignKey(
        "districts.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
    municipality_id = Column(Integer, ForeignKey(
        "municipalities.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
#     ward_id = Column(Integer, ForeignKey("wards.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
    ward_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, nullable=False)
    modified_on = Column(DateTime, nullable=False)
    reported_on = Column(DateTime, nullable=False)

    label = Column(String(20), nullable=True)
    gender = Column(String(10), nullable=True)
    age = Column(Integer, nullable=True)
    point = Column(JSONB, nullable=True)
    occupation = Column(String(50), nullable=True)
    recovered_on = Column(DateTime, nullable=True)
    death_on = Column(DateTime, nullable=True)
    current_state = Column(String(20), nullable=True)
    is_reinfected = Column(Boolean, nullable=True)
    source = Column(String(100), nullable=True)
    comment = Column(String(255), nullable=True)
    type = Column(String(50), nullable=True)
    country_id = Column(Integer, ForeignKey(
        "countries.id", onupdate="cascade", ondelete="cascade"), nullable=True, index=True)
    related_to = Column(JSON, nullable=True)

    def __init__(self, province_id, district_id, municipality_id, ward_id,
                 created_on, modified_on, reported_on, id=None, label=None, gender=None, age=None,
                 point=None, occupation=None, recovered_on=None, death_on=None, current_state=None,
                 is_reinfected=None, source=None, comment=None, type=None, country_id=None, related_to=None):
        self.id = id
        self.province_id = province_id
        self.district_id = district_id
        self.municipality_id = municipality_id
        self.ward_id = ward_id

        self.created_on = created_on
        self.modified_on = modified_on
        self.reported_on = reported_on

        self.label = label
        self.gender = gender
        self.age = age
        self.point = point
        self.occupation = occupation
        self.recovered_on = recovered_on
        self.death_on = death_on
        self.current_state = current_state
        self.is_reinfected = is_reinfected
        self.source = source
        self.comment = comment
        self.type = type
        self.country_id = country_id
        self.related_to = related_to

    def _asdict(self):
        return {
            'id': self.id,
            'province_id': self.province_id,
            'district_id': self.district_id,
            'municipality_id': self.municipality_id,
            'ward_id': self.ward_id,

            'created_on': self.created_on,
            'modified_on': self.modified_on,
            'reported_on': self.reported_on,

            'label': self.label,
            'gender': self.gender,
            'age': self.age,
            'point': self.point,
            'occupation': self.occupation,
            'recovered_on': self.recovered_on,
            'death_on': self.death_on,
            'current_state': self.current_state,
            'is_reinfected': self.is_reinfected,
            'source': self.source,
            'comment': self.comment,
            'type': self.type,
            'country_id': self.country_id,
            'related_to': self.related_to,
        }


class QuarantineInfo(Base):
    __tablename__ = "quarantine_info"

    id = Column(Integer, primary_key=True, nullable=False)
    province_id = Column(Integer, ForeignKey(
        "provinces.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)
    district_id = Column(Integer, ForeignKey(
        "districts.id", onupdate="cascade", ondelete="cascade"), nullable=False, index=True)

    tested_count = Column(Integer, nullable=False, default=0)
    tested_today_count = Column(Integer, nullable=False, default=0)
    released_count = Column(Integer, nullable=False, default=0)
    ambulance_count = Column(Integer, nullable=False, default=0)

    quarantine_bed_count = Column(Integer, nullable=False, default=0)
    has_quarantined_sick_food_service = Column(
        Boolean, nullable=False, default=True)
    quarantined_count = Column(Integer, nullable=False, default=0)
    quarantined_male_count = Column(Integer, nullable=False, default=0)
    quarantined_female_count = Column(Integer, nullable=False, default=0)
    quarantined_sick_count = Column(Integer, nullable=False, default=0)
    quarantined_release_count = Column(Integer, nullable=False, default=0)

    isolated_bed_count = Column(Integer, nullable=False, default=0)
    isolated_count = Column(Integer, nullable=False, default=0)
    isolated_male_count = Column(Integer, nullable=False, default=0)
    isolated_female_count = Column(Integer, nullable=False, default=0)
    isolated_sick_count = Column(Integer, nullable=False, default=0)
    isolated_release_count = Column(Integer, nullable=False, default=0)

    swab_collected_count = Column(Integer, nullable=False, default=0)
    swab_tested_count = Column(Integer, nullable=False, default=0)
    ppe_count = Column(Integer, nullable=False, default=0)
    relief_provided_count = Column(Integer, nullable=False, default=0)
    relief_provided_today_count = Column(Integer, nullable=False, default=0)
    remarks = Column(String, nullable=True)
    is_verified = Column(Boolean, nullable=True)

    created_on = Column(DateTime, nullable=False)
    modified_on = Column(DateTime, nullable=False)
    reported_on = Column(DateTime, nullable=False)

    def __init__(self, province_id, district_id, tested_count, tested_today_count, released_count, ambulance_count, quarantine_bed_count,
                 has_quarantined_sick_food_service, quarantined_count, quarantined_male_count, quarantined_female_count,
                 quarantined_sick_count, quarantined_release_count, isolated_bed_count, isolated_count, isolated_male_count, isolated_female_count,
                 isolated_sick_count, isolated_release_count, swab_collected_count, swab_tested_count, ppe_count,
                 relief_provided_count, relief_provided_today_count, remarks, created_on, modified_on, reported_on, is_verified=None, id=None):
        self.id = id
        self.province_id = province_id
        self.district_id = district_id
        self.tested_count = tested_count
        self.tested_today_count = tested_today_count
        self.released_count = released_count
        self.ambulance_count = ambulance_count
        self.quarantine_bed_count = quarantine_bed_count
        self.has_quarantined_sick_food_service = has_quarantined_sick_food_service
        self.quarantined_count = quarantined_count
        self.quarantined_male_count = quarantined_male_count
        self.quarantined_female_count = quarantined_female_count
        self.quarantined_sick_count = quarantined_sick_count
        self.quarantined_release_count = quarantined_release_count
        self.isolated_bed_count = isolated_bed_count
        self.isolated_count = isolated_count
        self.isolated_male_count = isolated_male_count
        self.isolated_female_count = isolated_female_count
        self.isolated_sick_count = isolated_sick_count
        self.isolated_release_count = isolated_release_count
        self.swab_collected_count = swab_collected_count
        self.swab_tested_count = swab_tested_count
        self.ppe_count = ppe_count
        self.relief_provided_count = relief_provided_count
        self.relief_provided_today_count = relief_provided_today_count
        self.remarks = remarks
        self.is_verified = is_verified
        self.created_on = created_on
        self.modified_on = modified_on
        self.reported_on = reported_on

    def _asdict(self):
        return {
            'id': self.id,
            'province_id': self.province_id,
            'district_id': self.district_id,
            'tested_count': self.tested_count,
            'tested_today_count': self.tested_today_count,
            'released_count': self.released_count,
            'ambulance_count': self.ambulance_count,
            'quarantine_bed_count': self.quarantine_bed_count,
            'has_quarantined_sick_food_service': self.has_quarantined_sick_food_service,
            'quarantined_count': self.quarantined_count,
            'quarantined_male_count': self.quarantined_male_count,
            'quarantined_female_count': self.quarantined_female_count,
            'quarantined_sick_count': self.quarantined_sick_count,
            'quarantined_release_count': self.quarantined_release_count,
            'isolated_bed_count': self.isolated_bed_count,
            'isolated_count': self.isolated_count,
            'isolated_male_count': self.isolated_male_count,
            'isolated_female_count': self.isolated_female_count,
            'isolated_sick_count': self.isolated_sick_count,
            'isolated_release_count': self.isolated_release_count,
            'swab_collected_count': self.swab_collected_count,
            'swab_tested_count': self.swab_tested_count,
            'ppe_count': self.ppe_count,
            'relief_provided_count': self.relief_provided_count,
            'relief_provided_today_count': self.relief_provided_today_count,
            'remarks': self.remarks,
            'is_verified': self.is_verified,
            'created_on': self.created_on,
            'modified_on': self.modified_on,
            'reported_on': self.reported_on
        }
