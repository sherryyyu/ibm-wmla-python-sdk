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

import json
from typing import Dict, Optional

from abc import ABC
from typing import Optional
import base64

import requests
from ibm_cloud_sdk_core.token_managers.token_manager import TokenManager
from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_sdk_core.authenticators.basic_authenticator import BasicAuthenticator

class EDITokenManager(TokenManager, ABC):
    """Token Manager of EDI.

    The Token Manager performs basic auth with a username and password
    to acquire tokens.

    Keyword Arguments:
        username: The username for authentication [required].
        password: The password for authentication [required if apikey not specified].
        url: The endpoint for JWT token requests [required].
        apikey: The apikey for authentication [required if password not specified].
        disable_ssl_verification: Disable ssl verification. Defaults to False.
        headers: Headers to be sent with every service token request. Defaults to None.
        proxies: Proxies to use for making request. Defaults to None.
        proxies.http (optional): The proxy endpoint to use for HTTP requests.
        proxies.https (optional): The proxy endpoint to use for HTTPS requests.

    Attributes:
        username (str): The username for authentication.
        password (str): The password for authentication.
        url (str): The endpoint for JWT token requests.
        headers (dict): Headers to be sent with every service token request.
        proxies (dict): Proxies to use for making token requests.
        proxies.http (str): The proxy endpoint to use for HTTP requests.
        proxies.https (str): The proxy endpoint to use for HTTPS requests.
    """
    TOKEN_NAME = 'token'
    VALIDATE_AUTH_PATH = '/dlim/v1/auth/token'

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
        self.username = username
        self.password = password
        self.user_access_token = user_access_token
        if url and not self.VALIDATE_AUTH_PATH in url:
            url = url + '/dlim/v1/auth/token'
        self.apikey = apikey
        self.headers = headers
        if self.headers is None:
            self.headers = {}
        self.headers['Content-Type'] = 'application/json'
        self.proxies = proxies
        self.authorization_header = self.__construct_basic_auth_header()
        super().__init__(url, disable_ssl_verification=disable_ssl_verification)

    def __construct_basic_auth_header(self) -> str:
        authstring = "{0}:{1}".format(self.username, self.password)
        base64_authorization = base64.b64encode(
            authstring.encode('utf-8')).decode('utf-8')
        return 'Basic {0}'.format(base64_authorization)

    def request_token(self) -> dict:
        """Makes a request for a token.
        """
        self.headers['Authorization'] = self.authorization_header
        if self.user_access_token is None:
            response = requests.request(
                method='POST',
                headers=self.headers,
                url=self.url,
                proxies=self.proxies)
            return response.json()
        else:
            return {'user_token': self.user_access_token, 'service_token': self.user_access_token}

    def set_headers(self, headers: Dict[str, str]) -> None:
        """Headers to be sent with every CP4D token request.

        Args:
            headers: The headers to be sent with every CP4D token request.
        """
        if isinstance(headers, dict):
            self.headers = headers
        else:
            raise TypeError('headers must be a dictionary')


    def _save_token_info(self, token_response: dict) -> None:
        """
        Decode the access token and save the response from the JWT service to the object's state
        Refresh time is set to approximately 80% of the token's TTL to ensure that
        the token refresh completes before the current token expires.
        Parameters
        ----------
        token_response : dict
            Response from token service
        """
        self.token_info = token_response
        self.access_token = token_response.get("user_token")


    def set_proxies(self, proxies: Dict[str, str]) -> None:
        """Sets the proxies the token manager will use to communicate with CP4D on behalf of the host.

        Args:
            proxies: Proxies to use for making request. Defaults to None.
            proxies.http (optional): The proxy endpoint to use for HTTP requests.
            proxies.https (optional): The proxy endpoint to use for HTTPS requests.
        """
        if isinstance(proxies, dict):
            self.proxies = proxies
        else:
            raise TypeError('proxies must be a dictionary')