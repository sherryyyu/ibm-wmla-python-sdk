# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Optional

from requests import Request

from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.authenticators.cp4d_authenticator import CP4DTokenManager
from ibm_wmla.edi_token import EDITokenManager
from ibm_cloud_sdk_core.utils import has_bad_first_or_last_char


class ElasticDistributedInferenceAuthenticator(Authenticator):
    """The ElasticDistributedInferenceAuthenticator utilizes a username and password pair to
    obtain a suitable auth token, and adds it requests.

    The auth token will be sent as an Authorization header in the form:

        X-Auth-Token: <auth-token>

    Keyword Args:
        username: The username used to obtain a auth token [required].
        password: The password used to obtain a auth token [required if apikey not specified].
        url: The URL representing the Cloud Pak for Data token service endpoint [required].
        disable_ssl_verification:  A flag that indicates whether verification of the server's SSL
            certificate should be disabled or not. Defaults to False.
        headers: Default headers to be sent with every CP4D token request. Defaults to None.
        proxies: Dictionary for mapping request protocol to proxy URL.
        proxies.http (optional): The proxy endpoint to use for HTTP requests.
        proxies.https (optional): The proxy endpoint to use for HTTPS requests.

    Attributes:
        token_manager (CP4DTokenManager): Retrieves and manages CP4D tokens from the endpoint specified by the url.

    Raises:
        TypeError: The `disable_ssl_verification` is not a bool.
        ValueError: The username, password/apikey, and/or url are not valid for CP4D token requests.
    """

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 user_access_token: str = None,
                 url: str = None,
                 *,
                 apikey: str = None,
                 disable_ssl_verification: bool = False,
                 headers: Optional[Dict[str, str]] = None,
                 proxies: Optional[Dict[str, str]] = None) -> None:
        # Check the type of `disable_ssl_verification`. Must be a bool.
        if not isinstance(disable_ssl_verification, bool):
            raise TypeError('disable_ssl_verification must be a bool')

        self.token_manager = EDITokenManager(
            username=username, password=password, user_access_token = user_access_token, apikey=apikey, url=url,
            disable_ssl_verification=disable_ssl_verification, headers=headers, proxies=proxies)

        self.validate()

    def authentication_type(self) -> str:
        """Returns this authenticator's type ('edi')."""
        return Authenticator.AUTHTYPE_EDI

    def validate(self) -> None:
        """Validate username, password, and url for token requests.

        Ensures the username, password, and url are not None. Additionally, ensures they do not contain invalid
        characters.

        Raises:
            ValueError: The username, password, and/or url are not valid for token requests.
        """

        if self.token_manager.username is None and self.token_manager.user_access_token is None:
            raise ValueError('A username or a user access token should be specified.')
        elif self.token_manager.user_access_token is None:
            if self.token_manager.username is None:
                raise ValueError('The username shouldn\'t be None.')

            if ((self.token_manager.password is None and self.token_manager.apikey is None)
                    or (self.token_manager.password is not None and self.token_manager.apikey is not None)):
                raise ValueError(
                    'Exactly one of `apikey` or `password` must be specified.')


        if self.token_manager.url is None:
            raise ValueError('The url shouldn\'t be None.')

        if has_bad_first_or_last_char(
                self.token_manager.username) or has_bad_first_or_last_char(self.token_manager.password):
            raise ValueError(
                'The username and password shouldn\'t start or end with curly brackets or quotes. '
                'Please remove any surrounding {, }, or \" characters.')

        if has_bad_first_or_last_char(self.token_manager.url):
            raise ValueError(
                'The url shouldn\'t start or end with curly brackets or quotes. '
                'Please remove any surrounding {, }, or \" characters.')

    def authenticate(self, req: Request) -> None:
        """Adds EDI authentication information to the request.

        The EDI auth token will be added to the request's headers in the form:

            'X-Auth-Token': <auth-token>

        Args:
            req:  The request to add EDI authentication information too. Must contain a key to a dictionary
            called headers.
        """
        headers = req.get('headers')
        x_auth_token = self.token_manager.get_token()
        headers['X-Auth-Token']= x_auth_token

    def set_disable_ssl_verification(self, status: bool = False) -> None:
        """Set the flag that indicates whether verification of the server's SSL certificate should be
        disabled or not. Defaults to False.

        Args:
            status: Set to true in order to disable SSL certificate verification. Defaults to False.

        Raises:
            TypeError: The `status` is not a bool.
        """
        self.token_manager.set_disable_ssl_verification(status)

    def set_headers(self, headers: Dict[str, str]) -> None:
        """Default headers to be sent with every CP4D token request.

        Args:
            headers: The headers to be sent with every CP4D token request.
        """
        self.token_manager.set_headers(headers)

    def set_proxies(self, proxies: Dict[str, str]) -> None:
        """Sets the proxies the token manager will use to communicate with CP4D on behalf of the host.

        Args:
            proxies: Dictionary for mapping request protocol to proxy URL.
            proxies.http (optional): The proxy endpoint to use for HTTP requests.
            proxies.https (optional): The proxy endpoint to use for HTTPS requests.
        """
        self.token_manager.set_proxies(proxies)