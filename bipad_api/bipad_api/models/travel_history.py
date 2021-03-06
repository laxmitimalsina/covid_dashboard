# coding: utf-8

"""
    BIPAD API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TravelHistory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'to_province': 'str',
        'to_district': 'str',
        'from_province': 'str',
        'from_district': 'str',
        'immigrant': 'int',
        'tole': 'str',
        'transits': 'list[Transit]',
        'key': 'str',
        'travel_type': 'str',
        'travel_mode': 'str',
        'departure_date': 'date',
        'departure_time': 'str',
        'arrival_date': 'date',
        'arrival_time': 'str',
        'flight_number': 'str',
        'border_post': 'str',
        'from_country': 'int',
        'to_country': 'int',
        'from_municipality': 'int',
        'to_municipality': 'int'
    }

    attribute_map = {
        'id': 'id',
        'to_province': 'toProvince',
        'to_district': 'toDistrict',
        'from_province': 'fromProvince',
        'from_district': 'fromDistrict',
        'immigrant': 'immigrant',
        'tole': 'tole',
        'transits': 'transits',
        'key': 'key',
        'travel_type': 'travelType',
        'travel_mode': 'travelMode',
        'departure_date': 'departureDate',
        'departure_time': 'departureTime',
        'arrival_date': 'arrivalDate',
        'arrival_time': 'arrivalTime',
        'flight_number': 'flightNumber',
        'border_post': 'borderPost',
        'from_country': 'fromCountry',
        'to_country': 'toCountry',
        'from_municipality': 'fromMunicipality',
        'to_municipality': 'toMunicipality'
    }

    def __init__(self, id=None, to_province=None, to_district=None, from_province=None, from_district=None, immigrant=None, tole=None, transits=None, key=None, travel_type=None, travel_mode=None, departure_date=None, departure_time=None, arrival_date=None, arrival_time=None, flight_number=None, border_post=None, from_country=None, to_country=None, from_municipality=None, to_municipality=None):  # noqa: E501
        """TravelHistory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._to_province = None
        self._to_district = None
        self._from_province = None
        self._from_district = None
        self._immigrant = None
        self._tole = None
        self._transits = None
        self._key = None
        self._travel_type = None
        self._travel_mode = None
        self._departure_date = None
        self._departure_time = None
        self._arrival_date = None
        self._arrival_time = None
        self._flight_number = None
        self._border_post = None
        self._from_country = None
        self._to_country = None
        self._from_municipality = None
        self._to_municipality = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if to_province is not None:
            self.to_province = to_province
        if to_district is not None:
            self.to_district = to_district
        if from_province is not None:
            self.from_province = from_province
        if from_district is not None:
            self.from_district = from_district
        if immigrant is not None:
            self.immigrant = immigrant
        if tole is not None:
            self.tole = tole
        if transits is not None:
            self.transits = transits
        if key is not None:
            self.key = key
        if travel_type is not None:
            self.travel_type = travel_type
        if travel_mode is not None:
            self.travel_mode = travel_mode
        self.departure_date = departure_date
        if departure_time is not None:
            self.departure_time = departure_time
        self.arrival_date = arrival_date
        if arrival_time is not None:
            self.arrival_time = arrival_time
        if flight_number is not None:
            self.flight_number = flight_number
        if border_post is not None:
            self.border_post = border_post
        if from_country is not None:
            self.from_country = from_country
        if to_country is not None:
            self.to_country = to_country
        if from_municipality is not None:
            self.from_municipality = from_municipality
        if to_municipality is not None:
            self.to_municipality = to_municipality

    @property
    def id(self):
        """Gets the id of this TravelHistory.  # noqa: E501


        :return: The id of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TravelHistory.


        :param id: The id of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def to_province(self):
        """Gets the to_province of this TravelHistory.  # noqa: E501


        :return: The to_province of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._to_province

    @to_province.setter
    def to_province(self, to_province):
        """Sets the to_province of this TravelHistory.


        :param to_province: The to_province of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._to_province = to_province

    @property
    def to_district(self):
        """Gets the to_district of this TravelHistory.  # noqa: E501


        :return: The to_district of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._to_district

    @to_district.setter
    def to_district(self, to_district):
        """Sets the to_district of this TravelHistory.


        :param to_district: The to_district of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._to_district = to_district

    @property
    def from_province(self):
        """Gets the from_province of this TravelHistory.  # noqa: E501


        :return: The from_province of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._from_province

    @from_province.setter
    def from_province(self, from_province):
        """Sets the from_province of this TravelHistory.


        :param from_province: The from_province of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._from_province = from_province

    @property
    def from_district(self):
        """Gets the from_district of this TravelHistory.  # noqa: E501


        :return: The from_district of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._from_district

    @from_district.setter
    def from_district(self, from_district):
        """Sets the from_district of this TravelHistory.


        :param from_district: The from_district of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._from_district = from_district

    @property
    def immigrant(self):
        """Gets the immigrant of this TravelHistory.  # noqa: E501


        :return: The immigrant of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._immigrant

    @immigrant.setter
    def immigrant(self, immigrant):
        """Sets the immigrant of this TravelHistory.


        :param immigrant: The immigrant of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._immigrant = immigrant

    @property
    def tole(self):
        """Gets the tole of this TravelHistory.  # noqa: E501


        :return: The tole of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._tole

    @tole.setter
    def tole(self, tole):
        """Sets the tole of this TravelHistory.


        :param tole: The tole of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._tole = tole

    @property
    def transits(self):
        """Gets the transits of this TravelHistory.  # noqa: E501


        :return: The transits of this TravelHistory.  # noqa: E501
        :rtype: list[Transit]
        """
        return self._transits

    @transits.setter
    def transits(self, transits):
        """Sets the transits of this TravelHistory.


        :param transits: The transits of this TravelHistory.  # noqa: E501
        :type: list[Transit]
        """

        self._transits = transits

    @property
    def key(self):
        """Gets the key of this TravelHistory.  # noqa: E501


        :return: The key of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TravelHistory.


        :param key: The key of this TravelHistory.  # noqa: E501
        :type: str
        """
        if key is not None and len(key) > 255:
            raise ValueError("Invalid value for `key`, length must be less than or equal to `255`")  # noqa: E501
        if key is not None and len(key) < 1:
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def travel_type(self):
        """Gets the travel_type of this TravelHistory.  # noqa: E501


        :return: The travel_type of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._travel_type

    @travel_type.setter
    def travel_type(self, travel_type):
        """Sets the travel_type of this TravelHistory.


        :param travel_type: The travel_type of this TravelHistory.  # noqa: E501
        :type: str
        """
        allowed_values = ["international", "national"]  # noqa: E501
        if travel_type not in allowed_values:
            raise ValueError(
                "Invalid value for `travel_type` ({0}), must be one of {1}"  # noqa: E501
                .format(travel_type, allowed_values)
            )

        self._travel_type = travel_type

    @property
    def travel_mode(self):
        """Gets the travel_mode of this TravelHistory.  # noqa: E501


        :return: The travel_mode of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._travel_mode

    @travel_mode.setter
    def travel_mode(self, travel_mode):
        """Sets the travel_mode of this TravelHistory.


        :param travel_mode: The travel_mode of this TravelHistory.  # noqa: E501
        :type: str
        """
        allowed_values = ["air", "land"]  # noqa: E501
        if travel_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `travel_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(travel_mode, allowed_values)
            )

        self._travel_mode = travel_mode

    @property
    def departure_date(self):
        """Gets the departure_date of this TravelHistory.  # noqa: E501


        :return: The departure_date of this TravelHistory.  # noqa: E501
        :rtype: date
        """
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        """Sets the departure_date of this TravelHistory.


        :param departure_date: The departure_date of this TravelHistory.  # noqa: E501
        :type: date
        """
        if departure_date is None:
            raise ValueError("Invalid value for `departure_date`, must not be `None`")  # noqa: E501

        self._departure_date = departure_date

    @property
    def departure_time(self):
        """Gets the departure_time of this TravelHistory.  # noqa: E501


        :return: The departure_time of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this TravelHistory.


        :param departure_time: The departure_time of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._departure_time = departure_time

    @property
    def arrival_date(self):
        """Gets the arrival_date of this TravelHistory.  # noqa: E501


        :return: The arrival_date of this TravelHistory.  # noqa: E501
        :rtype: date
        """
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        """Sets the arrival_date of this TravelHistory.


        :param arrival_date: The arrival_date of this TravelHistory.  # noqa: E501
        :type: date
        """
        if arrival_date is None:
            raise ValueError("Invalid value for `arrival_date`, must not be `None`")  # noqa: E501

        self._arrival_date = arrival_date

    @property
    def arrival_time(self):
        """Gets the arrival_time of this TravelHistory.  # noqa: E501


        :return: The arrival_time of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """Sets the arrival_time of this TravelHistory.


        :param arrival_time: The arrival_time of this TravelHistory.  # noqa: E501
        :type: str
        """

        self._arrival_time = arrival_time

    @property
    def flight_number(self):
        """Gets the flight_number of this TravelHistory.  # noqa: E501


        :return: The flight_number of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, flight_number):
        """Sets the flight_number of this TravelHistory.


        :param flight_number: The flight_number of this TravelHistory.  # noqa: E501
        :type: str
        """
        if flight_number is not None and len(flight_number) > 128:
            raise ValueError("Invalid value for `flight_number`, length must be less than or equal to `128`")  # noqa: E501

        self._flight_number = flight_number

    @property
    def border_post(self):
        """Gets the border_post of this TravelHistory.  # noqa: E501


        :return: The border_post of this TravelHistory.  # noqa: E501
        :rtype: str
        """
        return self._border_post

    @border_post.setter
    def border_post(self, border_post):
        """Sets the border_post of this TravelHistory.


        :param border_post: The border_post of this TravelHistory.  # noqa: E501
        :type: str
        """
        if border_post is not None and len(border_post) > 128:
            raise ValueError("Invalid value for `border_post`, length must be less than or equal to `128`")  # noqa: E501

        self._border_post = border_post

    @property
    def from_country(self):
        """Gets the from_country of this TravelHistory.  # noqa: E501


        :return: The from_country of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._from_country

    @from_country.setter
    def from_country(self, from_country):
        """Sets the from_country of this TravelHistory.


        :param from_country: The from_country of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._from_country = from_country

    @property
    def to_country(self):
        """Gets the to_country of this TravelHistory.  # noqa: E501


        :return: The to_country of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._to_country

    @to_country.setter
    def to_country(self, to_country):
        """Sets the to_country of this TravelHistory.


        :param to_country: The to_country of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._to_country = to_country

    @property
    def from_municipality(self):
        """Gets the from_municipality of this TravelHistory.  # noqa: E501


        :return: The from_municipality of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._from_municipality

    @from_municipality.setter
    def from_municipality(self, from_municipality):
        """Sets the from_municipality of this TravelHistory.


        :param from_municipality: The from_municipality of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._from_municipality = from_municipality

    @property
    def to_municipality(self):
        """Gets the to_municipality of this TravelHistory.  # noqa: E501


        :return: The to_municipality of this TravelHistory.  # noqa: E501
        :rtype: int
        """
        return self._to_municipality

    @to_municipality.setter
    def to_municipality(self, to_municipality):
        """Sets the to_municipality of this TravelHistory.


        :param to_municipality: The to_municipality of this TravelHistory.  # noqa: E501
        :type: int
        """

        self._to_municipality = to_municipality

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TravelHistory, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TravelHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
