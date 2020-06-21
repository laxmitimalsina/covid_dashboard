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


class ImmigrantVerified(object):
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
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'phone': 'str',
        'phone_owner': 'str',
        'phone_owner_relation': 'str',
        'passport_id': 'str',
        'citizenship_id': 'str',
        'tole': 'str',
        'created_on': 'datetime',
        'modified_on': 'datetime',
        'age': 'int',
        'gender': 'str',
        'arrival_date': 'date',
        'district': 'int',
        'municipality': 'int',
        'ward': 'int',
        'travelled_from': 'int'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'phone': 'phone',
        'phone_owner': 'phoneOwner',
        'phone_owner_relation': 'phoneOwnerRelation',
        'passport_id': 'passportId',
        'citizenship_id': 'citizenshipId',
        'tole': 'tole',
        'created_on': 'createdOn',
        'modified_on': 'modifiedOn',
        'age': 'age',
        'gender': 'gender',
        'arrival_date': 'arrivalDate',
        'district': 'district',
        'municipality': 'municipality',
        'ward': 'ward',
        'travelled_from': 'travelledFrom'
    }

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, phone=None, phone_owner=None, phone_owner_relation=None, passport_id=None, citizenship_id=None, tole=None, created_on=None, modified_on=None, age=None, gender=None, arrival_date=None, district=None, municipality=None, ward=None, travelled_from=None):  # noqa: E501
        """ImmigrantVerified - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._phone = None
        self._phone_owner = None
        self._phone_owner_relation = None
        self._passport_id = None
        self._citizenship_id = None
        self._tole = None
        self._created_on = None
        self._modified_on = None
        self._age = None
        self._gender = None
        self._arrival_date = None
        self._district = None
        self._municipality = None
        self._ward = None
        self._travelled_from = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        self.last_name = last_name
        self.phone = phone
        if phone_owner is not None:
            self.phone_owner = phone_owner
        if phone_owner_relation is not None:
            self.phone_owner_relation = phone_owner_relation
        if passport_id is not None:
            self.passport_id = passport_id
        if citizenship_id is not None:
            self.citizenship_id = citizenship_id
        if tole is not None:
            self.tole = tole
        if created_on is not None:
            self.created_on = created_on
        if modified_on is not None:
            self.modified_on = modified_on
        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if arrival_date is not None:
            self.arrival_date = arrival_date
        self.district = district
        if municipality is not None:
            self.municipality = municipality
        if ward is not None:
            self.ward = ward
        if travelled_from is not None:
            self.travelled_from = travelled_from

    @property
    def id(self):
        """Gets the id of this ImmigrantVerified.  # noqa: E501


        :return: The id of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImmigrantVerified.


        :param id: The id of this ImmigrantVerified.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this ImmigrantVerified.  # noqa: E501


        :return: The first_name of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ImmigrantVerified.


        :param first_name: The first_name of this ImmigrantVerified.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this ImmigrantVerified.  # noqa: E501


        :return: The middle_name of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ImmigrantVerified.


        :param middle_name: The middle_name of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this ImmigrantVerified.  # noqa: E501


        :return: The last_name of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ImmigrantVerified.


        :param last_name: The last_name of this ImmigrantVerified.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this ImmigrantVerified.  # noqa: E501


        :return: The phone of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ImmigrantVerified.


        :param phone: The phone of this ImmigrantVerified.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501
        if phone is not None and len(phone) < 1:
            raise ValueError("Invalid value for `phone`, length must be greater than or equal to `1`")  # noqa: E501

        self._phone = phone

    @property
    def phone_owner(self):
        """Gets the phone_owner of this ImmigrantVerified.  # noqa: E501


        :return: The phone_owner of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._phone_owner

    @phone_owner.setter
    def phone_owner(self, phone_owner):
        """Sets the phone_owner of this ImmigrantVerified.


        :param phone_owner: The phone_owner of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._phone_owner = phone_owner

    @property
    def phone_owner_relation(self):
        """Gets the phone_owner_relation of this ImmigrantVerified.  # noqa: E501


        :return: The phone_owner_relation of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._phone_owner_relation

    @phone_owner_relation.setter
    def phone_owner_relation(self, phone_owner_relation):
        """Sets the phone_owner_relation of this ImmigrantVerified.


        :param phone_owner_relation: The phone_owner_relation of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._phone_owner_relation = phone_owner_relation

    @property
    def passport_id(self):
        """Gets the passport_id of this ImmigrantVerified.  # noqa: E501


        :return: The passport_id of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._passport_id

    @passport_id.setter
    def passport_id(self, passport_id):
        """Sets the passport_id of this ImmigrantVerified.


        :param passport_id: The passport_id of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._passport_id = passport_id

    @property
    def citizenship_id(self):
        """Gets the citizenship_id of this ImmigrantVerified.  # noqa: E501


        :return: The citizenship_id of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._citizenship_id

    @citizenship_id.setter
    def citizenship_id(self, citizenship_id):
        """Sets the citizenship_id of this ImmigrantVerified.


        :param citizenship_id: The citizenship_id of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._citizenship_id = citizenship_id

    @property
    def tole(self):
        """Gets the tole of this ImmigrantVerified.  # noqa: E501


        :return: The tole of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._tole

    @tole.setter
    def tole(self, tole):
        """Sets the tole of this ImmigrantVerified.


        :param tole: The tole of this ImmigrantVerified.  # noqa: E501
        :type: str
        """

        self._tole = tole

    @property
    def created_on(self):
        """Gets the created_on of this ImmigrantVerified.  # noqa: E501


        :return: The created_on of this ImmigrantVerified.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ImmigrantVerified.


        :param created_on: The created_on of this ImmigrantVerified.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this ImmigrantVerified.  # noqa: E501


        :return: The modified_on of this ImmigrantVerified.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this ImmigrantVerified.


        :param modified_on: The modified_on of this ImmigrantVerified.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def age(self):
        """Gets the age of this ImmigrantVerified.  # noqa: E501


        :return: The age of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this ImmigrantVerified.


        :param age: The age of this ImmigrantVerified.  # noqa: E501
        :type: int
        """
        if age is not None and age > 32767:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value less than or equal to `32767`")  # noqa: E501
        if age is not None and age < -32768:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `-32768`")  # noqa: E501

        self._age = age

    @property
    def gender(self):
        """Gets the gender of this ImmigrantVerified.  # noqa: E501


        :return: The gender of this ImmigrantVerified.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ImmigrantVerified.


        :param gender: The gender of this ImmigrantVerified.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "others"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def arrival_date(self):
        """Gets the arrival_date of this ImmigrantVerified.  # noqa: E501


        :return: The arrival_date of this ImmigrantVerified.  # noqa: E501
        :rtype: date
        """
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        """Sets the arrival_date of this ImmigrantVerified.


        :param arrival_date: The arrival_date of this ImmigrantVerified.  # noqa: E501
        :type: date
        """

        self._arrival_date = arrival_date

    @property
    def district(self):
        """Gets the district of this ImmigrantVerified.  # noqa: E501


        :return: The district of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this ImmigrantVerified.


        :param district: The district of this ImmigrantVerified.  # noqa: E501
        :type: int
        """
        if district is None:
            raise ValueError("Invalid value for `district`, must not be `None`")  # noqa: E501

        self._district = district

    @property
    def municipality(self):
        """Gets the municipality of this ImmigrantVerified.  # noqa: E501


        :return: The municipality of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._municipality

    @municipality.setter
    def municipality(self, municipality):
        """Sets the municipality of this ImmigrantVerified.


        :param municipality: The municipality of this ImmigrantVerified.  # noqa: E501
        :type: int
        """

        self._municipality = municipality

    @property
    def ward(self):
        """Gets the ward of this ImmigrantVerified.  # noqa: E501


        :return: The ward of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._ward

    @ward.setter
    def ward(self, ward):
        """Sets the ward of this ImmigrantVerified.


        :param ward: The ward of this ImmigrantVerified.  # noqa: E501
        :type: int
        """

        self._ward = ward

    @property
    def travelled_from(self):
        """Gets the travelled_from of this ImmigrantVerified.  # noqa: E501


        :return: The travelled_from of this ImmigrantVerified.  # noqa: E501
        :rtype: int
        """
        return self._travelled_from

    @travelled_from.setter
    def travelled_from(self, travelled_from):
        """Sets the travelled_from of this ImmigrantVerified.


        :param travelled_from: The travelled_from of this ImmigrantVerified.  # noqa: E501
        :type: int
        """

        self._travelled_from = travelled_from

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
        if issubclass(ImmigrantVerified, dict):
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
        if not isinstance(other, ImmigrantVerified):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
