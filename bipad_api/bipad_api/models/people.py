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


class People(object):
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
        'created_on': 'datetime',
        'modified_on': 'datetime',
        'status': 'str',
        'name': 'str',
        'age': 'int',
        'gender': 'str',
        'below_poverty': 'bool',
        'count': 'int',
        'verified': 'bool',
        'verification_message': 'str',
        'nationality': 'int',
        'ward': 'int',
        'disability': 'int',
        'loss': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_on': 'createdOn',
        'modified_on': 'modifiedOn',
        'status': 'status',
        'name': 'name',
        'age': 'age',
        'gender': 'gender',
        'below_poverty': 'belowPoverty',
        'count': 'count',
        'verified': 'verified',
        'verification_message': 'verificationMessage',
        'nationality': 'nationality',
        'ward': 'ward',
        'disability': 'disability',
        'loss': 'loss'
    }

    def __init__(self, id=None, created_on=None, modified_on=None, status=None, name=None, age=None, gender=None, below_poverty=None, count=None, verified=None, verification_message=None, nationality=None, ward=None, disability=None, loss=None):  # noqa: E501
        """People - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_on = None
        self._modified_on = None
        self._status = None
        self._name = None
        self._age = None
        self._gender = None
        self._below_poverty = None
        self._count = None
        self._verified = None
        self._verification_message = None
        self._nationality = None
        self._ward = None
        self._disability = None
        self._loss = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if modified_on is not None:
            self.modified_on = modified_on
        self.status = status
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if below_poverty is not None:
            self.below_poverty = below_poverty
        if count is not None:
            self.count = count
        if verified is not None:
            self.verified = verified
        if verification_message is not None:
            self.verification_message = verification_message
        if nationality is not None:
            self.nationality = nationality
        if ward is not None:
            self.ward = ward
        if disability is not None:
            self.disability = disability
        self.loss = loss

    @property
    def id(self):
        """Gets the id of this People.  # noqa: E501


        :return: The id of this People.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this People.


        :param id: The id of this People.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this People.  # noqa: E501


        :return: The created_on of this People.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this People.


        :param created_on: The created_on of this People.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this People.  # noqa: E501


        :return: The modified_on of this People.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this People.


        :param modified_on: The modified_on of this People.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def status(self):
        """Gets the status of this People.  # noqa: E501


        :return: The status of this People.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this People.


        :param status: The status of this People.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["dead", "missing", "injured", "affected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def name(self):
        """Gets the name of this People.  # noqa: E501


        :return: The name of this People.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this People.


        :param name: The name of this People.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def age(self):
        """Gets the age of this People.  # noqa: E501


        :return: The age of this People.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this People.


        :param age: The age of this People.  # noqa: E501
        :type: int
        """
        if age is not None and age > 32767:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value less than or equal to `32767`")  # noqa: E501
        if age is not None and age < 0:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age = age

    @property
    def gender(self):
        """Gets the gender of this People.  # noqa: E501


        :return: The gender of this People.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this People.


        :param gender: The gender of this People.  # noqa: E501
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
    def below_poverty(self):
        """Gets the below_poverty of this People.  # noqa: E501


        :return: The below_poverty of this People.  # noqa: E501
        :rtype: bool
        """
        return self._below_poverty

    @below_poverty.setter
    def below_poverty(self, below_poverty):
        """Sets the below_poverty of this People.


        :param below_poverty: The below_poverty of this People.  # noqa: E501
        :type: bool
        """

        self._below_poverty = below_poverty

    @property
    def count(self):
        """Gets the count of this People.  # noqa: E501


        :return: The count of this People.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this People.


        :param count: The count of this People.  # noqa: E501
        :type: int
        """
        if count is not None and count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def verified(self):
        """Gets the verified of this People.  # noqa: E501


        :return: The verified of this People.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this People.


        :param verified: The verified of this People.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def verification_message(self):
        """Gets the verification_message of this People.  # noqa: E501


        :return: The verification_message of this People.  # noqa: E501
        :rtype: str
        """
        return self._verification_message

    @verification_message.setter
    def verification_message(self, verification_message):
        """Sets the verification_message of this People.


        :param verification_message: The verification_message of this People.  # noqa: E501
        :type: str
        """

        self._verification_message = verification_message

    @property
    def nationality(self):
        """Gets the nationality of this People.  # noqa: E501


        :return: The nationality of this People.  # noqa: E501
        :rtype: int
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this People.


        :param nationality: The nationality of this People.  # noqa: E501
        :type: int
        """

        self._nationality = nationality

    @property
    def ward(self):
        """Gets the ward of this People.  # noqa: E501


        :return: The ward of this People.  # noqa: E501
        :rtype: int
        """
        return self._ward

    @ward.setter
    def ward(self, ward):
        """Sets the ward of this People.


        :param ward: The ward of this People.  # noqa: E501
        :type: int
        """

        self._ward = ward

    @property
    def disability(self):
        """Gets the disability of this People.  # noqa: E501


        :return: The disability of this People.  # noqa: E501
        :rtype: int
        """
        return self._disability

    @disability.setter
    def disability(self, disability):
        """Sets the disability of this People.


        :param disability: The disability of this People.  # noqa: E501
        :type: int
        """

        self._disability = disability

    @property
    def loss(self):
        """Gets the loss of this People.  # noqa: E501


        :return: The loss of this People.  # noqa: E501
        :rtype: int
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        """Sets the loss of this People.


        :param loss: The loss of this People.  # noqa: E501
        :type: int
        """
        if loss is None:
            raise ValueError("Invalid value for `loss`, must not be `None`")  # noqa: E501

        self._loss = loss

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
        if issubclass(People, dict):
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
        if not isinstance(other, People):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other