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


class Training(object):
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
        'title': 'str',
        'duration_days': 'int',
        'contact': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'duration_days': 'durationDays',
        'contact': 'contact'
    }

    def __init__(self, id=None, title=None, duration_days=None, contact=None):  # noqa: E501
        """Training - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._duration_days = None
        self._contact = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.title = title
        self.duration_days = duration_days
        self.contact = contact

    @property
    def id(self):
        """Gets the id of this Training.  # noqa: E501


        :return: The id of this Training.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Training.


        :param id: The id of this Training.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Training.  # noqa: E501


        :return: The title of this Training.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Training.


        :param title: The title of this Training.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        allowed_values = ["rapid_assessment", "LSAR", "first_aid", "fire_fighting"]  # noqa: E501
        if title not in allowed_values:
            raise ValueError(
                "Invalid value for `title` ({0}), must be one of {1}"  # noqa: E501
                .format(title, allowed_values)
            )

        self._title = title

    @property
    def duration_days(self):
        """Gets the duration_days of this Training.  # noqa: E501


        :return: The duration_days of this Training.  # noqa: E501
        :rtype: int
        """
        return self._duration_days

    @duration_days.setter
    def duration_days(self, duration_days):
        """Sets the duration_days of this Training.


        :param duration_days: The duration_days of this Training.  # noqa: E501
        :type: int
        """
        if duration_days is None:
            raise ValueError("Invalid value for `duration_days`, must not be `None`")  # noqa: E501
        if duration_days is not None and duration_days > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `duration_days`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if duration_days is not None and duration_days < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration_days = duration_days

    @property
    def contact(self):
        """Gets the contact of this Training.  # noqa: E501


        :return: The contact of this Training.  # noqa: E501
        :rtype: int
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Training.


        :param contact: The contact of this Training.  # noqa: E501
        :type: int
        """
        if contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

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
        if issubclass(Training, dict):
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
        if not isinstance(other, Training):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
