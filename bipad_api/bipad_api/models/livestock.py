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


class Livestock(object):
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
        'title': 'str',
        'status': 'str',
        'count': 'int',
        'economic_loss': 'int',
        'verified': 'bool',
        'verification_message': 'str',
        'type': 'int',
        'loss': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_on': 'createdOn',
        'modified_on': 'modifiedOn',
        'title': 'title',
        'status': 'status',
        'count': 'count',
        'economic_loss': 'economicLoss',
        'verified': 'verified',
        'verification_message': 'verificationMessage',
        'type': 'type',
        'loss': 'loss'
    }

    def __init__(self, id=None, created_on=None, modified_on=None, title=None, status=None, count=None, economic_loss=None, verified=None, verification_message=None, type=None, loss=None):  # noqa: E501
        """Livestock - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_on = None
        self._modified_on = None
        self._title = None
        self._status = None
        self._count = None
        self._economic_loss = None
        self._verified = None
        self._verification_message = None
        self._type = None
        self._loss = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if modified_on is not None:
            self.modified_on = modified_on
        if title is not None:
            self.title = title
        self.status = status
        self.count = count
        if economic_loss is not None:
            self.economic_loss = economic_loss
        if verified is not None:
            self.verified = verified
        if verification_message is not None:
            self.verification_message = verification_message
        self.type = type
        self.loss = loss

    @property
    def id(self):
        """Gets the id of this Livestock.  # noqa: E501


        :return: The id of this Livestock.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Livestock.


        :param id: The id of this Livestock.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this Livestock.  # noqa: E501


        :return: The created_on of this Livestock.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Livestock.


        :param created_on: The created_on of this Livestock.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this Livestock.  # noqa: E501


        :return: The modified_on of this Livestock.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this Livestock.


        :param modified_on: The modified_on of this Livestock.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def title(self):
        """Gets the title of this Livestock.  # noqa: E501


        :return: The title of this Livestock.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Livestock.


        :param title: The title of this Livestock.  # noqa: E501
        :type: str
        """
        if title is not None and len(title) > 255:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `255`")  # noqa: E501

        self._title = title

    @property
    def status(self):
        """Gets the status of this Livestock.  # noqa: E501


        :return: The status of this Livestock.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Livestock.


        :param status: The status of this Livestock.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["destroyed", "affected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def count(self):
        """Gets the count of this Livestock.  # noqa: E501


        :return: The count of this Livestock.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Livestock.


        :param count: The count of this Livestock.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501
        if count is not None and count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def economic_loss(self):
        """Gets the economic_loss of this Livestock.  # noqa: E501


        :return: The economic_loss of this Livestock.  # noqa: E501
        :rtype: int
        """
        return self._economic_loss

    @economic_loss.setter
    def economic_loss(self, economic_loss):
        """Sets the economic_loss of this Livestock.


        :param economic_loss: The economic_loss of this Livestock.  # noqa: E501
        :type: int
        """
        if economic_loss is not None and economic_loss > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `economic_loss`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if economic_loss is not None and economic_loss < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `economic_loss`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._economic_loss = economic_loss

    @property
    def verified(self):
        """Gets the verified of this Livestock.  # noqa: E501


        :return: The verified of this Livestock.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this Livestock.


        :param verified: The verified of this Livestock.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def verification_message(self):
        """Gets the verification_message of this Livestock.  # noqa: E501


        :return: The verification_message of this Livestock.  # noqa: E501
        :rtype: str
        """
        return self._verification_message

    @verification_message.setter
    def verification_message(self, verification_message):
        """Sets the verification_message of this Livestock.


        :param verification_message: The verification_message of this Livestock.  # noqa: E501
        :type: str
        """

        self._verification_message = verification_message

    @property
    def type(self):
        """Gets the type of this Livestock.  # noqa: E501


        :return: The type of this Livestock.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Livestock.


        :param type: The type of this Livestock.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def loss(self):
        """Gets the loss of this Livestock.  # noqa: E501


        :return: The loss of this Livestock.  # noqa: E501
        :rtype: int
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        """Sets the loss of this Livestock.


        :param loss: The loss of this Livestock.  # noqa: E501
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
        if issubclass(Livestock, dict):
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
        if not isinstance(other, Livestock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other