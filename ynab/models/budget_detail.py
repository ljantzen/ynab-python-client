# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ynab.models.budget_summary import BudgetSummary  # noqa: F401,E501
from ynab.models.currency_format import CurrencyFormat  # noqa: F401,E501
from ynab.models.date_format import DateFormat  # noqa: F401,E501


class BudgetDetail(object):
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
        'date_format': 'DateFormat',
        'currency_format': 'CurrencyFormat'
    }

    attribute_map = {
        'date_format': 'date_format',
        'currency_format': 'currency_format'
    }

    def __init__(self, date_format=None, currency_format=None):  # noqa: E501
        """BudgetDetail - a model defined in Swagger"""  # noqa: E501

        self._date_format = None
        self._currency_format = None
        self.discriminator = None

        if date_format is not None:
            self.date_format = date_format
        if currency_format is not None:
            self.currency_format = currency_format

    @property
    def date_format(self):
        """Gets the date_format of this BudgetDetail.  # noqa: E501


        :return: The date_format of this BudgetDetail.  # noqa: E501
        :rtype: DateFormat
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this BudgetDetail.


        :param date_format: The date_format of this BudgetDetail.  # noqa: E501
        :type: DateFormat
        """

        self._date_format = date_format

    @property
    def currency_format(self):
        """Gets the currency_format of this BudgetDetail.  # noqa: E501


        :return: The currency_format of this BudgetDetail.  # noqa: E501
        :rtype: CurrencyFormat
        """
        return self._currency_format

    @currency_format.setter
    def currency_format(self, currency_format):
        """Sets the currency_format of this BudgetDetail.


        :param currency_format: The currency_format of this BudgetDetail.  # noqa: E501
        :type: CurrencyFormat
        """

        self._currency_format = currency_format

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BudgetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
