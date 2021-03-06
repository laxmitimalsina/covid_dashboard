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


class NationalInfo(object):
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
        'reported_on': 'date',
        'new_pcr_test_count': 'int',
        'total_pcr_test_count': 'int',
        'available_pcr_count': 'int',
        'new_rdt_test_count': 'int',
        'total_rdt_test_count': 'int',
        'nepalese_in_india_border_territory_count': 'int',
        'indians_in_nepal_border_territory_count': 'int',
        'outbound_truck_count': 'int',
        'inbound_truck_count': 'int',
        'people_disobeying_count': 'int',
        'vehicles_disobeying_count': 'int',
        'aboard_returnees_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'reported_on': 'reportedOn',
        'new_pcr_test_count': 'newPcrTestCount',
        'total_pcr_test_count': 'totalPcrTestCount',
        'available_pcr_count': 'availablePcrCount',
        'new_rdt_test_count': 'newRdtTestCount',
        'total_rdt_test_count': 'totalRdtTestCount',
        'nepalese_in_india_border_territory_count': 'nepaleseInIndiaBorderTerritoryCount',
        'indians_in_nepal_border_territory_count': 'indiansInNepalBorderTerritoryCount',
        'outbound_truck_count': 'outboundTruckCount',
        'inbound_truck_count': 'inboundTruckCount',
        'people_disobeying_count': 'peopleDisobeyingCount',
        'vehicles_disobeying_count': 'vehiclesDisobeyingCount',
        'aboard_returnees_count': 'aboardReturneesCount'
    }

    def __init__(self, id=None, reported_on=None, new_pcr_test_count=None, total_pcr_test_count=None, available_pcr_count=None, new_rdt_test_count=None, total_rdt_test_count=None, nepalese_in_india_border_territory_count=None, indians_in_nepal_border_territory_count=None, outbound_truck_count=None, inbound_truck_count=None, people_disobeying_count=None, vehicles_disobeying_count=None, aboard_returnees_count=None):  # noqa: E501
        """NationalInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._reported_on = None
        self._new_pcr_test_count = None
        self._total_pcr_test_count = None
        self._available_pcr_count = None
        self._new_rdt_test_count = None
        self._total_rdt_test_count = None
        self._nepalese_in_india_border_territory_count = None
        self._indians_in_nepal_border_territory_count = None
        self._outbound_truck_count = None
        self._inbound_truck_count = None
        self._people_disobeying_count = None
        self._vehicles_disobeying_count = None
        self._aboard_returnees_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.reported_on = reported_on
        self.new_pcr_test_count = new_pcr_test_count
        self.total_pcr_test_count = total_pcr_test_count
        self.available_pcr_count = available_pcr_count
        self.new_rdt_test_count = new_rdt_test_count
        self.total_rdt_test_count = total_rdt_test_count
        self.nepalese_in_india_border_territory_count = nepalese_in_india_border_territory_count
        self.indians_in_nepal_border_territory_count = indians_in_nepal_border_territory_count
        self.outbound_truck_count = outbound_truck_count
        self.inbound_truck_count = inbound_truck_count
        self.people_disobeying_count = people_disobeying_count
        self.vehicles_disobeying_count = vehicles_disobeying_count
        self.aboard_returnees_count = aboard_returnees_count

    @property
    def id(self):
        """Gets the id of this NationalInfo.  # noqa: E501


        :return: The id of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NationalInfo.


        :param id: The id of this NationalInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reported_on(self):
        """Gets the reported_on of this NationalInfo.  # noqa: E501


        :return: The reported_on of this NationalInfo.  # noqa: E501
        :rtype: date
        """
        return self._reported_on

    @reported_on.setter
    def reported_on(self, reported_on):
        """Sets the reported_on of this NationalInfo.


        :param reported_on: The reported_on of this NationalInfo.  # noqa: E501
        :type: date
        """
        if reported_on is None:
            raise ValueError("Invalid value for `reported_on`, must not be `None`")  # noqa: E501

        self._reported_on = reported_on

    @property
    def new_pcr_test_count(self):
        """Gets the new_pcr_test_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The new_pcr_test_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._new_pcr_test_count

    @new_pcr_test_count.setter
    def new_pcr_test_count(self, new_pcr_test_count):
        """Sets the new_pcr_test_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param new_pcr_test_count: The new_pcr_test_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if new_pcr_test_count is None:
            raise ValueError("Invalid value for `new_pcr_test_count`, must not be `None`")  # noqa: E501
        if new_pcr_test_count is not None and new_pcr_test_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `new_pcr_test_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if new_pcr_test_count is not None and new_pcr_test_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `new_pcr_test_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._new_pcr_test_count = new_pcr_test_count

    @property
    def total_pcr_test_count(self):
        """Gets the total_pcr_test_count of this NationalInfo.  # noqa: E501

        Until now  # noqa: E501

        :return: The total_pcr_test_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_pcr_test_count

    @total_pcr_test_count.setter
    def total_pcr_test_count(self, total_pcr_test_count):
        """Sets the total_pcr_test_count of this NationalInfo.

        Until now  # noqa: E501

        :param total_pcr_test_count: The total_pcr_test_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if total_pcr_test_count is None:
            raise ValueError("Invalid value for `total_pcr_test_count`, must not be `None`")  # noqa: E501
        if total_pcr_test_count is not None and total_pcr_test_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `total_pcr_test_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if total_pcr_test_count is not None and total_pcr_test_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_pcr_test_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_pcr_test_count = total_pcr_test_count

    @property
    def available_pcr_count(self):
        """Gets the available_pcr_count of this NationalInfo.  # noqa: E501

        As of now  # noqa: E501

        :return: The available_pcr_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._available_pcr_count

    @available_pcr_count.setter
    def available_pcr_count(self, available_pcr_count):
        """Sets the available_pcr_count of this NationalInfo.

        As of now  # noqa: E501

        :param available_pcr_count: The available_pcr_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if available_pcr_count is None:
            raise ValueError("Invalid value for `available_pcr_count`, must not be `None`")  # noqa: E501
        if available_pcr_count is not None and available_pcr_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `available_pcr_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if available_pcr_count is not None and available_pcr_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `available_pcr_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._available_pcr_count = available_pcr_count

    @property
    def new_rdt_test_count(self):
        """Gets the new_rdt_test_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The new_rdt_test_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._new_rdt_test_count

    @new_rdt_test_count.setter
    def new_rdt_test_count(self, new_rdt_test_count):
        """Sets the new_rdt_test_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param new_rdt_test_count: The new_rdt_test_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if new_rdt_test_count is None:
            raise ValueError("Invalid value for `new_rdt_test_count`, must not be `None`")  # noqa: E501
        if new_rdt_test_count is not None and new_rdt_test_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `new_rdt_test_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if new_rdt_test_count is not None and new_rdt_test_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `new_rdt_test_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._new_rdt_test_count = new_rdt_test_count

    @property
    def total_rdt_test_count(self):
        """Gets the total_rdt_test_count of this NationalInfo.  # noqa: E501

        Until now  # noqa: E501

        :return: The total_rdt_test_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_rdt_test_count

    @total_rdt_test_count.setter
    def total_rdt_test_count(self, total_rdt_test_count):
        """Sets the total_rdt_test_count of this NationalInfo.

        Until now  # noqa: E501

        :param total_rdt_test_count: The total_rdt_test_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if total_rdt_test_count is None:
            raise ValueError("Invalid value for `total_rdt_test_count`, must not be `None`")  # noqa: E501
        if total_rdt_test_count is not None and total_rdt_test_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `total_rdt_test_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if total_rdt_test_count is not None and total_rdt_test_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_rdt_test_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_rdt_test_count = total_rdt_test_count

    @property
    def nepalese_in_india_border_territory_count(self):
        """Gets the nepalese_in_india_border_territory_count of this NationalInfo.  # noqa: E501

        As of now  # noqa: E501

        :return: The nepalese_in_india_border_territory_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._nepalese_in_india_border_territory_count

    @nepalese_in_india_border_territory_count.setter
    def nepalese_in_india_border_territory_count(self, nepalese_in_india_border_territory_count):
        """Sets the nepalese_in_india_border_territory_count of this NationalInfo.

        As of now  # noqa: E501

        :param nepalese_in_india_border_territory_count: The nepalese_in_india_border_territory_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if nepalese_in_india_border_territory_count is None:
            raise ValueError("Invalid value for `nepalese_in_india_border_territory_count`, must not be `None`")  # noqa: E501
        if nepalese_in_india_border_territory_count is not None and nepalese_in_india_border_territory_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `nepalese_in_india_border_territory_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if nepalese_in_india_border_territory_count is not None and nepalese_in_india_border_territory_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `nepalese_in_india_border_territory_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nepalese_in_india_border_territory_count = nepalese_in_india_border_territory_count

    @property
    def indians_in_nepal_border_territory_count(self):
        """Gets the indians_in_nepal_border_territory_count of this NationalInfo.  # noqa: E501

        As of now  # noqa: E501

        :return: The indians_in_nepal_border_territory_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._indians_in_nepal_border_territory_count

    @indians_in_nepal_border_territory_count.setter
    def indians_in_nepal_border_territory_count(self, indians_in_nepal_border_territory_count):
        """Sets the indians_in_nepal_border_territory_count of this NationalInfo.

        As of now  # noqa: E501

        :param indians_in_nepal_border_territory_count: The indians_in_nepal_border_territory_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if indians_in_nepal_border_territory_count is None:
            raise ValueError("Invalid value for `indians_in_nepal_border_territory_count`, must not be `None`")  # noqa: E501
        if indians_in_nepal_border_territory_count is not None and indians_in_nepal_border_territory_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `indians_in_nepal_border_territory_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if indians_in_nepal_border_territory_count is not None and indians_in_nepal_border_territory_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `indians_in_nepal_border_territory_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._indians_in_nepal_border_territory_count = indians_in_nepal_border_territory_count

    @property
    def outbound_truck_count(self):
        """Gets the outbound_truck_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The outbound_truck_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._outbound_truck_count

    @outbound_truck_count.setter
    def outbound_truck_count(self, outbound_truck_count):
        """Sets the outbound_truck_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param outbound_truck_count: The outbound_truck_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if outbound_truck_count is None:
            raise ValueError("Invalid value for `outbound_truck_count`, must not be `None`")  # noqa: E501
        if outbound_truck_count is not None and outbound_truck_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `outbound_truck_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if outbound_truck_count is not None and outbound_truck_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `outbound_truck_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._outbound_truck_count = outbound_truck_count

    @property
    def inbound_truck_count(self):
        """Gets the inbound_truck_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The inbound_truck_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._inbound_truck_count

    @inbound_truck_count.setter
    def inbound_truck_count(self, inbound_truck_count):
        """Sets the inbound_truck_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param inbound_truck_count: The inbound_truck_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if inbound_truck_count is None:
            raise ValueError("Invalid value for `inbound_truck_count`, must not be `None`")  # noqa: E501
        if inbound_truck_count is not None and inbound_truck_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `inbound_truck_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if inbound_truck_count is not None and inbound_truck_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `inbound_truck_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._inbound_truck_count = inbound_truck_count

    @property
    def people_disobeying_count(self):
        """Gets the people_disobeying_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The people_disobeying_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._people_disobeying_count

    @people_disobeying_count.setter
    def people_disobeying_count(self, people_disobeying_count):
        """Sets the people_disobeying_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param people_disobeying_count: The people_disobeying_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if people_disobeying_count is None:
            raise ValueError("Invalid value for `people_disobeying_count`, must not be `None`")  # noqa: E501
        if people_disobeying_count is not None and people_disobeying_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `people_disobeying_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if people_disobeying_count is not None and people_disobeying_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `people_disobeying_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._people_disobeying_count = people_disobeying_count

    @property
    def vehicles_disobeying_count(self):
        """Gets the vehicles_disobeying_count of this NationalInfo.  # noqa: E501

        Within last 24 hours  # noqa: E501

        :return: The vehicles_disobeying_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._vehicles_disobeying_count

    @vehicles_disobeying_count.setter
    def vehicles_disobeying_count(self, vehicles_disobeying_count):
        """Sets the vehicles_disobeying_count of this NationalInfo.

        Within last 24 hours  # noqa: E501

        :param vehicles_disobeying_count: The vehicles_disobeying_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if vehicles_disobeying_count is None:
            raise ValueError("Invalid value for `vehicles_disobeying_count`, must not be `None`")  # noqa: E501
        if vehicles_disobeying_count is not None and vehicles_disobeying_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `vehicles_disobeying_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if vehicles_disobeying_count is not None and vehicles_disobeying_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `vehicles_disobeying_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vehicles_disobeying_count = vehicles_disobeying_count

    @property
    def aboard_returnees_count(self):
        """Gets the aboard_returnees_count of this NationalInfo.  # noqa: E501

        Until now  # noqa: E501

        :return: The aboard_returnees_count of this NationalInfo.  # noqa: E501
        :rtype: int
        """
        return self._aboard_returnees_count

    @aboard_returnees_count.setter
    def aboard_returnees_count(self, aboard_returnees_count):
        """Sets the aboard_returnees_count of this NationalInfo.

        Until now  # noqa: E501

        :param aboard_returnees_count: The aboard_returnees_count of this NationalInfo.  # noqa: E501
        :type: int
        """
        if aboard_returnees_count is None:
            raise ValueError("Invalid value for `aboard_returnees_count`, must not be `None`")  # noqa: E501
        if aboard_returnees_count is not None and aboard_returnees_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `aboard_returnees_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if aboard_returnees_count is not None and aboard_returnees_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `aboard_returnees_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._aboard_returnees_count = aboard_returnees_count

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
        if issubclass(NationalInfo, dict):
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
        if not isinstance(other, NationalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
