# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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

"""
Unit Tests for PowerCloudApiV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_pvs.power_cloud_api_v1 import *


service = PowerCloudApiV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://power-cloud-api.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: PCloudEvents
##############################################################################
# region

class TestPcloudEventsGetsince():
    """
    Test Class for pcloud_events_getsince
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_events_getsince_all_params(self):
        """
        pcloud_events_getsince()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events')
        mock_response = '{"events": [{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        time = 'testString'
        accept_language = 'testString'

        # Invoke method
        response = service.pcloud_events_getsince(
            cloud_instance_id,
            time,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'time={}'.format(time) in query_string


    @responses.activate
    def test_pcloud_events_getsince_required_params(self):
        """
        test_pcloud_events_getsince_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events')
        mock_response = '{"events": [{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        time = 'testString'

        # Invoke method
        response = service.pcloud_events_getsince(
            cloud_instance_id,
            time,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'time={}'.format(time) in query_string


    @responses.activate
    def test_pcloud_events_getsince_value_error(self):
        """
        test_pcloud_events_getsince_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events')
        mock_response = '{"events": [{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        time = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "time": time,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_events_getsince(**req_copy)



class TestPcloudEventsGet():
    """
    Test Class for pcloud_events_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_events_get_all_params(self):
        """
        pcloud_events_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events/testString')
        mock_response = '{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        event_id = 'testString'
        accept_language = 'testString'

        # Invoke method
        response = service.pcloud_events_get(
            cloud_instance_id,
            event_id,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_events_get_required_params(self):
        """
        test_pcloud_events_get_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events/testString')
        mock_response = '{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        event_id = 'testString'

        # Invoke method
        response = service.pcloud_events_get(
            cloud_instance_id,
            event_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_events_get_value_error(self):
        """
        test_pcloud_events_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/events/testString')
        mock_response = '{"eventID": "event_id", "time": "2019-01-01T12:00:00", "timestamp": 9, "user": {"userID": "user_id", "name": "name", "email": "email"}, "level": "notice", "resource": "resource", "action": "action", "message": "message", "metadata": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        event_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "event_id": event_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_events_get(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudEvents
##############################################################################

##############################################################################
# Start of Service: PCloudImages
##############################################################################
# region

class TestPcloudImagesGetall():
    """
    Test Class for pcloud_images_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_images_getall_all_params(self):
        """
        pcloud_images_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/images')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        sap = True

        # Invoke method
        response = service.pcloud_images_getall(
            sap=sap,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'sap={}'.format('true' if sap else 'false') in query_string


    @responses.activate
    def test_pcloud_images_getall_required_params(self):
        """
        test_pcloud_images_getall_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/images')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.pcloud_images_getall()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPcloudImagesGet():
    """
    Test Class for pcloud_images_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_images_get_all_params(self):
        """
        pcloud_images_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/images/testString')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image_id = 'testString'

        # Invoke method
        response = service.pcloud_images_get(
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_images_get_value_error(self):
        """
        test_pcloud_images_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/images/testString')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_images_get(**req_copy)



class TestPcloudCloudinstancesImagesPost():
    """
    Test Class for pcloud_cloudinstances_images_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_images_post_all_params(self):
        """
        pcloud_cloudinstances_images_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images')
        mock_response = '{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "size": 4, "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "volumes": [{"volumeID": "volume_id", "name": "name", "size": 4, "bootable": true}], "servers": ["servers"], "taskref": {"taskID": "task_id", "href": "href"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        source = 'root-project'
        image_id = 'testString'
        image_name = 'testString'
        image_path = 'testString'
        region = 'testString'
        image_filename = 'testString'
        bucket_name = 'testString'
        access_key = 'testString'
        secret_key = 'testString'
        os_type = 'aix'
        disk_type = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_images_post(
            cloud_instance_id,
            source,
            image_id=image_id,
            image_name=image_name,
            image_path=image_path,
            region=region,
            image_filename=image_filename,
            bucket_name=bucket_name,
            access_key=access_key,
            secret_key=secret_key,
            os_type=os_type,
            disk_type=disk_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == 'root-project'
        assert req_body['imageID'] == 'testString'
        assert req_body['imageName'] == 'testString'
        assert req_body['imagePath'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['imageFilename'] == 'testString'
        assert req_body['bucketName'] == 'testString'
        assert req_body['accessKey'] == 'testString'
        assert req_body['secretKey'] == 'testString'
        assert req_body['osType'] == 'aix'
        assert req_body['diskType'] == 'testString'


    @responses.activate
    def test_pcloud_cloudinstances_images_post_value_error(self):
        """
        test_pcloud_cloudinstances_images_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images')
        mock_response = '{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "size": 4, "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "volumes": [{"volumeID": "volume_id", "name": "name", "size": 4, "bootable": true}], "servers": ["servers"], "taskref": {"taskID": "task_id", "href": "href"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        source = 'root-project'
        image_id = 'testString'
        image_name = 'testString'
        image_path = 'testString'
        region = 'testString'
        image_filename = 'testString'
        bucket_name = 'testString'
        access_key = 'testString'
        secret_key = 'testString'
        os_type = 'aix'
        disk_type = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "source": source,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_images_post(**req_copy)



class TestPcloudCloudinstancesImagesGetall():
    """
    Test Class for pcloud_cloudinstances_images_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_images_getall_all_params(self):
        """
        pcloud_cloudinstances_images_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_images_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_images_getall_value_error(self):
        """
        test_pcloud_cloudinstances_images_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images')
        mock_response = '{"images": [{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "specifications": {"imageType": "image_type", "containerFormat": "container_format", "diskFormat": "disk_format", "operatingSystem": "operating_system", "hypervisorType": "hypervisor_type", "architecture": "architecture", "endianness": "endianness"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_images_getall(**req_copy)



class TestPcloudCloudinstancesImagesGet():
    """
    Test Class for pcloud_cloudinstances_images_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_images_get_all_params(self):
        """
        pcloud_cloudinstances_images_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString')
        mock_response = '{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "size": 4, "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "volumes": [{"volumeID": "volume_id", "name": "name", "size": 4, "bootable": true}], "servers": ["servers"], "taskref": {"taskID": "task_id", "href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_images_get(
            cloud_instance_id,
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_images_get_value_error(self):
        """
        test_pcloud_cloudinstances_images_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString')
        mock_response = '{"imageID": "image_id", "name": "name", "state": "state", "description": "description", "size": 4, "storageType": "storage_type", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "volumes": [{"volumeID": "volume_id", "name": "name", "size": 4, "bootable": true}], "servers": ["servers"], "taskref": {"taskID": "task_id", "href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_images_get(**req_copy)



class TestPcloudCloudinstancesImagesDelete():
    """
    Test Class for pcloud_cloudinstances_images_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_images_delete_all_params(self):
        """
        pcloud_cloudinstances_images_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_images_delete(
            cloud_instance_id,
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_images_delete_value_error(self):
        """
        test_pcloud_cloudinstances_images_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_images_delete(**req_copy)



class TestPcloudCloudinstancesImagesExportPost():
    """
    Test Class for pcloud_cloudinstances_images_export_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_images_export_post_all_params(self):
        """
        pcloud_cloudinstances_images_export_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString/export')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'
        bucket_name = 'testString'
        access_key = 'testString'
        region = 'testString'
        secret_key = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_images_export_post(
            cloud_instance_id,
            image_id,
            bucket_name,
            access_key,
            region=region,
            secret_key=secret_key,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bucketName'] == 'testString'
        assert req_body['accessKey'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['secretKey'] == 'testString'


    @responses.activate
    def test_pcloud_cloudinstances_images_export_post_value_error(self):
        """
        test_pcloud_cloudinstances_images_export_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/images/testString/export')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        image_id = 'testString'
        bucket_name = 'testString'
        access_key = 'testString'
        region = 'testString'
        secret_key = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "image_id": image_id,
            "bucket_name": bucket_name,
            "access_key": access_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_images_export_post(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudImages
##############################################################################

##############################################################################
# Start of Service: PCloudInstances
##############################################################################
# region

class TestPcloudCloudinstancesGet():
    """
    Test Class for pcloud_cloudinstances_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_get_all_params(self):
        """
        pcloud_cloudinstances_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        mock_response = '{"cloudInstanceID": "cloud_instance_id", "name": "name", "tenantID": "tenant_id", "openstackID": "openstack_id", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "usage": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_get(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_get_value_error(self):
        """
        test_pcloud_cloudinstances_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        mock_response = '{"cloudInstanceID": "cloud_instance_id", "name": "name", "tenantID": "tenant_id", "openstackID": "openstack_id", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "usage": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_get(**req_copy)



class TestPcloudCloudinstancesPut():
    """
    Test Class for pcloud_cloudinstances_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_put_all_params(self):
        """
        pcloud_cloudinstances_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        mock_response = '{"cloudInstanceID": "cloud_instance_id", "name": "name", "tenantID": "tenant_id", "openstackID": "openstack_id", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "usage": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        processors = 72.5
        proc_units = 72.5
        memory = 72.5
        instances = 72.5
        storage = 72.5

        # Invoke method
        response = service.pcloud_cloudinstances_put(
            cloud_instance_id,
            processors=processors,
            proc_units=proc_units,
            memory=memory,
            instances=instances,
            storage=storage,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['processors'] == 72.5
        assert req_body['procUnits'] == 72.5
        assert req_body['memory'] == 72.5
        assert req_body['instances'] == 72.5
        assert req_body['storage'] == 72.5


    @responses.activate
    def test_pcloud_cloudinstances_put_value_error(self):
        """
        test_pcloud_cloudinstances_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        mock_response = '{"cloudInstanceID": "cloud_instance_id", "name": "name", "tenantID": "tenant_id", "openstackID": "openstack_id", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "usage": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        processors = 72.5
        proc_units = 72.5
        memory = 72.5
        instances = 72.5
        storage = 72.5

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_put(**req_copy)



class TestPcloudCloudinstancesDelete():
    """
    Test Class for pcloud_cloudinstances_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_delete_all_params(self):
        """
        pcloud_cloudinstances_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_delete(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_delete_value_error(self):
        """
        test_pcloud_cloudinstances_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_delete(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudInstances
##############################################################################

##############################################################################
# Start of Service: PCloudNetworks
##############################################################################
# region

class TestPcloudNetworksPost():
    """
    Test Class for pcloud_networks_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_post_all_params(self):
        """
        pcloud_networks_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a IPAddressRange model
        ip_address_range_model = {}
        ip_address_range_model['startingIPAddress'] = 'testString'
        ip_address_range_model['endingIPAddress'] = 'testString'

        # Set up parameter values
        cloud_instance_id = 'testString'
        type = 'vlan'
        name = 'testString'
        cidr = 'testString'
        gateway = 'testString'
        dns_servers = ['testString']
        ip_address_ranges = [ip_address_range_model]
        jumbo = True

        # Invoke method
        response = service.pcloud_networks_post(
            cloud_instance_id,
            type,
            name=name,
            cidr=cidr,
            gateway=gateway,
            dns_servers=dns_servers,
            ip_address_ranges=ip_address_ranges,
            jumbo=jumbo,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'vlan'
        assert req_body['name'] == 'testString'
        assert req_body['cidr'] == 'testString'
        assert req_body['gateway'] == 'testString'
        assert req_body['dnsServers'] == ['testString']
        assert req_body['ipAddressRanges'] == [ip_address_range_model]
        assert req_body['jumbo'] == True


    @responses.activate
    def test_pcloud_networks_post_value_error(self):
        """
        test_pcloud_networks_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a IPAddressRange model
        ip_address_range_model = {}
        ip_address_range_model['startingIPAddress'] = 'testString'
        ip_address_range_model['endingIPAddress'] = 'testString'

        # Set up parameter values
        cloud_instance_id = 'testString'
        type = 'vlan'
        name = 'testString'
        cidr = 'testString'
        gateway = 'testString'
        dns_servers = ['testString']
        ip_address_ranges = [ip_address_range_model]
        jumbo = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_post(**req_copy)



class TestPcloudNetworksGetall():
    """
    Test Class for pcloud_networks_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_getall_all_params(self):
        """
        pcloud_networks_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks')
        mock_response = '{"networks": [{"networkID": "network_id", "name": "name", "vlanID": 7, "type": "vlan", "jumbo": false, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        filter = 'testString'

        # Invoke method
        response = service.pcloud_networks_getall(
            cloud_instance_id,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string


    @responses.activate
    def test_pcloud_networks_getall_required_params(self):
        """
        test_pcloud_networks_getall_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks')
        mock_response = '{"networks": [{"networkID": "network_id", "name": "name", "vlanID": 7, "type": "vlan", "jumbo": false, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_getall_value_error(self):
        """
        test_pcloud_networks_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks')
        mock_response = '{"networks": [{"networkID": "network_id", "name": "name", "vlanID": 7, "type": "vlan", "jumbo": false, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_getall(**req_copy)



class TestPcloudNetworksGet():
    """
    Test Class for pcloud_networks_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_get_all_params(self):
        """
        pcloud_networks_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_get(
            cloud_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_get_value_error(self):
        """
        test_pcloud_networks_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_get(**req_copy)



class TestPcloudNetworksPut():
    """
    Test Class for pcloud_networks_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_put_all_params(self):
        """
        pcloud_networks_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a IPAddressRange model
        ip_address_range_model = {}
        ip_address_range_model['startingIPAddress'] = 'testString'
        ip_address_range_model['endingIPAddress'] = 'testString'

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        name = 'testString'
        gateway = 'testString'
        dns_servers = ['testString']
        ip_address_ranges = [ip_address_range_model]

        # Invoke method
        response = service.pcloud_networks_put(
            cloud_instance_id,
            network_id,
            name=name,
            gateway=gateway,
            dns_servers=dns_servers,
            ip_address_ranges=ip_address_ranges,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['gateway'] == 'testString'
        assert req_body['dnsServers'] == ['testString']
        assert req_body['ipAddressRanges'] == [ip_address_range_model]


    @responses.activate
    def test_pcloud_networks_put_value_error(self):
        """
        test_pcloud_networks_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        mock_response = '{"networkID": "network_id", "name": "name", "type": "vlan", "vlanID": 7, "cidr": "cidr", "gateway": "gateway", "dnsServers": ["dns_servers"], "ipAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "ipAddressMetrics": {"available": 9, "used": 4, "total": 5, "utilization": 11}, "publicIPAddressRanges": [{"startingIPAddress": "starting_ip_address", "endingIPAddress": "ending_ip_address"}], "jumbo": false}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a IPAddressRange model
        ip_address_range_model = {}
        ip_address_range_model['startingIPAddress'] = 'testString'
        ip_address_range_model['endingIPAddress'] = 'testString'

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        name = 'testString'
        gateway = 'testString'
        dns_servers = ['testString']
        ip_address_ranges = [ip_address_range_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_put(**req_copy)



class TestPcloudNetworksDelete():
    """
    Test Class for pcloud_networks_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_delete_all_params(self):
        """
        pcloud_networks_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_delete(
            cloud_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_delete_value_error(self):
        """
        test_pcloud_networks_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_delete(**req_copy)



class TestPcloudNetworksPortsPost():
    """
    Test Class for pcloud_networks_ports_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_ports_post_all_params(self):
        """
        pcloud_networks_ports_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        description = 'testString'
        ip_address = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_post(
            cloud_instance_id,
            network_id,
            description=description,
            ip_address=ip_address,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'
        assert req_body['ipAddress'] == 'testString'


    @responses.activate
    def test_pcloud_networks_ports_post_required_params(self):
        """
        test_pcloud_networks_ports_post_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_post(
            cloud_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_pcloud_networks_ports_post_value_error(self):
        """
        test_pcloud_networks_ports_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_ports_post(**req_copy)



class TestPcloudNetworksPortsGetall():
    """
    Test Class for pcloud_networks_ports_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_ports_getall_all_params(self):
        """
        pcloud_networks_ports_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports')
        mock_response = '{"ports": [{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_getall(
            cloud_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_ports_getall_value_error(self):
        """
        test_pcloud_networks_ports_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports')
        mock_response = '{"ports": [{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_ports_getall(**req_copy)



class TestPcloudNetworksPortsGet():
    """
    Test Class for pcloud_networks_ports_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_ports_get_all_params(self):
        """
        pcloud_networks_ports_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'
        accept = 'application/json'

        # Invoke method
        response = service.pcloud_networks_ports_get(
            cloud_instance_id,
            network_id,
            port_id,
            accept=accept,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_ports_get_required_params(self):
        """
        test_pcloud_networks_ports_get_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_get(
            cloud_instance_id,
            network_id,
            port_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_ports_get_value_error(self):
        """
        test_pcloud_networks_ports_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
            "port_id": port_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_ports_get(**req_copy)



class TestPcloudNetworksPortsPut():
    """
    Test Class for pcloud_networks_ports_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_ports_put_all_params(self):
        """
        pcloud_networks_ports_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'
        description = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_put(
            cloud_instance_id,
            network_id,
            port_id,
            description=description,
            pvm_instance_id=pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'
        assert req_body['pvmInstanceID'] == 'testString'


    @responses.activate
    def test_pcloud_networks_ports_put_value_error(self):
        """
        test_pcloud_networks_ports_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        mock_response = '{"portID": "port_id", "description": "description", "status": "status", "macAddress": "mac_address", "ipAddress": "ip_address", "pvmInstance": {"pvmInstanceID": "pvm_instance_id", "href": "href"}, "href": "href"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'
        description = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
            "port_id": port_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_ports_put(**req_copy)



class TestPcloudNetworksPortsDelete():
    """
    Test Class for pcloud_networks_ports_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_networks_ports_delete_all_params(self):
        """
        pcloud_networks_ports_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'

        # Invoke method
        response = service.pcloud_networks_ports_delete(
            cloud_instance_id,
            network_id,
            port_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_networks_ports_delete_value_error(self):
        """
        test_pcloud_networks_ports_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/networks/testString/ports/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        network_id = 'testString'
        port_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "network_id": network_id,
            "port_id": port_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_networks_ports_delete(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudNetworks
##############################################################################

##############################################################################
# Start of Service: PCloudPVMInstances
##############################################################################
# region

class TestPcloudPvminstancesPost():
    """
    Test Class for pcloud_pvminstances_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_post_all_params(self):
        """
        pcloud_pvminstances_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances')
        mock_response = '[{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model = {}
        pvm_instance_add_network_model['networkID'] = 'testString'
        pvm_instance_add_network_model['ipAddress'] = 'testString'

        # Construct a dict representation of a PVMInstanceCreateSoftwareLicenses model
        pvm_instance_create_software_licenses_model = {}
        pvm_instance_create_software_licenses_model['ibmiCSS'] = True
        pvm_instance_create_software_licenses_model['ibmiPHA'] = True
        pvm_instance_create_software_licenses_model['ibmiRDS'] = True
        pvm_instance_create_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_create_software_licenses_model['ibmiDBQ'] = True

        # Construct a dict representation of a VirtualCores model
        virtual_cores_model = {}
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Set up parameter values
        cloud_instance_id = 'testString'
        server_name = 'testString'
        image_id = 'testString'
        processors = 72.5
        proc_type = 'dedicated'
        memory = 72.5
        replicants = 72.5
        replicant_naming_scheme = 'prefix'
        replicant_affinity_policy = 'affinity'
        network_i_ds = ['testString']
        networks = [pvm_instance_add_network_model]
        volume_i_ds = ['testString']
        key_pair_name = 'testString'
        sys_type = 'testString'
        migratable = True
        user_data = 'testString'
        storage_type = 'testString'
        software_licenses = pvm_instance_create_software_licenses_model
        pin_policy = 'none'
        virtual_cores = virtual_cores_model
        skip_host_validation = True

        # Invoke method
        response = service.pcloud_pvminstances_post(
            cloud_instance_id,
            server_name,
            image_id,
            processors,
            proc_type,
            memory,
            replicants=replicants,
            replicant_naming_scheme=replicant_naming_scheme,
            replicant_affinity_policy=replicant_affinity_policy,
            network_i_ds=network_i_ds,
            networks=networks,
            volume_i_ds=volume_i_ds,
            key_pair_name=key_pair_name,
            sys_type=sys_type,
            migratable=migratable,
            user_data=user_data,
            storage_type=storage_type,
            software_licenses=software_licenses,
            pin_policy=pin_policy,
            virtual_cores=virtual_cores,
            skip_host_validation=skip_host_validation,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'skipHostValidation={}'.format('true' if skip_host_validation else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['serverName'] == 'testString'
        assert req_body['imageID'] == 'testString'
        assert req_body['processors'] == 72.5
        assert req_body['procType'] == 'dedicated'
        assert req_body['memory'] == 72.5
        assert req_body['replicants'] == 72.5
        assert req_body['replicantNamingScheme'] == 'prefix'
        assert req_body['replicantAffinityPolicy'] == 'affinity'
        assert req_body['networkIDs'] == ['testString']
        assert req_body['networks'] == [pvm_instance_add_network_model]
        assert req_body['volumeIDs'] == ['testString']
        assert req_body['keyPairName'] == 'testString'
        assert req_body['sysType'] == 'testString'
        assert req_body['migratable'] == True
        assert req_body['userData'] == 'testString'
        assert req_body['storageType'] == 'testString'
        assert req_body['softwareLicenses'] == pvm_instance_create_software_licenses_model
        assert req_body['pinPolicy'] == 'none'
        assert req_body['virtualCores'] == virtual_cores_model


    @responses.activate
    def test_pcloud_pvminstances_post_required_params(self):
        """
        test_pcloud_pvminstances_post_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances')
        mock_response = '[{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model = {}
        pvm_instance_add_network_model['networkID'] = 'testString'
        pvm_instance_add_network_model['ipAddress'] = 'testString'

        # Construct a dict representation of a PVMInstanceCreateSoftwareLicenses model
        pvm_instance_create_software_licenses_model = {}
        pvm_instance_create_software_licenses_model['ibmiCSS'] = True
        pvm_instance_create_software_licenses_model['ibmiPHA'] = True
        pvm_instance_create_software_licenses_model['ibmiRDS'] = True
        pvm_instance_create_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_create_software_licenses_model['ibmiDBQ'] = True

        # Construct a dict representation of a VirtualCores model
        virtual_cores_model = {}
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Set up parameter values
        cloud_instance_id = 'testString'
        server_name = 'testString'
        image_id = 'testString'
        processors = 72.5
        proc_type = 'dedicated'
        memory = 72.5
        replicants = 72.5
        replicant_naming_scheme = 'prefix'
        replicant_affinity_policy = 'affinity'
        network_i_ds = ['testString']
        networks = [pvm_instance_add_network_model]
        volume_i_ds = ['testString']
        key_pair_name = 'testString'
        sys_type = 'testString'
        migratable = True
        user_data = 'testString'
        storage_type = 'testString'
        software_licenses = pvm_instance_create_software_licenses_model
        pin_policy = 'none'
        virtual_cores = virtual_cores_model

        # Invoke method
        response = service.pcloud_pvminstances_post(
            cloud_instance_id,
            server_name,
            image_id,
            processors,
            proc_type,
            memory,
            replicants=replicants,
            replicant_naming_scheme=replicant_naming_scheme,
            replicant_affinity_policy=replicant_affinity_policy,
            network_i_ds=network_i_ds,
            networks=networks,
            volume_i_ds=volume_i_ds,
            key_pair_name=key_pair_name,
            sys_type=sys_type,
            migratable=migratable,
            user_data=user_data,
            storage_type=storage_type,
            software_licenses=software_licenses,
            pin_policy=pin_policy,
            virtual_cores=virtual_cores,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['serverName'] == 'testString'
        assert req_body['imageID'] == 'testString'
        assert req_body['processors'] == 72.5
        assert req_body['procType'] == 'dedicated'
        assert req_body['memory'] == 72.5
        assert req_body['replicants'] == 72.5
        assert req_body['replicantNamingScheme'] == 'prefix'
        assert req_body['replicantAffinityPolicy'] == 'affinity'
        assert req_body['networkIDs'] == ['testString']
        assert req_body['networks'] == [pvm_instance_add_network_model]
        assert req_body['volumeIDs'] == ['testString']
        assert req_body['keyPairName'] == 'testString'
        assert req_body['sysType'] == 'testString'
        assert req_body['migratable'] == True
        assert req_body['userData'] == 'testString'
        assert req_body['storageType'] == 'testString'
        assert req_body['softwareLicenses'] == pvm_instance_create_software_licenses_model
        assert req_body['pinPolicy'] == 'none'
        assert req_body['virtualCores'] == virtual_cores_model


    @responses.activate
    def test_pcloud_pvminstances_post_value_error(self):
        """
        test_pcloud_pvminstances_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances')
        mock_response = '[{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model = {}
        pvm_instance_add_network_model['networkID'] = 'testString'
        pvm_instance_add_network_model['ipAddress'] = 'testString'

        # Construct a dict representation of a PVMInstanceCreateSoftwareLicenses model
        pvm_instance_create_software_licenses_model = {}
        pvm_instance_create_software_licenses_model['ibmiCSS'] = True
        pvm_instance_create_software_licenses_model['ibmiPHA'] = True
        pvm_instance_create_software_licenses_model['ibmiRDS'] = True
        pvm_instance_create_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_create_software_licenses_model['ibmiDBQ'] = True

        # Construct a dict representation of a VirtualCores model
        virtual_cores_model = {}
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Set up parameter values
        cloud_instance_id = 'testString'
        server_name = 'testString'
        image_id = 'testString'
        processors = 72.5
        proc_type = 'dedicated'
        memory = 72.5
        replicants = 72.5
        replicant_naming_scheme = 'prefix'
        replicant_affinity_policy = 'affinity'
        network_i_ds = ['testString']
        networks = [pvm_instance_add_network_model]
        volume_i_ds = ['testString']
        key_pair_name = 'testString'
        sys_type = 'testString'
        migratable = True
        user_data = 'testString'
        storage_type = 'testString'
        software_licenses = pvm_instance_create_software_licenses_model
        pin_policy = 'none'
        virtual_cores = virtual_cores_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "server_name": server_name,
            "image_id": image_id,
            "processors": processors,
            "proc_type": proc_type,
            "memory": memory,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_post(**req_copy)



class TestPcloudPvminstancesGetall():
    """
    Test Class for pcloud_pvminstances_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_getall_all_params(self):
        """
        pcloud_pvminstances_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances')
        mock_response = '{"pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_getall_value_error(self):
        """
        test_pcloud_pvminstances_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances')
        mock_response = '{"pvmInstances": [{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "href": "href", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_getall(**req_copy)



class TestPcloudPvminstancesGet():
    """
    Test Class for pcloud_pvminstances_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_get_all_params(self):
        """
        pcloud_pvminstances_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        mock_response = '{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_get(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_get_value_error(self):
        """
        test_pcloud_pvminstances_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        mock_response = '{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_get(**req_copy)



class TestPcloudPvminstancesPut():
    """
    Test Class for pcloud_pvminstances_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_put_all_params(self):
        """
        pcloud_pvminstances_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        mock_response = '{"serverName": "server_name", "statusUrl": "status_url", "processors": 10, "procType": "dedicated", "memory": 6, "pinPolicy": "none"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a PVMInstanceUpdateSoftwareLicenses model
        pvm_instance_update_software_licenses_model = {}
        pvm_instance_update_software_licenses_model['ibmiCSS'] = True
        pvm_instance_update_software_licenses_model['ibmiPHA'] = True
        pvm_instance_update_software_licenses_model['ibmiRDS'] = True
        pvm_instance_update_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_update_software_licenses_model['ibmiDBQ'] = True

        # Construct a dict representation of a VirtualCores model
        virtual_cores_model = {}
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        server_name = 'testString'
        processors = 72.5
        proc_type = 'dedicated'
        memory = 72.5
        migratable = True
        software_licenses = pvm_instance_update_software_licenses_model
        pin_policy = 'none'
        sap_profile_id = 'testString'
        virtual_cores = virtual_cores_model

        # Invoke method
        response = service.pcloud_pvminstances_put(
            cloud_instance_id,
            pvm_instance_id,
            server_name=server_name,
            processors=processors,
            proc_type=proc_type,
            memory=memory,
            migratable=migratable,
            software_licenses=software_licenses,
            pin_policy=pin_policy,
            sap_profile_id=sap_profile_id,
            virtual_cores=virtual_cores,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['serverName'] == 'testString'
        assert req_body['processors'] == 72.5
        assert req_body['procType'] == 'dedicated'
        assert req_body['memory'] == 72.5
        assert req_body['migratable'] == True
        assert req_body['softwareLicenses'] == pvm_instance_update_software_licenses_model
        assert req_body['pinPolicy'] == 'none'
        assert req_body['sapProfileID'] == 'testString'
        assert req_body['virtualCores'] == virtual_cores_model


    @responses.activate
    def test_pcloud_pvminstances_put_value_error(self):
        """
        test_pcloud_pvminstances_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        mock_response = '{"serverName": "server_name", "statusUrl": "status_url", "processors": 10, "procType": "dedicated", "memory": 6, "pinPolicy": "none"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a PVMInstanceUpdateSoftwareLicenses model
        pvm_instance_update_software_licenses_model = {}
        pvm_instance_update_software_licenses_model['ibmiCSS'] = True
        pvm_instance_update_software_licenses_model['ibmiPHA'] = True
        pvm_instance_update_software_licenses_model['ibmiRDS'] = True
        pvm_instance_update_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_update_software_licenses_model['ibmiDBQ'] = True

        # Construct a dict representation of a VirtualCores model
        virtual_cores_model = {}
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        server_name = 'testString'
        processors = 72.5
        proc_type = 'dedicated'
        memory = 72.5
        migratable = True
        software_licenses = pvm_instance_update_software_licenses_model
        pin_policy = 'none'
        sap_profile_id = 'testString'
        virtual_cores = virtual_cores_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_put(**req_copy)



class TestPcloudPvminstancesDelete():
    """
    Test Class for pcloud_pvminstances_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_delete_all_params(self):
        """
        pcloud_pvminstances_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_delete(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_delete_value_error(self):
        """
        test_pcloud_pvminstances_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_delete(**req_copy)



class TestPcloudPvminstancesNetworksPost():
    """
    Test Class for pcloud_pvminstances_networks_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_networks_post_all_params(self):
        """
        pcloud_pvminstances_networks_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks')
        mock_response = '{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'
        ip_address = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_networks_post(
            cloud_instance_id,
            pvm_instance_id,
            network_id,
            ip_address=ip_address,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['networkID'] == 'testString'
        assert req_body['ipAddress'] == 'testString'


    @responses.activate
    def test_pcloud_pvminstances_networks_post_value_error(self):
        """
        test_pcloud_pvminstances_networks_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks')
        mock_response = '{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'
        ip_address = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_networks_post(**req_copy)



class TestPcloudPvminstancesNetworksGetall():
    """
    Test Class for pcloud_pvminstances_networks_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_networks_getall_all_params(self):
        """
        pcloud_pvminstances_networks_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks')
        mock_response = '{"networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_networks_getall(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_networks_getall_value_error(self):
        """
        test_pcloud_pvminstances_networks_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks')
        mock_response = '{"networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_networks_getall(**req_copy)



class TestPcloudPvminstancesNetworksGet():
    """
    Test Class for pcloud_pvminstances_networks_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_networks_get_all_params(self):
        """
        pcloud_pvminstances_networks_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks/testString')
        mock_response = '{"networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_networks_get(
            cloud_instance_id,
            pvm_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_networks_get_value_error(self):
        """
        test_pcloud_pvminstances_networks_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks/testString')
        mock_response = '{"networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_networks_get(**req_copy)



class TestPcloudPvminstancesNetworksDelete():
    """
    Test Class for pcloud_pvminstances_networks_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_networks_delete_all_params(self):
        """
        pcloud_pvminstances_networks_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'
        mac_address = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_networks_delete(
            cloud_instance_id,
            pvm_instance_id,
            network_id,
            mac_address=mac_address,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['macAddress'] == 'testString'


    @responses.activate
    def test_pcloud_pvminstances_networks_delete_required_params(self):
        """
        test_pcloud_pvminstances_networks_delete_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_networks_delete(
            cloud_instance_id,
            pvm_instance_id,
            network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_networks_delete_value_error(self):
        """
        test_pcloud_pvminstances_networks_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/networks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "network_id": network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_networks_delete(**req_copy)



class TestPcloudPvminstancesOperationsPost():
    """
    Test Class for pcloud_pvminstances_operations_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_operations_post_all_params(self):
        """
        pcloud_pvminstances_operations_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/operations')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Operations model
        operations_model = {}
        operations_model['bootMode'] = 'a'
        operations_model['operatingMode'] = 'normal'
        operations_model['task'] = 'dston'

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        operation_type = 'job'
        operation = operations_model

        # Invoke method
        response = service.pcloud_pvminstances_operations_post(
            cloud_instance_id,
            pvm_instance_id,
            operation_type,
            operation,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['operationType'] == 'job'
        assert req_body['operation'] == operations_model


    @responses.activate
    def test_pcloud_pvminstances_operations_post_value_error(self):
        """
        test_pcloud_pvminstances_operations_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/operations')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Operations model
        operations_model = {}
        operations_model['bootMode'] = 'a'
        operations_model['operatingMode'] = 'normal'
        operations_model['task'] = 'dston'

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        operation_type = 'job'
        operation = operations_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "operation_type": operation_type,
            "operation": operation,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_operations_post(**req_copy)



class TestPcloudPvminstancesActionPost():
    """
    Test Class for pcloud_pvminstances_action_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_action_post_all_params(self):
        """
        pcloud_pvminstances_action_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/action')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        action = 'start'

        # Invoke method
        response = service.pcloud_pvminstances_action_post(
            cloud_instance_id,
            pvm_instance_id,
            action,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'start'


    @responses.activate
    def test_pcloud_pvminstances_action_post_value_error(self):
        """
        test_pcloud_pvminstances_action_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/action')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        action = 'start'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "action": action,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_action_post(**req_copy)



class TestPcloudPvminstancesCapturePost():
    """
    Test Class for pcloud_pvminstances_capture_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_capture_post_all_params(self):
        """
        pcloud_pvminstances_capture_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/capture')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        capture_name = 'testString'
        capture_destination = 'image-catalog'
        capture_volume_i_ds = ['testString']
        cloud_storage_image_path = 'testString'
        cloud_storage_region = 'testString'
        cloud_storage_access_key = 'testString'
        cloud_storage_secret_key = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_capture_post(
            cloud_instance_id,
            pvm_instance_id,
            capture_name,
            capture_destination,
            capture_volume_i_ds=capture_volume_i_ds,
            cloud_storage_image_path=cloud_storage_image_path,
            cloud_storage_region=cloud_storage_region,
            cloud_storage_access_key=cloud_storage_access_key,
            cloud_storage_secret_key=cloud_storage_secret_key,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['captureName'] == 'testString'
        assert req_body['captureDestination'] == 'image-catalog'
        assert req_body['captureVolumeIDs'] == ['testString']
        assert req_body['cloudStorageImagePath'] == 'testString'
        assert req_body['cloudStorageRegion'] == 'testString'
        assert req_body['cloudStorageAccessKey'] == 'testString'
        assert req_body['cloudStorageSecretKey'] == 'testString'


    @responses.activate
    def test_pcloud_pvminstances_capture_post_value_error(self):
        """
        test_pcloud_pvminstances_capture_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/capture')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        capture_name = 'testString'
        capture_destination = 'image-catalog'
        capture_volume_i_ds = ['testString']
        cloud_storage_image_path = 'testString'
        cloud_storage_region = 'testString'
        cloud_storage_access_key = 'testString'
        cloud_storage_secret_key = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "capture_name": capture_name,
            "capture_destination": capture_destination,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_capture_post(**req_copy)



class TestPcloudPvminstancesConsolePost():
    """
    Test Class for pcloud_pvminstances_console_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_console_post_all_params(self):
        """
        pcloud_pvminstances_console_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/console')
        mock_response = '{"consoleURL": "console_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_console_post(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_pcloud_pvminstances_console_post_value_error(self):
        """
        test_pcloud_pvminstances_console_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/console')
        mock_response = '{"consoleURL": "console_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_console_post(**req_copy)



class TestPcloudPvminstancesSnapshotsPost():
    """
    Test Class for pcloud_pvminstances_snapshots_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_snapshots_post_all_params(self):
        """
        pcloud_pvminstances_snapshots_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots')
        mock_response = '{"snapshotID": "snapshot_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        volume_i_ds = ['testString']

        # Invoke method
        response = service.pcloud_pvminstances_snapshots_post(
            cloud_instance_id,
            pvm_instance_id,
            name,
            description=description,
            volume_i_ds=volume_i_ds,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['volumeIDs'] == ['testString']


    @responses.activate
    def test_pcloud_pvminstances_snapshots_post_value_error(self):
        """
        test_pcloud_pvminstances_snapshots_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots')
        mock_response = '{"snapshotID": "snapshot_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        volume_i_ds = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_snapshots_post(**req_copy)



class TestPcloudPvminstancesSnapshotsGetall():
    """
    Test Class for pcloud_pvminstances_snapshots_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_snapshots_getall_all_params(self):
        """
        pcloud_pvminstances_snapshots_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots')
        mock_response = '{"snapshots": [{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_snapshots_getall(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_snapshots_getall_value_error(self):
        """
        test_pcloud_pvminstances_snapshots_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots')
        mock_response = '{"snapshots": [{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_snapshots_getall(**req_copy)



class TestPcloudPvminstancesSnapshotsRestorePost():
    """
    Test Class for pcloud_pvminstances_snapshots_restore_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_snapshots_restore_post_all_params(self):
        """
        pcloud_pvminstances_snapshots_restore_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots/testString/restore')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        snapshot_id = 'testString'
        force = True
        restore_fail_action = 'retry'

        # Invoke method
        response = service.pcloud_pvminstances_snapshots_restore_post(
            cloud_instance_id,
            pvm_instance_id,
            snapshot_id,
            force=force,
            restore_fail_action=restore_fail_action,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'restore_fail_action={}'.format(restore_fail_action) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['force'] == True


    @responses.activate
    def test_pcloud_pvminstances_snapshots_restore_post_required_params(self):
        """
        test_pcloud_pvminstances_snapshots_restore_post_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots/testString/restore')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        snapshot_id = 'testString'
        force = True

        # Invoke method
        response = service.pcloud_pvminstances_snapshots_restore_post(
            cloud_instance_id,
            pvm_instance_id,
            snapshot_id,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['force'] == True


    @responses.activate
    def test_pcloud_pvminstances_snapshots_restore_post_value_error(self):
        """
        test_pcloud_pvminstances_snapshots_restore_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/snapshots/testString/restore')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        snapshot_id = 'testString'
        force = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "snapshot_id": snapshot_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_snapshots_restore_post(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudPVMInstances
##############################################################################

##############################################################################
# Start of Service: PCloudSAP
##############################################################################
# region

class TestPcloudSapGetall():
    """
    Test Class for pcloud_sap_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_sap_getall_all_params(self):
        """
        pcloud_sap_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap')
        mock_response = '{"profiles": [{"profileID": "profile_id", "type": "balanced", "cores": 5, "memory": 6, "certified": false}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_sap_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_sap_getall_value_error(self):
        """
        test_pcloud_sap_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap')
        mock_response = '{"profiles": [{"profileID": "profile_id", "type": "balanced", "cores": 5, "memory": 6, "certified": false}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_sap_getall(**req_copy)



class TestPcloudSapPost():
    """
    Test Class for pcloud_sap_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_sap_post_all_params(self):
        """
        pcloud_sap_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap')
        mock_response = '[{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model = {}
        pvm_instance_add_network_model['networkID'] = 'testString'
        pvm_instance_add_network_model['ipAddress'] = 'testString'

        # Construct a dict representation of a PVMInstanceMultiCreate model
        pvm_instance_multi_create_model = {}
        pvm_instance_multi_create_model['count'] = 38
        pvm_instance_multi_create_model['affinityPolicy'] = 'affinity'
        pvm_instance_multi_create_model['numerical'] = 'prefix'

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        image_id = 'testString'
        profile_id = 'testString'
        networks = [pvm_instance_add_network_model]
        volume_i_ds = ['testString']
        instances = pvm_instance_multi_create_model
        ssh_key_name = 'testString'
        user_data = 'testString'
        pin_policy = 'none'

        # Invoke method
        response = service.pcloud_sap_post(
            cloud_instance_id,
            name,
            image_id,
            profile_id,
            networks,
            volume_i_ds=volume_i_ds,
            instances=instances,
            ssh_key_name=ssh_key_name,
            user_data=user_data,
            pin_policy=pin_policy,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['imageID'] == 'testString'
        assert req_body['profileID'] == 'testString'
        assert req_body['networks'] == [pvm_instance_add_network_model]
        assert req_body['volumeIDs'] == ['testString']
        assert req_body['instances'] == pvm_instance_multi_create_model
        assert req_body['sshKeyName'] == 'testString'
        assert req_body['userData'] == 'testString'
        assert req_body['pinPolicy'] == 'none'


    @responses.activate
    def test_pcloud_sap_post_value_error(self):
        """
        test_pcloud_sap_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap')
        mock_response = '[{"pvmInstanceID": "pvm_instance_id", "serverName": "server_name", "imageID": "image_id", "processors": 10, "minproc": 7, "maxproc": 7, "procType": "dedicated", "memory": 6, "minmem": 6, "maxmem": 6, "diskSize": 9, "networkIDs": ["network_i_ds"], "volumeIDs": ["volume_i_ds"], "addresses": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "networks": [{"version": 7, "networkID": "network_id", "networkName": "network_name", "macAddress": "mac_address", "type": "type", "ip": "ip", "ipAddress": "ip_address", "externalIP": "external_ip", "href": "href"}], "status": "status", "progress": 8, "fault": {"code": 4, "details": "details", "message": "message", "created": "2019-01-01T12:00:00"}, "creationDate": "2019-01-01T12:00:00", "updatedDate": "2019-01-01T12:00:00", "sysType": "sys_type", "health": {"status": "status", "lastUpdate": "last_update", "reason": "reason"}, "migratable": true, "storageType": "storage_type", "softwareLicenses": {"ibmiCSS": true, "ibmiPHA": true, "ibmiRDS": true, "ibmiRDSUsers": 14, "ibmiDBQ": true}, "srcs": [[{"mapKey": {"anyKey": "anyValue"}}]], "pinPolicy": "pin_policy", "osType": "os_type", "operatingSystem": "operating_system", "sapProfile": {"profileID": "profile_id", "href": "href"}, "virtualCores": {"min": 3, "max": 3, "assigned": 1}}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model = {}
        pvm_instance_add_network_model['networkID'] = 'testString'
        pvm_instance_add_network_model['ipAddress'] = 'testString'

        # Construct a dict representation of a PVMInstanceMultiCreate model
        pvm_instance_multi_create_model = {}
        pvm_instance_multi_create_model['count'] = 38
        pvm_instance_multi_create_model['affinityPolicy'] = 'affinity'
        pvm_instance_multi_create_model['numerical'] = 'prefix'

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        image_id = 'testString'
        profile_id = 'testString'
        networks = [pvm_instance_add_network_model]
        volume_i_ds = ['testString']
        instances = pvm_instance_multi_create_model
        ssh_key_name = 'testString'
        user_data = 'testString'
        pin_policy = 'none'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "name": name,
            "image_id": image_id,
            "profile_id": profile_id,
            "networks": networks,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_sap_post(**req_copy)



class TestPcloudSapGet():
    """
    Test Class for pcloud_sap_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_sap_get_all_params(self):
        """
        pcloud_sap_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap/testString')
        mock_response = '{"profileID": "profile_id", "type": "balanced", "cores": 5, "memory": 6, "certified": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        sap_profile_id = 'testString'

        # Invoke method
        response = service.pcloud_sap_get(
            cloud_instance_id,
            sap_profile_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_sap_get_value_error(self):
        """
        test_pcloud_sap_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/sap/testString')
        mock_response = '{"profileID": "profile_id", "type": "balanced", "cores": 5, "memory": 6, "certified": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        sap_profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "sap_profile_id": sap_profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_sap_get(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudSAP
##############################################################################

##############################################################################
# Start of Service: PCloudSnapshots
##############################################################################
# region

class TestPcloudCloudinstancesSnapshotsGetall():
    """
    Test Class for pcloud_cloudinstances_snapshots_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_snapshots_getall_all_params(self):
        """
        pcloud_cloudinstances_snapshots_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots')
        mock_response = '{"snapshots": [{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_snapshots_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_snapshots_getall_value_error(self):
        """
        test_pcloud_cloudinstances_snapshots_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots')
        mock_response = '{"snapshots": [{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_snapshots_getall(**req_copy)



class TestPcloudCloudinstancesSnapshotsGet():
    """
    Test Class for pcloud_cloudinstances_snapshots_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_snapshots_get_all_params(self):
        """
        pcloud_cloudinstances_snapshots_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        mock_response = '{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_snapshots_get(
            cloud_instance_id,
            snapshot_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_snapshots_get_value_error(self):
        """
        test_pcloud_cloudinstances_snapshots_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        mock_response = '{"snapshotID": "snapshot_id", "pvmInstanceID": "pvm_instance_id", "name": "name", "description": "description", "status": "status", "volumeSnapshots": {"mapKey": "inner"}, "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "action": "action", "percentComplete": 16}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "snapshot_id": snapshot_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_snapshots_get(**req_copy)



class TestPcloudCloudinstancesSnapshotsPut():
    """
    Test Class for pcloud_cloudinstances_snapshots_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_snapshots_put_all_params(self):
        """
        pcloud_cloudinstances_snapshots_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_snapshots_put(
            cloud_instance_id,
            snapshot_id,
            name=name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_pcloud_cloudinstances_snapshots_put_value_error(self):
        """
        test_pcloud_cloudinstances_snapshots_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "snapshot_id": snapshot_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_snapshots_put(**req_copy)



class TestPcloudCloudinstancesSnapshotsDelete():
    """
    Test Class for pcloud_cloudinstances_snapshots_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_snapshots_delete_all_params(self):
        """
        pcloud_cloudinstances_snapshots_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_snapshots_delete(
            cloud_instance_id,
            snapshot_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_pcloud_cloudinstances_snapshots_delete_value_error(self):
        """
        test_pcloud_cloudinstances_snapshots_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/snapshots/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        snapshot_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "snapshot_id": snapshot_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_snapshots_delete(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudSnapshots
##############################################################################

##############################################################################
# Start of Service: PCloudSystemPools
##############################################################################
# region

class TestPcloudSystempoolsGet():
    """
    Test Class for pcloud_systempools_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_systempools_get_all_params(self):
        """
        pcloud_systempools_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/system-pools')
        mock_response = '{"mapKey": {"systems": [{"cores": 5, "id": 2, "memory": 6}], "sharedCoreRatio": {"min": 3, "max": 3, "default": 7}, "maxAvailable": {"cores": 5, "id": 2, "memory": 6}, "capacity": {"cores": 5, "id": 2, "memory": 6}, "maxCoresAvailable": {"cores": 5, "id": 2, "memory": 6}, "maxMemoryAvailable": {"cores": 5, "id": 2, "memory": 6}, "coreMemoryRatio": 17, "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_systempools_get(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_systempools_get_value_error(self):
        """
        test_pcloud_systempools_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/system-pools')
        mock_response = '{"mapKey": {"systems": [{"cores": 5, "id": 2, "memory": 6}], "sharedCoreRatio": {"min": 3, "max": 3, "default": 7}, "maxAvailable": {"cores": 5, "id": 2, "memory": 6}, "capacity": {"cores": 5, "id": 2, "memory": 6}, "maxCoresAvailable": {"cores": 5, "id": 2, "memory": 6}, "maxMemoryAvailable": {"cores": 5, "id": 2, "memory": 6}, "coreMemoryRatio": 17, "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_systempools_get(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudSystemPools
##############################################################################

##############################################################################
# Start of Service: PCloudTasks
##############################################################################
# region

class TestPcloudTasksGet():
    """
    Test Class for pcloud_tasks_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tasks_get_all_params(self):
        """
        pcloud_tasks_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tasks/testString')
        mock_response = '{"taskID": "task_id", "operation": "operation", "cloudInstanceID": "cloud_instance_id", "componentType": "component_type", "componentID": "component_id", "status": "status", "statusDetail": "status_detail", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        task_id = 'testString'

        # Invoke method
        response = service.pcloud_tasks_get(
            task_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tasks_get_value_error(self):
        """
        test_pcloud_tasks_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tasks/testString')
        mock_response = '{"taskID": "task_id", "operation": "operation", "cloudInstanceID": "cloud_instance_id", "componentType": "component_type", "componentID": "component_id", "status": "status", "statusDetail": "status_detail", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        task_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "task_id": task_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tasks_get(**req_copy)



class TestPcloudTasksDelete():
    """
    Test Class for pcloud_tasks_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tasks_delete_all_params(self):
        """
        pcloud_tasks_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tasks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        task_id = 'testString'

        # Invoke method
        response = service.pcloud_tasks_delete(
            task_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tasks_delete_value_error(self):
        """
        test_pcloud_tasks_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tasks/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        task_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "task_id": task_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tasks_delete(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudTasks
##############################################################################

##############################################################################
# Start of Service: PCloudTenants
##############################################################################
# region

class TestPcloudTenantsGet():
    """
    Test Class for pcloud_tenants_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_get_all_params(self):
        """
        pcloud_tenants_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString')
        mock_response = '{"tenantID": "tenant_id", "enabled": false, "creationDate": "2019-01-01T12:00:00", "sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}], "cloudInstances": [{"cloudInstanceID": "cloud_instance_id", "name": "name", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "href": "href"}], "icn": "icn", "peeringNetworks": [{"projectName": "project_name", "cidr": "cidr", "dnsServers": ["dns_servers"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'

        # Invoke method
        response = service.pcloud_tenants_get(
            tenant_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tenants_get_value_error(self):
        """
        test_pcloud_tenants_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString')
        mock_response = '{"tenantID": "tenant_id", "enabled": false, "creationDate": "2019-01-01T12:00:00", "sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}], "cloudInstances": [{"cloudInstanceID": "cloud_instance_id", "name": "name", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "href": "href"}], "icn": "icn", "peeringNetworks": [{"projectName": "project_name", "cidr": "cidr", "dnsServers": ["dns_servers"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_get(**req_copy)



class TestPcloudTenantsPut():
    """
    Test Class for pcloud_tenants_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_put_all_params(self):
        """
        pcloud_tenants_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString')
        mock_response = '{"tenantID": "tenant_id", "enabled": false, "creationDate": "2019-01-01T12:00:00", "sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}], "cloudInstances": [{"cloudInstanceID": "cloud_instance_id", "name": "name", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "href": "href"}], "icn": "icn", "peeringNetworks": [{"projectName": "project_name", "cidr": "cidr", "dnsServers": ["dns_servers"]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PeeringNetwork model
        peering_network_model = {}
        peering_network_model['projectName'] = 'testString'
        peering_network_model['cidr'] = 'testString'
        peering_network_model['dnsServers'] = ['testString']

        # Set up parameter values
        tenant_id = 'testString'
        icn = 'testString'
        peering_networks = [peering_network_model]

        # Invoke method
        response = service.pcloud_tenants_put(
            tenant_id,
            icn=icn,
            peering_networks=peering_networks,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['icn'] == 'testString'
        assert req_body['peeringNetworks'] == [peering_network_model]


    @responses.activate
    def test_pcloud_tenants_put_value_error(self):
        """
        test_pcloud_tenants_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString')
        mock_response = '{"tenantID": "tenant_id", "enabled": false, "creationDate": "2019-01-01T12:00:00", "sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}], "cloudInstances": [{"cloudInstanceID": "cloud_instance_id", "name": "name", "region": "region", "enabled": false, "initialized": false, "limits": {"instances": 9, "memory": 6, "procUnits": 10, "processors": 10, "storage": 7, "instanceMemory": 15, "instanceProcUnits": 19, "peeringNetworks": 16, "peeringBandwidth": 17, "storageSSD": 11, "storageStandard": 16}, "capabilities": ["capabilities"], "href": "href"}], "icn": "icn", "peeringNetworks": [{"projectName": "project_name", "cidr": "cidr", "dnsServers": ["dns_servers"]}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PeeringNetwork model
        peering_network_model = {}
        peering_network_model['projectName'] = 'testString'
        peering_network_model['cidr'] = 'testString'
        peering_network_model['dnsServers'] = ['testString']

        # Set up parameter values
        tenant_id = 'testString'
        icn = 'testString'
        peering_networks = [peering_network_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_put(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudTenants
##############################################################################

##############################################################################
# Start of Service: PCloudTenantsSSHKeys
##############################################################################
# region

class TestPcloudTenantsSshkeysPost():
    """
    Test Class for pcloud_tenants_sshkeys_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_sshkeys_post_all_params(self):
        """
        pcloud_tenants_sshkeys_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        name = 'testString'
        ssh_key = 'testString'
        creation_date = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Invoke method
        response = service.pcloud_tenants_sshkeys_post(
            tenant_id,
            name,
            ssh_key,
            creation_date=creation_date,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['sshKey'] == 'testString'
        assert req_body['creationDate'] == '2020-01-28T18:40:40.123456Z'


    @responses.activate
    def test_pcloud_tenants_sshkeys_post_value_error(self):
        """
        test_pcloud_tenants_sshkeys_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        name = 'testString'
        ssh_key = 'testString'
        creation_date = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
            "name": name,
            "ssh_key": ssh_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_sshkeys_post(**req_copy)



class TestPcloudTenantsSshkeysGetall():
    """
    Test Class for pcloud_tenants_sshkeys_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_sshkeys_getall_all_params(self):
        """
        pcloud_tenants_sshkeys_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys')
        mock_response = '{"sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'

        # Invoke method
        response = service.pcloud_tenants_sshkeys_getall(
            tenant_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tenants_sshkeys_getall_value_error(self):
        """
        test_pcloud_tenants_sshkeys_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys')
        mock_response = '{"sshKeys": [{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_sshkeys_getall(**req_copy)



class TestPcloudTenantsSshkeysGet():
    """
    Test Class for pcloud_tenants_sshkeys_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_sshkeys_get_all_params(self):
        """
        pcloud_tenants_sshkeys_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'

        # Invoke method
        response = service.pcloud_tenants_sshkeys_get(
            tenant_id,
            sshkey_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tenants_sshkeys_get_value_error(self):
        """
        test_pcloud_tenants_sshkeys_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
            "sshkey_name": sshkey_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_sshkeys_get(**req_copy)



class TestPcloudTenantsSshkeysPut():
    """
    Test Class for pcloud_tenants_sshkeys_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_sshkeys_put_all_params(self):
        """
        pcloud_tenants_sshkeys_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'
        name = 'testString'
        ssh_key = 'testString'
        creation_date = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Invoke method
        response = service.pcloud_tenants_sshkeys_put(
            tenant_id,
            sshkey_name,
            name,
            ssh_key,
            creation_date=creation_date,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['sshKey'] == 'testString'
        assert req_body['creationDate'] == '2020-01-28T18:40:40.123456Z'


    @responses.activate
    def test_pcloud_tenants_sshkeys_put_value_error(self):
        """
        test_pcloud_tenants_sshkeys_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        mock_response = '{"name": "name", "sshKey": "ssh_key", "creationDate": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'
        name = 'testString'
        ssh_key = 'testString'
        creation_date = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
            "sshkey_name": sshkey_name,
            "name": name,
            "ssh_key": ssh_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_sshkeys_put(**req_copy)



class TestPcloudTenantsSshkeysDelete():
    """
    Test Class for pcloud_tenants_sshkeys_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_tenants_sshkeys_delete_all_params(self):
        """
        pcloud_tenants_sshkeys_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'

        # Invoke method
        response = service.pcloud_tenants_sshkeys_delete(
            tenant_id,
            sshkey_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_tenants_sshkeys_delete_value_error(self):
        """
        test_pcloud_tenants_sshkeys_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/tenants/testString/sshkeys/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        tenant_id = 'testString'
        sshkey_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tenant_id": tenant_id,
            "sshkey_name": sshkey_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_tenants_sshkeys_delete(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudTenantsSSHKeys
##############################################################################

##############################################################################
# Start of Service: PCloudVolumes
##############################################################################
# region

class TestPcloudCloudinstancesVolumesPost():
    """
    Test Class for pcloud_cloudinstances_volumes_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_volumes_post_all_params(self):
        """
        pcloud_cloudinstances_volumes_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        size = 72.5
        disk_type = 'testString'
        volume_pool = 'testString'
        shareable = True
        affinity_policy = 'affinity'
        affinity_volume = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_post(
            cloud_instance_id,
            name,
            size,
            disk_type=disk_type,
            volume_pool=volume_pool,
            shareable=shareable,
            affinity_policy=affinity_policy,
            affinity_volume=affinity_volume,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['size'] == 72.5
        assert req_body['diskType'] == 'testString'
        assert req_body['volumePool'] == 'testString'
        assert req_body['shareable'] == True
        assert req_body['affinityPolicy'] == 'affinity'
        assert req_body['affinityVolume'] == 'testString'


    @responses.activate
    def test_pcloud_cloudinstances_volumes_post_value_error(self):
        """
        test_pcloud_cloudinstances_volumes_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        size = 72.5
        disk_type = 'testString'
        volume_pool = 'testString'
        shareable = True
        affinity_policy = 'affinity'
        affinity_volume = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "name": name,
            "size": size,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_volumes_post(**req_copy)



class TestPcloudCloudinstancesVolumesGetall():
    """
    Test Class for pcloud_cloudinstances_volumes_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_volumes_getall_all_params(self):
        """
        pcloud_cloudinstances_volumes_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        affinity = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_getall(
            cloud_instance_id,
            affinity=affinity,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'affinity={}'.format(affinity) in query_string


    @responses.activate
    def test_pcloud_cloudinstances_volumes_getall_required_params(self):
        """
        test_pcloud_cloudinstances_volumes_getall_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_getall(
            cloud_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_volumes_getall_value_error(self):
        """
        test_pcloud_cloudinstances_volumes_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_volumes_getall(**req_copy)



class TestPcloudVolumesClonePost():
    """
    Test Class for pcloud_volumes_clone_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_volumes_clone_post_all_params(self):
        """
        pcloud_volumes_clone_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/clone')
        mock_response = '{"clonedVolumes": {"mapKey": "inner"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        display_name = 'testString'
        volume_i_ds = ['testString']

        # Invoke method
        response = service.pcloud_volumes_clone_post(
            cloud_instance_id,
            display_name,
            volume_i_ds,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['displayName'] == 'testString'
        assert req_body['volumeIDs'] == ['testString']


    @responses.activate
    def test_pcloud_volumes_clone_post_value_error(self):
        """
        test_pcloud_volumes_clone_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/clone')
        mock_response = '{"clonedVolumes": {"mapKey": "inner"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        display_name = 'testString'
        volume_i_ds = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "display_name": display_name,
            "volume_i_ds": volume_i_ds,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_volumes_clone_post(**req_copy)



class TestPcloudV2VolumesClonePost():
    """
    Test Class for pcloud_v2_volumes_clone_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_v2_volumes_clone_post_all_params(self):
        """
        pcloud_v2_volumes_clone_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes/clone')
        mock_response = '{"cloneTaskID": "clone_task_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        volume_i_ds = ['testString']

        # Invoke method
        response = service.pcloud_v2_volumes_clone_post(
            cloud_instance_id,
            name,
            volume_i_ds,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['volumeIDs'] == ['testString']


    @responses.activate
    def test_pcloud_v2_volumes_clone_post_value_error(self):
        """
        test_pcloud_v2_volumes_clone_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes/clone')
        mock_response = '{"cloneTaskID": "clone_task_id", "href": "href"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        volume_i_ds = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "name": name,
            "volume_i_ds": volume_i_ds,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_v2_volumes_clone_post(**req_copy)



class TestPcloudV2VolumesClonetasksGet():
    """
    Test Class for pcloud_v2_volumes_clonetasks_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_v2_volumes_clonetasks_get_all_params(self):
        """
        pcloud_v2_volumes_clonetasks_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes/clone-tasks/testString')
        mock_response = '{"status": "running", "percentComplete": 16, "clonedVolumes": [{"sourceVolumeID": "source_volume_id", "clonedVolumeID": "cloned_volume_id"}], "failedReason": "failed_reason"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        clone_task_id = 'testString'

        # Invoke method
        response = service.pcloud_v2_volumes_clonetasks_get(
            cloud_instance_id,
            clone_task_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_v2_volumes_clonetasks_get_value_error(self):
        """
        test_pcloud_v2_volumes_clonetasks_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes/clone-tasks/testString')
        mock_response = '{"status": "running", "percentComplete": 16, "clonedVolumes": [{"sourceVolumeID": "source_volume_id", "clonedVolumeID": "cloned_volume_id"}], "failedReason": "failed_reason"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        clone_task_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "clone_task_id": clone_task_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_v2_volumes_clonetasks_get(**req_copy)



class TestPcloudCloudinstancesVolumesGet():
    """
    Test Class for pcloud_cloudinstances_volumes_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_volumes_get_all_params(self):
        """
        pcloud_cloudinstances_volumes_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_get(
            cloud_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_volumes_get_value_error(self):
        """
        test_pcloud_cloudinstances_volumes_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_volumes_get(**req_copy)



class TestPcloudCloudinstancesVolumesPut():
    """
    Test Class for pcloud_cloudinstances_volumes_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_volumes_put_all_params(self):
        """
        pcloud_cloudinstances_volumes_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'
        name = 'testString'
        size = 72.5
        shareable = True
        bootable = True

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_put(
            cloud_instance_id,
            volume_id,
            name=name,
            size=size,
            shareable=shareable,
            bootable=bootable,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['size'] == 72.5
        assert req_body['shareable'] == True
        assert req_body['bootable'] == True


    @responses.activate
    def test_pcloud_cloudinstances_volumes_put_value_error(self):
        """
        test_pcloud_cloudinstances_volumes_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'
        name = 'testString'
        size = 72.5
        shareable = True
        bootable = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_volumes_put(**req_copy)



class TestPcloudCloudinstancesVolumesDelete():
    """
    Test Class for pcloud_cloudinstances_volumes_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_cloudinstances_volumes_delete_all_params(self):
        """
        pcloud_cloudinstances_volumes_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_cloudinstances_volumes_delete(
            cloud_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_cloudinstances_volumes_delete_value_error(self):
        """
        test_pcloud_cloudinstances_volumes_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/volumes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_cloudinstances_volumes_delete(**req_copy)



class TestPcloudV2VolumesPost():
    """
    Test Class for pcloud_v2_volumes_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_v2_volumes_post_all_params(self):
        """
        pcloud_v2_volumes_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        size = 38
        count = 38
        shareable = True
        disk_type = 'testString'
        affinity_policy = 'affinity'
        affinity_volume = 'testString'

        # Invoke method
        response = service.pcloud_v2_volumes_post(
            cloud_instance_id,
            name,
            size,
            count=count,
            shareable=shareable,
            disk_type=disk_type,
            affinity_policy=affinity_policy,
            affinity_volume=affinity_volume,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['size'] == 38
        assert req_body['count'] == 38
        assert req_body['shareable'] == True
        assert req_body['diskType'] == 'testString'
        assert req_body['affinityPolicy'] == 'affinity'
        assert req_body['affinityVolume'] == 'testString'


    @responses.activate
    def test_pcloud_v2_volumes_post_value_error(self):
        """
        test_pcloud_v2_volumes_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v2/cloud-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        cloud_instance_id = 'testString'
        name = 'testString'
        size = 38
        count = 38
        shareable = True
        disk_type = 'testString'
        affinity_policy = 'affinity'
        affinity_volume = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "name": name,
            "size": size,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_v2_volumes_post(**req_copy)



class TestPcloudPvminstancesVolumesGetall():
    """
    Test Class for pcloud_pvminstances_volumes_getall
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_getall_all_params(self):
        """
        pcloud_pvminstances_volumes_getall()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_volumes_getall(
            cloud_instance_id,
            pvm_instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_volumes_getall_value_error(self):
        """
        test_pcloud_pvminstances_volumes_getall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes')
        mock_response = '{"volumes": [{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "href": "href", "pvmInstanceIDs": ["pvm_instance_i_ds"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_getall(**req_copy)



class TestPcloudPvminstancesVolumesGet():
    """
    Test Class for pcloud_pvminstances_volumes_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_get_all_params(self):
        """
        pcloud_pvminstances_volumes_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_volumes_get(
            cloud_instance_id,
            pvm_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_volumes_get_value_error(self):
        """
        test_pcloud_pvminstances_volumes_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        mock_response = '{"volumeID": "volume_id", "name": "name", "state": "state", "size": 4, "shareable": false, "bootable": true, "bootVolume": false, "deleteOnTermination": false, "diskType": "disk_type", "wwn": "wwn", "creationDate": "2019-01-01T12:00:00", "lastUpdateDate": "2019-01-01T12:00:00", "pvmInstanceIDs": ["pvm_instance_i_ds"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_get(**req_copy)



class TestPcloudPvminstancesVolumesPost():
    """
    Test Class for pcloud_pvminstances_volumes_post
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_post_all_params(self):
        """
        pcloud_pvminstances_volumes_post()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_volumes_post(
            cloud_instance_id,
            pvm_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_volumes_post_value_error(self):
        """
        test_pcloud_pvminstances_volumes_post_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_post(**req_copy)



class TestPcloudPvminstancesVolumesDelete():
    """
    Test Class for pcloud_pvminstances_volumes_delete
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_delete_all_params(self):
        """
        pcloud_pvminstances_volumes_delete()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_volumes_delete(
            cloud_instance_id,
            pvm_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_pcloud_pvminstances_volumes_delete_value_error(self):
        """
        test_pcloud_pvminstances_volumes_delete_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_delete(**req_copy)



class TestPcloudPvminstancesVolumesPut():
    """
    Test Class for pcloud_pvminstances_volumes_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_put_all_params(self):
        """
        pcloud_pvminstances_volumes_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'
        delete_on_termination = True

        # Invoke method
        response = service.pcloud_pvminstances_volumes_put(
            cloud_instance_id,
            pvm_instance_id,
            volume_id,
            delete_on_termination,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['deleteOnTermination'] == True


    @responses.activate
    def test_pcloud_pvminstances_volumes_put_value_error(self):
        """
        test_pcloud_pvminstances_volumes_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'
        delete_on_termination = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "volume_id": volume_id,
            "delete_on_termination": delete_on_termination,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_put(**req_copy)



class TestPcloudPvminstancesVolumesSetbootPut():
    """
    Test Class for pcloud_pvminstances_volumes_setboot_put
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_pcloud_pvminstances_volumes_setboot_put_all_params(self):
        """
        pcloud_pvminstances_volumes_setboot_put()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString/setboot')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Invoke method
        response = service.pcloud_pvminstances_volumes_setboot_put(
            cloud_instance_id,
            pvm_instance_id,
            volume_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_pcloud_pvminstances_volumes_setboot_put_value_error(self):
        """
        test_pcloud_pvminstances_volumes_setboot_put_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/pcloud/v1/cloud-instances/testString/pvm-instances/testString/volumes/testString/setboot')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        cloud_instance_id = 'testString'
        pvm_instance_id = 'testString'
        volume_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cloud_instance_id": cloud_instance_id,
            "pvm_instance_id": pvm_instance_id,
            "volume_id": volume_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.pcloud_pvminstances_volumes_setboot_put(**req_copy)



# endregion
##############################################################################
# End of Service: PCloudVolumes
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestCloneTaskReference():
    """
    Test Class for CloneTaskReference
    """

    def test_clone_task_reference_serialization(self):
        """
        Test serialization/deserialization for CloneTaskReference
        """

        # Construct a json representation of a CloneTaskReference model
        clone_task_reference_model_json = {}
        clone_task_reference_model_json['cloneTaskID'] = 'testString'
        clone_task_reference_model_json['href'] = 'testString'

        # Construct a model instance of CloneTaskReference by calling from_dict on the json representation
        clone_task_reference_model = CloneTaskReference.from_dict(clone_task_reference_model_json)
        assert clone_task_reference_model != False

        # Construct a model instance of CloneTaskReference by calling from_dict on the json representation
        clone_task_reference_model_dict = CloneTaskReference.from_dict(clone_task_reference_model_json).__dict__
        clone_task_reference_model2 = CloneTaskReference(**clone_task_reference_model_dict)

        # Verify the model instances are equivalent
        assert clone_task_reference_model == clone_task_reference_model2

        # Convert model instance back to dict and verify no loss of data
        clone_task_reference_model_json2 = clone_task_reference_model.to_dict()
        assert clone_task_reference_model_json2 == clone_task_reference_model_json

class TestCloneTaskStatus():
    """
    Test Class for CloneTaskStatus
    """

    def test_clone_task_status_serialization(self):
        """
        Test serialization/deserialization for CloneTaskStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cloned_volume_model = {} # ClonedVolume
        cloned_volume_model['sourceVolumeID'] = 'testString'
        cloned_volume_model['clonedVolumeID'] = 'testString'

        # Construct a json representation of a CloneTaskStatus model
        clone_task_status_model_json = {}
        clone_task_status_model_json['status'] = 'running'
        clone_task_status_model_json['percentComplete'] = 38
        clone_task_status_model_json['clonedVolumes'] = [cloned_volume_model]
        clone_task_status_model_json['failedReason'] = 'testString'

        # Construct a model instance of CloneTaskStatus by calling from_dict on the json representation
        clone_task_status_model = CloneTaskStatus.from_dict(clone_task_status_model_json)
        assert clone_task_status_model != False

        # Construct a model instance of CloneTaskStatus by calling from_dict on the json representation
        clone_task_status_model_dict = CloneTaskStatus.from_dict(clone_task_status_model_json).__dict__
        clone_task_status_model2 = CloneTaskStatus(**clone_task_status_model_dict)

        # Verify the model instances are equivalent
        assert clone_task_status_model == clone_task_status_model2

        # Convert model instance back to dict and verify no loss of data
        clone_task_status_model_json2 = clone_task_status_model.to_dict()
        assert clone_task_status_model_json2 == clone_task_status_model_json

class TestClonedVolume():
    """
    Test Class for ClonedVolume
    """

    def test_cloned_volume_serialization(self):
        """
        Test serialization/deserialization for ClonedVolume
        """

        # Construct a json representation of a ClonedVolume model
        cloned_volume_model_json = {}
        cloned_volume_model_json['sourceVolumeID'] = 'testString'
        cloned_volume_model_json['clonedVolumeID'] = 'testString'

        # Construct a model instance of ClonedVolume by calling from_dict on the json representation
        cloned_volume_model = ClonedVolume.from_dict(cloned_volume_model_json)
        assert cloned_volume_model != False

        # Construct a model instance of ClonedVolume by calling from_dict on the json representation
        cloned_volume_model_dict = ClonedVolume.from_dict(cloned_volume_model_json).__dict__
        cloned_volume_model2 = ClonedVolume(**cloned_volume_model_dict)

        # Verify the model instances are equivalent
        assert cloned_volume_model == cloned_volume_model2

        # Convert model instance back to dict and verify no loss of data
        cloned_volume_model_json2 = cloned_volume_model.to_dict()
        assert cloned_volume_model_json2 == cloned_volume_model_json

class TestCloudInstance():
    """
    Test Class for CloudInstance
    """

    def test_cloud_instance_serialization(self):
        """
        Test serialization/deserialization for CloudInstance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cloud_instance_usage_limits_model = {} # CloudInstanceUsageLimits
        cloud_instance_usage_limits_model['instances'] = 72.5
        cloud_instance_usage_limits_model['memory'] = 72.5
        cloud_instance_usage_limits_model['procUnits'] = 72.5
        cloud_instance_usage_limits_model['processors'] = 72.5
        cloud_instance_usage_limits_model['storage'] = 72.5
        cloud_instance_usage_limits_model['instanceMemory'] = 72.5
        cloud_instance_usage_limits_model['instanceProcUnits'] = 72.5
        cloud_instance_usage_limits_model['peeringNetworks'] = 38
        cloud_instance_usage_limits_model['peeringBandwidth'] = 38
        cloud_instance_usage_limits_model['storageSSD'] = 72.5
        cloud_instance_usage_limits_model['storageStandard'] = 72.5

        pvm_instance_network_model = {} # PVMInstanceNetwork
        pvm_instance_network_model['version'] = 72.5
        pvm_instance_network_model['networkID'] = 'testString'
        pvm_instance_network_model['networkName'] = 'testString'
        pvm_instance_network_model['macAddress'] = 'testString'
        pvm_instance_network_model['type'] = 'testString'
        pvm_instance_network_model['ip'] = 'testString'
        pvm_instance_network_model['ipAddress'] = 'testString'
        pvm_instance_network_model['externalIP'] = 'testString'
        pvm_instance_network_model['href'] = 'testString'

        pvm_instance_fault_model = {} # PVMInstanceFault
        pvm_instance_fault_model['code'] = 72.5
        pvm_instance_fault_model['details'] = 'testString'
        pvm_instance_fault_model['message'] = 'testString'
        pvm_instance_fault_model['created'] = '2020-01-28T18:40:40.123456Z'

        pvm_instance_health_model = {} # PVMInstanceHealth
        pvm_instance_health_model['status'] = 'testString'
        pvm_instance_health_model['lastUpdate'] = 'testString'
        pvm_instance_health_model['reason'] = 'testString'

        pvm_instance_reference_software_licenses_model = {} # PVMInstanceReferenceSoftwareLicenses
        pvm_instance_reference_software_licenses_model['ibmiCSS'] = True
        pvm_instance_reference_software_licenses_model['ibmiPHA'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDS'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_reference_software_licenses_model['ibmiDBQ'] = True

        sap_profile_reference_model = {} # SAPProfileReference
        sap_profile_reference_model['profileID'] = 'testString'
        sap_profile_reference_model['href'] = 'testString'

        virtual_cores_model = {} # VirtualCores
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        pvm_instance_reference_model = {} # PVMInstanceReference
        pvm_instance_reference_model['pvmInstanceID'] = 'testString'
        pvm_instance_reference_model['serverName'] = 'testString'
        pvm_instance_reference_model['imageID'] = 'testString'
        pvm_instance_reference_model['processors'] = 72.5
        pvm_instance_reference_model['minproc'] = 72.5
        pvm_instance_reference_model['maxproc'] = 72.5
        pvm_instance_reference_model['procType'] = 'dedicated'
        pvm_instance_reference_model['memory'] = 72.5
        pvm_instance_reference_model['minmem'] = 72.5
        pvm_instance_reference_model['maxmem'] = 72.5
        pvm_instance_reference_model['diskSize'] = 72.5
        pvm_instance_reference_model['networks'] = [pvm_instance_network_model]
        pvm_instance_reference_model['status'] = 'testString'
        pvm_instance_reference_model['progress'] = 72.5
        pvm_instance_reference_model['fault'] = pvm_instance_fault_model
        pvm_instance_reference_model['creationDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model['updatedDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model['sysType'] = 'testString'
        pvm_instance_reference_model['health'] = pvm_instance_health_model
        pvm_instance_reference_model['href'] = 'testString'
        pvm_instance_reference_model['softwareLicenses'] = pvm_instance_reference_software_licenses_model
        pvm_instance_reference_model['srcs'] = [[{}]]
        pvm_instance_reference_model['pinPolicy'] = 'testString'
        pvm_instance_reference_model['osType'] = 'testString'
        pvm_instance_reference_model['operatingSystem'] = 'testString'
        pvm_instance_reference_model['sapProfile'] = sap_profile_reference_model
        pvm_instance_reference_model['virtualCores'] = virtual_cores_model

        # Construct a json representation of a CloudInstance model
        cloud_instance_model_json = {}
        cloud_instance_model_json['cloudInstanceID'] = 'testString'
        cloud_instance_model_json['name'] = 'testString'
        cloud_instance_model_json['tenantID'] = 'testString'
        cloud_instance_model_json['openstackID'] = 'testString'
        cloud_instance_model_json['region'] = 'testString'
        cloud_instance_model_json['enabled'] = True
        cloud_instance_model_json['initialized'] = True
        cloud_instance_model_json['limits'] = cloud_instance_usage_limits_model
        cloud_instance_model_json['usage'] = cloud_instance_usage_limits_model
        cloud_instance_model_json['capabilities'] = ['testString']
        cloud_instance_model_json['pvmInstances'] = [pvm_instance_reference_model]

        # Construct a model instance of CloudInstance by calling from_dict on the json representation
        cloud_instance_model = CloudInstance.from_dict(cloud_instance_model_json)
        assert cloud_instance_model != False

        # Construct a model instance of CloudInstance by calling from_dict on the json representation
        cloud_instance_model_dict = CloudInstance.from_dict(cloud_instance_model_json).__dict__
        cloud_instance_model2 = CloudInstance(**cloud_instance_model_dict)

        # Verify the model instances are equivalent
        assert cloud_instance_model == cloud_instance_model2

        # Convert model instance back to dict and verify no loss of data
        cloud_instance_model_json2 = cloud_instance_model.to_dict()
        assert cloud_instance_model_json2 == cloud_instance_model_json

class TestCloudInstanceReference():
    """
    Test Class for CloudInstanceReference
    """

    def test_cloud_instance_reference_serialization(self):
        """
        Test serialization/deserialization for CloudInstanceReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cloud_instance_usage_limits_model = {} # CloudInstanceUsageLimits
        cloud_instance_usage_limits_model['instances'] = 72.5
        cloud_instance_usage_limits_model['memory'] = 72.5
        cloud_instance_usage_limits_model['procUnits'] = 72.5
        cloud_instance_usage_limits_model['processors'] = 72.5
        cloud_instance_usage_limits_model['storage'] = 72.5
        cloud_instance_usage_limits_model['instanceMemory'] = 72.5
        cloud_instance_usage_limits_model['instanceProcUnits'] = 72.5
        cloud_instance_usage_limits_model['peeringNetworks'] = 38
        cloud_instance_usage_limits_model['peeringBandwidth'] = 38
        cloud_instance_usage_limits_model['storageSSD'] = 72.5
        cloud_instance_usage_limits_model['storageStandard'] = 72.5

        # Construct a json representation of a CloudInstanceReference model
        cloud_instance_reference_model_json = {}
        cloud_instance_reference_model_json['cloudInstanceID'] = 'testString'
        cloud_instance_reference_model_json['name'] = 'testString'
        cloud_instance_reference_model_json['region'] = 'testString'
        cloud_instance_reference_model_json['enabled'] = True
        cloud_instance_reference_model_json['initialized'] = True
        cloud_instance_reference_model_json['limits'] = cloud_instance_usage_limits_model
        cloud_instance_reference_model_json['capabilities'] = ['testString']
        cloud_instance_reference_model_json['href'] = 'testString'

        # Construct a model instance of CloudInstanceReference by calling from_dict on the json representation
        cloud_instance_reference_model = CloudInstanceReference.from_dict(cloud_instance_reference_model_json)
        assert cloud_instance_reference_model != False

        # Construct a model instance of CloudInstanceReference by calling from_dict on the json representation
        cloud_instance_reference_model_dict = CloudInstanceReference.from_dict(cloud_instance_reference_model_json).__dict__
        cloud_instance_reference_model2 = CloudInstanceReference(**cloud_instance_reference_model_dict)

        # Verify the model instances are equivalent
        assert cloud_instance_reference_model == cloud_instance_reference_model2

        # Convert model instance back to dict and verify no loss of data
        cloud_instance_reference_model_json2 = cloud_instance_reference_model.to_dict()
        assert cloud_instance_reference_model_json2 == cloud_instance_reference_model_json

class TestCloudInstanceUsageLimits():
    """
    Test Class for CloudInstanceUsageLimits
    """

    def test_cloud_instance_usage_limits_serialization(self):
        """
        Test serialization/deserialization for CloudInstanceUsageLimits
        """

        # Construct a json representation of a CloudInstanceUsageLimits model
        cloud_instance_usage_limits_model_json = {}
        cloud_instance_usage_limits_model_json['instances'] = 72.5
        cloud_instance_usage_limits_model_json['memory'] = 72.5
        cloud_instance_usage_limits_model_json['procUnits'] = 72.5
        cloud_instance_usage_limits_model_json['processors'] = 72.5
        cloud_instance_usage_limits_model_json['storage'] = 72.5
        cloud_instance_usage_limits_model_json['instanceMemory'] = 72.5
        cloud_instance_usage_limits_model_json['instanceProcUnits'] = 72.5
        cloud_instance_usage_limits_model_json['peeringNetworks'] = 38
        cloud_instance_usage_limits_model_json['peeringBandwidth'] = 38
        cloud_instance_usage_limits_model_json['storageSSD'] = 72.5
        cloud_instance_usage_limits_model_json['storageStandard'] = 72.5

        # Construct a model instance of CloudInstanceUsageLimits by calling from_dict on the json representation
        cloud_instance_usage_limits_model = CloudInstanceUsageLimits.from_dict(cloud_instance_usage_limits_model_json)
        assert cloud_instance_usage_limits_model != False

        # Construct a model instance of CloudInstanceUsageLimits by calling from_dict on the json representation
        cloud_instance_usage_limits_model_dict = CloudInstanceUsageLimits.from_dict(cloud_instance_usage_limits_model_json).__dict__
        cloud_instance_usage_limits_model2 = CloudInstanceUsageLimits(**cloud_instance_usage_limits_model_dict)

        # Verify the model instances are equivalent
        assert cloud_instance_usage_limits_model == cloud_instance_usage_limits_model2

        # Convert model instance back to dict and verify no loss of data
        cloud_instance_usage_limits_model_json2 = cloud_instance_usage_limits_model.to_dict()
        assert cloud_instance_usage_limits_model_json2 == cloud_instance_usage_limits_model_json

class TestEvent():
    """
    Test Class for Event
    """

    def test_event_serialization(self):
        """
        Test serialization/deserialization for Event
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_user_model = {} # EventUser
        event_user_model['userID'] = 'testString'
        event_user_model['name'] = 'testString'
        event_user_model['email'] = 'testString'

        # Construct a json representation of a Event model
        event_model_json = {}
        event_model_json['eventID'] = 'testString'
        event_model_json['time'] = '2020-01-28T18:40:40.123456Z'
        event_model_json['timestamp'] = 38
        event_model_json['user'] = event_user_model
        event_model_json['level'] = 'notice'
        event_model_json['resource'] = 'testString'
        event_model_json['action'] = 'testString'
        event_model_json['message'] = 'testString'
        event_model_json['metadata'] = { 'foo': 'bar' }

        # Construct a model instance of Event by calling from_dict on the json representation
        event_model = Event.from_dict(event_model_json)
        assert event_model != False

        # Construct a model instance of Event by calling from_dict on the json representation
        event_model_dict = Event.from_dict(event_model_json).__dict__
        event_model2 = Event(**event_model_dict)

        # Verify the model instances are equivalent
        assert event_model == event_model2

        # Convert model instance back to dict and verify no loss of data
        event_model_json2 = event_model.to_dict()
        assert event_model_json2 == event_model_json

class TestEventUser():
    """
    Test Class for EventUser
    """

    def test_event_user_serialization(self):
        """
        Test serialization/deserialization for EventUser
        """

        # Construct a json representation of a EventUser model
        event_user_model_json = {}
        event_user_model_json['userID'] = 'testString'
        event_user_model_json['name'] = 'testString'
        event_user_model_json['email'] = 'testString'

        # Construct a model instance of EventUser by calling from_dict on the json representation
        event_user_model = EventUser.from_dict(event_user_model_json)
        assert event_user_model != False

        # Construct a model instance of EventUser by calling from_dict on the json representation
        event_user_model_dict = EventUser.from_dict(event_user_model_json).__dict__
        event_user_model2 = EventUser(**event_user_model_dict)

        # Verify the model instances are equivalent
        assert event_user_model == event_user_model2

        # Convert model instance back to dict and verify no loss of data
        event_user_model_json2 = event_user_model.to_dict()
        assert event_user_model_json2 == event_user_model_json

class TestEvents():
    """
    Test Class for Events
    """

    def test_events_serialization(self):
        """
        Test serialization/deserialization for Events
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_user_model = {} # EventUser
        event_user_model['userID'] = 'testString'
        event_user_model['name'] = 'testString'
        event_user_model['email'] = 'testString'

        event_model = {} # Event
        event_model['eventID'] = 'testString'
        event_model['time'] = '2020-01-28T18:40:40.123456Z'
        event_model['timestamp'] = 38
        event_model['user'] = event_user_model
        event_model['level'] = 'notice'
        event_model['resource'] = 'testString'
        event_model['action'] = 'testString'
        event_model['message'] = 'testString'
        event_model['metadata'] = { 'foo': 'bar' }

        # Construct a json representation of a Events model
        events_model_json = {}
        events_model_json['events'] = [event_model]

        # Construct a model instance of Events by calling from_dict on the json representation
        events_model = Events.from_dict(events_model_json)
        assert events_model != False

        # Construct a model instance of Events by calling from_dict on the json representation
        events_model_dict = Events.from_dict(events_model_json).__dict__
        events_model2 = Events(**events_model_dict)

        # Verify the model instances are equivalent
        assert events_model == events_model2

        # Convert model instance back to dict and verify no loss of data
        events_model_json2 = events_model.to_dict()
        assert events_model_json2 == events_model_json

class TestIPAddressRange():
    """
    Test Class for IPAddressRange
    """

    def test_ip_address_range_serialization(self):
        """
        Test serialization/deserialization for IPAddressRange
        """

        # Construct a json representation of a IPAddressRange model
        ip_address_range_model_json = {}
        ip_address_range_model_json['startingIPAddress'] = 'testString'
        ip_address_range_model_json['endingIPAddress'] = 'testString'

        # Construct a model instance of IPAddressRange by calling from_dict on the json representation
        ip_address_range_model = IPAddressRange.from_dict(ip_address_range_model_json)
        assert ip_address_range_model != False

        # Construct a model instance of IPAddressRange by calling from_dict on the json representation
        ip_address_range_model_dict = IPAddressRange.from_dict(ip_address_range_model_json).__dict__
        ip_address_range_model2 = IPAddressRange(**ip_address_range_model_dict)

        # Verify the model instances are equivalent
        assert ip_address_range_model == ip_address_range_model2

        # Convert model instance back to dict and verify no loss of data
        ip_address_range_model_json2 = ip_address_range_model.to_dict()
        assert ip_address_range_model_json2 == ip_address_range_model_json

class TestImage():
    """
    Test Class for Image
    """

    def test_image_serialization(self):
        """
        Test serialization/deserialization for Image
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_volume_model = {} # ImageVolume
        image_volume_model['volumeID'] = 'testString'
        image_volume_model['name'] = 'testString'
        image_volume_model['size'] = 72.5
        image_volume_model['bootable'] = True

        image_taskref_model = {} # ImageTaskref
        image_taskref_model['taskID'] = 'testString'
        image_taskref_model['href'] = 'testString'

        # Construct a json representation of a Image model
        image_model_json = {}
        image_model_json['imageID'] = 'testString'
        image_model_json['name'] = 'testString'
        image_model_json['state'] = 'testString'
        image_model_json['description'] = 'testString'
        image_model_json['size'] = 72.5
        image_model_json['storageType'] = 'testString'
        image_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        image_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        image_model_json['volumes'] = [image_volume_model]
        image_model_json['servers'] = ['testString']
        image_model_json['taskref'] = image_taskref_model

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model = Image.from_dict(image_model_json)
        assert image_model != False

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model_dict = Image.from_dict(image_model_json).__dict__
        image_model2 = Image(**image_model_dict)

        # Verify the model instances are equivalent
        assert image_model == image_model2

        # Convert model instance back to dict and verify no loss of data
        image_model_json2 = image_model.to_dict()
        assert image_model_json2 == image_model_json

class TestImageReference():
    """
    Test Class for ImageReference
    """

    def test_image_reference_serialization(self):
        """
        Test serialization/deserialization for ImageReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_reference_specifications_model = {} # ImageReferenceSpecifications
        image_reference_specifications_model['imageType'] = 'testString'
        image_reference_specifications_model['containerFormat'] = 'testString'
        image_reference_specifications_model['diskFormat'] = 'testString'
        image_reference_specifications_model['operatingSystem'] = 'testString'
        image_reference_specifications_model['hypervisorType'] = 'testString'
        image_reference_specifications_model['architecture'] = 'testString'
        image_reference_specifications_model['endianness'] = 'testString'

        # Construct a json representation of a ImageReference model
        image_reference_model_json = {}
        image_reference_model_json['imageID'] = 'testString'
        image_reference_model_json['name'] = 'testString'
        image_reference_model_json['state'] = 'testString'
        image_reference_model_json['description'] = 'testString'
        image_reference_model_json['storageType'] = 'testString'
        image_reference_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        image_reference_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        image_reference_model_json['specifications'] = image_reference_specifications_model
        image_reference_model_json['href'] = 'testString'

        # Construct a model instance of ImageReference by calling from_dict on the json representation
        image_reference_model = ImageReference.from_dict(image_reference_model_json)
        assert image_reference_model != False

        # Construct a model instance of ImageReference by calling from_dict on the json representation
        image_reference_model_dict = ImageReference.from_dict(image_reference_model_json).__dict__
        image_reference_model2 = ImageReference(**image_reference_model_dict)

        # Verify the model instances are equivalent
        assert image_reference_model == image_reference_model2

        # Convert model instance back to dict and verify no loss of data
        image_reference_model_json2 = image_reference_model.to_dict()
        assert image_reference_model_json2 == image_reference_model_json

class TestImageReferenceSpecifications():
    """
    Test Class for ImageReferenceSpecifications
    """

    def test_image_reference_specifications_serialization(self):
        """
        Test serialization/deserialization for ImageReferenceSpecifications
        """

        # Construct a json representation of a ImageReferenceSpecifications model
        image_reference_specifications_model_json = {}
        image_reference_specifications_model_json['imageType'] = 'testString'
        image_reference_specifications_model_json['containerFormat'] = 'testString'
        image_reference_specifications_model_json['diskFormat'] = 'testString'
        image_reference_specifications_model_json['operatingSystem'] = 'testString'
        image_reference_specifications_model_json['hypervisorType'] = 'testString'
        image_reference_specifications_model_json['architecture'] = 'testString'
        image_reference_specifications_model_json['endianness'] = 'testString'

        # Construct a model instance of ImageReferenceSpecifications by calling from_dict on the json representation
        image_reference_specifications_model = ImageReferenceSpecifications.from_dict(image_reference_specifications_model_json)
        assert image_reference_specifications_model != False

        # Construct a model instance of ImageReferenceSpecifications by calling from_dict on the json representation
        image_reference_specifications_model_dict = ImageReferenceSpecifications.from_dict(image_reference_specifications_model_json).__dict__
        image_reference_specifications_model2 = ImageReferenceSpecifications(**image_reference_specifications_model_dict)

        # Verify the model instances are equivalent
        assert image_reference_specifications_model == image_reference_specifications_model2

        # Convert model instance back to dict and verify no loss of data
        image_reference_specifications_model_json2 = image_reference_specifications_model.to_dict()
        assert image_reference_specifications_model_json2 == image_reference_specifications_model_json

class TestImageTaskref():
    """
    Test Class for ImageTaskref
    """

    def test_image_taskref_serialization(self):
        """
        Test serialization/deserialization for ImageTaskref
        """

        # Construct a json representation of a ImageTaskref model
        image_taskref_model_json = {}
        image_taskref_model_json['taskID'] = 'testString'
        image_taskref_model_json['href'] = 'testString'

        # Construct a model instance of ImageTaskref by calling from_dict on the json representation
        image_taskref_model = ImageTaskref.from_dict(image_taskref_model_json)
        assert image_taskref_model != False

        # Construct a model instance of ImageTaskref by calling from_dict on the json representation
        image_taskref_model_dict = ImageTaskref.from_dict(image_taskref_model_json).__dict__
        image_taskref_model2 = ImageTaskref(**image_taskref_model_dict)

        # Verify the model instances are equivalent
        assert image_taskref_model == image_taskref_model2

        # Convert model instance back to dict and verify no loss of data
        image_taskref_model_json2 = image_taskref_model.to_dict()
        assert image_taskref_model_json2 == image_taskref_model_json

class TestImageVolume():
    """
    Test Class for ImageVolume
    """

    def test_image_volume_serialization(self):
        """
        Test serialization/deserialization for ImageVolume
        """

        # Construct a json representation of a ImageVolume model
        image_volume_model_json = {}
        image_volume_model_json['volumeID'] = 'testString'
        image_volume_model_json['name'] = 'testString'
        image_volume_model_json['size'] = 72.5
        image_volume_model_json['bootable'] = True

        # Construct a model instance of ImageVolume by calling from_dict on the json representation
        image_volume_model = ImageVolume.from_dict(image_volume_model_json)
        assert image_volume_model != False

        # Construct a model instance of ImageVolume by calling from_dict on the json representation
        image_volume_model_dict = ImageVolume.from_dict(image_volume_model_json).__dict__
        image_volume_model2 = ImageVolume(**image_volume_model_dict)

        # Verify the model instances are equivalent
        assert image_volume_model == image_volume_model2

        # Convert model instance back to dict and verify no loss of data
        image_volume_model_json2 = image_volume_model.to_dict()
        assert image_volume_model_json2 == image_volume_model_json

class TestImages():
    """
    Test Class for Images
    """

    def test_images_serialization(self):
        """
        Test serialization/deserialization for Images
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_reference_specifications_model = {} # ImageReferenceSpecifications
        image_reference_specifications_model['imageType'] = 'testString'
        image_reference_specifications_model['containerFormat'] = 'testString'
        image_reference_specifications_model['diskFormat'] = 'testString'
        image_reference_specifications_model['operatingSystem'] = 'testString'
        image_reference_specifications_model['hypervisorType'] = 'testString'
        image_reference_specifications_model['architecture'] = 'testString'
        image_reference_specifications_model['endianness'] = 'testString'

        image_reference_model = {} # ImageReference
        image_reference_model['imageID'] = 'testString'
        image_reference_model['name'] = 'testString'
        image_reference_model['state'] = 'testString'
        image_reference_model['description'] = 'testString'
        image_reference_model['storageType'] = 'testString'
        image_reference_model['creationDate'] = '2020-01-28T18:40:40.123456Z'
        image_reference_model['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        image_reference_model['specifications'] = image_reference_specifications_model
        image_reference_model['href'] = 'testString'

        # Construct a json representation of a Images model
        images_model_json = {}
        images_model_json['images'] = [image_reference_model]

        # Construct a model instance of Images by calling from_dict on the json representation
        images_model = Images.from_dict(images_model_json)
        assert images_model != False

        # Construct a model instance of Images by calling from_dict on the json representation
        images_model_dict = Images.from_dict(images_model_json).__dict__
        images_model2 = Images(**images_model_dict)

        # Verify the model instances are equivalent
        assert images_model == images_model2

        # Convert model instance back to dict and verify no loss of data
        images_model_json2 = images_model.to_dict()
        assert images_model_json2 == images_model_json

class TestNetwork():
    """
    Test Class for Network
    """

    def test_network_serialization(self):
        """
        Test serialization/deserialization for Network
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ip_address_range_model = {} # IPAddressRange
        ip_address_range_model['startingIPAddress'] = 'testString'
        ip_address_range_model['endingIPAddress'] = 'testString'

        network_ip_address_metrics_model = {} # NetworkIpAddressMetrics
        network_ip_address_metrics_model['available'] = 72.5
        network_ip_address_metrics_model['used'] = 72.5
        network_ip_address_metrics_model['total'] = 72.5
        network_ip_address_metrics_model['utilization'] = 72.5

        # Construct a json representation of a Network model
        network_model_json = {}
        network_model_json['networkID'] = 'testString'
        network_model_json['name'] = 'testString'
        network_model_json['type'] = 'vlan'
        network_model_json['vlanID'] = 72.5
        network_model_json['cidr'] = 'testString'
        network_model_json['gateway'] = 'testString'
        network_model_json['dnsServers'] = ['testString']
        network_model_json['ipAddressRanges'] = [ip_address_range_model]
        network_model_json['ipAddressMetrics'] = network_ip_address_metrics_model
        network_model_json['publicIPAddressRanges'] = [ip_address_range_model]
        network_model_json['jumbo'] = True

        # Construct a model instance of Network by calling from_dict on the json representation
        network_model = Network.from_dict(network_model_json)
        assert network_model != False

        # Construct a model instance of Network by calling from_dict on the json representation
        network_model_dict = Network.from_dict(network_model_json).__dict__
        network_model2 = Network(**network_model_dict)

        # Verify the model instances are equivalent
        assert network_model == network_model2

        # Convert model instance back to dict and verify no loss of data
        network_model_json2 = network_model.to_dict()
        assert network_model_json2 == network_model_json

class TestNetworkIpAddressMetrics():
    """
    Test Class for NetworkIpAddressMetrics
    """

    def test_network_ip_address_metrics_serialization(self):
        """
        Test serialization/deserialization for NetworkIpAddressMetrics
        """

        # Construct a json representation of a NetworkIpAddressMetrics model
        network_ip_address_metrics_model_json = {}
        network_ip_address_metrics_model_json['available'] = 72.5
        network_ip_address_metrics_model_json['used'] = 72.5
        network_ip_address_metrics_model_json['total'] = 72.5
        network_ip_address_metrics_model_json['utilization'] = 72.5

        # Construct a model instance of NetworkIpAddressMetrics by calling from_dict on the json representation
        network_ip_address_metrics_model = NetworkIpAddressMetrics.from_dict(network_ip_address_metrics_model_json)
        assert network_ip_address_metrics_model != False

        # Construct a model instance of NetworkIpAddressMetrics by calling from_dict on the json representation
        network_ip_address_metrics_model_dict = NetworkIpAddressMetrics.from_dict(network_ip_address_metrics_model_json).__dict__
        network_ip_address_metrics_model2 = NetworkIpAddressMetrics(**network_ip_address_metrics_model_dict)

        # Verify the model instances are equivalent
        assert network_ip_address_metrics_model == network_ip_address_metrics_model2

        # Convert model instance back to dict and verify no loss of data
        network_ip_address_metrics_model_json2 = network_ip_address_metrics_model.to_dict()
        assert network_ip_address_metrics_model_json2 == network_ip_address_metrics_model_json

class TestNetworkPort():
    """
    Test Class for NetworkPort
    """

    def test_network_port_serialization(self):
        """
        Test serialization/deserialization for NetworkPort
        """

        # Construct dict forms of any model objects needed in order to build this model.

        network_port_pvm_instance_model = {} # NetworkPortPvmInstance
        network_port_pvm_instance_model['pvmInstanceID'] = 'testString'
        network_port_pvm_instance_model['href'] = 'testString'

        # Construct a json representation of a NetworkPort model
        network_port_model_json = {}
        network_port_model_json['portID'] = 'testString'
        network_port_model_json['description'] = 'testString'
        network_port_model_json['status'] = 'testString'
        network_port_model_json['macAddress'] = 'testString'
        network_port_model_json['ipAddress'] = 'testString'
        network_port_model_json['pvmInstance'] = network_port_pvm_instance_model
        network_port_model_json['href'] = 'testString'

        # Construct a model instance of NetworkPort by calling from_dict on the json representation
        network_port_model = NetworkPort.from_dict(network_port_model_json)
        assert network_port_model != False

        # Construct a model instance of NetworkPort by calling from_dict on the json representation
        network_port_model_dict = NetworkPort.from_dict(network_port_model_json).__dict__
        network_port_model2 = NetworkPort(**network_port_model_dict)

        # Verify the model instances are equivalent
        assert network_port_model == network_port_model2

        # Convert model instance back to dict and verify no loss of data
        network_port_model_json2 = network_port_model.to_dict()
        assert network_port_model_json2 == network_port_model_json

class TestNetworkPortPvmInstance():
    """
    Test Class for NetworkPortPvmInstance
    """

    def test_network_port_pvm_instance_serialization(self):
        """
        Test serialization/deserialization for NetworkPortPvmInstance
        """

        # Construct a json representation of a NetworkPortPvmInstance model
        network_port_pvm_instance_model_json = {}
        network_port_pvm_instance_model_json['pvmInstanceID'] = 'testString'
        network_port_pvm_instance_model_json['href'] = 'testString'

        # Construct a model instance of NetworkPortPvmInstance by calling from_dict on the json representation
        network_port_pvm_instance_model = NetworkPortPvmInstance.from_dict(network_port_pvm_instance_model_json)
        assert network_port_pvm_instance_model != False

        # Construct a model instance of NetworkPortPvmInstance by calling from_dict on the json representation
        network_port_pvm_instance_model_dict = NetworkPortPvmInstance.from_dict(network_port_pvm_instance_model_json).__dict__
        network_port_pvm_instance_model2 = NetworkPortPvmInstance(**network_port_pvm_instance_model_dict)

        # Verify the model instances are equivalent
        assert network_port_pvm_instance_model == network_port_pvm_instance_model2

        # Convert model instance back to dict and verify no loss of data
        network_port_pvm_instance_model_json2 = network_port_pvm_instance_model.to_dict()
        assert network_port_pvm_instance_model_json2 == network_port_pvm_instance_model_json

class TestNetworkPorts():
    """
    Test Class for NetworkPorts
    """

    def test_network_ports_serialization(self):
        """
        Test serialization/deserialization for NetworkPorts
        """

        # Construct dict forms of any model objects needed in order to build this model.

        network_port_pvm_instance_model = {} # NetworkPortPvmInstance
        network_port_pvm_instance_model['pvmInstanceID'] = 'testString'
        network_port_pvm_instance_model['href'] = 'testString'

        network_port_model = {} # NetworkPort
        network_port_model['portID'] = 'testString'
        network_port_model['description'] = 'testString'
        network_port_model['status'] = 'testString'
        network_port_model['macAddress'] = 'testString'
        network_port_model['ipAddress'] = 'testString'
        network_port_model['pvmInstance'] = network_port_pvm_instance_model
        network_port_model['href'] = 'testString'

        # Construct a json representation of a NetworkPorts model
        network_ports_model_json = {}
        network_ports_model_json['ports'] = [network_port_model]

        # Construct a model instance of NetworkPorts by calling from_dict on the json representation
        network_ports_model = NetworkPorts.from_dict(network_ports_model_json)
        assert network_ports_model != False

        # Construct a model instance of NetworkPorts by calling from_dict on the json representation
        network_ports_model_dict = NetworkPorts.from_dict(network_ports_model_json).__dict__
        network_ports_model2 = NetworkPorts(**network_ports_model_dict)

        # Verify the model instances are equivalent
        assert network_ports_model == network_ports_model2

        # Convert model instance back to dict and verify no loss of data
        network_ports_model_json2 = network_ports_model.to_dict()
        assert network_ports_model_json2 == network_ports_model_json

class TestNetworkReference():
    """
    Test Class for NetworkReference
    """

    def test_network_reference_serialization(self):
        """
        Test serialization/deserialization for NetworkReference
        """

        # Construct a json representation of a NetworkReference model
        network_reference_model_json = {}
        network_reference_model_json['networkID'] = 'testString'
        network_reference_model_json['name'] = 'testString'
        network_reference_model_json['vlanID'] = 72.5
        network_reference_model_json['type'] = 'vlan'
        network_reference_model_json['jumbo'] = True
        network_reference_model_json['href'] = 'testString'

        # Construct a model instance of NetworkReference by calling from_dict on the json representation
        network_reference_model = NetworkReference.from_dict(network_reference_model_json)
        assert network_reference_model != False

        # Construct a model instance of NetworkReference by calling from_dict on the json representation
        network_reference_model_dict = NetworkReference.from_dict(network_reference_model_json).__dict__
        network_reference_model2 = NetworkReference(**network_reference_model_dict)

        # Verify the model instances are equivalent
        assert network_reference_model == network_reference_model2

        # Convert model instance back to dict and verify no loss of data
        network_reference_model_json2 = network_reference_model.to_dict()
        assert network_reference_model_json2 == network_reference_model_json

class TestNetworks():
    """
    Test Class for Networks
    """

    def test_networks_serialization(self):
        """
        Test serialization/deserialization for Networks
        """

        # Construct dict forms of any model objects needed in order to build this model.

        network_reference_model = {} # NetworkReference
        network_reference_model['networkID'] = 'testString'
        network_reference_model['name'] = 'testString'
        network_reference_model['vlanID'] = 72.5
        network_reference_model['type'] = 'vlan'
        network_reference_model['jumbo'] = True
        network_reference_model['href'] = 'testString'

        # Construct a json representation of a Networks model
        networks_model_json = {}
        networks_model_json['networks'] = [network_reference_model]

        # Construct a model instance of Networks by calling from_dict on the json representation
        networks_model = Networks.from_dict(networks_model_json)
        assert networks_model != False

        # Construct a model instance of Networks by calling from_dict on the json representation
        networks_model_dict = Networks.from_dict(networks_model_json).__dict__
        networks_model2 = Networks(**networks_model_dict)

        # Verify the model instances are equivalent
        assert networks_model == networks_model2

        # Convert model instance back to dict and verify no loss of data
        networks_model_json2 = networks_model.to_dict()
        assert networks_model_json2 == networks_model_json

class TestOperations():
    """
    Test Class for Operations
    """

    def test_operations_serialization(self):
        """
        Test serialization/deserialization for Operations
        """

        # Construct a json representation of a Operations model
        operations_model_json = {}
        operations_model_json['bootMode'] = 'a'
        operations_model_json['operatingMode'] = 'normal'
        operations_model_json['task'] = 'dston'

        # Construct a model instance of Operations by calling from_dict on the json representation
        operations_model = Operations.from_dict(operations_model_json)
        assert operations_model != False

        # Construct a model instance of Operations by calling from_dict on the json representation
        operations_model_dict = Operations.from_dict(operations_model_json).__dict__
        operations_model2 = Operations(**operations_model_dict)

        # Verify the model instances are equivalent
        assert operations_model == operations_model2

        # Convert model instance back to dict and verify no loss of data
        operations_model_json2 = operations_model.to_dict()
        assert operations_model_json2 == operations_model_json

class TestPVMInstance():
    """
    Test Class for PVMInstance
    """

    def test_pvm_instance_serialization(self):
        """
        Test serialization/deserialization for PVMInstance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pvm_instance_network_model = {} # PVMInstanceNetwork
        pvm_instance_network_model['version'] = 72.5
        pvm_instance_network_model['networkID'] = 'testString'
        pvm_instance_network_model['networkName'] = 'testString'
        pvm_instance_network_model['macAddress'] = 'testString'
        pvm_instance_network_model['type'] = 'testString'
        pvm_instance_network_model['ip'] = 'testString'
        pvm_instance_network_model['ipAddress'] = 'testString'
        pvm_instance_network_model['externalIP'] = 'testString'
        pvm_instance_network_model['href'] = 'testString'

        pvm_instance_fault_model = {} # PVMInstanceFault
        pvm_instance_fault_model['code'] = 72.5
        pvm_instance_fault_model['details'] = 'testString'
        pvm_instance_fault_model['message'] = 'testString'
        pvm_instance_fault_model['created'] = '2020-01-28T18:40:40.123456Z'

        pvm_instance_health_model = {} # PVMInstanceHealth
        pvm_instance_health_model['status'] = 'testString'
        pvm_instance_health_model['lastUpdate'] = 'testString'
        pvm_instance_health_model['reason'] = 'testString'

        pvm_instance_software_licenses_model = {} # PVMInstanceSoftwareLicenses
        pvm_instance_software_licenses_model['ibmiCSS'] = True
        pvm_instance_software_licenses_model['ibmiPHA'] = True
        pvm_instance_software_licenses_model['ibmiRDS'] = True
        pvm_instance_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_software_licenses_model['ibmiDBQ'] = True

        sap_profile_reference_model = {} # SAPProfileReference
        sap_profile_reference_model['profileID'] = 'testString'
        sap_profile_reference_model['href'] = 'testString'

        virtual_cores_model = {} # VirtualCores
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Construct a json representation of a PVMInstance model
        pvm_instance_model_json = {}
        pvm_instance_model_json['pvmInstanceID'] = 'testString'
        pvm_instance_model_json['serverName'] = 'testString'
        pvm_instance_model_json['imageID'] = 'testString'
        pvm_instance_model_json['processors'] = 72.5
        pvm_instance_model_json['minproc'] = 72.5
        pvm_instance_model_json['maxproc'] = 72.5
        pvm_instance_model_json['procType'] = 'dedicated'
        pvm_instance_model_json['memory'] = 72.5
        pvm_instance_model_json['minmem'] = 72.5
        pvm_instance_model_json['maxmem'] = 72.5
        pvm_instance_model_json['diskSize'] = 72.5
        pvm_instance_model_json['networkIDs'] = ['testString']
        pvm_instance_model_json['volumeIDs'] = ['testString']
        pvm_instance_model_json['addresses'] = [pvm_instance_network_model]
        pvm_instance_model_json['networks'] = [pvm_instance_network_model]
        pvm_instance_model_json['status'] = 'testString'
        pvm_instance_model_json['progress'] = 72.5
        pvm_instance_model_json['fault'] = pvm_instance_fault_model
        pvm_instance_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_model_json['updatedDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_model_json['sysType'] = 'testString'
        pvm_instance_model_json['health'] = pvm_instance_health_model
        pvm_instance_model_json['migratable'] = True
        pvm_instance_model_json['storageType'] = 'testString'
        pvm_instance_model_json['softwareLicenses'] = pvm_instance_software_licenses_model
        pvm_instance_model_json['srcs'] = [[{}]]
        pvm_instance_model_json['pinPolicy'] = 'testString'
        pvm_instance_model_json['osType'] = 'testString'
        pvm_instance_model_json['operatingSystem'] = 'testString'
        pvm_instance_model_json['sapProfile'] = sap_profile_reference_model
        pvm_instance_model_json['virtualCores'] = virtual_cores_model

        # Construct a model instance of PVMInstance by calling from_dict on the json representation
        pvm_instance_model = PVMInstance.from_dict(pvm_instance_model_json)
        assert pvm_instance_model != False

        # Construct a model instance of PVMInstance by calling from_dict on the json representation
        pvm_instance_model_dict = PVMInstance.from_dict(pvm_instance_model_json).__dict__
        pvm_instance_model2 = PVMInstance(**pvm_instance_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_model == pvm_instance_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_model_json2 = pvm_instance_model.to_dict()
        assert pvm_instance_model_json2 == pvm_instance_model_json

class TestPVMInstanceAddNetwork():
    """
    Test Class for PVMInstanceAddNetwork
    """

    def test_pvm_instance_add_network_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceAddNetwork
        """

        # Construct a json representation of a PVMInstanceAddNetwork model
        pvm_instance_add_network_model_json = {}
        pvm_instance_add_network_model_json['networkID'] = 'testString'
        pvm_instance_add_network_model_json['ipAddress'] = 'testString'

        # Construct a model instance of PVMInstanceAddNetwork by calling from_dict on the json representation
        pvm_instance_add_network_model = PVMInstanceAddNetwork.from_dict(pvm_instance_add_network_model_json)
        assert pvm_instance_add_network_model != False

        # Construct a model instance of PVMInstanceAddNetwork by calling from_dict on the json representation
        pvm_instance_add_network_model_dict = PVMInstanceAddNetwork.from_dict(pvm_instance_add_network_model_json).__dict__
        pvm_instance_add_network_model2 = PVMInstanceAddNetwork(**pvm_instance_add_network_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_add_network_model == pvm_instance_add_network_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_add_network_model_json2 = pvm_instance_add_network_model.to_dict()
        assert pvm_instance_add_network_model_json2 == pvm_instance_add_network_model_json

class TestPVMInstanceConsole():
    """
    Test Class for PVMInstanceConsole
    """

    def test_pvm_instance_console_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceConsole
        """

        # Construct a json representation of a PVMInstanceConsole model
        pvm_instance_console_model_json = {}
        pvm_instance_console_model_json['consoleURL'] = 'testString'

        # Construct a model instance of PVMInstanceConsole by calling from_dict on the json representation
        pvm_instance_console_model = PVMInstanceConsole.from_dict(pvm_instance_console_model_json)
        assert pvm_instance_console_model != False

        # Construct a model instance of PVMInstanceConsole by calling from_dict on the json representation
        pvm_instance_console_model_dict = PVMInstanceConsole.from_dict(pvm_instance_console_model_json).__dict__
        pvm_instance_console_model2 = PVMInstanceConsole(**pvm_instance_console_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_console_model == pvm_instance_console_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_console_model_json2 = pvm_instance_console_model.to_dict()
        assert pvm_instance_console_model_json2 == pvm_instance_console_model_json

class TestPVMInstanceCreateSoftwareLicenses():
    """
    Test Class for PVMInstanceCreateSoftwareLicenses
    """

    def test_pvm_instance_create_software_licenses_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceCreateSoftwareLicenses
        """

        # Construct a json representation of a PVMInstanceCreateSoftwareLicenses model
        pvm_instance_create_software_licenses_model_json = {}
        pvm_instance_create_software_licenses_model_json['ibmiCSS'] = True
        pvm_instance_create_software_licenses_model_json['ibmiPHA'] = True
        pvm_instance_create_software_licenses_model_json['ibmiRDS'] = True
        pvm_instance_create_software_licenses_model_json['ibmiRDSUsers'] = 38
        pvm_instance_create_software_licenses_model_json['ibmiDBQ'] = True

        # Construct a model instance of PVMInstanceCreateSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_create_software_licenses_model = PVMInstanceCreateSoftwareLicenses.from_dict(pvm_instance_create_software_licenses_model_json)
        assert pvm_instance_create_software_licenses_model != False

        # Construct a model instance of PVMInstanceCreateSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_create_software_licenses_model_dict = PVMInstanceCreateSoftwareLicenses.from_dict(pvm_instance_create_software_licenses_model_json).__dict__
        pvm_instance_create_software_licenses_model2 = PVMInstanceCreateSoftwareLicenses(**pvm_instance_create_software_licenses_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_create_software_licenses_model == pvm_instance_create_software_licenses_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_create_software_licenses_model_json2 = pvm_instance_create_software_licenses_model.to_dict()
        assert pvm_instance_create_software_licenses_model_json2 == pvm_instance_create_software_licenses_model_json

class TestPVMInstanceFault():
    """
    Test Class for PVMInstanceFault
    """

    def test_pvm_instance_fault_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceFault
        """

        # Construct a json representation of a PVMInstanceFault model
        pvm_instance_fault_model_json = {}
        pvm_instance_fault_model_json['code'] = 72.5
        pvm_instance_fault_model_json['details'] = 'testString'
        pvm_instance_fault_model_json['message'] = 'testString'
        pvm_instance_fault_model_json['created'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of PVMInstanceFault by calling from_dict on the json representation
        pvm_instance_fault_model = PVMInstanceFault.from_dict(pvm_instance_fault_model_json)
        assert pvm_instance_fault_model != False

        # Construct a model instance of PVMInstanceFault by calling from_dict on the json representation
        pvm_instance_fault_model_dict = PVMInstanceFault.from_dict(pvm_instance_fault_model_json).__dict__
        pvm_instance_fault_model2 = PVMInstanceFault(**pvm_instance_fault_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_fault_model == pvm_instance_fault_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_fault_model_json2 = pvm_instance_fault_model.to_dict()
        assert pvm_instance_fault_model_json2 == pvm_instance_fault_model_json

class TestPVMInstanceHealth():
    """
    Test Class for PVMInstanceHealth
    """

    def test_pvm_instance_health_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceHealth
        """

        # Construct a json representation of a PVMInstanceHealth model
        pvm_instance_health_model_json = {}
        pvm_instance_health_model_json['status'] = 'testString'
        pvm_instance_health_model_json['lastUpdate'] = 'testString'
        pvm_instance_health_model_json['reason'] = 'testString'

        # Construct a model instance of PVMInstanceHealth by calling from_dict on the json representation
        pvm_instance_health_model = PVMInstanceHealth.from_dict(pvm_instance_health_model_json)
        assert pvm_instance_health_model != False

        # Construct a model instance of PVMInstanceHealth by calling from_dict on the json representation
        pvm_instance_health_model_dict = PVMInstanceHealth.from_dict(pvm_instance_health_model_json).__dict__
        pvm_instance_health_model2 = PVMInstanceHealth(**pvm_instance_health_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_health_model == pvm_instance_health_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_health_model_json2 = pvm_instance_health_model.to_dict()
        assert pvm_instance_health_model_json2 == pvm_instance_health_model_json

class TestPVMInstanceMultiCreate():
    """
    Test Class for PVMInstanceMultiCreate
    """

    def test_pvm_instance_multi_create_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceMultiCreate
        """

        # Construct a json representation of a PVMInstanceMultiCreate model
        pvm_instance_multi_create_model_json = {}
        pvm_instance_multi_create_model_json['count'] = 38
        pvm_instance_multi_create_model_json['affinityPolicy'] = 'affinity'
        pvm_instance_multi_create_model_json['numerical'] = 'prefix'

        # Construct a model instance of PVMInstanceMultiCreate by calling from_dict on the json representation
        pvm_instance_multi_create_model = PVMInstanceMultiCreate.from_dict(pvm_instance_multi_create_model_json)
        assert pvm_instance_multi_create_model != False

        # Construct a model instance of PVMInstanceMultiCreate by calling from_dict on the json representation
        pvm_instance_multi_create_model_dict = PVMInstanceMultiCreate.from_dict(pvm_instance_multi_create_model_json).__dict__
        pvm_instance_multi_create_model2 = PVMInstanceMultiCreate(**pvm_instance_multi_create_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_multi_create_model == pvm_instance_multi_create_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_multi_create_model_json2 = pvm_instance_multi_create_model.to_dict()
        assert pvm_instance_multi_create_model_json2 == pvm_instance_multi_create_model_json

class TestPVMInstanceNetwork():
    """
    Test Class for PVMInstanceNetwork
    """

    def test_pvm_instance_network_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceNetwork
        """

        # Construct a json representation of a PVMInstanceNetwork model
        pvm_instance_network_model_json = {}
        pvm_instance_network_model_json['version'] = 72.5
        pvm_instance_network_model_json['networkID'] = 'testString'
        pvm_instance_network_model_json['networkName'] = 'testString'
        pvm_instance_network_model_json['macAddress'] = 'testString'
        pvm_instance_network_model_json['type'] = 'testString'
        pvm_instance_network_model_json['ip'] = 'testString'
        pvm_instance_network_model_json['ipAddress'] = 'testString'
        pvm_instance_network_model_json['externalIP'] = 'testString'
        pvm_instance_network_model_json['href'] = 'testString'

        # Construct a model instance of PVMInstanceNetwork by calling from_dict on the json representation
        pvm_instance_network_model = PVMInstanceNetwork.from_dict(pvm_instance_network_model_json)
        assert pvm_instance_network_model != False

        # Construct a model instance of PVMInstanceNetwork by calling from_dict on the json representation
        pvm_instance_network_model_dict = PVMInstanceNetwork.from_dict(pvm_instance_network_model_json).__dict__
        pvm_instance_network_model2 = PVMInstanceNetwork(**pvm_instance_network_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_network_model == pvm_instance_network_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_network_model_json2 = pvm_instance_network_model.to_dict()
        assert pvm_instance_network_model_json2 == pvm_instance_network_model_json

class TestPVMInstanceNetworks():
    """
    Test Class for PVMInstanceNetworks
    """

    def test_pvm_instance_networks_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceNetworks
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pvm_instance_network_model = {} # PVMInstanceNetwork
        pvm_instance_network_model['version'] = 72.5
        pvm_instance_network_model['networkID'] = 'testString'
        pvm_instance_network_model['networkName'] = 'testString'
        pvm_instance_network_model['macAddress'] = 'testString'
        pvm_instance_network_model['type'] = 'testString'
        pvm_instance_network_model['ip'] = 'testString'
        pvm_instance_network_model['ipAddress'] = 'testString'
        pvm_instance_network_model['externalIP'] = 'testString'
        pvm_instance_network_model['href'] = 'testString'

        # Construct a json representation of a PVMInstanceNetworks model
        pvm_instance_networks_model_json = {}
        pvm_instance_networks_model_json['networks'] = [pvm_instance_network_model]

        # Construct a model instance of PVMInstanceNetworks by calling from_dict on the json representation
        pvm_instance_networks_model = PVMInstanceNetworks.from_dict(pvm_instance_networks_model_json)
        assert pvm_instance_networks_model != False

        # Construct a model instance of PVMInstanceNetworks by calling from_dict on the json representation
        pvm_instance_networks_model_dict = PVMInstanceNetworks.from_dict(pvm_instance_networks_model_json).__dict__
        pvm_instance_networks_model2 = PVMInstanceNetworks(**pvm_instance_networks_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_networks_model == pvm_instance_networks_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_networks_model_json2 = pvm_instance_networks_model.to_dict()
        assert pvm_instance_networks_model_json2 == pvm_instance_networks_model_json

class TestPVMInstanceReference():
    """
    Test Class for PVMInstanceReference
    """

    def test_pvm_instance_reference_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pvm_instance_network_model = {} # PVMInstanceNetwork
        pvm_instance_network_model['version'] = 72.5
        pvm_instance_network_model['networkID'] = 'testString'
        pvm_instance_network_model['networkName'] = 'testString'
        pvm_instance_network_model['macAddress'] = 'testString'
        pvm_instance_network_model['type'] = 'testString'
        pvm_instance_network_model['ip'] = 'testString'
        pvm_instance_network_model['ipAddress'] = 'testString'
        pvm_instance_network_model['externalIP'] = 'testString'
        pvm_instance_network_model['href'] = 'testString'

        pvm_instance_fault_model = {} # PVMInstanceFault
        pvm_instance_fault_model['code'] = 72.5
        pvm_instance_fault_model['details'] = 'testString'
        pvm_instance_fault_model['message'] = 'testString'
        pvm_instance_fault_model['created'] = '2020-01-28T18:40:40.123456Z'

        pvm_instance_health_model = {} # PVMInstanceHealth
        pvm_instance_health_model['status'] = 'testString'
        pvm_instance_health_model['lastUpdate'] = 'testString'
        pvm_instance_health_model['reason'] = 'testString'

        pvm_instance_reference_software_licenses_model = {} # PVMInstanceReferenceSoftwareLicenses
        pvm_instance_reference_software_licenses_model['ibmiCSS'] = True
        pvm_instance_reference_software_licenses_model['ibmiPHA'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDS'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_reference_software_licenses_model['ibmiDBQ'] = True

        sap_profile_reference_model = {} # SAPProfileReference
        sap_profile_reference_model['profileID'] = 'testString'
        sap_profile_reference_model['href'] = 'testString'

        virtual_cores_model = {} # VirtualCores
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        # Construct a json representation of a PVMInstanceReference model
        pvm_instance_reference_model_json = {}
        pvm_instance_reference_model_json['pvmInstanceID'] = 'testString'
        pvm_instance_reference_model_json['serverName'] = 'testString'
        pvm_instance_reference_model_json['imageID'] = 'testString'
        pvm_instance_reference_model_json['processors'] = 72.5
        pvm_instance_reference_model_json['minproc'] = 72.5
        pvm_instance_reference_model_json['maxproc'] = 72.5
        pvm_instance_reference_model_json['procType'] = 'dedicated'
        pvm_instance_reference_model_json['memory'] = 72.5
        pvm_instance_reference_model_json['minmem'] = 72.5
        pvm_instance_reference_model_json['maxmem'] = 72.5
        pvm_instance_reference_model_json['diskSize'] = 72.5
        pvm_instance_reference_model_json['networks'] = [pvm_instance_network_model]
        pvm_instance_reference_model_json['status'] = 'testString'
        pvm_instance_reference_model_json['progress'] = 72.5
        pvm_instance_reference_model_json['fault'] = pvm_instance_fault_model
        pvm_instance_reference_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model_json['updatedDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model_json['sysType'] = 'testString'
        pvm_instance_reference_model_json['health'] = pvm_instance_health_model
        pvm_instance_reference_model_json['href'] = 'testString'
        pvm_instance_reference_model_json['softwareLicenses'] = pvm_instance_reference_software_licenses_model
        pvm_instance_reference_model_json['srcs'] = [[{}]]
        pvm_instance_reference_model_json['pinPolicy'] = 'testString'
        pvm_instance_reference_model_json['osType'] = 'testString'
        pvm_instance_reference_model_json['operatingSystem'] = 'testString'
        pvm_instance_reference_model_json['sapProfile'] = sap_profile_reference_model
        pvm_instance_reference_model_json['virtualCores'] = virtual_cores_model

        # Construct a model instance of PVMInstanceReference by calling from_dict on the json representation
        pvm_instance_reference_model = PVMInstanceReference.from_dict(pvm_instance_reference_model_json)
        assert pvm_instance_reference_model != False

        # Construct a model instance of PVMInstanceReference by calling from_dict on the json representation
        pvm_instance_reference_model_dict = PVMInstanceReference.from_dict(pvm_instance_reference_model_json).__dict__
        pvm_instance_reference_model2 = PVMInstanceReference(**pvm_instance_reference_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_reference_model == pvm_instance_reference_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_reference_model_json2 = pvm_instance_reference_model.to_dict()
        assert pvm_instance_reference_model_json2 == pvm_instance_reference_model_json

class TestPVMInstanceReferenceSoftwareLicenses():
    """
    Test Class for PVMInstanceReferenceSoftwareLicenses
    """

    def test_pvm_instance_reference_software_licenses_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceReferenceSoftwareLicenses
        """

        # Construct a json representation of a PVMInstanceReferenceSoftwareLicenses model
        pvm_instance_reference_software_licenses_model_json = {}
        pvm_instance_reference_software_licenses_model_json['ibmiCSS'] = True
        pvm_instance_reference_software_licenses_model_json['ibmiPHA'] = True
        pvm_instance_reference_software_licenses_model_json['ibmiRDS'] = True
        pvm_instance_reference_software_licenses_model_json['ibmiRDSUsers'] = 38
        pvm_instance_reference_software_licenses_model_json['ibmiDBQ'] = True

        # Construct a model instance of PVMInstanceReferenceSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_reference_software_licenses_model = PVMInstanceReferenceSoftwareLicenses.from_dict(pvm_instance_reference_software_licenses_model_json)
        assert pvm_instance_reference_software_licenses_model != False

        # Construct a model instance of PVMInstanceReferenceSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_reference_software_licenses_model_dict = PVMInstanceReferenceSoftwareLicenses.from_dict(pvm_instance_reference_software_licenses_model_json).__dict__
        pvm_instance_reference_software_licenses_model2 = PVMInstanceReferenceSoftwareLicenses(**pvm_instance_reference_software_licenses_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_reference_software_licenses_model == pvm_instance_reference_software_licenses_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_reference_software_licenses_model_json2 = pvm_instance_reference_software_licenses_model.to_dict()
        assert pvm_instance_reference_software_licenses_model_json2 == pvm_instance_reference_software_licenses_model_json

class TestPVMInstanceSoftwareLicenses():
    """
    Test Class for PVMInstanceSoftwareLicenses
    """

    def test_pvm_instance_software_licenses_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceSoftwareLicenses
        """

        # Construct a json representation of a PVMInstanceSoftwareLicenses model
        pvm_instance_software_licenses_model_json = {}
        pvm_instance_software_licenses_model_json['ibmiCSS'] = True
        pvm_instance_software_licenses_model_json['ibmiPHA'] = True
        pvm_instance_software_licenses_model_json['ibmiRDS'] = True
        pvm_instance_software_licenses_model_json['ibmiRDSUsers'] = 38
        pvm_instance_software_licenses_model_json['ibmiDBQ'] = True

        # Construct a model instance of PVMInstanceSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_software_licenses_model = PVMInstanceSoftwareLicenses.from_dict(pvm_instance_software_licenses_model_json)
        assert pvm_instance_software_licenses_model != False

        # Construct a model instance of PVMInstanceSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_software_licenses_model_dict = PVMInstanceSoftwareLicenses.from_dict(pvm_instance_software_licenses_model_json).__dict__
        pvm_instance_software_licenses_model2 = PVMInstanceSoftwareLicenses(**pvm_instance_software_licenses_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_software_licenses_model == pvm_instance_software_licenses_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_software_licenses_model_json2 = pvm_instance_software_licenses_model.to_dict()
        assert pvm_instance_software_licenses_model_json2 == pvm_instance_software_licenses_model_json

class TestPVMInstanceUpdateResponse():
    """
    Test Class for PVMInstanceUpdateResponse
    """

    def test_pvm_instance_update_response_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceUpdateResponse
        """

        # Construct a json representation of a PVMInstanceUpdateResponse model
        pvm_instance_update_response_model_json = {}
        pvm_instance_update_response_model_json['serverName'] = 'testString'
        pvm_instance_update_response_model_json['statusUrl'] = 'testString'
        pvm_instance_update_response_model_json['processors'] = 72.5
        pvm_instance_update_response_model_json['procType'] = 'dedicated'
        pvm_instance_update_response_model_json['memory'] = 72.5
        pvm_instance_update_response_model_json['pinPolicy'] = 'none'

        # Construct a model instance of PVMInstanceUpdateResponse by calling from_dict on the json representation
        pvm_instance_update_response_model = PVMInstanceUpdateResponse.from_dict(pvm_instance_update_response_model_json)
        assert pvm_instance_update_response_model != False

        # Construct a model instance of PVMInstanceUpdateResponse by calling from_dict on the json representation
        pvm_instance_update_response_model_dict = PVMInstanceUpdateResponse.from_dict(pvm_instance_update_response_model_json).__dict__
        pvm_instance_update_response_model2 = PVMInstanceUpdateResponse(**pvm_instance_update_response_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_update_response_model == pvm_instance_update_response_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_update_response_model_json2 = pvm_instance_update_response_model.to_dict()
        assert pvm_instance_update_response_model_json2 == pvm_instance_update_response_model_json

class TestPVMInstanceUpdateSoftwareLicenses():
    """
    Test Class for PVMInstanceUpdateSoftwareLicenses
    """

    def test_pvm_instance_update_software_licenses_serialization(self):
        """
        Test serialization/deserialization for PVMInstanceUpdateSoftwareLicenses
        """

        # Construct a json representation of a PVMInstanceUpdateSoftwareLicenses model
        pvm_instance_update_software_licenses_model_json = {}
        pvm_instance_update_software_licenses_model_json['ibmiCSS'] = True
        pvm_instance_update_software_licenses_model_json['ibmiPHA'] = True
        pvm_instance_update_software_licenses_model_json['ibmiRDS'] = True
        pvm_instance_update_software_licenses_model_json['ibmiRDSUsers'] = 38
        pvm_instance_update_software_licenses_model_json['ibmiDBQ'] = True

        # Construct a model instance of PVMInstanceUpdateSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_update_software_licenses_model = PVMInstanceUpdateSoftwareLicenses.from_dict(pvm_instance_update_software_licenses_model_json)
        assert pvm_instance_update_software_licenses_model != False

        # Construct a model instance of PVMInstanceUpdateSoftwareLicenses by calling from_dict on the json representation
        pvm_instance_update_software_licenses_model_dict = PVMInstanceUpdateSoftwareLicenses.from_dict(pvm_instance_update_software_licenses_model_json).__dict__
        pvm_instance_update_software_licenses_model2 = PVMInstanceUpdateSoftwareLicenses(**pvm_instance_update_software_licenses_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instance_update_software_licenses_model == pvm_instance_update_software_licenses_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instance_update_software_licenses_model_json2 = pvm_instance_update_software_licenses_model.to_dict()
        assert pvm_instance_update_software_licenses_model_json2 == pvm_instance_update_software_licenses_model_json

class TestPVMInstances():
    """
    Test Class for PVMInstances
    """

    def test_pvm_instances_serialization(self):
        """
        Test serialization/deserialization for PVMInstances
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pvm_instance_network_model = {} # PVMInstanceNetwork
        pvm_instance_network_model['version'] = 72.5
        pvm_instance_network_model['networkID'] = 'testString'
        pvm_instance_network_model['networkName'] = 'testString'
        pvm_instance_network_model['macAddress'] = 'testString'
        pvm_instance_network_model['type'] = 'testString'
        pvm_instance_network_model['ip'] = 'testString'
        pvm_instance_network_model['ipAddress'] = 'testString'
        pvm_instance_network_model['externalIP'] = 'testString'
        pvm_instance_network_model['href'] = 'testString'

        pvm_instance_fault_model = {} # PVMInstanceFault
        pvm_instance_fault_model['code'] = 72.5
        pvm_instance_fault_model['details'] = 'testString'
        pvm_instance_fault_model['message'] = 'testString'
        pvm_instance_fault_model['created'] = '2020-01-28T18:40:40.123456Z'

        pvm_instance_health_model = {} # PVMInstanceHealth
        pvm_instance_health_model['status'] = 'testString'
        pvm_instance_health_model['lastUpdate'] = 'testString'
        pvm_instance_health_model['reason'] = 'testString'

        pvm_instance_reference_software_licenses_model = {} # PVMInstanceReferenceSoftwareLicenses
        pvm_instance_reference_software_licenses_model['ibmiCSS'] = True
        pvm_instance_reference_software_licenses_model['ibmiPHA'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDS'] = True
        pvm_instance_reference_software_licenses_model['ibmiRDSUsers'] = 38
        pvm_instance_reference_software_licenses_model['ibmiDBQ'] = True

        sap_profile_reference_model = {} # SAPProfileReference
        sap_profile_reference_model['profileID'] = 'testString'
        sap_profile_reference_model['href'] = 'testString'

        virtual_cores_model = {} # VirtualCores
        virtual_cores_model['min'] = 38
        virtual_cores_model['max'] = 38
        virtual_cores_model['assigned'] = 1

        pvm_instance_reference_model = {} # PVMInstanceReference
        pvm_instance_reference_model['pvmInstanceID'] = 'testString'
        pvm_instance_reference_model['serverName'] = 'testString'
        pvm_instance_reference_model['imageID'] = 'testString'
        pvm_instance_reference_model['processors'] = 72.5
        pvm_instance_reference_model['minproc'] = 72.5
        pvm_instance_reference_model['maxproc'] = 72.5
        pvm_instance_reference_model['procType'] = 'dedicated'
        pvm_instance_reference_model['memory'] = 72.5
        pvm_instance_reference_model['minmem'] = 72.5
        pvm_instance_reference_model['maxmem'] = 72.5
        pvm_instance_reference_model['diskSize'] = 72.5
        pvm_instance_reference_model['networks'] = [pvm_instance_network_model]
        pvm_instance_reference_model['status'] = 'testString'
        pvm_instance_reference_model['progress'] = 72.5
        pvm_instance_reference_model['fault'] = pvm_instance_fault_model
        pvm_instance_reference_model['creationDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model['updatedDate'] = '2020-01-28T18:40:40.123456Z'
        pvm_instance_reference_model['sysType'] = 'testString'
        pvm_instance_reference_model['health'] = pvm_instance_health_model
        pvm_instance_reference_model['href'] = 'testString'
        pvm_instance_reference_model['softwareLicenses'] = pvm_instance_reference_software_licenses_model
        pvm_instance_reference_model['srcs'] = [[{}]]
        pvm_instance_reference_model['pinPolicy'] = 'testString'
        pvm_instance_reference_model['osType'] = 'testString'
        pvm_instance_reference_model['operatingSystem'] = 'testString'
        pvm_instance_reference_model['sapProfile'] = sap_profile_reference_model
        pvm_instance_reference_model['virtualCores'] = virtual_cores_model

        # Construct a json representation of a PVMInstances model
        pvm_instances_model_json = {}
        pvm_instances_model_json['pvmInstances'] = [pvm_instance_reference_model]

        # Construct a model instance of PVMInstances by calling from_dict on the json representation
        pvm_instances_model = PVMInstances.from_dict(pvm_instances_model_json)
        assert pvm_instances_model != False

        # Construct a model instance of PVMInstances by calling from_dict on the json representation
        pvm_instances_model_dict = PVMInstances.from_dict(pvm_instances_model_json).__dict__
        pvm_instances_model2 = PVMInstances(**pvm_instances_model_dict)

        # Verify the model instances are equivalent
        assert pvm_instances_model == pvm_instances_model2

        # Convert model instance back to dict and verify no loss of data
        pvm_instances_model_json2 = pvm_instances_model.to_dict()
        assert pvm_instances_model_json2 == pvm_instances_model_json

class TestPeeringNetwork():
    """
    Test Class for PeeringNetwork
    """

    def test_peering_network_serialization(self):
        """
        Test serialization/deserialization for PeeringNetwork
        """

        # Construct a json representation of a PeeringNetwork model
        peering_network_model_json = {}
        peering_network_model_json['projectName'] = 'testString'
        peering_network_model_json['cidr'] = 'testString'
        peering_network_model_json['dnsServers'] = ['testString']

        # Construct a model instance of PeeringNetwork by calling from_dict on the json representation
        peering_network_model = PeeringNetwork.from_dict(peering_network_model_json)
        assert peering_network_model != False

        # Construct a model instance of PeeringNetwork by calling from_dict on the json representation
        peering_network_model_dict = PeeringNetwork.from_dict(peering_network_model_json).__dict__
        peering_network_model2 = PeeringNetwork(**peering_network_model_dict)

        # Verify the model instances are equivalent
        assert peering_network_model == peering_network_model2

        # Convert model instance back to dict and verify no loss of data
        peering_network_model_json2 = peering_network_model.to_dict()
        assert peering_network_model_json2 == peering_network_model_json

class TestSAPProfile():
    """
    Test Class for SAPProfile
    """

    def test_sap_profile_serialization(self):
        """
        Test serialization/deserialization for SAPProfile
        """

        # Construct a json representation of a SAPProfile model
        sap_profile_model_json = {}
        sap_profile_model_json['profileID'] = 'testString'
        sap_profile_model_json['type'] = 'balanced'
        sap_profile_model_json['cores'] = 38
        sap_profile_model_json['memory'] = 38
        sap_profile_model_json['certified'] = True

        # Construct a model instance of SAPProfile by calling from_dict on the json representation
        sap_profile_model = SAPProfile.from_dict(sap_profile_model_json)
        assert sap_profile_model != False

        # Construct a model instance of SAPProfile by calling from_dict on the json representation
        sap_profile_model_dict = SAPProfile.from_dict(sap_profile_model_json).__dict__
        sap_profile_model2 = SAPProfile(**sap_profile_model_dict)

        # Verify the model instances are equivalent
        assert sap_profile_model == sap_profile_model2

        # Convert model instance back to dict and verify no loss of data
        sap_profile_model_json2 = sap_profile_model.to_dict()
        assert sap_profile_model_json2 == sap_profile_model_json

class TestSAPProfileReference():
    """
    Test Class for SAPProfileReference
    """

    def test_sap_profile_reference_serialization(self):
        """
        Test serialization/deserialization for SAPProfileReference
        """

        # Construct a json representation of a SAPProfileReference model
        sap_profile_reference_model_json = {}
        sap_profile_reference_model_json['profileID'] = 'testString'
        sap_profile_reference_model_json['href'] = 'testString'

        # Construct a model instance of SAPProfileReference by calling from_dict on the json representation
        sap_profile_reference_model = SAPProfileReference.from_dict(sap_profile_reference_model_json)
        assert sap_profile_reference_model != False

        # Construct a model instance of SAPProfileReference by calling from_dict on the json representation
        sap_profile_reference_model_dict = SAPProfileReference.from_dict(sap_profile_reference_model_json).__dict__
        sap_profile_reference_model2 = SAPProfileReference(**sap_profile_reference_model_dict)

        # Verify the model instances are equivalent
        assert sap_profile_reference_model == sap_profile_reference_model2

        # Convert model instance back to dict and verify no loss of data
        sap_profile_reference_model_json2 = sap_profile_reference_model.to_dict()
        assert sap_profile_reference_model_json2 == sap_profile_reference_model_json

class TestSAPProfiles():
    """
    Test Class for SAPProfiles
    """

    def test_sap_profiles_serialization(self):
        """
        Test serialization/deserialization for SAPProfiles
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sap_profile_model = {} # SAPProfile
        sap_profile_model['profileID'] = 'testString'
        sap_profile_model['type'] = 'balanced'
        sap_profile_model['cores'] = 38
        sap_profile_model['memory'] = 38
        sap_profile_model['certified'] = True

        # Construct a json representation of a SAPProfiles model
        sap_profiles_model_json = {}
        sap_profiles_model_json['profiles'] = [sap_profile_model]

        # Construct a model instance of SAPProfiles by calling from_dict on the json representation
        sap_profiles_model = SAPProfiles.from_dict(sap_profiles_model_json)
        assert sap_profiles_model != False

        # Construct a model instance of SAPProfiles by calling from_dict on the json representation
        sap_profiles_model_dict = SAPProfiles.from_dict(sap_profiles_model_json).__dict__
        sap_profiles_model2 = SAPProfiles(**sap_profiles_model_dict)

        # Verify the model instances are equivalent
        assert sap_profiles_model == sap_profiles_model2

        # Convert model instance back to dict and verify no loss of data
        sap_profiles_model_json2 = sap_profiles_model.to_dict()
        assert sap_profiles_model_json2 == sap_profiles_model_json

class TestSSHKey():
    """
    Test Class for SSHKey
    """

    def test_ssh_key_serialization(self):
        """
        Test serialization/deserialization for SSHKey
        """

        # Construct a json representation of a SSHKey model
        ssh_key_model_json = {}
        ssh_key_model_json['name'] = 'testString'
        ssh_key_model_json['sshKey'] = 'testString'
        ssh_key_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of SSHKey by calling from_dict on the json representation
        ssh_key_model = SSHKey.from_dict(ssh_key_model_json)
        assert ssh_key_model != False

        # Construct a model instance of SSHKey by calling from_dict on the json representation
        ssh_key_model_dict = SSHKey.from_dict(ssh_key_model_json).__dict__
        ssh_key_model2 = SSHKey(**ssh_key_model_dict)

        # Verify the model instances are equivalent
        assert ssh_key_model == ssh_key_model2

        # Convert model instance back to dict and verify no loss of data
        ssh_key_model_json2 = ssh_key_model.to_dict()
        assert ssh_key_model_json2 == ssh_key_model_json

class TestSSHKeys():
    """
    Test Class for SSHKeys
    """

    def test_ssh_keys_serialization(self):
        """
        Test serialization/deserialization for SSHKeys
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ssh_key_model = {} # SSHKey
        ssh_key_model['name'] = 'testString'
        ssh_key_model['sshKey'] = 'testString'
        ssh_key_model['creationDate'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a SSHKeys model
        ssh_keys_model_json = {}
        ssh_keys_model_json['sshKeys'] = [ssh_key_model]

        # Construct a model instance of SSHKeys by calling from_dict on the json representation
        ssh_keys_model = SSHKeys.from_dict(ssh_keys_model_json)
        assert ssh_keys_model != False

        # Construct a model instance of SSHKeys by calling from_dict on the json representation
        ssh_keys_model_dict = SSHKeys.from_dict(ssh_keys_model_json).__dict__
        ssh_keys_model2 = SSHKeys(**ssh_keys_model_dict)

        # Verify the model instances are equivalent
        assert ssh_keys_model == ssh_keys_model2

        # Convert model instance back to dict and verify no loss of data
        ssh_keys_model_json2 = ssh_keys_model.to_dict()
        assert ssh_keys_model_json2 == ssh_keys_model_json

class TestSnapshot():
    """
    Test Class for Snapshot
    """

    def test_snapshot_serialization(self):
        """
        Test serialization/deserialization for Snapshot
        """

        # Construct a json representation of a Snapshot model
        snapshot_model_json = {}
        snapshot_model_json['snapshotID'] = 'testString'
        snapshot_model_json['pvmInstanceID'] = 'testString'
        snapshot_model_json['name'] = 'testString'
        snapshot_model_json['description'] = 'testString'
        snapshot_model_json['status'] = 'testString'
        snapshot_model_json['volumeSnapshots'] = {}
        snapshot_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        snapshot_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        snapshot_model_json['action'] = 'testString'
        snapshot_model_json['percentComplete'] = 72.5

        # Construct a model instance of Snapshot by calling from_dict on the json representation
        snapshot_model = Snapshot.from_dict(snapshot_model_json)
        assert snapshot_model != False

        # Construct a model instance of Snapshot by calling from_dict on the json representation
        snapshot_model_dict = Snapshot.from_dict(snapshot_model_json).__dict__
        snapshot_model2 = Snapshot(**snapshot_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_model == snapshot_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_model_json2 = snapshot_model.to_dict()
        assert snapshot_model_json2 == snapshot_model_json

class TestSnapshotCreateResponse():
    """
    Test Class for SnapshotCreateResponse
    """

    def test_snapshot_create_response_serialization(self):
        """
        Test serialization/deserialization for SnapshotCreateResponse
        """

        # Construct a json representation of a SnapshotCreateResponse model
        snapshot_create_response_model_json = {}
        snapshot_create_response_model_json['snapshotID'] = 'testString'

        # Construct a model instance of SnapshotCreateResponse by calling from_dict on the json representation
        snapshot_create_response_model = SnapshotCreateResponse.from_dict(snapshot_create_response_model_json)
        assert snapshot_create_response_model != False

        # Construct a model instance of SnapshotCreateResponse by calling from_dict on the json representation
        snapshot_create_response_model_dict = SnapshotCreateResponse.from_dict(snapshot_create_response_model_json).__dict__
        snapshot_create_response_model2 = SnapshotCreateResponse(**snapshot_create_response_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_create_response_model == snapshot_create_response_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_create_response_model_json2 = snapshot_create_response_model.to_dict()
        assert snapshot_create_response_model_json2 == snapshot_create_response_model_json

class TestSnapshots():
    """
    Test Class for Snapshots
    """

    def test_snapshots_serialization(self):
        """
        Test serialization/deserialization for Snapshots
        """

        # Construct dict forms of any model objects needed in order to build this model.

        snapshot_model = {} # Snapshot
        snapshot_model['snapshotID'] = 'testString'
        snapshot_model['pvmInstanceID'] = 'testString'
        snapshot_model['name'] = 'testString'
        snapshot_model['description'] = 'testString'
        snapshot_model['status'] = 'testString'
        snapshot_model['volumeSnapshots'] = {}
        snapshot_model['creationDate'] = '2020-01-28T18:40:40.123456Z'
        snapshot_model['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        snapshot_model['action'] = 'testString'
        snapshot_model['percentComplete'] = 72.5

        # Construct a json representation of a Snapshots model
        snapshots_model_json = {}
        snapshots_model_json['snapshots'] = [snapshot_model]

        # Construct a model instance of Snapshots by calling from_dict on the json representation
        snapshots_model = Snapshots.from_dict(snapshots_model_json)
        assert snapshots_model != False

        # Construct a model instance of Snapshots by calling from_dict on the json representation
        snapshots_model_dict = Snapshots.from_dict(snapshots_model_json).__dict__
        snapshots_model2 = Snapshots(**snapshots_model_dict)

        # Verify the model instances are equivalent
        assert snapshots_model == snapshots_model2

        # Convert model instance back to dict and verify no loss of data
        snapshots_model_json2 = snapshots_model.to_dict()
        assert snapshots_model_json2 == snapshots_model_json

class TestSystem():
    """
    Test Class for System
    """

    def test_system_serialization(self):
        """
        Test serialization/deserialization for System
        """

        # Construct a json representation of a System model
        system_model_json = {}
        system_model_json['cores'] = 72.5
        system_model_json['id'] = 38
        system_model_json['memory'] = 38

        # Construct a model instance of System by calling from_dict on the json representation
        system_model = System.from_dict(system_model_json)
        assert system_model != False

        # Construct a model instance of System by calling from_dict on the json representation
        system_model_dict = System.from_dict(system_model_json).__dict__
        system_model2 = System(**system_model_dict)

        # Verify the model instances are equivalent
        assert system_model == system_model2

        # Convert model instance back to dict and verify no loss of data
        system_model_json2 = system_model.to_dict()
        assert system_model_json2 == system_model_json

class TestSystemPool():
    """
    Test Class for SystemPool
    """

    def test_system_pool_serialization(self):
        """
        Test serialization/deserialization for SystemPool
        """

        # Construct dict forms of any model objects needed in order to build this model.

        system_model = {} # System
        system_model['cores'] = 72.5
        system_model['id'] = 38
        system_model['memory'] = 38

        system_pool_shared_core_ratio_model = {} # SystemPoolSharedCoreRatio
        system_pool_shared_core_ratio_model['min'] = 72.5
        system_pool_shared_core_ratio_model['max'] = 72.5
        system_pool_shared_core_ratio_model['default'] = 72.5

        system_pool_max_available_model = {} # SystemPoolMaxAvailable
        system_pool_max_available_model['cores'] = 72.5
        system_pool_max_available_model['id'] = 38
        system_pool_max_available_model['memory'] = 38

        system_pool_capacity_model = {} # SystemPoolCapacity
        system_pool_capacity_model['cores'] = 72.5
        system_pool_capacity_model['id'] = 38
        system_pool_capacity_model['memory'] = 38

        system_pool_max_cores_available_model = {} # SystemPoolMaxCoresAvailable
        system_pool_max_cores_available_model['cores'] = 72.5
        system_pool_max_cores_available_model['id'] = 38
        system_pool_max_cores_available_model['memory'] = 38

        system_pool_max_memory_available_model = {} # SystemPoolMaxMemoryAvailable
        system_pool_max_memory_available_model['cores'] = 72.5
        system_pool_max_memory_available_model['id'] = 38
        system_pool_max_memory_available_model['memory'] = 38

        # Construct a json representation of a SystemPool model
        system_pool_model_json = {}
        system_pool_model_json['systems'] = [system_model]
        system_pool_model_json['sharedCoreRatio'] = system_pool_shared_core_ratio_model
        system_pool_model_json['maxAvailable'] = system_pool_max_available_model
        system_pool_model_json['capacity'] = system_pool_capacity_model
        system_pool_model_json['maxCoresAvailable'] = system_pool_max_cores_available_model
        system_pool_model_json['maxMemoryAvailable'] = system_pool_max_memory_available_model
        system_pool_model_json['coreMemoryRatio'] = 72.5
        system_pool_model_json['type'] = 'testString'

        # Construct a model instance of SystemPool by calling from_dict on the json representation
        system_pool_model = SystemPool.from_dict(system_pool_model_json)
        assert system_pool_model != False

        # Construct a model instance of SystemPool by calling from_dict on the json representation
        system_pool_model_dict = SystemPool.from_dict(system_pool_model_json).__dict__
        system_pool_model2 = SystemPool(**system_pool_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_model == system_pool_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_model_json2 = system_pool_model.to_dict()
        assert system_pool_model_json2 == system_pool_model_json

class TestSystemPoolCapacity():
    """
    Test Class for SystemPoolCapacity
    """

    def test_system_pool_capacity_serialization(self):
        """
        Test serialization/deserialization for SystemPoolCapacity
        """

        # Construct a json representation of a SystemPoolCapacity model
        system_pool_capacity_model_json = {}
        system_pool_capacity_model_json['cores'] = 72.5
        system_pool_capacity_model_json['id'] = 38
        system_pool_capacity_model_json['memory'] = 38

        # Construct a model instance of SystemPoolCapacity by calling from_dict on the json representation
        system_pool_capacity_model = SystemPoolCapacity.from_dict(system_pool_capacity_model_json)
        assert system_pool_capacity_model != False

        # Construct a model instance of SystemPoolCapacity by calling from_dict on the json representation
        system_pool_capacity_model_dict = SystemPoolCapacity.from_dict(system_pool_capacity_model_json).__dict__
        system_pool_capacity_model2 = SystemPoolCapacity(**system_pool_capacity_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_capacity_model == system_pool_capacity_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_capacity_model_json2 = system_pool_capacity_model.to_dict()
        assert system_pool_capacity_model_json2 == system_pool_capacity_model_json

class TestSystemPoolMaxAvailable():
    """
    Test Class for SystemPoolMaxAvailable
    """

    def test_system_pool_max_available_serialization(self):
        """
        Test serialization/deserialization for SystemPoolMaxAvailable
        """

        # Construct a json representation of a SystemPoolMaxAvailable model
        system_pool_max_available_model_json = {}
        system_pool_max_available_model_json['cores'] = 72.5
        system_pool_max_available_model_json['id'] = 38
        system_pool_max_available_model_json['memory'] = 38

        # Construct a model instance of SystemPoolMaxAvailable by calling from_dict on the json representation
        system_pool_max_available_model = SystemPoolMaxAvailable.from_dict(system_pool_max_available_model_json)
        assert system_pool_max_available_model != False

        # Construct a model instance of SystemPoolMaxAvailable by calling from_dict on the json representation
        system_pool_max_available_model_dict = SystemPoolMaxAvailable.from_dict(system_pool_max_available_model_json).__dict__
        system_pool_max_available_model2 = SystemPoolMaxAvailable(**system_pool_max_available_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_max_available_model == system_pool_max_available_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_max_available_model_json2 = system_pool_max_available_model.to_dict()
        assert system_pool_max_available_model_json2 == system_pool_max_available_model_json

class TestSystemPoolMaxCoresAvailable():
    """
    Test Class for SystemPoolMaxCoresAvailable
    """

    def test_system_pool_max_cores_available_serialization(self):
        """
        Test serialization/deserialization for SystemPoolMaxCoresAvailable
        """

        # Construct a json representation of a SystemPoolMaxCoresAvailable model
        system_pool_max_cores_available_model_json = {}
        system_pool_max_cores_available_model_json['cores'] = 72.5
        system_pool_max_cores_available_model_json['id'] = 38
        system_pool_max_cores_available_model_json['memory'] = 38

        # Construct a model instance of SystemPoolMaxCoresAvailable by calling from_dict on the json representation
        system_pool_max_cores_available_model = SystemPoolMaxCoresAvailable.from_dict(system_pool_max_cores_available_model_json)
        assert system_pool_max_cores_available_model != False

        # Construct a model instance of SystemPoolMaxCoresAvailable by calling from_dict on the json representation
        system_pool_max_cores_available_model_dict = SystemPoolMaxCoresAvailable.from_dict(system_pool_max_cores_available_model_json).__dict__
        system_pool_max_cores_available_model2 = SystemPoolMaxCoresAvailable(**system_pool_max_cores_available_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_max_cores_available_model == system_pool_max_cores_available_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_max_cores_available_model_json2 = system_pool_max_cores_available_model.to_dict()
        assert system_pool_max_cores_available_model_json2 == system_pool_max_cores_available_model_json

class TestSystemPoolMaxMemoryAvailable():
    """
    Test Class for SystemPoolMaxMemoryAvailable
    """

    def test_system_pool_max_memory_available_serialization(self):
        """
        Test serialization/deserialization for SystemPoolMaxMemoryAvailable
        """

        # Construct a json representation of a SystemPoolMaxMemoryAvailable model
        system_pool_max_memory_available_model_json = {}
        system_pool_max_memory_available_model_json['cores'] = 72.5
        system_pool_max_memory_available_model_json['id'] = 38
        system_pool_max_memory_available_model_json['memory'] = 38

        # Construct a model instance of SystemPoolMaxMemoryAvailable by calling from_dict on the json representation
        system_pool_max_memory_available_model = SystemPoolMaxMemoryAvailable.from_dict(system_pool_max_memory_available_model_json)
        assert system_pool_max_memory_available_model != False

        # Construct a model instance of SystemPoolMaxMemoryAvailable by calling from_dict on the json representation
        system_pool_max_memory_available_model_dict = SystemPoolMaxMemoryAvailable.from_dict(system_pool_max_memory_available_model_json).__dict__
        system_pool_max_memory_available_model2 = SystemPoolMaxMemoryAvailable(**system_pool_max_memory_available_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_max_memory_available_model == system_pool_max_memory_available_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_max_memory_available_model_json2 = system_pool_max_memory_available_model.to_dict()
        assert system_pool_max_memory_available_model_json2 == system_pool_max_memory_available_model_json

class TestSystemPoolSharedCoreRatio():
    """
    Test Class for SystemPoolSharedCoreRatio
    """

    def test_system_pool_shared_core_ratio_serialization(self):
        """
        Test serialization/deserialization for SystemPoolSharedCoreRatio
        """

        # Construct a json representation of a SystemPoolSharedCoreRatio model
        system_pool_shared_core_ratio_model_json = {}
        system_pool_shared_core_ratio_model_json['min'] = 72.5
        system_pool_shared_core_ratio_model_json['max'] = 72.5
        system_pool_shared_core_ratio_model_json['default'] = 72.5

        # Construct a model instance of SystemPoolSharedCoreRatio by calling from_dict on the json representation
        system_pool_shared_core_ratio_model = SystemPoolSharedCoreRatio.from_dict(system_pool_shared_core_ratio_model_json)
        assert system_pool_shared_core_ratio_model != False

        # Construct a model instance of SystemPoolSharedCoreRatio by calling from_dict on the json representation
        system_pool_shared_core_ratio_model_dict = SystemPoolSharedCoreRatio.from_dict(system_pool_shared_core_ratio_model_json).__dict__
        system_pool_shared_core_ratio_model2 = SystemPoolSharedCoreRatio(**system_pool_shared_core_ratio_model_dict)

        # Verify the model instances are equivalent
        assert system_pool_shared_core_ratio_model == system_pool_shared_core_ratio_model2

        # Convert model instance back to dict and verify no loss of data
        system_pool_shared_core_ratio_model_json2 = system_pool_shared_core_ratio_model.to_dict()
        assert system_pool_shared_core_ratio_model_json2 == system_pool_shared_core_ratio_model_json

class TestTask():
    """
    Test Class for Task
    """

    def test_task_serialization(self):
        """
        Test serialization/deserialization for Task
        """

        # Construct a json representation of a Task model
        task_model_json = {}
        task_model_json['taskID'] = 'testString'
        task_model_json['operation'] = 'testString'
        task_model_json['cloudInstanceID'] = 'testString'
        task_model_json['componentType'] = 'testString'
        task_model_json['componentID'] = 'testString'
        task_model_json['status'] = 'testString'
        task_model_json['statusDetail'] = 'testString'
        task_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        task_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model = Task.from_dict(task_model_json)
        assert task_model != False

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model_dict = Task.from_dict(task_model_json).__dict__
        task_model2 = Task(**task_model_dict)

        # Verify the model instances are equivalent
        assert task_model == task_model2

        # Convert model instance back to dict and verify no loss of data
        task_model_json2 = task_model.to_dict()
        assert task_model_json2 == task_model_json

class TestTenant():
    """
    Test Class for Tenant
    """

    def test_tenant_serialization(self):
        """
        Test serialization/deserialization for Tenant
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ssh_key_model = {} # SSHKey
        ssh_key_model['name'] = 'testString'
        ssh_key_model['sshKey'] = 'testString'
        ssh_key_model['creationDate'] = '2020-01-28T18:40:40.123456Z'

        cloud_instance_usage_limits_model = {} # CloudInstanceUsageLimits
        cloud_instance_usage_limits_model['instances'] = 72.5
        cloud_instance_usage_limits_model['memory'] = 72.5
        cloud_instance_usage_limits_model['procUnits'] = 72.5
        cloud_instance_usage_limits_model['processors'] = 72.5
        cloud_instance_usage_limits_model['storage'] = 72.5
        cloud_instance_usage_limits_model['instanceMemory'] = 72.5
        cloud_instance_usage_limits_model['instanceProcUnits'] = 72.5
        cloud_instance_usage_limits_model['peeringNetworks'] = 38
        cloud_instance_usage_limits_model['peeringBandwidth'] = 38
        cloud_instance_usage_limits_model['storageSSD'] = 72.5
        cloud_instance_usage_limits_model['storageStandard'] = 72.5

        cloud_instance_reference_model = {} # CloudInstanceReference
        cloud_instance_reference_model['cloudInstanceID'] = 'testString'
        cloud_instance_reference_model['name'] = 'testString'
        cloud_instance_reference_model['region'] = 'testString'
        cloud_instance_reference_model['enabled'] = True
        cloud_instance_reference_model['initialized'] = True
        cloud_instance_reference_model['limits'] = cloud_instance_usage_limits_model
        cloud_instance_reference_model['capabilities'] = ['testString']
        cloud_instance_reference_model['href'] = 'testString'

        peering_network_model = {} # PeeringNetwork
        peering_network_model['projectName'] = 'testString'
        peering_network_model['cidr'] = 'testString'
        peering_network_model['dnsServers'] = ['testString']

        # Construct a json representation of a Tenant model
        tenant_model_json = {}
        tenant_model_json['tenantID'] = 'testString'
        tenant_model_json['enabled'] = True
        tenant_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        tenant_model_json['sshKeys'] = [ssh_key_model]
        tenant_model_json['cloudInstances'] = [cloud_instance_reference_model]
        tenant_model_json['icn'] = 'testString'
        tenant_model_json['peeringNetworks'] = [peering_network_model]

        # Construct a model instance of Tenant by calling from_dict on the json representation
        tenant_model = Tenant.from_dict(tenant_model_json)
        assert tenant_model != False

        # Construct a model instance of Tenant by calling from_dict on the json representation
        tenant_model_dict = Tenant.from_dict(tenant_model_json).__dict__
        tenant_model2 = Tenant(**tenant_model_dict)

        # Verify the model instances are equivalent
        assert tenant_model == tenant_model2

        # Convert model instance back to dict and verify no loss of data
        tenant_model_json2 = tenant_model.to_dict()
        assert tenant_model_json2 == tenant_model_json

class TestVirtualCores():
    """
    Test Class for VirtualCores
    """

    def test_virtual_cores_serialization(self):
        """
        Test serialization/deserialization for VirtualCores
        """

        # Construct a json representation of a VirtualCores model
        virtual_cores_model_json = {}
        virtual_cores_model_json['min'] = 38
        virtual_cores_model_json['max'] = 38
        virtual_cores_model_json['assigned'] = 1

        # Construct a model instance of VirtualCores by calling from_dict on the json representation
        virtual_cores_model = VirtualCores.from_dict(virtual_cores_model_json)
        assert virtual_cores_model != False

        # Construct a model instance of VirtualCores by calling from_dict on the json representation
        virtual_cores_model_dict = VirtualCores.from_dict(virtual_cores_model_json).__dict__
        virtual_cores_model2 = VirtualCores(**virtual_cores_model_dict)

        # Verify the model instances are equivalent
        assert virtual_cores_model == virtual_cores_model2

        # Convert model instance back to dict and verify no loss of data
        virtual_cores_model_json2 = virtual_cores_model.to_dict()
        assert virtual_cores_model_json2 == virtual_cores_model_json

class TestVolume():
    """
    Test Class for Volume
    """

    def test_volume_serialization(self):
        """
        Test serialization/deserialization for Volume
        """

        # Construct a json representation of a Volume model
        volume_model_json = {}
        volume_model_json['volumeID'] = 'testString'
        volume_model_json['name'] = 'testString'
        volume_model_json['state'] = 'testString'
        volume_model_json['size'] = 72.5
        volume_model_json['shareable'] = True
        volume_model_json['bootable'] = True
        volume_model_json['bootVolume'] = True
        volume_model_json['deleteOnTermination'] = True
        volume_model_json['diskType'] = 'testString'
        volume_model_json['wwn'] = 'testString'
        volume_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        volume_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        volume_model_json['pvmInstanceIDs'] = ['testString']

        # Construct a model instance of Volume by calling from_dict on the json representation
        volume_model = Volume.from_dict(volume_model_json)
        assert volume_model != False

        # Construct a model instance of Volume by calling from_dict on the json representation
        volume_model_dict = Volume.from_dict(volume_model_json).__dict__
        volume_model2 = Volume(**volume_model_dict)

        # Verify the model instances are equivalent
        assert volume_model == volume_model2

        # Convert model instance back to dict and verify no loss of data
        volume_model_json2 = volume_model.to_dict()
        assert volume_model_json2 == volume_model_json

class TestVolumeReference():
    """
    Test Class for VolumeReference
    """

    def test_volume_reference_serialization(self):
        """
        Test serialization/deserialization for VolumeReference
        """

        # Construct a json representation of a VolumeReference model
        volume_reference_model_json = {}
        volume_reference_model_json['volumeID'] = 'testString'
        volume_reference_model_json['name'] = 'testString'
        volume_reference_model_json['state'] = 'testString'
        volume_reference_model_json['size'] = 72.5
        volume_reference_model_json['shareable'] = True
        volume_reference_model_json['bootable'] = True
        volume_reference_model_json['bootVolume'] = True
        volume_reference_model_json['deleteOnTermination'] = True
        volume_reference_model_json['diskType'] = 'testString'
        volume_reference_model_json['wwn'] = 'testString'
        volume_reference_model_json['creationDate'] = '2020-01-28T18:40:40.123456Z'
        volume_reference_model_json['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        volume_reference_model_json['href'] = 'testString'
        volume_reference_model_json['pvmInstanceIDs'] = ['testString']

        # Construct a model instance of VolumeReference by calling from_dict on the json representation
        volume_reference_model = VolumeReference.from_dict(volume_reference_model_json)
        assert volume_reference_model != False

        # Construct a model instance of VolumeReference by calling from_dict on the json representation
        volume_reference_model_dict = VolumeReference.from_dict(volume_reference_model_json).__dict__
        volume_reference_model2 = VolumeReference(**volume_reference_model_dict)

        # Verify the model instances are equivalent
        assert volume_reference_model == volume_reference_model2

        # Convert model instance back to dict and verify no loss of data
        volume_reference_model_json2 = volume_reference_model.to_dict()
        assert volume_reference_model_json2 == volume_reference_model_json

class TestVolumes():
    """
    Test Class for Volumes
    """

    def test_volumes_serialization(self):
        """
        Test serialization/deserialization for Volumes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        volume_reference_model = {} # VolumeReference
        volume_reference_model['volumeID'] = 'testString'
        volume_reference_model['name'] = 'testString'
        volume_reference_model['state'] = 'testString'
        volume_reference_model['size'] = 72.5
        volume_reference_model['shareable'] = True
        volume_reference_model['bootable'] = True
        volume_reference_model['bootVolume'] = True
        volume_reference_model['deleteOnTermination'] = True
        volume_reference_model['diskType'] = 'testString'
        volume_reference_model['wwn'] = 'testString'
        volume_reference_model['creationDate'] = '2020-01-28T18:40:40.123456Z'
        volume_reference_model['lastUpdateDate'] = '2020-01-28T18:40:40.123456Z'
        volume_reference_model['href'] = 'testString'
        volume_reference_model['pvmInstanceIDs'] = ['testString']

        # Construct a json representation of a Volumes model
        volumes_model_json = {}
        volumes_model_json['volumes'] = [volume_reference_model]

        # Construct a model instance of Volumes by calling from_dict on the json representation
        volumes_model = Volumes.from_dict(volumes_model_json)
        assert volumes_model != False

        # Construct a model instance of Volumes by calling from_dict on the json representation
        volumes_model_dict = Volumes.from_dict(volumes_model_json).__dict__
        volumes_model2 = Volumes(**volumes_model_dict)

        # Verify the model instances are equivalent
        assert volumes_model == volumes_model2

        # Convert model instance back to dict and verify no loss of data
        volumes_model_json2 = volumes_model.to_dict()
        assert volumes_model_json2 == volumes_model_json

class TestVolumesCloneResponse():
    """
    Test Class for VolumesCloneResponse
    """

    def test_volumes_clone_response_serialization(self):
        """
        Test serialization/deserialization for VolumesCloneResponse
        """

        # Construct a json representation of a VolumesCloneResponse model
        volumes_clone_response_model_json = {}
        volumes_clone_response_model_json['clonedVolumes'] = {}

        # Construct a model instance of VolumesCloneResponse by calling from_dict on the json representation
        volumes_clone_response_model = VolumesCloneResponse.from_dict(volumes_clone_response_model_json)
        assert volumes_clone_response_model != False

        # Construct a model instance of VolumesCloneResponse by calling from_dict on the json representation
        volumes_clone_response_model_dict = VolumesCloneResponse.from_dict(volumes_clone_response_model_json).__dict__
        volumes_clone_response_model2 = VolumesCloneResponse(**volumes_clone_response_model_dict)

        # Verify the model instances are equivalent
        assert volumes_clone_response_model == volumes_clone_response_model2

        # Convert model instance back to dict and verify no loss of data
        volumes_clone_response_model_json2 = volumes_clone_response_model.to_dict()
        assert volumes_clone_response_model_json2 == volumes_clone_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
