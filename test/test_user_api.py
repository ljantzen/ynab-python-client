# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ynab
from ynab.api.user_api import UserApi  # noqa: E501
from ynab.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = ynab.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user(self):
        """Test case for get_user

        User info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
