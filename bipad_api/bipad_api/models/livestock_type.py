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


class LivestockType(object):
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
        'title_en': 'str',
        'title_ne': 'str',
        'description': 'str',
        'lft': 'int',
        'rght': 'int',
        'tree_id': 'int',
        'level': 'int',
        'parent': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'title_en': 'titleEn',
        'title_ne': 'titleNe',
        'description': 'description',
        'lft': 'lft',
        'rght': 'rght',
        'tree_id': 'treeId',
        'level': 'level',
        'parent': 'parent'
    }

    def __init__(self, id=None, title=None, title_en=None, title_ne=None, description=None, lft=None, rght=None, tree_id=None, level=None, parent=None):  # noqa: E501
        """LivestockType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._title_en = None
        self._title_ne = None
        self._description = None
        self._lft = None
        self._rght = None
        self._tree_id = None
        self._level = None
        self._parent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.title = title
        if title_en is not None:
            self.title_en = title_en
        if title_ne is not None:
            self.title_ne = title_ne
        if description is not None:
            self.description = description
        if lft is not None:
            self.lft = lft
        if rght is not None:
            self.rght = rght
        if tree_id is not None:
            self.tree_id = tree_id
        if level is not None:
            self.level = level
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this LivestockType.  # noqa: E501


        :return: The id of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LivestockType.


        :param id: The id of this LivestockType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this LivestockType.  # noqa: E501


        :return: The title of this LivestockType.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LivestockType.


        :param title: The title of this LivestockType.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) > 255:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `255`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def title_en(self):
        """Gets the title_en of this LivestockType.  # noqa: E501


        :return: The title_en of this LivestockType.  # noqa: E501
        :rtype: str
        """
        return self._title_en

    @title_en.setter
    def title_en(self, title_en):
        """Sets the title_en of this LivestockType.


        :param title_en: The title_en of this LivestockType.  # noqa: E501
        :type: str
        """
        if title_en is not None and len(title_en) > 255:
            raise ValueError("Invalid value for `title_en`, length must be less than or equal to `255`")  # noqa: E501

        self._title_en = title_en

    @property
    def title_ne(self):
        """Gets the title_ne of this LivestockType.  # noqa: E501


        :return: The title_ne of this LivestockType.  # noqa: E501
        :rtype: str
        """
        return self._title_ne

    @title_ne.setter
    def title_ne(self, title_ne):
        """Sets the title_ne of this LivestockType.


        :param title_ne: The title_ne of this LivestockType.  # noqa: E501
        :type: str
        """
        if title_ne is not None and len(title_ne) > 255:
            raise ValueError("Invalid value for `title_ne`, length must be less than or equal to `255`")  # noqa: E501

        self._title_ne = title_ne

    @property
    def description(self):
        """Gets the description of this LivestockType.  # noqa: E501


        :return: The description of this LivestockType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LivestockType.


        :param description: The description of this LivestockType.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def lft(self):
        """Gets the lft of this LivestockType.  # noqa: E501


        :return: The lft of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._lft

    @lft.setter
    def lft(self, lft):
        """Sets the lft of this LivestockType.


        :param lft: The lft of this LivestockType.  # noqa: E501
        :type: int
        """

        self._lft = lft

    @property
    def rght(self):
        """Gets the rght of this LivestockType.  # noqa: E501


        :return: The rght of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._rght

    @rght.setter
    def rght(self, rght):
        """Sets the rght of this LivestockType.


        :param rght: The rght of this LivestockType.  # noqa: E501
        :type: int
        """

        self._rght = rght

    @property
    def tree_id(self):
        """Gets the tree_id of this LivestockType.  # noqa: E501


        :return: The tree_id of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._tree_id

    @tree_id.setter
    def tree_id(self, tree_id):
        """Sets the tree_id of this LivestockType.


        :param tree_id: The tree_id of this LivestockType.  # noqa: E501
        :type: int
        """

        self._tree_id = tree_id

    @property
    def level(self):
        """Gets the level of this LivestockType.  # noqa: E501


        :return: The level of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LivestockType.


        :param level: The level of this LivestockType.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def parent(self):
        """Gets the parent of this LivestockType.  # noqa: E501


        :return: The parent of this LivestockType.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this LivestockType.


        :param parent: The parent of this LivestockType.  # noqa: E501
        :type: int
        """

        self._parent = parent

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
        if issubclass(LivestockType, dict):
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
        if not isinstance(other, LivestockType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
