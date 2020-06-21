import logging
from functools import lru_cache
from urllib.request import urlopen
import json


class LoggerMixin:
    @property
    def logger(self):
        name = '.'.join([self.__class__.__name__])
        return logging.getLogger(name)


class GeoJson:

    @staticmethod
    @lru_cache()
    def get_provinces_geojson():
        with urlopen('https://github.com/mesaugat/geoJSON-Nepal/raw/master/nepal-states.geojson') as response:
            return json.load(response)

    @staticmethod
    @lru_cache()
    def get_districts_geojson():
        district_url = "https://github.com/mesaugat/geoJSON-Nepal/raw/master/nepal-districts-new.geojson"
        with urlopen(district_url) as response:
            districts = json.load(response)

        for f in districts['features']:
            incoming_dist_name = f['properties']['DIST_EN']
            correct_dist_name = f['properties']['DIST_EN']
            if incoming_dist_name == 'Chitawan':
                correct_dist_name = 'Chitwan'
            elif incoming_dist_name == 'Kabhrepalanchok':
                correct_dist_name = 'Kavrepalanchok'
            elif incoming_dist_name == 'Makawanpur':
                correct_dist_name = 'Makwanpur'

            f['properties']['DIST_EN'] = correct_dist_name

        return districts
