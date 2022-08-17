# coding: utf-8

# (C) Copyright IBM Corp. 2022.
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

# IBM OpenAPI SDK Code Generator Version: 3.44.0-98838c07-20220128-151531

"""
IBM WML Elastic Distributed Inference

API Version: 2.3.0
"""

from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
# from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ElasticDistributedInferenceV2(BaseService):
    """The IBM WML Elastic Distributed Inference V2 service."""

    DEFAULT_SERVICE_URL = 'https://ibm-wml-elastic-distributed-inference.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'ibm_wml_elastic_distributed_inference'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ElasticDistributedInferenceV2':
        """
        Return a new client for the IBM WML Elastic Distributed Inference service
               using the specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the IBM WML Elastic Distributed Inference service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Auth
    #########################


    def get_auth_token(self,
        **kwargs
    ) -> DetailedResponse:
        """
        User logon and get auth token with Basic Auth mode.

        User logon and get auth token with Basic Auth mode.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Token` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_auth_token')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=UTF-8'

        url = '/dlim/v1/auth/token'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_inference_token(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Auth to get a service token to do inference.

        Accquire a service token which is used as token in any inference request.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_inference_token')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/dlim/v1/auth/token/inference'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Inference
    #########################


    def run_inference(self,
        model_name: str,
        data: dict, 
        *,
        run_inference_request: 'RunInferenceRequest' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Input data for inference, and return inference result.

        Input data for inference, and return inference result.  Permission required:
        Inference Run.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param RunInferenceRequest run_inference_request: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='run_inference')
        headers.update(sdk_headers)

        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/inference/{model_name}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Deployment
    #########################


    def deploy_model(self,
        
        *,
        body: BinaryIO = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Upload model package files.

        Upload model package files.  Permission required: Inference Publish.

        :param str x_auth_token:
        :param BinaryIO body: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='deploy_model')
        headers.update(sdk_headers)
        
        data = body
        headers['content-type'] = 'application/octet-stream'
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/dlim/v1/deployment/model'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def re_deploy_model(self,
        model: str,
        *,
        body: BinaryIO = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Re-deploy and publish a model package.

        Deploy and publish an exsiting model package.  Permission required: Inference
        Publish.

        :param str x_auth_token:
        :param str model: An existing model name which must be matched with the
               model description in your package for redeploying.
        :param BinaryIO body: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if model is None:
            raise ValueError('model must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='re_deploy_model')
        headers.update(sdk_headers)

        data = body
        headers['content-type'] = 'application/octet-stream'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model']
        path_param_values = self.encode_path_vars(model)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/deployment/model/{model}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Runtime
    #########################


    def get_runtimes(self,
        
        **kwargs
    ) -> DetailedResponse:
        """
        Get all the available runtimes.

        Get all the available runtimes.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Runtimes` object
        """

    
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_runtimes')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/dlim/v1/deployment/runtime'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def new_runtime(self,
        runtime: dict,
        **kwargs
    ) -> DetailedResponse:
        """
        Insert a new custom runtime.

        Insert a new custom runtime.  Permission required: Inference Publish.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param dict runtime: a `dict` containing the new runtime definition
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Success` object
        """
        if runtime is None:
            raise ValueError('runtime must be provided')

        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='new_runtime')
        headers.update(sdk_headers)

        data = json.dumps(runtime)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/dlim/v1/deployment/runtime'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def update_runtime(self,
        custom_runtime: str,
        runtime: dict,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the provided runtime.

        Update the provided runtime.  Permission required: Inference Update.

        :param str custom_runtime: runtime name.
        :param dict runtime: runtime definition to be updated.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Success` object
        """
        if custom_runtime is None:
            raise ValueError('custom_runtime must be provided')

        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_runtime')
        headers.update(sdk_headers)

        data = json.dumps(runtime)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'


        path_param_keys = ['custom_runtime']
        path_param_values = self.encode_path_vars(custom_runtime)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/deployment/runtime/{custom_runtime}'.format(**path_param_dict)

        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_runtime_details(self,
        
        custom_runtime: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get provided runtime detail.

        Get provided runtime detail.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str custom_runtime: Name of the custom runtime.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Runtime` object
        """

        
            
        if custom_runtime is None:
            raise ValueError('custom_runtime must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_runtime_details')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['custom_runtime']
        path_param_values = self.encode_path_vars(custom_runtime)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/deployment/runtime/{custom_runtime}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_runtime(self,
        
        custom_runtime: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete the provided runtime.

        Delete the provided runtime.  Permission required: Inference Delete.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str custom_runtime: Name of the custom runtime.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Success` object
        """

        
            
        if custom_runtime is None:
            raise ValueError('custom_runtime must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_runtime')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['custom_runtime']
        path_param_values = self.encode_path_vars(custom_runtime)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/deployment/runtime/{custom_runtime}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Model
    #########################


    def get_models(self,
        
        **kwargs
    ) -> DetailedResponse:
        """
        Get all models.

        Get all models.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[Model]` result
        """

        
            
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_models')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/dlim/v1/model'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def new_model(self,
        
        *,
        schema_version: str = None,
        name: str = None,
        tag: str = None,
        weight_path: str = None,
        model_path: str = None,
        size: int = None,
        runtime: str = None,
        kernel_path: str = None,
        uid: str = None,
        create_time: int = None,
        last_updated_time: int = None,
        started_at: int = None,
        creator: str = None,
        attributes: List['ModelAttributesItem'] = None,
        mk_environments: List['ModelMkEnvironmentsItem'] = None,
        service_uri: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new model.

        Create a new model.  Permission required: Inference Publish.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str schema_version: (optional)
        :param str name: (optional)
        :param str tag: (optional)
        :param str weight_path: (optional)
        :param str model_path: (optional)
        :param int size: (optional)
        :param str runtime: (optional)
        :param str kernel_path: (optional)
        :param str uid: (optional)
        :param int create_time: (optional)
        :param int last_updated_time: (optional)
        :param int started_at: (optional)
        :param str creator: (optional)
        :param List[ModelAttributesItem] attributes: (optional)
        :param List[ModelMkEnvironmentsItem] mk_environments: (optional)
        :param str service_uri: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if attributes is not None:
            attributes = [convert_model(x) for x in attributes]
        if mk_environments is not None:
            mk_environments = [convert_model(x) for x in mk_environments]
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='new_model')
        headers.update(sdk_headers)

        data = {
            'schema_version': schema_version,
            'name': name,
            'tag': tag,
            'weight_path': weight_path,
            'model_path': model_path,
            'size': size,
            'runtime': runtime,
            'kernel_path': kernel_path,
            'uid': uid,
            'create_time': create_time,
            'last_updated_time': last_updated_time,
            'started_at': started_at,
            'creator': creator,
            'attributes': attributes,
            'mk_environments': mk_environments,
            'service_uri': service_uri
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/dlim/v1/model'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_extensions(self,
        
        **kwargs
    ) -> DetailedResponse:
        """
        Get all models and extension information.

        Get all models.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ModelExtensions` object
        """

        
            
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model_extensions')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/dlim/v1/modelextension'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a specific model.

        Get a specific model.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Model` object
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_model(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a specific model.

        Delete a specific model.  Permission required: Inference Delete.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model(self,
        
        model_name: str,
        schema_version: str,
        name: str,
        tag: str,
        weight_path: str,
        model_path: str,
        size: int,
        runtime: str,
        kernel_path: str,
        *,
        uid: str = None,
        create_time: int = None,
        last_updated_time: int = None,
        started_at: int = None,
        creator: str = None,
        attributes: List['ModelAttributesItem'] = None,
        mk_environments: List['ModelMkEnvironmentsItem'] = None,
        service_uri: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a specific model.

        Update a specific model.  Permission required: Inference Update.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param str schema_version:
        :param str name:
        :param str tag:
        :param str weight_path:
        :param str model_path:
        :param int size:
        :param str runtime:
        :param str kernel_path:
        :param str uid: (optional)
        :param int create_time: (optional)
        :param int last_updated_time: (optional)
        :param int started_at: (optional)
        :param str creator: (optional)
        :param List[ModelAttributesItem] attributes: (optional)
        :param List[ModelMkEnvironmentsItem] mk_environments: (optional)
        :param str service_uri: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        if schema_version is None:
            raise ValueError('schema_version must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if tag is None:
            raise ValueError('tag must be provided')
        if weight_path is None:
            raise ValueError('weight_path must be provided')
        if model_path is None:
            raise ValueError('model_path must be provided')
        if size is None:
            raise ValueError('size must be provided')
        if runtime is None:
            raise ValueError('runtime must be provided')
        if kernel_path is None:
            raise ValueError('kernel_path must be provided')
        if attributes is not None:
            attributes = [convert_model(x) for x in attributes]
        if mk_environments is not None:
            mk_environments = [convert_model(x) for x in mk_environments]
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_model')
        headers.update(sdk_headers)

        data = {
            'schema_version': schema_version,
            'name': name,
            'tag': tag,
            'weight_path': weight_path,
            'model_path': model_path,
            'size': size,
            'runtime': runtime,
            'kernel_path': kernel_path,
            'uid': uid,
            'create_time': create_time,
            'last_updated_time': last_updated_time,
            'started_at': started_at,
            'creator': creator,
            'attributes': attributes,
            'mk_environments': mk_environments,
            'service_uri': service_uri
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def start_model_inference(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Start a specific model.

        Start a specific model.  Permission required: Inference Start.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='start_model_inference')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/operation/start'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_model_inference(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop a specific model.

        Stop a specific model.  Permission required: Inference Stop.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='stop_model_inference')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/operation/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_instance(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a specific model instance information.

        Get a specific model instance information.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ModelInstance` object
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/instance'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_readme(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a specific model readme information.

        Get a specific model readme information.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetModelReadmeResponse` object
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model_readme')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/readme'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model_readme(self,
        
        model_name: str,
        *,
        readme: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a specific model readme information.

        Update a specific model readme information.  Permission required: Inference
        Update.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param str readme: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_model_readme')
        headers.update(sdk_headers)

        data = {
            'readme': readme
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/readme'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_stream_url(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a specific model streaming URL.

        Get a specific model streaming URL.  Permission required: Inference List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetModelStreamURLResponse` object
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model_stream_url')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/streaming'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Profile
    #########################


    def get_model_profile(self,
        
        model_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get application profile for a specific model.

        Get application profile for a specific model.  Permission required: Inference
        List.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ModelAppProfile` object
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')
        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_model_profile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/appprofile'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model_profile(self,
        
        model_name: str,
        mode_profile: dict,
        *,
        create_time: str = None,
        last_update_time: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update application profile for a specific model.

        Update application profile for a specific model.  Permission required: Inference
        Update.

        :param str x_auth_token: Auth Token used to authenticate API.
        :param str model_name: Name of the model.
        :param dict mode_profile: The model profile.
        :param str create_time: (optional)
        :param str last_update_time: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        
            
        if model_name is None:
            raise ValueError('model_name must be provided')

        headers = {
            
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_model_profile')
        headers.update(sdk_headers)

        data = json.dumps(mode_profile)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['model_name']
        path_param_values = self.encode_path_vars(model_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/dlim/v1/model/{model_name}/appprofile'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class GetModelReadmeResponse():
    """
    GetModelReadmeResponse.

    :attr str readme: (optional)
    """

    def __init__(self,
                 *,
                 readme: str = None) -> None:
        """
        Initialize a GetModelReadmeResponse object.

        :param str readme: (optional)
        """
        self.readme = readme

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetModelReadmeResponse':
        """Initialize a GetModelReadmeResponse object from a json dictionary."""
        args = {}
        if 'readme' in _dict:
            args['readme'] = _dict.get('readme')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetModelReadmeResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'readme') and self.readme is not None:
            _dict['readme'] = self.readme
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetModelReadmeResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetModelReadmeResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetModelReadmeResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetModelStreamURLResponse():
    """
    GetModelStreamURLResponse.

    :attr str streaming_service_uri: (optional)
    """

    def __init__(self,
                 *,
                 streaming_service_uri: str = None) -> None:
        """
        Initialize a GetModelStreamURLResponse object.

        :param str streaming_service_uri: (optional)
        """
        self.streaming_service_uri = streaming_service_uri

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetModelStreamURLResponse':
        """Initialize a GetModelStreamURLResponse object from a json dictionary."""
        args = {}
        if 'streaming_service_uri' in _dict:
            args['streaming_service_uri'] = _dict.get('streaming_service_uri')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetModelStreamURLResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'streaming_service_uri') and self.streaming_service_uri is not None:
            _dict['streaming_service_uri'] = self.streaming_service_uri
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetModelStreamURLResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetModelStreamURLResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetModelStreamURLResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Model():
    """
    Model.

    :attr str schema_version:
    :attr str uid: (optional)
    :attr str name:
    :attr str tag:
    :attr str weight_path:
    :attr str model_path:
    :attr int size:
    :attr int create_time: (optional)
    :attr int last_updated_time: (optional)
    :attr int started_at: (optional)
    :attr str creator: (optional)
    :attr List[ModelAttributesItem] attributes: (optional)
    :attr str runtime:
    :attr str kernel_path:
    :attr List[ModelMkEnvironmentsItem] mk_environments: (optional)
    :attr str service_uri: (optional)
    """

    def __init__(self,
                 schema_version: str,
                 name: str,
                 tag: str,
                 weight_path: str,
                 model_path: str,
                 size: int,
                 runtime: str,
                 kernel_path: str,
                 *,
                 uid: str = None,
                 create_time: int = None,
                 last_updated_time: int = None,
                 started_at: int = None,
                 creator: str = None,
                 attributes: List['ModelAttributesItem'] = None,
                 mk_environments: List['ModelMkEnvironmentsItem'] = None,
                 service_uri: str = None) -> None:
        """
        Initialize a Model object.

        :param str schema_version:
        :param str name:
        :param str tag:
        :param str weight_path:
        :param str model_path:
        :param int size:
        :param str runtime:
        :param str kernel_path:
        :param str uid: (optional)
        :param int create_time: (optional)
        :param int last_updated_time: (optional)
        :param int started_at: (optional)
        :param str creator: (optional)
        :param List[ModelAttributesItem] attributes: (optional)
        :param List[ModelMkEnvironmentsItem] mk_environments: (optional)
        :param str service_uri: (optional)
        """
        self.schema_version = schema_version
        self.uid = uid
        self.name = name
        self.tag = tag
        self.weight_path = weight_path
        self.model_path = model_path
        self.size = size
        self.create_time = create_time
        self.last_updated_time = last_updated_time
        self.started_at = started_at
        self.creator = creator
        self.attributes = attributes
        self.runtime = runtime
        self.kernel_path = kernel_path
        self.mk_environments = mk_environments
        self.service_uri = service_uri

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Model':
        """Initialize a Model object from a json dictionary."""
        args = {}
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        else:
            raise ValueError('Required property \'schema_version\' not present in Model JSON')
        if 'uid' in _dict:
            args['uid'] = _dict.get('uid')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Model JSON')
        if 'tag' in _dict:
            args['tag'] = _dict.get('tag')
        else:
            raise ValueError('Required property \'tag\' not present in Model JSON')
        if 'weight_path' in _dict:
            args['weight_path'] = _dict.get('weight_path')
        else:
            raise ValueError('Required property \'weight_path\' not present in Model JSON')
        if 'model_path' in _dict:
            args['model_path'] = _dict.get('model_path')
        else:
            raise ValueError('Required property \'model_path\' not present in Model JSON')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        else:
            raise ValueError('Required property \'size\' not present in Model JSON')
        if 'create_time' in _dict:
            args['create_time'] = _dict.get('create_time')
        if 'last_updated_time' in _dict:
            args['last_updated_time'] = _dict.get('last_updated_time')
        if 'started_at' in _dict:
            args['started_at'] = _dict.get('started_at')
        if 'creator' in _dict:
            args['creator'] = _dict.get('creator')
        if 'attributes' in _dict:
            args['attributes'] = [ModelAttributesItem.from_dict(x) for x in _dict.get('attributes')]
        if 'runtime' in _dict:
            args['runtime'] = _dict.get('runtime')
        else:
            raise ValueError('Required property \'runtime\' not present in Model JSON')
        if 'kernel_path' in _dict:
            args['kernel_path'] = _dict.get('kernel_path')
        else:
            raise ValueError('Required property \'kernel_path\' not present in Model JSON')
        if 'mk_environments' in _dict:
            args['mk_environments'] = [ModelMkEnvironmentsItem.from_dict(x) for x in _dict.get('mk_environments')]
        if 'service_uri' in _dict:
            args['service_uri'] = _dict.get('service_uri')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Model object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tag') and self.tag is not None:
            _dict['tag'] = self.tag
        if hasattr(self, 'weight_path') and self.weight_path is not None:
            _dict['weight_path'] = self.weight_path
        if hasattr(self, 'model_path') and self.model_path is not None:
            _dict['model_path'] = self.model_path
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = self.create_time
        if hasattr(self, 'last_updated_time') and self.last_updated_time is not None:
            _dict['last_updated_time'] = self.last_updated_time
        if hasattr(self, 'started_at') and self.started_at is not None:
            _dict['started_at'] = self.started_at
        if hasattr(self, 'creator') and self.creator is not None:
            _dict['creator'] = self.creator
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime
        if hasattr(self, 'kernel_path') and self.kernel_path is not None:
            _dict['kernel_path'] = self.kernel_path
        if hasattr(self, 'mk_environments') and self.mk_environments is not None:
            _dict['mk_environments'] = [x.to_dict() for x in self.mk_environments]
        if hasattr(self, 'service_uri') and self.service_uri is not None:
            _dict['service_uri'] = self.service_uri
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Model object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Model') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Model') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfile():
    """
    ModelAppProfile.

    :attr str create_time: (optional)
    :attr ModelAppProfileKernel kernel:
    :attr str last_update_time: (optional)
    :attr str name:
    :attr ModelAppProfilePolicy policy:
    :attr int replica:
    :attr ModelAppProfileResourceAllocation resource_allocation:
    :attr str schema_version:
    :attr str type:
    """

    def __init__(self,
                 kernel: 'ModelAppProfileKernel',
                 name: str,
                 policy: 'ModelAppProfilePolicy',
                 replica: int,
                 resource_allocation: 'ModelAppProfileResourceAllocation',
                 schema_version: str,
                 type: str,
                 *,
                 create_time: str = None,
                 last_update_time: str = None) -> None:
        """
        Initialize a ModelAppProfile object.

        :param ModelAppProfileKernel kernel:
        :param str name:
        :param ModelAppProfilePolicy policy:
        :param int replica:
        :param ModelAppProfileResourceAllocation resource_allocation:
        :param str schema_version:
        :param str type:
        :param str create_time: (optional)
        :param str last_update_time: (optional)
        """
        self.create_time = create_time
        self.kernel = kernel
        self.last_update_time = last_update_time
        self.name = name
        self.policy = policy
        self.replica = replica
        self.resource_allocation = resource_allocation
        self.schema_version = schema_version
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfile':
        """Initialize a ModelAppProfile object from a json dictionary."""
        args = {}
        if 'create_time' in _dict:
            args['create_time'] = _dict.get('create_time')
        if 'kernel' in _dict:
            args['kernel'] = ModelAppProfileKernel.from_dict(_dict.get('kernel'))
        else:
            raise ValueError('Required property \'kernel\' not present in ModelAppProfile JSON')
        if 'last_update_time' in _dict:
            args['last_update_time'] = _dict.get('last_update_time')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ModelAppProfile JSON')
        if 'policy' in _dict:
            args['policy'] = ModelAppProfilePolicy.from_dict(_dict.get('policy'))
        else:
            raise ValueError('Required property \'policy\' not present in ModelAppProfile JSON')
        if 'replica' in _dict:
            args['replica'] = _dict.get('replica')
        else:
            raise ValueError('Required property \'replica\' not present in ModelAppProfile JSON')
        if 'resource_allocation' in _dict:
            args['resource_allocation'] = ModelAppProfileResourceAllocation.from_dict(_dict.get('resource_allocation'))
        else:
            raise ValueError('Required property \'resource_allocation\' not present in ModelAppProfile JSON')
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        else:
            raise ValueError('Required property \'schema_version\' not present in ModelAppProfile JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ModelAppProfile JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = self.create_time
        if hasattr(self, 'kernel') and self.kernel is not None:
            _dict['kernel'] = self.kernel.to_dict()
        if hasattr(self, 'last_update_time') and self.last_update_time is not None:
            _dict['last_update_time'] = self.last_update_time
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'policy') and self.policy is not None:
            _dict['policy'] = self.policy.to_dict()
        if hasattr(self, 'replica') and self.replica is not None:
            _dict['replica'] = self.replica
        if hasattr(self, 'resource_allocation') and self.resource_allocation is not None:
            _dict['resource_allocation'] = self.resource_allocation.to_dict()
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfileKernel():
    """
    ModelAppProfileKernel.

    :attr int connection_timeout:
    :attr List[ModelAppProfileKernelEnvsItem] envs:
    :attr str gpu:
    :attr str log_directory:
    :attr str run_as:
    :attr str umask:
    :attr str working_directory:
    """

    def __init__(self,
                 connection_timeout: int,
                 envs: List['ModelAppProfileKernelEnvsItem'],
                 gpu: str,
                 log_directory: str,
                 run_as: str,
                 umask: str,
                 working_directory: str) -> None:
        """
        Initialize a ModelAppProfileKernel object.

        :param int connection_timeout:
        :param List[ModelAppProfileKernelEnvsItem] envs:
        :param str gpu:
        :param str log_directory:
        :param str run_as:
        :param str umask:
        :param str working_directory:
        """
        self.connection_timeout = connection_timeout
        self.envs = envs
        self.gpu = gpu
        self.log_directory = log_directory
        self.run_as = run_as
        self.umask = umask
        self.working_directory = working_directory

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfileKernel':
        """Initialize a ModelAppProfileKernel object from a json dictionary."""
        args = {}
        if 'connection_timeout' in _dict:
            args['connection_timeout'] = _dict.get('connection_timeout')
        else:
            raise ValueError('Required property \'connection_timeout\' not present in ModelAppProfileKernel JSON')
        if 'envs' in _dict:
            args['envs'] = [ModelAppProfileKernelEnvsItem.from_dict(x) for x in _dict.get('envs')]
        else:
            raise ValueError('Required property \'envs\' not present in ModelAppProfileKernel JSON')
        if 'gpu' in _dict:
            args['gpu'] = _dict.get('gpu')
        else:
            raise ValueError('Required property \'gpu\' not present in ModelAppProfileKernel JSON')
        if 'log_directory' in _dict:
            args['log_directory'] = _dict.get('log_directory')
        else:
            raise ValueError('Required property \'log_directory\' not present in ModelAppProfileKernel JSON')
        if 'run_as' in _dict:
            args['run_as'] = _dict.get('run_as')
        else:
            raise ValueError('Required property \'run_as\' not present in ModelAppProfileKernel JSON')
        if 'umask' in _dict:
            args['umask'] = _dict.get('umask')
        else:
            raise ValueError('Required property \'umask\' not present in ModelAppProfileKernel JSON')
        if 'working_directory' in _dict:
            args['working_directory'] = _dict.get('working_directory')
        else:
            raise ValueError('Required property \'working_directory\' not present in ModelAppProfileKernel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfileKernel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'connection_timeout') and self.connection_timeout is not None:
            _dict['connection_timeout'] = self.connection_timeout
        if hasattr(self, 'envs') and self.envs is not None:
            _dict['envs'] = [x.to_dict() for x in self.envs]
        if hasattr(self, 'gpu') and self.gpu is not None:
            _dict['gpu'] = self.gpu
        if hasattr(self, 'log_directory') and self.log_directory is not None:
            _dict['log_directory'] = self.log_directory
        if hasattr(self, 'run_as') and self.run_as is not None:
            _dict['run_as'] = self.run_as
        if hasattr(self, 'umask') and self.umask is not None:
            _dict['umask'] = self.umask
        if hasattr(self, 'working_directory') and self.working_directory is not None:
            _dict['working_directory'] = self.working_directory
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfileKernel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfileKernel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfileKernel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfileKernelEnvsItem():
    """
    ModelAppProfileKernelEnvsItem.

    :attr str name:
    :attr str value:
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a ModelAppProfileKernelEnvsItem object.

        :param str name:
        :param str value:
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfileKernelEnvsItem':
        """Initialize a ModelAppProfileKernelEnvsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ModelAppProfileKernelEnvsItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ModelAppProfileKernelEnvsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfileKernelEnvsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfileKernelEnvsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfileKernelEnvsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfileKernelEnvsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfilePolicy():
    """
    ModelAppProfilePolicy.

    :attr int kernel_delay_release_time:
    :attr int kernel_max:
    :attr int kernel_min:
    :attr str name:
    :attr int schedule_interval:
    :attr bool stream_discard_slow_tasks:
    :attr int stream_number_per_group:
    :attr int task_batch_size:
    :attr int task_execution_timeout:
    :attr int task_pipe_size:
    """

    def __init__(self,
                 kernel_delay_release_time: int,
                 kernel_max: int,
                 kernel_min: int,
                 name: str,
                 schedule_interval: int,
                 stream_discard_slow_tasks: bool,
                 stream_number_per_group: int,
                 task_batch_size: int,
                 task_execution_timeout: int,
                 task_pipe_size: int) -> None:
        """
        Initialize a ModelAppProfilePolicy object.

        :param int kernel_delay_release_time:
        :param int kernel_max:
        :param int kernel_min:
        :param str name:
        :param int schedule_interval:
        :param bool stream_discard_slow_tasks:
        :param int stream_number_per_group:
        :param int task_batch_size:
        :param int task_execution_timeout:
        :param int task_pipe_size:
        """
        self.kernel_delay_release_time = kernel_delay_release_time
        self.kernel_max = kernel_max
        self.kernel_min = kernel_min
        self.name = name
        self.schedule_interval = schedule_interval
        self.stream_discard_slow_tasks = stream_discard_slow_tasks
        self.stream_number_per_group = stream_number_per_group
        self.task_batch_size = task_batch_size
        self.task_execution_timeout = task_execution_timeout
        self.task_pipe_size = task_pipe_size

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfilePolicy':
        """Initialize a ModelAppProfilePolicy object from a json dictionary."""
        args = {}
        if 'kernel_delay_release_time' in _dict:
            args['kernel_delay_release_time'] = _dict.get('kernel_delay_release_time')
        else:
            raise ValueError('Required property \'kernel_delay_release_time\' not present in ModelAppProfilePolicy JSON')
        if 'kernel_max' in _dict:
            args['kernel_max'] = _dict.get('kernel_max')
        else:
            raise ValueError('Required property \'kernel_max\' not present in ModelAppProfilePolicy JSON')
        if 'kernel_min' in _dict:
            args['kernel_min'] = _dict.get('kernel_min')
        else:
            raise ValueError('Required property \'kernel_min\' not present in ModelAppProfilePolicy JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ModelAppProfilePolicy JSON')
        if 'schedule_interval' in _dict:
            args['schedule_interval'] = _dict.get('schedule_interval')
        else:
            raise ValueError('Required property \'schedule_interval\' not present in ModelAppProfilePolicy JSON')
        if 'stream_discard_slow_tasks' in _dict:
            args['stream_discard_slow_tasks'] = _dict.get('stream_discard_slow_tasks')
        else:
            raise ValueError('Required property \'stream_discard_slow_tasks\' not present in ModelAppProfilePolicy JSON')
        if 'stream_number_per_group' in _dict:
            args['stream_number_per_group'] = _dict.get('stream_number_per_group')
        else:
            raise ValueError('Required property \'stream_number_per_group\' not present in ModelAppProfilePolicy JSON')
        if 'task_batch_size' in _dict:
            args['task_batch_size'] = _dict.get('task_batch_size')
        else:
            raise ValueError('Required property \'task_batch_size\' not present in ModelAppProfilePolicy JSON')
        if 'task_execution_timeout' in _dict:
            args['task_execution_timeout'] = _dict.get('task_execution_timeout')
        else:
            raise ValueError('Required property \'task_execution_timeout\' not present in ModelAppProfilePolicy JSON')
        if 'task_pipe_size' in _dict:
            args['task_pipe_size'] = _dict.get('task_pipe_size')
        else:
            raise ValueError('Required property \'task_pipe_size\' not present in ModelAppProfilePolicy JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfilePolicy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kernel_delay_release_time') and self.kernel_delay_release_time is not None:
            _dict['kernel_delay_release_time'] = self.kernel_delay_release_time
        if hasattr(self, 'kernel_max') and self.kernel_max is not None:
            _dict['kernel_max'] = self.kernel_max
        if hasattr(self, 'kernel_min') and self.kernel_min is not None:
            _dict['kernel_min'] = self.kernel_min
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'schedule_interval') and self.schedule_interval is not None:
            _dict['schedule_interval'] = self.schedule_interval
        if hasattr(self, 'stream_discard_slow_tasks') and self.stream_discard_slow_tasks is not None:
            _dict['stream_discard_slow_tasks'] = self.stream_discard_slow_tasks
        if hasattr(self, 'stream_number_per_group') and self.stream_number_per_group is not None:
            _dict['stream_number_per_group'] = self.stream_number_per_group
        if hasattr(self, 'task_batch_size') and self.task_batch_size is not None:
            _dict['task_batch_size'] = self.task_batch_size
        if hasattr(self, 'task_execution_timeout') and self.task_execution_timeout is not None:
            _dict['task_execution_timeout'] = self.task_execution_timeout
        if hasattr(self, 'task_pipe_size') and self.task_pipe_size is not None:
            _dict['task_pipe_size'] = self.task_pipe_size
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfilePolicy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfilePolicy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfilePolicy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfileResourceAllocation():
    """
    ModelAppProfileResourceAllocation.

    :attr ModelAppProfileResourceAllocationKernel kernel:
    :attr ModelAppProfileResourceAllocationService service:
    """

    def __init__(self,
                 kernel: 'ModelAppProfileResourceAllocationKernel',
                 service: 'ModelAppProfileResourceAllocationService') -> None:
        """
        Initialize a ModelAppProfileResourceAllocation object.

        :param ModelAppProfileResourceAllocationKernel kernel:
        :param ModelAppProfileResourceAllocationService service:
        """
        self.kernel = kernel
        self.service = service

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfileResourceAllocation':
        """Initialize a ModelAppProfileResourceAllocation object from a json dictionary."""
        args = {}
        if 'kernel' in _dict:
            args['kernel'] = ModelAppProfileResourceAllocationKernel.from_dict(_dict.get('kernel'))
        else:
            raise ValueError('Required property \'kernel\' not present in ModelAppProfileResourceAllocation JSON')
        if 'service' in _dict:
            args['service'] = ModelAppProfileResourceAllocationService.from_dict(_dict.get('service'))
        else:
            raise ValueError('Required property \'service\' not present in ModelAppProfileResourceAllocation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfileResourceAllocation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kernel') and self.kernel is not None:
            _dict['kernel'] = self.kernel.to_dict()
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfileResourceAllocation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfileResourceAllocation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfileResourceAllocation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfileResourceAllocationKernel():
    """
    ModelAppProfileResourceAllocationKernel.

    :attr str consumer:
    :attr str resource_group:
    :attr str resreq:
    :attr str type:
    """

    def __init__(self,
                 consumer: str,
                 resource_group: str,
                 resreq: str,
                 type: str) -> None:
        """
        Initialize a ModelAppProfileResourceAllocationKernel object.

        :param str consumer:
        :param str resource_group:
        :param str resreq:
        :param str type:
        """
        self.consumer = consumer
        self.resource_group = resource_group
        self.resreq = resreq
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfileResourceAllocationKernel':
        """Initialize a ModelAppProfileResourceAllocationKernel object from a json dictionary."""
        args = {}
        if 'consumer' in _dict:
            args['consumer'] = _dict.get('consumer')
        else:
            raise ValueError('Required property \'consumer\' not present in ModelAppProfileResourceAllocationKernel JSON')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in ModelAppProfileResourceAllocationKernel JSON')
        if 'resreq' in _dict:
            args['resreq'] = _dict.get('resreq')
        else:
            raise ValueError('Required property \'resreq\' not present in ModelAppProfileResourceAllocationKernel JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ModelAppProfileResourceAllocationKernel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfileResourceAllocationKernel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'consumer') and self.consumer is not None:
            _dict['consumer'] = self.consumer
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'resreq') and self.resreq is not None:
            _dict['resreq'] = self.resreq
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfileResourceAllocationKernel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfileResourceAllocationKernel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfileResourceAllocationKernel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAppProfileResourceAllocationService():
    """
    ModelAppProfileResourceAllocationService.

    :attr str consumer:
    :attr str resource_group:
    :attr str resreq:
    :attr str type:
    """

    def __init__(self,
                 consumer: str,
                 resource_group: str,
                 resreq: str,
                 type: str) -> None:
        """
        Initialize a ModelAppProfileResourceAllocationService object.

        :param str consumer:
        :param str resource_group:
        :param str resreq:
        :param str type:
        """
        self.consumer = consumer
        self.resource_group = resource_group
        self.resreq = resreq
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAppProfileResourceAllocationService':
        """Initialize a ModelAppProfileResourceAllocationService object from a json dictionary."""
        args = {}
        if 'consumer' in _dict:
            args['consumer'] = _dict.get('consumer')
        else:
            raise ValueError('Required property \'consumer\' not present in ModelAppProfileResourceAllocationService JSON')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in ModelAppProfileResourceAllocationService JSON')
        if 'resreq' in _dict:
            args['resreq'] = _dict.get('resreq')
        else:
            raise ValueError('Required property \'resreq\' not present in ModelAppProfileResourceAllocationService JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ModelAppProfileResourceAllocationService JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAppProfileResourceAllocationService object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'consumer') and self.consumer is not None:
            _dict['consumer'] = self.consumer
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'resreq') and self.resreq is not None:
            _dict['resreq'] = self.resreq
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAppProfileResourceAllocationService object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAppProfileResourceAllocationService') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAppProfileResourceAllocationService') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelAttributesItem():
    """
    ModelAttributesItem.

    :attr str key:
    :attr str value:
    """

    def __init__(self,
                 key: str,
                 value: str) -> None:
        """
        Initialize a ModelAttributesItem object.

        :param str key:
        :param str value:
        """
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelAttributesItem':
        """Initialize a ModelAttributesItem object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in ModelAttributesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ModelAttributesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelAttributesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelAttributesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelAttributesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelAttributesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelExtension():
    """
    ModelExtension.

    :attr str name: (optional)
    :attr str resource_plan: (optional)
    """

    def __init__(self,
                 *,
                 name: str = None,
                 resource_plan: str = None) -> None:
        """
        Initialize a ModelExtension object.

        :param str name: (optional)
        :param str resource_plan: (optional)
        """
        self.name = name
        self.resource_plan = resource_plan

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelExtension':
        """Initialize a ModelExtension object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'resource_plan' in _dict:
            args['resource_plan'] = _dict.get('resource_plan')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelExtension object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'resource_plan') and self.resource_plan is not None:
            _dict['resource_plan'] = self.resource_plan
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelExtension object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelExtension') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelExtension') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelExtensions():
    """
    ModelExtensions.

    :attr List[Model] model_list: (optional)
    :attr List[ModelExtension] extension_list: (optional)
    """

    def __init__(self,
                 *,
                 model_list: List['Model'] = None,
                 extension_list: List['ModelExtension'] = None) -> None:
        """
        Initialize a ModelExtensions object.

        :param List[Model] model_list: (optional)
        :param List[ModelExtension] extension_list: (optional)
        """
        self.model_list = model_list
        self.extension_list = extension_list

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelExtensions':
        """Initialize a ModelExtensions object from a json dictionary."""
        args = {}
        if 'model_list' in _dict:
            args['model_list'] = [Model.from_dict(x) for x in _dict.get('model_list')]
        if 'extension_list' in _dict:
            args['extension_list'] = [ModelExtension.from_dict(x) for x in _dict.get('extension_list')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelExtensions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_list') and self.model_list is not None:
            _dict['model_list'] = [x.to_dict() for x in self.model_list]
        if hasattr(self, 'extension_list') and self.extension_list is not None:
            _dict['extension_list'] = [x.to_dict() for x in self.extension_list]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelExtensions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelExtensions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelExtensions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelInstance():
    """
    ModelInstance.

    :attr List[ModelInstanceInstancesItem] instances:
    :attr str name:
    :attr str state:
    """

    def __init__(self,
                 instances: List['ModelInstanceInstancesItem'],
                 name: str,
                 state: str) -> None:
        """
        Initialize a ModelInstance object.

        :param List[ModelInstanceInstancesItem] instances:
        :param str name:
        :param str state:
        """
        self.instances = instances
        self.name = name
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelInstance':
        """Initialize a ModelInstance object from a json dictionary."""
        args = {}
        if 'instances' in _dict:
            args['instances'] = [ModelInstanceInstancesItem.from_dict(x) for x in _dict.get('instances')]
        else:
            raise ValueError('Required property \'instances\' not present in ModelInstance JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ModelInstance JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ModelInstance JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelInstance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instances') and self.instances is not None:
            _dict['instances'] = [x.to_dict() for x in self.instances]
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelInstance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelInstance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelInstance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelInstanceInstancesItem():
    """
    ModelInstanceInstancesItem.

    :attr int client_number:
    :attr float data_size_per_sec:
    :attr List[ModelInstanceInstancesItemIsdContainerItem] isd_container:
    :attr str isd_uid:
    :attr int pending_tasks:
    :attr float request_per_sec:
    """

    def __init__(self,
                 client_number: int,
                 data_size_per_sec: float,
                 isd_container: List['ModelInstanceInstancesItemIsdContainerItem'],
                 isd_uid: str,
                 pending_tasks: int,
                 request_per_sec: float) -> None:
        """
        Initialize a ModelInstanceInstancesItem object.

        :param int client_number:
        :param float data_size_per_sec:
        :param List[ModelInstanceInstancesItemIsdContainerItem] isd_container:
        :param str isd_uid:
        :param int pending_tasks:
        :param float request_per_sec:
        """
        self.client_number = client_number
        self.data_size_per_sec = data_size_per_sec
        self.isd_container = isd_container
        self.isd_uid = isd_uid
        self.pending_tasks = pending_tasks
        self.request_per_sec = request_per_sec

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelInstanceInstancesItem':
        """Initialize a ModelInstanceInstancesItem object from a json dictionary."""
        args = {}
        if 'client_number' in _dict:
            args['client_number'] = _dict.get('client_number')
        else:
            raise ValueError('Required property \'client_number\' not present in ModelInstanceInstancesItem JSON')
        if 'data_size_per_sec' in _dict:
            args['data_size_per_sec'] = _dict.get('data_size_per_sec')
        else:
            raise ValueError('Required property \'data_size_per_sec\' not present in ModelInstanceInstancesItem JSON')
        if 'isd_container' in _dict:
            args['isd_container'] = [ModelInstanceInstancesItemIsdContainerItem.from_dict(x) for x in _dict.get('isd_container')]
        else:
            raise ValueError('Required property \'isd_container\' not present in ModelInstanceInstancesItem JSON')
        if 'isd_uid' in _dict:
            args['isd_uid'] = _dict.get('isd_uid')
        else:
            raise ValueError('Required property \'isd_uid\' not present in ModelInstanceInstancesItem JSON')
        if 'pending_tasks' in _dict:
            args['pending_tasks'] = _dict.get('pending_tasks')
        else:
            raise ValueError('Required property \'pending_tasks\' not present in ModelInstanceInstancesItem JSON')
        if 'request_per_sec' in _dict:
            args['request_per_sec'] = _dict.get('request_per_sec')
        else:
            raise ValueError('Required property \'request_per_sec\' not present in ModelInstanceInstancesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelInstanceInstancesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_number') and self.client_number is not None:
            _dict['client_number'] = self.client_number
        if hasattr(self, 'data_size_per_sec') and self.data_size_per_sec is not None:
            _dict['data_size_per_sec'] = self.data_size_per_sec
        if hasattr(self, 'isd_container') and self.isd_container is not None:
            _dict['isd_container'] = [x.to_dict() for x in self.isd_container]
        if hasattr(self, 'isd_uid') and self.isd_uid is not None:
            _dict['isd_uid'] = self.isd_uid
        if hasattr(self, 'pending_tasks') and self.pending_tasks is not None:
            _dict['pending_tasks'] = self.pending_tasks
        if hasattr(self, 'request_per_sec') and self.request_per_sec is not None:
            _dict['request_per_sec'] = self.request_per_sec
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelInstanceInstancesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelInstanceInstancesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelInstanceInstancesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelInstanceInstancesItemIsdContainerItem():
    """
    ModelInstanceInstancesItemIsdContainerItem.

    :attr str container_host:
    :attr str container_status:
    :attr str container_uid:
    :attr int failed_task:
    :attr int finished_task:
    :attr int running_task:
    :attr int total_task:
    """

    def __init__(self,
                 container_host: str,
                 container_status: str,
                 container_uid: str,
                 failed_task: int,
                 finished_task: int,
                 running_task: int,
                 total_task: int) -> None:
        """
        Initialize a ModelInstanceInstancesItemIsdContainerItem object.

        :param str container_host:
        :param str container_status:
        :param str container_uid:
        :param int failed_task:
        :param int finished_task:
        :param int running_task:
        :param int total_task:
        """
        self.container_host = container_host
        self.container_status = container_status
        self.container_uid = container_uid
        self.failed_task = failed_task
        self.finished_task = finished_task
        self.running_task = running_task
        self.total_task = total_task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelInstanceInstancesItemIsdContainerItem':
        """Initialize a ModelInstanceInstancesItemIsdContainerItem object from a json dictionary."""
        args = {}
        if 'container_host' in _dict:
            args['container_host'] = _dict.get('container_host')
        else:
            raise ValueError('Required property \'container_host\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'container_status' in _dict:
            args['container_status'] = _dict.get('container_status')
        else:
            raise ValueError('Required property \'container_status\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'container_uid' in _dict:
            args['container_uid'] = _dict.get('container_uid')
        else:
            raise ValueError('Required property \'container_uid\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'failed_task' in _dict:
            args['failed_task'] = _dict.get('failed_task')
        else:
            raise ValueError('Required property \'failed_task\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'finished_task' in _dict:
            args['finished_task'] = _dict.get('finished_task')
        else:
            raise ValueError('Required property \'finished_task\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'running_task' in _dict:
            args['running_task'] = _dict.get('running_task')
        else:
            raise ValueError('Required property \'running_task\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        if 'total_task' in _dict:
            args['total_task'] = _dict.get('total_task')
        else:
            raise ValueError('Required property \'total_task\' not present in ModelInstanceInstancesItemIsdContainerItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelInstanceInstancesItemIsdContainerItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'container_host') and self.container_host is not None:
            _dict['container_host'] = self.container_host
        if hasattr(self, 'container_status') and self.container_status is not None:
            _dict['container_status'] = self.container_status
        if hasattr(self, 'container_uid') and self.container_uid is not None:
            _dict['container_uid'] = self.container_uid
        if hasattr(self, 'failed_task') and self.failed_task is not None:
            _dict['failed_task'] = self.failed_task
        if hasattr(self, 'finished_task') and self.finished_task is not None:
            _dict['finished_task'] = self.finished_task
        if hasattr(self, 'running_task') and self.running_task is not None:
            _dict['running_task'] = self.running_task
        if hasattr(self, 'total_task') and self.total_task is not None:
            _dict['total_task'] = self.total_task
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelInstanceInstancesItemIsdContainerItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelInstanceInstancesItemIsdContainerItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelInstanceInstancesItemIsdContainerItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelMkEnvironmentsItem():
    """
    ModelMkEnvironmentsItem.

    :attr str name:
    :attr str value:
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a ModelMkEnvironmentsItem object.

        :param str name:
        :param str value:
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelMkEnvironmentsItem':
        """Initialize a ModelMkEnvironmentsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ModelMkEnvironmentsItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ModelMkEnvironmentsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelMkEnvironmentsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelMkEnvironmentsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelMkEnvironmentsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelMkEnvironmentsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Runtime():
    """
    Runtime.

    :attr str schema_version: (optional)
    :attr str pre_exec: (optional)
    :attr str machine_type: (optional)
    :attr List[RuntimeEnvsItem] envs: (optional)
    :attr str description: (optional)
    :attr str conda_home: (optional)
    :attr str conda_env_name: (optional)
    :attr str type:
    :attr str docker_img: (optional)
    :attr str launcher:
    :attr int epoch_created: (optional)
    :attr int epoch_updated: (optional)
    """

    def __init__(self,
                 type: str,
                 launcher: str,
                 *,
                 schema_version: str = None,
                 pre_exec: str = None,
                 machine_type: str = None,
                 envs: List['RuntimeEnvsItem'] = None,
                 description: str = None,
                 conda_home: str = None,
                 conda_env_name: str = None,
                 docker_img: str = None,
                 epoch_created: int = None,
                 epoch_updated: int = None) -> None:
        """
        Initialize a Runtime object.

        :param str type:
        :param str launcher:
        :param str schema_version: (optional)
        :param str pre_exec: (optional)
        :param str machine_type: (optional)
        :param List[RuntimeEnvsItem] envs: (optional)
        :param str description: (optional)
        :param str conda_home: (optional)
        :param str conda_env_name: (optional)
        :param str docker_img: (optional)
        :param int epoch_created: (optional)
        :param int epoch_updated: (optional)
        """
        self.schema_version = schema_version
        self.pre_exec = pre_exec
        self.machine_type = machine_type
        self.envs = envs
        self.description = description
        self.conda_home = conda_home
        self.conda_env_name = conda_env_name
        self.type = type
        self.docker_img = docker_img
        self.launcher = launcher
        self.epoch_created = epoch_created
        self.epoch_updated = epoch_updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Runtime':
        """Initialize a Runtime object from a json dictionary."""
        args = {}
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        if 'pre_exec' in _dict:
            args['pre_exec'] = _dict.get('pre_exec')
        if 'machine_type' in _dict:
            args['machine_type'] = _dict.get('machine_type')
        if 'envs' in _dict:
            args['envs'] = [RuntimeEnvsItem.from_dict(x) for x in _dict.get('envs')]
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'conda_home' in _dict:
            args['conda_home'] = _dict.get('conda_home')
        if 'conda_env_name' in _dict:
            args['conda_env_name'] = _dict.get('conda_env_name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in Runtime JSON')
        if 'docker_img' in _dict:
            args['docker_img'] = _dict.get('docker_img')
        if 'launcher' in _dict:
            args['launcher'] = _dict.get('launcher')
        else:
            raise ValueError('Required property \'launcher\' not present in Runtime JSON')
        if 'epoch_created' in _dict:
            args['epoch_created'] = _dict.get('epoch_created')
        if 'epoch_updated' in _dict:
            args['epoch_updated'] = _dict.get('epoch_updated')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Runtime object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'pre_exec') and self.pre_exec is not None:
            _dict['pre_exec'] = self.pre_exec
        if hasattr(self, 'machine_type') and self.machine_type is not None:
            _dict['machine_type'] = self.machine_type
        if hasattr(self, 'envs') and self.envs is not None:
            _dict['envs'] = [x.to_dict() for x in self.envs]
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'conda_home') and self.conda_home is not None:
            _dict['conda_home'] = self.conda_home
        if hasattr(self, 'conda_env_name') and self.conda_env_name is not None:
            _dict['conda_env_name'] = self.conda_env_name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'docker_img') and self.docker_img is not None:
            _dict['docker_img'] = self.docker_img
        if hasattr(self, 'launcher') and self.launcher is not None:
            _dict['launcher'] = self.launcher
        if hasattr(self, 'epoch_created') and self.epoch_created is not None:
            _dict['epoch_created'] = self.epoch_created
        if hasattr(self, 'epoch_updated') and self.epoch_updated is not None:
            _dict['epoch_updated'] = self.epoch_updated
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Runtime object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Runtime') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Runtime') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RuntimeEnvsItem():
    """
    RuntimeEnvsItem.

    :attr str name: (optional)
    :attr str value: (optional)
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None) -> None:
        """
        Initialize a RuntimeEnvsItem object.

        :param str name: (optional)
        :param str value: (optional)
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEnvsItem':
        """Initialize a RuntimeEnvsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEnvsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeEnvsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeEnvsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeEnvsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Runtimes():
    """
    Runtimes.

    :attr str schema_version:
    :attr List[Runtime] runtimes:
    """

    def __init__(self,
                 schema_version: str,
                 runtimes: List['Runtime']) -> None:
        """
        Initialize a Runtimes object.

        :param str schema_version:
        :param List[Runtime] runtimes:
        """
        self.schema_version = schema_version
        self.runtimes = runtimes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Runtimes':
        """Initialize a Runtimes object from a json dictionary."""
        args = {}
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        else:
            raise ValueError('Required property \'schema_version\' not present in Runtimes JSON')
        if 'runtimes' in _dict:
            args['runtimes'] = [Runtime.from_dict(x) for x in _dict.get('runtimes')]
        else:
            raise ValueError('Required property \'runtimes\' not present in Runtimes JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Runtimes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'runtimes') and self.runtimes is not None:
            _dict['runtimes'] = [x.to_dict() for x in self.runtimes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Runtimes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Runtimes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Runtimes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Success():
    """
    Success.

    :attr str status: (optional)
    """

    def __init__(self,
                 *,
                 status: str = None) -> None:
        """
        Initialize a Success object.

        :param str status: (optional)
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Success':
        """Initialize a Success object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Success object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Success object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Success') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Success') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Token():
    """
    Token.

    :attr str user_token: (optional)
    :attr str service_token: (optional)
    """

    def __init__(self,
                 *,
                 user_token: str = None,
                 service_token: str = None) -> None:
        """
        Initialize a Token object.

        :param str user_token: (optional)
        :param str service_token: (optional)
        """
        self.user_token = user_token
        self.service_token = service_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Token':
        """Initialize a Token object from a json dictionary."""
        args = {}
        if 'user_token' in _dict:
            args['user_token'] = _dict.get('user_token')
        if 'service_token' in _dict:
            args['service_token'] = _dict.get('service_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Token object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_token') and self.user_token is not None:
            _dict['user_token'] = self.user_token
        if hasattr(self, 'service_token') and self.service_token is not None:
            _dict['service_token'] = self.service_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Token object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Token') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Token') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
