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


class Agriculture(object):
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
        'beneficiary_owner': 'str',
        'beneficiary_count': 'int',
        'quantity': 'int',
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
        'status': 'status',
        'beneficiary_owner': 'beneficiaryOwner',
        'beneficiary_count': 'beneficiaryCount',
        'quantity': 'quantity',
        'economic_loss': 'economicLoss',
        'verified': 'verified',
        'verification_message': 'verificationMessage',
        'type': 'type',
        'loss': 'loss'
    }

    def __init__(self, id=None, created_on=None, modified_on=None, status=None, beneficiary_owner=None, beneficiary_count=None, quantity=None, economic_loss=None, verified=None, verification_message=None, type=None, loss=None):  # noqa: E501
        """Agriculture - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_on = None
        self._modified_on = None
        self._status = None
        self._beneficiary_owner = None
        self._beneficiary_count = None
        self._quantity = None
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
        self.status = status
        if beneficiary_owner is not None:
            self.beneficiary_owner = beneficiary_owner
        if beneficiary_count is not None:
            self.beneficiary_count = beneficiary_count
        self.quantity = quantity
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
        """Gets the id of this Agriculture.  # noqa: E501


        :return: The id of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Agriculture.


        :param id: The id of this Agriculture.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this Agriculture.  # noqa: E501


        :return: The created_on of this Agriculture.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Agriculture.


        :param created_on: The created_on of this Agriculture.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this Agriculture.  # noqa: E501


        :return: The modified_on of this Agriculture.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this Agriculture.


        :param modified_on: The modified_on of this Agriculture.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def status(self):
        """Gets the status of this Agriculture.  # noqa: E501


        :return: The status of this Agriculture.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Agriculture.


        :param status: The status of this Agriculture.  # noqa: E501
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
    def beneficiary_owner(self):
        """Gets the beneficiary_owner of this Agriculture.  # noqa: E501


        :return: The beneficiary_owner of this Agriculture.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_owner

    @beneficiary_owner.setter
    def beneficiary_owner(self, beneficiary_owner):
        """Sets the beneficiary_owner of this Agriculture.


        :param beneficiary_owner: The beneficiary_owner of this Agriculture.  # noqa: E501
        :type: str
        """
        if beneficiary_owner is not None and len(beneficiary_owner) > 255:
            raise ValueError("Invalid value for `beneficiary_owner`, length must be less than or equal to `255`")  # noqa: E501

        self._beneficiary_owner = beneficiary_owner

    @property
    def beneficiary_count(self):
        """Gets the beneficiary_count of this Agriculture.  # noqa: E501


        :return: The beneficiary_count of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._beneficiary_count

    @beneficiary_count.setter
    def beneficiary_count(self, beneficiary_count):
        """Sets the beneficiary_count of this Agriculture.


        :param beneficiary_count: The beneficiary_count of this Agriculture.  # noqa: E501
        :type: int
        """
        if beneficiary_count is not None and beneficiary_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `beneficiary_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if beneficiary_count is not None and beneficiary_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `beneficiary_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._beneficiary_count = beneficiary_count

    @property
    def quantity(self):
        """Gets the quantity of this Agriculture.  # noqa: E501


        :return: The quantity of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Agriculture.


        :param quantity: The quantity of this Agriculture.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if quantity is not None and quantity > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if quantity is not None and quantity < 0:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quantity = quantity

    @property
    def economic_loss(self):
        """Gets the economic_loss of this Agriculture.  # noqa: E501


        :return: The economic_loss of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._economic_loss

    @economic_loss.setter
    def economic_loss(self, economic_loss):
        """Sets the economic_loss of this Agriculture.


        :param economic_loss: The economic_loss of this Agriculture.  # noqa: E501
        :type: int
        """
        if economic_loss is not None and economic_loss > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `economic_loss`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if economic_loss is not None and economic_loss < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `economic_loss`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._economic_loss = economic_loss

    @property
    def verified(self):
        """Gets the verified of this Agriculture.  # noqa: E501


        :return: The verified of this Agriculture.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this Agriculture.


        :param verified: The verified of this Agriculture.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def verification_message(self):
        """Gets the verification_message of this Agriculture.  # noqa: E501


        :return: The verification_message of this Agriculture.  # noqa: E501
        :rtype: str
        """
        return self._verification_message

    @verification_message.setter
    def verification_message(self, verification_message):
        """Sets the verification_message of this Agriculture.


        :param verification_message: The verification_message of this Agriculture.  # noqa: E501
        :type: str
        """

        self._verification_message = verification_message

    @property
    def type(self):
        """Gets the type of this Agriculture.  # noqa: E501


        :return: The type of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Agriculture.


        :param type: The type of this Agriculture.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def loss(self):
        """Gets the loss of this Agriculture.  # noqa: E501


        :return: The loss of this Agriculture.  # noqa: E501
        :rtype: int
        """
        return self._loss

    @loss.setter
    def loss(self, loss):
        """Sets the loss of this Agriculture.


        :param loss: The loss of this Agriculture.  # noqa: E501
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
        if issubclass(Agriculture, dict):
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
        if not isinstance(other, Agriculture):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
