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
A set of RESTful APIs for managing deep learning jobs

API Version: 1.0.0
"""

from enum import Enum
from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DeepLearningImpactV1(BaseService):
    """The Deep Learning Impact RESTful APIs V1 service."""

    DEFAULT_SERVICE_URL = 'https://deep_learning_impact'
    DEFAULT_SERVICE_NAME = 'deep_learning_impact_res_tful_ap_is'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DeepLearningImpactV1':
        """
        Return a new client for the Deep Learning Impact RESTful APIs service using
               the specified parameters and external configuration.
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
        Construct a new client for the Deep Learning Impact RESTful APIs service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # ModelTemplates
    #########################


    def get_model_template_details(self,
        *,
        framework: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all deep learning model templates.

        Retrieves all deep learning model templates.

        :param str framework: (optional) The deep learning framework name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[ModelTemplateDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_template_details')
        headers.update(sdk_headers)

        params = {
            'framework': framework
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/modeltemplates'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def add_model_template(self,
        name: str,
        path: str,
        framework: str,
        *,
        description: str = None,
        framework_version: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Creates a new deep learning model template.

        Creates a new deep learning model template.

        :param str name: The name of the model template.
        :param str path: The path of the model template.
        :param str framework: The deep learning framework.
        :param str description: (optional) The description.
        :param str framework_version: (optional) The framework version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if path is None:
            raise ValueError('path must be provided')
        if framework is None:
            raise ValueError('framework must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_model_template')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'path': path,
            'framework': framework,
            'description': description,
            'frameworkVersion': framework_version
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/modeltemplates'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_template_file_content_by_name(self,
        filename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves the specified model template file contents.

        Returns the contents of a specified model template file.

        :param str filename: The model template file name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if filename is None:
            raise ValueError('filename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_template_file_content_by_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['filename']
        path_param_values = self.encode_path_vars(filename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/modeltemplates/files/{filename}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_template_by_name(self,
        modeltemplatename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves model template details.

        Returns full details for the specified model template.

        :param str modeltemplatename: The deep learning model template name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ModelTemplateDetail` object
        """

        if modeltemplatename is None:
            raise ValueError('modeltemplatename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_template_by_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modeltemplatename']
        path_param_values = self.encode_path_vars(modeltemplatename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/modeltemplates/{modeltemplatename}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model_template(self,
        modeltemplatename: str,
        *,
        name: str = None,
        path: str = None,
        description: str = None,
        hyperparameter: 'HyperParameter' = None,
        framework: str = None,
        solverprototxtpath: str = None,
        traintestprototxtpath: str = None,
        inferenceprototxtpath: str = None,
        solver_content: str = None,
        train_test_content: str = None,
        inference_content: str = None,
        tfmainpath: str = None,
        tfmain_content: str = None,
        framework_version: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modifies a deep learning model template.

        Modifies a deep learning model template.

        :param str modeltemplatename: The deep learning model template name.
        :param str name: (optional) The name of the model template.
        :param str path: (optional) The path of the model template.
        :param str description: (optional) The description.
        :param HyperParameter hyperparameter: (optional)
        :param str framework: (optional) The deep learning framework name.
        :param str solverprototxtpath: (optional) The path to Caffe
               *solver.prototxt configuration file.
        :param str traintestprototxtpath: (optional) The path to Caffe
               *train_test.prototxt configuration file.
        :param str inferenceprototxtpath: (optional) The path to inference prototxt
               configuration file.
        :param str solver_content: (optional) The solverContent.
        :param str train_test_content: (optional) The trainTestContent.
        :param str inference_content: (optional) The inferenceContent.
        :param str tfmainpath: (optional) The main executor file path.
        :param str tfmain_content: (optional) The contents of the main.py.
        :param str framework_version: (optional) The framework version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modeltemplatename is None:
            raise ValueError('modeltemplatename must be provided')
        if hyperparameter is not None:
            hyperparameter = convert_model(hyperparameter)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_model_template')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'path': path,
            'description': description,
            'hyperparameter': hyperparameter,
            'framework': framework,
            'solverprototxtpath': solverprototxtpath,
            'traintestprototxtpath': traintestprototxtpath,
            'inferenceprototxtpath': inferenceprototxtpath,
            'solverContent': solver_content,
            'trainTestContent': train_test_content,
            'inferenceContent': inference_content,
            'tfmainpath': tfmainpath,
            'tfmainContent': tfmain_content,
            'frameworkVersion': framework_version
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modeltemplatename']
        path_param_values = self.encode_path_vars(modeltemplatename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/modeltemplates/{modeltemplatename}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_model_template(self,
        modeltemplatename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a model template.

        Deletes a deep learning model template.

        :param str modeltemplatename: The deep learning model template name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modeltemplatename is None:
            raise ValueError('modeltemplatename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_model_template')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modeltemplatename']
        path_param_values = self.encode_path_vars(modeltemplatename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/modeltemplates/{modeltemplatename}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_template_files(self,
        modeltemplatename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves model template files.

        Returns full list of the files related with the specified model template.

        :param str modeltemplatename: The deep learning model template name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if modeltemplatename is None:
            raise ValueError('modeltemplatename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_template_files')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modeltemplatename']
        path_param_values = self.encode_path_vars(modeltemplatename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/modeltemplates/{modeltemplatename}/files'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # HyperSearch
    #########################


    def get_all_hpo(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve all hpo tasks.

        Get all the hpo tasks that the login user can access.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[HpoTaskState]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_all_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/hypersearch'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def start_hpo(self,
        file: BinaryIO,
        data: str,
        *,
        file_content_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Start a new hpo task.

        Start a new hpo task by providing sample images as well as other required
        parameters.
        To start a hpo task, we need string format of input parameters, which is python
        dict or json format as below:
        ## data sepcification:
        ```
        {
           'hpoName': 'optional, string, name/id for the hpo task, will generate one if
        none specified here.',
           'modelSpec':
           {
               'sigName': 'required, string, same as BYOF training',
               'args': 'required, string, same as BYOF training'
           },
           'algoDef':
           {
               'algorithm': 'required, string, it can be build in algorithms like Random,
        Bayesian, Tpe, Hyperband and ExperimentGridSearch, or user installed algorithms',
               'maxRunTime': 'optional, int, max running time of the hpo task in minutes,
        default -1(unlimited)',
               'maxJobNum': 'optional, int, max number of training job to submitted for
        hpo task, default -1(unlimited)',
               'maxParalleJob': 'optinal, int, max number of training job to run in
        parallel, default 1',
               'objectiveMetric': 'required, string, name of metric will be optimized,
        same one in the val_dict_list.json',
               'objective': 'required, string, optimize policy, one of minimize,
        maximize',
               'additionalMetrics': 'optional, dict like {'metric_name': 'metric
        strategy'}, where metric stragety can be one of minimize, maximize, latest. latest
        will be used as the strategy if other names than those three is specified.',
               'algoParams': 'optional, list like [{'name':'', value:''}], additional
        algorithm parameters and it could be different for each algorithm which will be
        covered in later part'
           },
           'hyperParams':
           [
               {
                   'name': 'required, string, hyperparameter name, the same name will be
        used in the config.json so user model can load it',
                   'type': 'required, string, one of Range, Discrete',
                   'dataType': 'required, string, one of int, double, str',
                   'minDbVal': 'double, required if type=Range and datatype=double',
                   'maxDbVal': 'double, required if type=Range and datatype=double',
                   'minIntVal': 'int, required if type=Range and datatype=int',
                   'maxIntVal': 'int, required if type=Range and datatype=int',
                   'discreteDbVal': 'double, list like [0.1, 0.2], required if
        type=Discrete and dataType=double',
                   'discreteIntVal': 'int, list like [1, 2], required if type=Discrete and
        datatype=int',
                   'discreateStrVal': 'string, list like ['1', '2'], required if
        type=Discrete and datatype=str',
                   'power': 'a number value in string format, the base value for power
        calculation. ONLY valid when type is Range',
                   'step': 'a number value in string format, step size to split the Range
        space. ONLY valid when type is Range'
               }
           ],
           'experiments':
           [
               {
                  'id': 'required, int, hyperparameter experiment id',
                  'hyperParams':
                  [
                      {
                          'name': 'required, string, hyperparameter name, the same name
        will be used in the config.json so user model can load it',
                          'dataType': 'required, string, one of int, double, str',
                          'fixedVal': 'required, the same type with datatype specified, if
        dataTye=double, need fixedVal type doulbe'
                      }
                  ]
               }
            ]
        }
        ```  Each new hpo task request could only choose one from `hyperParams` and
        `experiments`, for search algorithm ExperimentGridSearch, only `experiments` is
        supported, for other algorithms, only `hyperParams` is supported:
        For Random, `algoParams` can be provided as this:
        ```
        'algoParams':
        [
            {
                'name': 'RandomSeed',
                'value': 'Optional, string, the random seed used to propose hyperparameter
        combinations.'
            }
        ]
        ``` For Hyperband, `algoParams` can be provided as this:
        ```
        'algoParams':
        [
            {
                'name': 'RandomSeed',
                'value': 'Optional, string, the random seed used by Hyperband to propose
        hyperparameter combinations in the first rung of brackets.'
            },
            {
                'name': 'eta',
                'value': 'Optional, string, the reduction factor to control the proportion
        of configurations discarded in each Hyperband brackets. Default 3.'
            },
            {
                'name': 'ResourceName',
                'value': 'Required, string, the parameter name that will be taken as
        resource in Hyperband, normally training epochs or iterations. User can get this
        parameter from config.json just like other hyper-parameters.'
            },
            {
                'name': 'ResourceValue',
                'value': 'Required, int value in string format, it is the corresponding
        upper limited value for the ResourceName.'
            }
        ]
        ``` For Tpe, `algoParams` can be provided as this:
        ```
        'algoParams':
        [
            {
                'name': 'RandomSeed',
                'value': ''Optional, string, the random seed used for the initial warm up
        hyperparameter combinations and the random generator of Gaussian Mixture Model.'
            },
            {
                'name': 'WarmUp',
                'value': 'Optional, string, the number of initial warm up hyperparameter
        combinations. It should be bigger than 2. If maxJobNum is smaller than this value,
        maxJobNum will be taken as the value. Default 20.'
            },
            {
                'name': 'EICandidate',
                'value': 'Optional, string, the number of hyperparameter combinations
        proposed each round as the candidates for Expected Improvement to propose the
        final one hyperparameter combination. It should be bigger than 1. Default 24.'
            },
            {
                'name': 'GoodRatio',
                'value': 'Optional, string, the fraction to use as good hyperparameter
        combinations from previous completed experiment training to build the good
        Gaussian Mixture Model. It should be bigger than 0. Default 0.25.'
            },
            {
                'name': 'GoodMax',
                'value': 'Optional, string, the max number of good hyperparameter
        combinations from previous completed experiment training to build the good
        Gaussian Mixture Model. It should be bigger than 1. Default 25.'
            }
        ]
        ``` For Bayesian, `algoParams` can be provided as this:
        ```
        'algoParams':
        [
            {
                'name': 'RandomSeed',
                'value': 'Optional, string, the random seed used by Bayesian. If not
        given, HPO will generate a random RandomSeed.'
            },
            {
                'name': 'InitPoints',
                'value': 'Optional, string, number of random search before approximating
        with Bayesian algorithm. Default 10.'
            },
            {
                'name': 'CubeSize',
                'value': 'Optional, string, the Bayesian candidate size. The value of
        CubeSize should not be smaller than the max maxJobNum. If maxJobNum=-1, CubeSize
        is max(10000, CubeSize), otherwise the default cubSize is maxJobNum*100. '
            },
            {
                'name': 'Noiseless',
                'value': 'Optional, string, specify whether the bayesian sampling will
        disable noise or not. If your model is entirely deterministic (e.g. analytic),
        then specify it true to speed up the optimization. If your model is not
        deterministic (as expected for most Machine Learning or Deep Learning models),
        then specify it false. Default true (noiseless).'
            }
        ]
        ```.

        :param BinaryIO file: If the model consists of one file then specify that
               file. If the model consists of a directory, then it's the tar of the
               directory with suffix ".modelDir.tar".
        :param str data: Python dict or json format, convert to string when calling
               REST.
        :param str file_content_type: (optional) The content type of file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreationResponse` object
        """

        if file is None:
            raise ValueError('file must be provided')
        if data is None:
            raise ValueError('data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_hpo')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(('file', (None, file, file_content_type or 'application/octet-stream')))
        form_data.append(('data', (None, data, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/hypersearch'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response


    def delete_all_hpo(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete all hpo tasks.

        Delete all hpo tasks.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_all_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/hypersearch'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_all_hpo_algorithm(self,
        *,
        type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve all hpo algorithm by algorithm type.

        Get all the hpo tasks that the login user can access.

        :param str type: (optional) The algorithm type, BUILD_IN or USER_PLUGIN, if
               not specified, it will query all algorithms.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[HpoAlgorithmDesc]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_all_hpo_algorithm')
        headers.update(sdk_headers)

        params = {
            'type': type
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/hypersearch/algorithm'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def install_hpo_algorithm(self,
        data: str,
        *,
        file: BinaryIO = None,
        file_content_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Install a new hpo plugin algorithm.

        Install a new hpo plugin algorithm by providing algorithm scipts as well as other
        required parameters.
        To install a new hpo plugin algorithm, we need string format of input parameters,
        which is python dict or json format as below:
        ## data sepcification:
        ```
        {
           'name': 'required, string, name/id for the plugin algorithm, should be
        unique.',
           'path': 'optional, string, the path for plugin algorithm scripts on server,
        required for local installation mode.',
           'condaHome': 'optional, string, the CONDA_HOME to run the algorithm scripts, it
        will use the DLI_CONDA_HOME if not specified.',
           'condaEnv': 'optional, string, the conda environment to run the algorithm
        scripts, it will use the DLI default conda environment if not specified.',
           'remoteExec': 'optional, boolean, whether to deploy algorithm execution
        remotely, the default value is false.',
           'logLevel': 'optional, string, the log level of the plugin algorithm, the
        default value is INFO.'
        }
        ```.

        :param str data: Python dict or json format, convert to string when calling
               REST.
        :param BinaryIO file: (optional) tar the plugin algorithm directory with
               suffix ".tar", require if the using upload installation mode.
        :param str file_content_type: (optional) The content type of file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreationResponse` object
        """

        if data is None:
            raise ValueError('data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='install_hpo_algorithm')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(('data', (None, data, 'text/plain')))
        if file:
            form_data.append(('file', (None, file, file_content_type or 'application/octet-stream')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/hypersearch/algorithm/install'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response


    def get_one_algorithm(self,
        algo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the hpo algorithm detail.

        Retrieve the hpo algorithm detail with the specified name in URL.

        :param str algo_name: The hpo algorithm name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HpoAlgorithmDesc` object
        """

        if algo_name is None:
            raise ValueError('algo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_one_algorithm')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['algoName']
        path_param_values = self.encode_path_vars(algo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/algorithm/{algoName}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_one_hpoalgorithm(self,
        algo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a hpo plugin algorithm.

        Delete a hpo plugin algorithm.

        :param str algo_name: The hpo plugin algorithm name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if algo_name is None:
            raise ValueError('algo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_one_hpoalgorithm')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['algoName']
        path_param_values = self.encode_path_vars(algo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/algorithm/{algoName}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_one_hpo(self,
        hpo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the hpo task detail.

        Retrieve the hpo task detail with the specified hpo task name in URL.

        :param str hpo_name: The hpo task name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HpoTaskState` object
        """

        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_one_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['hpoName']
        path_param_values = self.encode_path_vars(hpo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/{hpoName}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_one_hpo(self,
        hpo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a hpo task.

        Stops a running hpo task.

        :param str hpo_name: The HPO task name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_one_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['hpoName']
        path_param_values = self.encode_path_vars(hpo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/{hpoName}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_one_hpo(self,
        hpo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a hpo task.

        Delete a hpo task.

        :param str hpo_name: The hpo task name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_one_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['hpoName']
        path_param_values = self.encode_path_vars(hpo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/{hpoName}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_one_hpo_force(self,
        hpo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop a hpo task forcely.

        Stop a running hpo task forcely.

        :param str hpo_name: The hpo task name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_one_hpo_force')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['hpoName']
        path_param_values = self.encode_path_vars(hpo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/{hpoName}/force'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def restart_one_hpo(self,
        hpo_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Restart a hpo task forcely.

        Restart a stopped or recoverfailed hpo task.

        :param str hpo_name: The hpo task name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='restart_one_hpo')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['hpoName']
        path_param_values = self.encode_path_vars(hpo_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/hypersearch/{hpoName}/restart'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Configuration
    #########################


    def get_deep_learning_conf(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all dlpd configuration parameters.

        Returns all properties that are defined in
        $EGO_CONFDIR/../../dli/conf/dlpd/dlpd.conf.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StringMap` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_deep_learning_conf')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/conf'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Execute
    #########################


    def list_execs(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all tasks started through Execute.

        Retrieves all tasks started through Execute.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[Batch]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_execs')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/execs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_exec(self,
        sig_name: str,
        args: str,
        file: BinaryIO,
        **kwargs
    ) -> DetailedResponse:
        """
        Starts a task through Execute.

        Starts a task through Execute.

        :param str sig_name: The Spark instance group in which to start the task.
        :param str args: Arguments to the task. These arguments can be found in the
               command line interface. They can be model specific arguments. Examples are
               "--exec-start tensorflow --model-main TF_mnist.py", "--exec-start PyTorch
               --model-main PyTorch_mnist.py --batch-size 200".
        :param BinaryIO file: If the model consists of one file then specify that
               file. If the model consists of a directory, then it's the tar of the
               directory with suffix ".modelDir.tar".
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if sig_name is None:
            raise ValueError('sig_name must be provided')
        if args is None:
            raise ValueError('args must be provided')
        if file is None:
            raise ValueError('file must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_exec')
        headers.update(sdk_headers)

        params = {
            'sigName': sig_name,
            'args': args
        }

        form_data = []
        form_data.append(('file', (None, file, )))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/execs'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response


    def delete_exec(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes all tasks started by the current users.

        Delete all tasks.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_exec')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/execs'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_platform_rest_deeplearning_execs_frameworks(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all deep learning framework plugins.

        Retrieves all deep learning framework plugins.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DLFramework]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_platform_rest_deeplearning_execs_frameworks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/execs/frameworks'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_exec(self,
        exec_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves a task started through Execute.

        Retrieves a task started through Execute. The returned values 'sigId',
        'submissionId' can be used to make other Conductor REST calls to get additional
        task details.

        :param str exec_id: ID of task.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Batch` object
        """

        if exec_id is None:
            raise ValueError('exec_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_exec')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['execId']
        path_param_values = self.encode_path_vars(exec_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/execs/{execId}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_platform_rest_deeplearning_exec_log(self,
        exec_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve logs of the training task by execution ID.

        Retrieve logs of the training task by execution ID.

        :param str exec_id: Execution ID of the training task.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if exec_id is None:
            raise ValueError('exec_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_platform_rest_deeplearning_exec_log')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['execId']
        path_param_values = self.encode_path_vars(exec_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/execs/{execId}/log'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_platform_rest_deeplearning_exec_result(self,
        exec_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the result of the training task using an execution ID.

        Retrieve the result of the training task using an execution ID.

        :param str exec_id: Execution ID of the training task.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if exec_id is None:
            raise ValueError('exec_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_platform_rest_deeplearning_exec_result')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['execId']
        path_param_values = self.encode_path_vars(exec_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/execs/{execId}/result'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def post_platform_rest_deeplearning_exec_stop(self,
        exec_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop the training task by execution ID.

        Stop the training task by execution ID.

        :param str exec_id: Execution ID of the training task.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if exec_id is None:
            raise ValueError('exec_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_platform_rest_deeplearning_exec_stop')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['execId']
        path_param_values = self.encode_path_vars(exec_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/execs/{execId}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # ModelValidations
    #########################


    def get_validations(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all model validations.

        Returns full listing of all the validations for a deep learning model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[ValidateDetail]` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_validations')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/validations'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def start_validation(self,
        modelname: str,
        val_name: str,
        train_name: str,
        metrics: List[str],
        *,
        threshold: float = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Starts a new model validation.

        Starts a new validation for a deep learning model.

        :param str modelname: The deep learning model name.
        :param str val_name: The deep learning validation name.
        :param str train_name: Name of the training to validate.
        :param List[str] metrics: The list of metrics, for example, "Top1",
               "ConfusionMatrix", "IoU", "mAP".
        :param float threshold: (optional) The threshold value, for example, 0.1.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if val_name is None:
            raise ValueError('val_name must be provided')
        if train_name is None:
            raise ValueError('train_name must be provided')
        if metrics is None:
            raise ValueError('metrics must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_validation')
        headers.update(sdk_headers)

        data = {
            'valName': val_name,
            'trainName': train_name,
            'metrics': metrics,
            'threshold': threshold
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/validations'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_validation(self,
        modelname: str,
        valname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a validation for a model.

        Deletes a validation for a deep learning model.

        :param str modelname: The deep learning model name to delete.
        :param str valname: The deep learning validation name to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if valname is None:
            raise ValueError('valname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_validation')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'valname']
        path_param_values = self.encode_path_vars(modelname, valname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/validations/{valname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_validation(self,
        modelname: str,
        valname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a model validation task.

        Stops a running deep learning model validation task.

        :param str modelname: The deep learning model name.
        :param str valname: The deep learning validation name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if valname is None:
            raise ValueError('valname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_validation')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'valname']
        path_param_values = self.encode_path_vars(modelname, valname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/validations/{valname}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Scheduler
    #########################


    def get_applications(self,
        *,
        applicationid: str = None,
        applicationname: str = None,
        driverid: str = None,
        search: str = None,
        sort: str = None,
        order: str = None,
        start: str = None,
        length: str = None,
        state: str = None,
        sig_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves deep learning Spark applications.

        Retrieves deep learning Spark applications.

        :param str applicationid: (optional) The ID of the Spark application.
        :param str applicationname: (optional) The name of the Spark application.
        :param str driverid: (optional) The ID of the Spark application driver.
        :param str search: (optional) search.
        :param str sort: (optional) The field name to sort the response by. Only
               one field name can be specified as the sort type. Prefix the field name
               with "-" to sort in descending order.
        :param str order: (optional) order.
        :param str start: (optional) start.
        :param str length: (optional) length.
        :param str state: (optional) state.
        :param str sig_id: (optional) The ID of the Spark instance group.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[SparkApplicationDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_applications')
        headers.update(sdk_headers)

        params = {
            'applicationid': applicationid,
            'applicationname': applicationname,
            'driverid': driverid,
            'search': search,
            'sort': sort,
            'order': order,
            'start': start,
            'length': length,
            'state': state,
            'sigId': sig_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/scheduler/applications'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_app_instances(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all Spark application instances.

        Retrieves all the Spark application instances.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[SigAppInstanceDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_app_instances')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/scheduler/instances'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Inferences
    #########################


    def get_all_predicts_by_model_name(self,
        modelname: str,
        flag: bool,
        **kwargs
    ) -> DetailedResponse:
        """
        Get all inference instances for a model.

        Get all inference instances for a model.

        :param str modelname: The deep learning model name.
        :param bool flag: Save results to a file?  Currently, saving results is NOT
               supported, and the flag must be set to "false".
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[InferenceDetail]` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if flag is None:
            raise ValueError('flag must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_all_predicts_by_model_name')
        headers.update(sdk_headers)

        params = {
            'modelname': modelname,
            'flag': flag
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/inferences'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_model_train_inference(self,
        model_name: str,
        train_name: str,
        *,
        inference_model_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new inference from the model training.

        Create a new inference from the model training.

        :param str model_name: The name of the model.
        :param str train_name: The name of the model training.
        :param str inference_model_name: (optional) The name of the new inference
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if model_name is None:
            raise ValueError('model_name must be provided')
        if train_name is None:
            raise ValueError('train_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_model_train_inference')
        headers.update(sdk_headers)

        data = {
            'modelName': model_name,
            'trainName': train_name,
            'inferenceModelName': inference_model_name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/inferences'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def start_predict(self,
        image0: BinaryIO,
        image1: BinaryIO,
        modelname: str,
        threshold: str,
        predictname: str,
        *,
        image0_content_type: str = None,
        image1_content_type: str = None,
        master_url: str = None,
        sigid: str = None,
        signame: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Start predicting an inference model.

        Start predicting an inference model by providing sample images as well as other
        required parameters.
        # NOTE You can provide arbitrary number of image files as an input to start a
        prediction.  Here, we only require two files, as an example.

        :param BinaryIO image0: First image file for testing the prediction.
        :param BinaryIO image1: Second image file for testing the prediction.
        :param str modelname: The model name.
        :param str threshold: The probability threshold for the classification.
        :param str predictname: The prediction name. Must be unique.
        :param str image0_content_type: (optional) The content type of image0.
        :param str image1_content_type: (optional) The content type of image1.
        :param str master_url: (optional) The Spark instance group master URL.
        :param str sigid: (optional) The Spark instance group ID.
        :param str signame: (optional) The Spark instance group name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if image0 is None:
            raise ValueError('image0 must be provided')
        if image1 is None:
            raise ValueError('image1 must be provided')
        if modelname is None:
            raise ValueError('modelname must be provided')
        if threshold is None:
            raise ValueError('threshold must be provided')
        if predictname is None:
            raise ValueError('predictname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_predict')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(('image0', (None, image0, image0_content_type or 'application/octet-stream')))
        form_data.append(('image1', (None, image1, image1_content_type or 'application/octet-stream')))
        form_data.append(('modelname', (None, modelname, 'text/plain')))
        form_data.append(('threshold', (None, threshold, 'text/plain')))
        form_data.append(('predictname', (None, predictname, 'text/plain')))
        if master_url:
            form_data.append(('masterUrl', (None, master_url, 'text/plain')))
        if sigid:
            form_data.append(('sigid', (None, sigid, 'text/plain')))
        if signame:
            form_data.append(('signame', (None, signame, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/inferences/startpredict'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response


    def get_predict_by_predict_name(self,
        predict_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the inference instance details.

        Retrieves the details for one model inference instance.

        :param str predict_name: The prediction name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InferenceDetail` object
        """

        if predict_name is None:
            raise ValueError('predict_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_predict_by_predict_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['predictName']
        path_param_values = self.encode_path_vars(predict_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/inferences/{predictName}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_predict(self,
        predict_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a prediction.

        Deletes a prediction.

        :param str predict_name: The prediction name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if predict_name is None:
            raise ValueError('predict_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_predict')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['predictName']
        path_param_values = self.encode_path_vars(predict_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/inferences/{predictName}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_predict_results(self,
        predict_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the prediction results for an inference.

        Retrieves full prediction results for one inference instance.

        :param str predict_name: The prediction name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PredictResult` object
        """

        if predict_name is None:
            raise ValueError('predict_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_predict_results')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['predictName']
        path_param_values = self.encode_path_vars(predict_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/inferences/{predictName}/predicts'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_inference(self,
        predict_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a prediction.

        Stops a running prediction task.

        :param str predict_name: The prediction name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if predict_name is None:
            raise ValueError('predict_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_inference')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['predictName']
        path_param_values = self.encode_path_vars(predict_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/inferences/{predictName}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # ModelTunings
    #########################


    def get_model_auto_tuning_status(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve all tunings for a model.

        Returns full listing of all tunings for a deep learning model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[HpoTaskDetail]` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_auto_tuning_status')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def start_model_auto_tuning(self,
        modelname: str,
        model_name: str,
        hpo_name: str,
        res_def: 'ResDef',
        algo_def: 'AlgoDef',
        *,
        hyper_params: List['HpoHyperParameter'] = None,
        experiments: List['SearchExperiment'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Creates new model tuning.

        Crates a new deep learning model tuning.

        :param str modelname: The deep learning model name.
        :param str model_name: The deep learning model name.
        :param str hpo_name: The deep learning tuning name.
        :param ResDef res_def: The deep learning tuning resource definition.
        :param AlgoDef algo_def: algorithm definition.
        :param List[HpoHyperParameter] hyper_params: (optional) The deep learning
               tuning hyperparameters.
        :param List[SearchExperiment] experiments: (optional) Only valid for
               ExperimentGridSearch algorithm which will submit train with this list of
               experiments.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if model_name is None:
            raise ValueError('model_name must be provided')
        if hpo_name is None:
            raise ValueError('hpo_name must be provided')
        if res_def is None:
            raise ValueError('res_def must be provided')
        if algo_def is None:
            raise ValueError('algo_def must be provided')
        res_def = convert_model(res_def)
        algo_def = convert_model(algo_def)
        if hyper_params is not None:
            hyper_params = [convert_model(x) for x in hyper_params]
        if experiments is not None:
            experiments = [convert_model(x) for x in experiments]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_model_auto_tuning')
        headers.update(sdk_headers)

        data = {
            'modelName': model_name,
            'hpoName': hpo_name,
            'resDef': res_def,
            'algoDef': algo_def,
            'hyperParams': hyper_params,
            'experiments': experiments
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_auto_tuning_status_by_name(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves tuning details.

        Returns full details for a deep learning model tuning.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HpoTaskDetail` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_auto_tuning_status_by_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_model_auto_tuning(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a model tuning.

        Deletes a model tuning.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_model_auto_tuning')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_model_using_tuning_result(self,
        modelname: str,
        tuningname: str,
        newmodelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new model using the tuning result.

        Create a new model using the tuning result.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param str newmodelname: The deep learning new created model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        if newmodelname is None:
            raise ValueError('newmodelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_model_using_tuning_result')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname', 'newmodelname']
        path_param_values = self.encode_path_vars(modelname, tuningname, newmodelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}/create/{newmodelname}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_model_auto_tuning_force(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop a model tuning forcely.

        Stops a running deep learning model tuning task forcely.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_model_auto_tuning_force')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}/force'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def restart_model_auto_tuning(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Restart a model tuning.

        Restart a stopped or recoverfailed deep learning model tuning task.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='restart_model_auto_tuning')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}/restart'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_model_auto_tuning(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a model tuning task.

        Stops a running deep learning model tuning task.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_model_auto_tuning')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model_using_tuning_result(self,
        modelname: str,
        tuningname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the model using the tuning result.

        Update the model using the tuning result.

        :param str modelname: The deep learning model name.
        :param str tuningname: The deep learning tuning name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if tuningname is None:
            raise ValueError('tuningname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_model_using_tuning_result')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'tuningname']
        path_param_values = self.encode_path_vars(modelname, tuningname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/hypersearch/{tuningname}/update'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Datasets
    #########################


    def get_full_dataset_details(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all deep learning datasets.

        Returns full listing of all the datasets defined in the system.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DatasetDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_full_dataset_details')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/datasets'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def add_dataset(self,
        name: str,
        dbbackend: str,
        sigid: str,
        datasourcetype: str,
        *,
        trainpath: str = None,
        valpath: str = None,
        testpath: str = None,
        meanfilepath: str = None,
        imagedetail: 'ImageDetail' = None,
        shards: int = None,
        byclass: bool = None,
        plugin: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Creates a new deep learning dataset.

        A dataset can be created in the following ways - 1) Import the existing LMDB,
        TFRecords, or Other dataset; 2) Create a LMDB or TFRecords dataset from existing
        image files for image classification; 3) Import images for object detection; 4)
        Import a CVS dataset; 5) Import images for vector output; 6) Import plugin dataset
        including customized plugins and the ready-made NLP plugin; 7) Raw data.

        :param str name: The dataset name.
        :param str dbbackend: The backend database (e.g. LMDB, TFrecords, CSV,
               ImageVector, ObjectDetection, Other).
        :param str sigid: The Spark instance group ID.
        :param str datasourcetype: Type of source data for creating a new dataset.
        :param str trainpath: (optional) The dataset training folder path.
        :param str valpath: (optional) The dataset validation folder path.
        :param str testpath: (optional) The dataset test folder path.
        :param str meanfilepath: (optional) The dataset mean file path.
        :param ImageDetail imagedetail: (optional)
        :param int shards: (optional) The number of shards of the dataset. This
               parameter is only used when dbbackend is TFrecords.
        :param bool byclass: (optional) Whether to generate records by class. This
               parameter is only used when dbbackend is TFrecords.
        :param str plugin: (optional) the csv plugin file path. This parameter is
               only used when dbbackend is CSV.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if dbbackend is None:
            raise ValueError('dbbackend must be provided')
        if sigid is None:
            raise ValueError('sigid must be provided')
        if datasourcetype is None:
            raise ValueError('datasourcetype must be provided')
        if imagedetail is not None:
            imagedetail = convert_model(imagedetail)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_dataset')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'dbbackend': dbbackend,
            'sigid': sigid,
            'datasourcetype': datasourcetype,
            'trainpath': trainpath,
            'valpath': valpath,
            'testpath': testpath,
            'meanfilepath': meanfilepath,
            'imagedetail': imagedetail,
            'shards': shards,
            'byclass': byclass,
            'plugin': plugin
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/datasets'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_dataset_info(self,
        datasetname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves a deep learning dataset by its name.

        Retrieves a deep learning dataset by its name.

        :param str datasetname: The deep learning dataset name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DatasetDetail` object
        """

        if datasetname is None:
            raise ValueError('datasetname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_dataset_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['datasetname']
        path_param_values = self.encode_path_vars(datasetname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/datasets/{datasetname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_dataset_info(self,
        datasetname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a deep learning dataset.

        Deletes a deep learning dataset.

        :param str datasetname: The deep learning dataset name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if datasetname is None:
            raise ValueError('datasetname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_dataset_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['datasetname']
        path_param_values = self.encode_path_vars(datasetname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/datasets/{datasetname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def csv_list(self,
        datasetname: str,
        type: str,
        *,
        start: str = None,
        length: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve required dataset CSV data.

        Retrieve required dataset CSV data.

        :param str datasetname: The dataset name.
        :param str type: The type of CSV data to review, for example - validation,
               test or training.
        :param str start: (optional) You can request a specific range of results by
               specifying the start index of the data and the length of the data.
        :param str length: (optional) You can request a specific range of results
               by specifying the start index of the data and the length of the data.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CsvDetail` object
        """

        if datasetname is None:
            raise ValueError('datasetname must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='csv_list')
        headers.update(sdk_headers)

        params = {
            'type': type,
            'start': start,
            'length': length
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['datasetname']
        path_param_values = self.encode_path_vars(datasetname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/datasets/{datasetname}/csvs'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def objectimage_list(self,
        datasetname: str,
        type: str,
        *,
        start: str = None,
        length: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves required object images.

        Retrieves required object images.

        :param str datasetname: The dataset name.
        :param str type: The type of image data to review, for example -
               validation, test or training.
        :param str start: (optional) You can request a specific range of results by
               specifying the start index of the data and the length of the data.
        :param str length: (optional) You can request a specific range of results
               by specifying the start index of the data and the length of the data.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[Pictures]` result
        """

        if datasetname is None:
            raise ValueError('datasetname must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='objectimage_list')
        headers.update(sdk_headers)

        params = {
            'type': type,
            'start': start,
            'length': length
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['datasetname']
        path_param_values = self.encode_path_vars(datasetname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/datasets/{datasetname}/objectimages'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def stop_data_set(self,
        datasetname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a dataset task.

        Stops a running dataset task.

        :param str datasetname: The dataset name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if datasetname is None:
            raise ValueError('datasetname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_data_set')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['datasetname']
        path_param_values = self.encode_path_vars(datasetname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/datasets/{datasetname}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # ElasticDistributedInference
    #########################


    def get_edi_models(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all elastic distributed inference services defined in the system.

        Returns full listing of all the elastic distributed inference services defined in
        the system.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[IaSModelDescription]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_models')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/edimodels'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def new_edi_model(self,
        edi_py: str,
        name: str,
        model_path: str,
        weight_path: str,
        runtime: str,
        *,
        attribute: str = None,
        mcenv: str = None,
        type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new elastic distributed inference service.

        Create a new elastic distributed inference service.

        :param str edi_py: The execution kernel for inference model.
        :param str name: The name inference model.
        :param str model_path: The model file path for inference model.
        :param str weight_path: The weight file path for inference model.
        :param str runtime: The runtime for inference model.
        :param str attribute: (optional) Key-value of attributes can be accessed in
               model kernel.
        :param str mcenv: (optional) Additional environment variables to run model
               kernel.
        :param str type: (optional) The type for inference model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if edi_py is None:
            raise ValueError('edi_py must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if model_path is None:
            raise ValueError('model_path must be provided')
        if weight_path is None:
            raise ValueError('weight_path must be provided')
        if runtime is None:
            raise ValueError('runtime must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='new_edi_model')
        headers.update(sdk_headers)

        data = {
            'edi_py': edi_py,
            'name': name,
            'modelPath': model_path,
            'weightPath': weight_path,
            'runtime': runtime,
            'attribute': attribute,
            'mcenv': mcenv,
            'type': type
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/edimodels/new'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_edi_model(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves detail for a elastic distributed inference service.

        Returns full details for a elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IaSModelDescription` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def publish_edi_model(self,
        modelname: str,
        edi_py: str,
        name: str,
        model_path: str,
        weight_path: str,
        runtime: str,
        *,
        attribute: str = None,
        mcenv: str = None,
        type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Publish a new elastic distributed inference service from the DLI inference model.

        Publish a new elastic distributed inference service from the DLI inference model.

        :param str modelname: The name of deep learning model, which will be
               published to Elastic Distributed Inference service.
        :param str edi_py: The execution kernel for inference model.
        :param str name: The name inference model.
        :param str model_path: The model file path for inference model.
        :param str weight_path: The weight file path for inference model.
        :param str runtime: The runtime for inference model.
        :param str attribute: (optional) Key-value of attributes can be accessed in
               model kernel.
        :param str mcenv: (optional) Additional environment variables to run model
               kernel.
        :param str type: (optional) The type for inference model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if edi_py is None:
            raise ValueError('edi_py must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if model_path is None:
            raise ValueError('model_path must be provided')
        if weight_path is None:
            raise ValueError('weight_path must be provided')
        if runtime is None:
            raise ValueError('runtime must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='publish_edi_model')
        headers.update(sdk_headers)

        data = {
            'edi_py': edi_py,
            'name': name,
            'modelPath': model_path,
            'weightPath': weight_path,
            'runtime': runtime,
            'attribute': attribute,
            'mcenv': mcenv,
            'type': type
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def update_edi_model(self,
        modelname: str,
        name: str,
        *,
        schema_version: str = None,
        tag: str = None,
        weight_path: str = None,
        model_path: str = None,
        creator: str = None,
        runtime: str = None,
        kernel_path: str = None,
        mk_resource_req: str = None,
        mk_umask: str = None,
        attributes: List['Attr'] = None,
        mk_environments: List['Envs'] = None,
        service_uri: str = None,
        size: int = None,
        mk_instance_min: int = None,
        mk_instance_max: int = None,
        create_time: str = None,
        last_update_time: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update elastic distributed inference service.

        Update elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param str name: The name of the Elastic Distributed Inference model.
        :param str schema_version: (optional) The version of Elastic Distributed
               Inference model.
        :param str tag: (optional) The tag of the Elastic Distributed Inference
               model.
        :param str weight_path: (optional) The model weight which used for
               inference.
        :param str model_path: (optional) The inference model path.
        :param str creator: (optional) The creator of the Elastic Distributed
               Inference model.
        :param str runtime: (optional) The runtime of Elastic Distributed Inference
               model.
        :param str kernel_path: (optional) The execution kernel for inference
               model.
        :param str mk_resource_req: (optional) The kernel resource request of the
               Elastic Distributed Inference model.
        :param str mk_umask: (optional) The kernel umask of Elastic Distributed
               Inference model.
        :param List[Attr] attributes: (optional) Key-value of attributes can be
               accessed in model kernel.
        :param List[Envs] mk_environments: (optional) Additional environment
               variables to run model kernel.
        :param str service_uri: (optional) Rest Service URL.
        :param int size: (optional) The size of the Elastic Distributed Inference
               model.
        :param int mk_instance_min: (optional) The minimal number of instance.
        :param int mk_instance_max: (optional) The maximal number of instance.
        :param str create_time: (optional) The create time of the Elastic
               Distributed Inference model.
        :param str last_update_time: (optional) The last update time of the Elastic
               Distributed Inference model.
        :param str state: (optional) The state of Elastic Distributed Inference
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if attributes is not None:
            attributes = [convert_model(x) for x in attributes]
        if mk_environments is not None:
            mk_environments = [convert_model(x) for x in mk_environments]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_edi_model')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'schema_version': schema_version,
            'tag': tag,
            'weight_path': weight_path,
            'model_path': model_path,
            'creator': creator,
            'runtime': runtime,
            'kernel_path': kernel_path,
            'mk_resource_req': mk_resource_req,
            'mk_umask': mk_umask,
            'attributes': attributes,
            'mk_environments': mk_environments,
            'service_uri': service_uri,
            'size': size,
            'mk_instance_min': mk_instance_min,
            'mk_instance_max': mk_instance_max,
            'create_time': create_time,
            'last_update_time': last_update_time,
            'state': state
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_edi_model(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes an elastic distributed inference service.

        Deletes an elastic distributed inference service.

        :param str modelname: The elastic distributed inference model service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_edi_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_edi_model_porfile(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves detail for app profile of an elastic distributed inference service.

        Returns full details for app profile of an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IaSProfileParam` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_model_porfile')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/appprofile'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_edi_model_porfile(self,
        modelname: str,
        name: str,
        *,
        create_time: str = None,
        update_time: str = None,
        replica: int = None,
        type: str = None,
        schema_version: str = None,
        policy: 'Policy' = None,
        kernel: 'Kernel' = None,
        resource_allocation: 'ResourceAllocation' = None,
        envs: List['Envs'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update app profile of an elastic distributed inference service.

        Update app profile of an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param str name: The name for Elastic Distributed Inference model.
        :param str create_time: (optional) The create time for Elastic Distributed
               Inference model.
        :param str update_time: (optional) The update time for Elastic Distributed
               Inference model.
        :param int replica: (optional) The replication number for inference model
               instance.
        :param str type: (optional) The type for Elastic Distributed Inference
               model.
        :param str schema_version: (optional) The schema version for Elastic
               Distributed Inference model.
        :param Policy policy: (optional)
        :param Kernel kernel: (optional)
        :param ResourceAllocation resource_allocation: (optional)
        :param List[Envs] envs: (optional) Additional environment variables to run
               model kernel.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if policy is not None:
            policy = convert_model(policy)
        if kernel is not None:
            kernel = convert_model(kernel)
        if resource_allocation is not None:
            resource_allocation = convert_model(resource_allocation)
        if envs is not None:
            envs = [convert_model(x) for x in envs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_edi_model_porfile')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'create_time': create_time,
            'update_time': update_time,
            'replica': replica,
            'type': type,
            'schema_version': schema_version,
            'policy': policy,
            'kernel': kernel,
            'resource_allocation': resource_allocation,
            'envs': envs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/appprofile'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def do_edi_inference(self,
        modelname: str,
        action_type: str,
        data_type: str,
        data_value: List['Attr'],
        *,
        user: str = None,
        attributes: List['Attr'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Do inference using an elastic distributed inference service.

        Do inference using an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param str action_type: The action type for the inference, including
               Classification, Object Detection.
        :param str data_type: The data type for the inference, including
               image:raw_data, image:jpeg_uri.
        :param List[Attr] data_value: Key-value for inference data.
        :param str user: (optional) The usr who run the inference.
        :param List[Attr] attributes: (optional) The attributes for inference, for
               example threshold.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IaSTestResultParam` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if action_type is None:
            raise ValueError('action_type must be provided')
        if data_type is None:
            raise ValueError('data_type must be provided')
        if data_value is None:
            raise ValueError('data_value must be provided')
        data_value = [convert_model(x) for x in data_value]
        if attributes is not None:
            attributes = [convert_model(x) for x in attributes]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='do_edi_inference')
        headers.update(sdk_headers)

        data = {
            'action_type': action_type,
            'data_type': data_type,
            'data_value': data_value,
            'user': user,
            'attributes': attributes
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/inference'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_edi_model_instance(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves detail for instance of an elastic distributed inference service.

        Returns full details for instance of an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IaSInstanceParam` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_model_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/instance'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def start_edi_model(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Start an elastic distributed inference service.

        Start an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_edi_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/operation/start'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_edi_model(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop an elastic distributed inference service.

        Stop an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_edi_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/operation/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_edi_model_readme(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves readme of an elastic distributed inference service.

        Returns readme of an elastic distributed inference service.

        :param str modelname: The elastic distributed inference service name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IaSReadmeParam` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_model_readme')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/readme'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_edi_model_streaming(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves streaming uri for the elastic distributed inference service.

        Retrieves streaming uri for the elastic distributed inference service.

        :param str modelname: The elastic distributed inference services name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_edi_model_streaming')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/edimodels/{modelname}/streaming'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # ModelTrainings
    #########################


    def get_model_training_names(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get training names of all trainings for a specified model.

        Get training names of all trainings for a specified model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_training_names')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainingnames'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_trainings(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get status of all trainings for a specified model.

        Get status of all trainings for a specified model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[TrainDetail]` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_trainings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def start_model_training(self,
        modelname: str,
        train_name: str,
        dl_framework: str,
        cluster_size: int,
        *,
        cmd: str = None,
        wt_url: str = None,
        wfinit: str = None,
        wtfolder: str = None,
        gpu_ratio: int = None,
        test_interval: int = None,
        test_iteration: int = None,
        sync_mode: str = None,
        distribute: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Start a new model training task.

        Start a new model training task.

        :param str modelname: The deep learning model name.
        :param str train_name: The deep learning training name.
        :param str dl_framework: The deep learning framework name.
        :param int cluster_size: The number of workers in the cluster.
        :param str cmd: (optional) The training command.
        :param str wt_url: (optional) The training weight file URL.
        :param str wfinit: (optional) The initial weight file for training.
        :param str wtfolder: (optional) The training weight file folder name.
        :param int gpu_ratio: (optional) The gpu ratio.
        :param int test_interval: (optional) Number of training runs that are run
               in a test interval. At each test interval the model is run against the test
               dataset to verify that the accuracy is sufficient. By default, the interval
               is set to 100.
        :param int test_iteration: (optional) Number of times that the model runs
               against the test dataset in each interval. By default, the iteration is set
               to 10.  For example, if the test interval is set to 100 and the iteration
               is set to 10, on the hundredth training run, the model will run against the
               test dataset 10 times.
        :param str sync_mode: (optional) The gradient synchronization mode in
               elastic distributed training. This parameter to specify whether the
               training is a synchronous training, or an asynchronous training.
        :param bool distribute: (optional) Denotes whether it is distributed or
               not.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if train_name is None:
            raise ValueError('train_name must be provided')
        if dl_framework is None:
            raise ValueError('dl_framework must be provided')
        if cluster_size is None:
            raise ValueError('cluster_size must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='start_model_training')
        headers.update(sdk_headers)

        data = {
            'trainName': train_name,
            'dlFramework': dl_framework,
            'clusterSize': cluster_size,
            'cmd': cmd,
            'wtURL': wt_url,
            'wfinit': wfinit,
            'wtfolder': wtfolder,
            'gpuRatio': gpu_ratio,
            'testInterval': test_interval,
            'testIteration': test_iteration,
            'syncMode': sync_mode,
            'distribute': distribute
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_trainingby_name(self,
        modelname: str,
        trainingname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get status of the specified training for a specified model.

        Get status of the specified training for a specified model.

        :param str modelname: The deep learning model name.
        :param str trainingname: The deep learning training name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainDetail` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if trainingname is None:
            raise ValueError('trainingname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_trainingby_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname', 'trainingname']
        path_param_values = self.encode_path_vars(modelname, trainingname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings/{trainingname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def del_model_training(self,
        modelname: str,
        trainingname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a model training.

        Deletes a single deep learning model training.

        :param str modelname: The deep learning model name.
        :param str trainingname: The deep learning training name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if trainingname is None:
            raise ValueError('trainingname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='del_model_training')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'trainingname']
        path_param_values = self.encode_path_vars(modelname, trainingname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings/{trainingname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def stop_model_training(self,
        modelname: str,
        trainingname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops a model training task.

        Stops a running deep learning model training task.

        :param str modelname: The deep learning model name.
        :param str trainingname: The deep learning training name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if trainingname is None:
            raise ValueError('trainingname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='stop_model_training')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname', 'trainingname']
        path_param_values = self.encode_path_vars(modelname, trainingname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings/{trainingname}/stop'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_training_weightfiles(self,
        modelname: str,
        trainingname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get weight files for a model training.

        Retrieves weight files for a deep learning model training.

        :param str modelname: The deep learning model name.
        :param str trainingname: The deep learning training name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if trainingname is None:
            raise ValueError('trainingname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_training_weightfiles')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname', 'trainingname']
        path_param_values = self.encode_path_vars(modelname, trainingname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/trainings/{trainingname}/weightfile'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Frameworks
    #########################


    def get_deep_learning_frameworks(self,
        *,
        backend: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves details for all defined frameworks.

        Returns the configuration information for all deep learning framework or a
        specified deep learning framework.

        :param str backend: (optional) Filter deep learning frameworks by the
               backend framework name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[FrameworkDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_deep_learning_frameworks')
        headers.update(sdk_headers)

        params = {
            'backend': backend
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/frameworks'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_all_deep_learning_frameworks(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves training engine name for all defined frameworks.

        Returns training engine name for all deep learning framework.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_all_deep_learning_frameworks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/frameworks/all'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Models
    #########################


    def get_models(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves all models defined in the system.

        Returns full listing of all the deep learning models defined in the system.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[ModelDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_models')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/platform/rest/deeplearning/v1/models'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def add_model(self,
        name: str,
        templatename: str,
        *,
        description: str = None,
        sig: str = None,
        accelerator: str = None,
        hyperparameter: 'HyperParameter' = None,
        dataset: str = None,
        batchsize: int = None,
        tfmain_content: str = None,
        type: str = None,
        wtfolder: str = None,
        framework_version: str = None,
        distribute_strategy: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Creates a new deep learning model.

        Creates a new deep learning model.

        :param str name: The name of the deep learning model.
        :param str templatename: The deep learning model template name.
        :param str description: (optional) The description of the deep learning
               model.
        :param str sig: (optional) The Spark instance group id. This parameter is
               required when create an inference model.
        :param str accelerator: (optional) The deep learning model training engine.
        :param HyperParameter hyperparameter: (optional)
        :param str dataset: (optional) The name of the the dataset associated with
               the deep learning model. This parameter is required when create a training
               model.
        :param int batchsize: (optional) The batch size.
        :param str tfmain_content: (optional) The contents of the main.py file.
        :param str type: (optional) The type of the model, indicates whether it is
               inference model or normal model.
        :param str wtfolder: (optional) The folder that contains the weight file.
        :param str framework_version: (optional) The framework version.
        :param str distribute_strategy: (optional) The distribution strategy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if templatename is None:
            raise ValueError('templatename must be provided')
        if hyperparameter is not None:
            hyperparameter = convert_model(hyperparameter)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_model')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'templatename': templatename,
            'description': description,
            'sig': sig,
            'accelerator': accelerator,
            'hyperparameter': hyperparameter,
            'dataset': dataset,
            'batchsize': batchsize,
            'tfmainContent': tfmain_content,
            'type': type,
            'wtfolder': wtfolder,
            'frameworkVersion': framework_version,
            'distributeStrategy': distribute_strategy
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/models'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_model_file_content_by_name(self,
        filename: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves the specified model file contents.

        Returns the contents of a specified model file.

        :param str filename: The model file name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if filename is None:
            raise ValueError('filename must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_file_content_by_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['filename']
        path_param_values = self.encode_path_vars(filename)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/files/{filename}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def upload_wf(self,
        file: BinaryIO,
        *,
        file_content_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Uploads a new weight file.

        Upload a new weight file which can be used for trainings and inferences.

        :param BinaryIO file: Weight file for model training or inference.
        :param str file_content_type: (optional) The content type of file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='upload_wf')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(('file', (None, file, file_content_type or 'application/octet-stream')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/platform/rest/deeplearning/v1/models/weightfile'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response


    def get_model_by_name(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves details for a model.

        Returns full details for a deep learning model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ModelDetail` object
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_by_name')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_model(self,
        modelname: str,
        *,
        name: str = None,
        path: str = None,
        description: str = None,
        templatename: str = None,
        framework: str = None,
        accelerator: str = None,
        hyperparameter: 'HyperParameter' = None,
        dataset: str = None,
        batchsize: int = None,
        solverprototxtpath: str = None,
        traintestprototxtpath: str = None,
        inferenceprototxtpath: str = None,
        dimimage: str = None,
        solver_content: str = None,
        train_test_content: str = None,
        inference_content: str = None,
        tfmainpath: str = None,
        tfmain_content: str = None,
        sig: str = None,
        signame: str = None,
        tmpfile_path: str = None,
        tmpfile_content: str = None,
        wfinit: str = None,
        wtfolder: str = None,
        type: str = None,
        user: str = None,
        create_time: str = None,
        framework_version: str = None,
        distribute_strategy: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modifies a deep learning model.

        Modifies a deep learning model.

        :param str modelname: The deep learning model name.
        :param str name: (optional) The name of the deep learning model.
        :param str path: (optional) The path of the deep learning model.
        :param str description: (optional) The description of the deep learning
               model.
        :param str templatename: (optional) The deep learning model template name.
        :param str framework: (optional) The deep learning model framework.
        :param str accelerator: (optional) The deep learning model training engine.
        :param HyperParameter hyperparameter: (optional)
        :param str dataset: (optional) The name of the the dataset associated with
               the deep learning model.
        :param int batchsize: (optional) The batch size.
        :param str solverprototxtpath: (optional) The path to *solver.prototxt
               configuration file.
        :param str traintestprototxtpath: (optional) The path to
               *train_test.prototxt configuration file.
        :param str inferenceprototxtpath: (optional) The path for inference
               configuration file.
        :param str dimimage: (optional) The dimimage.
        :param str solver_content: (optional) The content of the *solver.prototxt
               configuration file.
        :param str train_test_content: (optional) The content of the
               *train_test.prototxt configuration file.
        :param str inference_content: (optional) The content of the inference
               configuration file.
        :param str tfmainpath: (optional) The main executor file path.
        :param str tfmain_content: (optional) The contents of the main.py file.
        :param str sig: (optional) The Spark instance group id.
        :param str signame: (optional) The Spark instance group name.
        :param str tmpfile_path: (optional) The path of the temporary file.
        :param str tmpfile_content: (optional) Contents of the temporary file.
        :param str wfinit: (optional) The initial weight file.
        :param str wtfolder: (optional) The folder that contains the weight file.
        :param str type: (optional) The type of the model, indicates whether it is
               inference model or training model.
        :param str user: (optional) The user who created the model.
        :param str create_time: (optional) The time the model was created.
        :param str framework_version: (optional) The framework version.
        :param str distribute_strategy: (optional) The distribution strategy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if hyperparameter is not None:
            hyperparameter = convert_model(hyperparameter)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_model')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'path': path,
            'description': description,
            'templatename': templatename,
            'framework': framework,
            'accelerator': accelerator,
            'hyperparameter': hyperparameter,
            'dataset': dataset,
            'batchsize': batchsize,
            'solverprototxtpath': solverprototxtpath,
            'traintestprototxtpath': traintestprototxtpath,
            'inferenceprototxtpath': inferenceprototxtpath,
            'dimimage': dimimage,
            'solverContent': solver_content,
            'trainTestContent': train_test_content,
            'inferenceContent': inference_content,
            'tfmainpath': tfmainpath,
            'tfmainContent': tfmain_content,
            'sig': sig,
            'signame': signame,
            'tmpfilePath': tmpfile_path,
            'tmpfileContent': tmpfile_content,
            'wfinit': wfinit,
            'wtfolder': wtfolder,
            'type': type,
            'user': user,
            'createTime': create_time,
            'frameworkVersion': framework_version,
            'distributeStrategy': distribute_strategy
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_model(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a deep learning model.

        Deletes a deep learning model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_model_files(self,
        modelname: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieves model files.

        Returns full list of the files related with the specified model.

        :param str modelname: The deep learning model name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `str` result
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_model_files')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/files'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def save_model_file_content_by_name(self,
        modelname: str,
        *,
        name: str = None,
        path: str = None,
        description: str = None,
        templatename: str = None,
        framework: str = None,
        accelerator: str = None,
        hyperparameter: 'HyperParameter' = None,
        dataset: str = None,
        batchsize: int = None,
        solverprototxtpath: str = None,
        traintestprototxtpath: str = None,
        inferenceprototxtpath: str = None,
        dimimage: str = None,
        solver_content: str = None,
        train_test_content: str = None,
        inference_content: str = None,
        tfmainpath: str = None,
        tfmain_content: str = None,
        sig: str = None,
        signame: str = None,
        tmpfile_path: str = None,
        tmpfile_content: str = None,
        wfinit: str = None,
        wtfolder: str = None,
        type: str = None,
        user: str = None,
        create_time: str = None,
        framework_version: str = None,
        distribute_strategy: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modifies a deep learning model file.

        Modifies a deep learning model file.

        :param str modelname: The deep learning model name.
        :param str name: (optional) The name of the deep learning model.
        :param str path: (optional) The path of the deep learning model.
        :param str description: (optional) The description of the deep learning
               model.
        :param str templatename: (optional) The deep learning model template name.
        :param str framework: (optional) The deep learning model framework.
        :param str accelerator: (optional) The deep learning model training engine.
        :param HyperParameter hyperparameter: (optional)
        :param str dataset: (optional) The name of the the dataset associated with
               the deep learning model.
        :param int batchsize: (optional) The batch size.
        :param str solverprototxtpath: (optional) The path to *solver.prototxt
               configuration file.
        :param str traintestprototxtpath: (optional) The path to
               *train_test.prototxt configuration file.
        :param str inferenceprototxtpath: (optional) The path for inference
               configuration file.
        :param str dimimage: (optional) The dimimage.
        :param str solver_content: (optional) The content of the *solver.prototxt
               configuration file.
        :param str train_test_content: (optional) The content of the
               *train_test.prototxt configuration file.
        :param str inference_content: (optional) The content of the inference
               configuration file.
        :param str tfmainpath: (optional) The main executor file path.
        :param str tfmain_content: (optional) The contents of the main.py file.
        :param str sig: (optional) The Spark instance group id.
        :param str signame: (optional) The Spark instance group name.
        :param str tmpfile_path: (optional) The path of the temporary file.
        :param str tmpfile_content: (optional) Contents of the temporary file.
        :param str wfinit: (optional) The initial weight file.
        :param str wtfolder: (optional) The folder that contains the weight file.
        :param str type: (optional) The type of the model, indicates whether it is
               inference model or training model.
        :param str user: (optional) The user who created the model.
        :param str create_time: (optional) The time the model was created.
        :param str framework_version: (optional) The framework version.
        :param str distribute_strategy: (optional) The distribution strategy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if modelname is None:
            raise ValueError('modelname must be provided')
        if hyperparameter is not None:
            hyperparameter = convert_model(hyperparameter)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='save_model_file_content_by_name')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'path': path,
            'description': description,
            'templatename': templatename,
            'framework': framework,
            'accelerator': accelerator,
            'hyperparameter': hyperparameter,
            'dataset': dataset,
            'batchsize': batchsize,
            'solverprototxtpath': solverprototxtpath,
            'traintestprototxtpath': traintestprototxtpath,
            'inferenceprototxtpath': inferenceprototxtpath,
            'dimimage': dimimage,
            'solverContent': solver_content,
            'trainTestContent': train_test_content,
            'inferenceContent': inference_content,
            'tfmainpath': tfmainpath,
            'tfmainContent': tfmain_content,
            'sig': sig,
            'signame': signame,
            'tmpfilePath': tmpfile_path,
            'tmpfileContent': tmpfile_content,
            'wfinit': wfinit,
            'wtfolder': wtfolder,
            'type': type,
            'user': user,
            'createTime': create_time,
            'frameworkVersion': framework_version,
            'distributeStrategy': distribute_strategy
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['modelname']
        path_param_values = self.encode_path_vars(modelname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/platform/rest/deeplearning/v1/models/{modelname}/files'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


class GetModelTemplateDetailsEnums:
    """
    Enums for get_model_template_details parameters.
    """

    class Framework(str, Enum):
        """
        The deep learning framework name.
        """
        CAFFE = 'Caffe'
        TENSORFLOW = 'TensorFlow'
        PYTORCH = 'PyTorch'


class CsvListEnums:
    """
    Enums for csv_list parameters.
    """

    class Type(str, Enum):
        """
        The type of CSV data to review, for example - validation, test or training.
        """
        TRAIN = 'Train'
        TEST = 'Test'
        VAL = 'Val'


class ObjectimageListEnums:
    """
    Enums for objectimage_list parameters.
    """

    class Type(str, Enum):
        """
        The type of image data to review, for example - validation, test or training.
        """
        TRAIN = 'Train'
        VAL = 'Val'
        TEST = 'Test'


class GetDeepLearningFrameworksEnums:
    """
    Enums for get_deep_learning_frameworks parameters.
    """

    class Backend(str, Enum):
        """
        Filter deep learning frameworks by the backend framework name.
        """
        CAFFE = 'Caffe'
        TENSORFLOW = 'TensorFlow'
        PYTORCH = 'PyTorch'


##############################################################################
# Models
##############################################################################


class Attr():
    """
    Attr.

    :attr str key: The key.
    :attr str value: The value.
    """

    def __init__(self,
                 key: str,
                 value: str) -> None:
        """
        Initialize a Attr object.

        :param str key: The key.
        :param str value: The value.
        """
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attr':
        """Initialize a Attr object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError('Required property \'key\' not present in Attr JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Attr JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attr object from a json dictionary."""
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
        """Return a `str` version of this Attr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Attr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Attr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Batch():
    """
    Batch.

    :attr str user_name: (optional) Name of the user who started the task.
    :attr str sig_name: (optional) Name of the Spark instance group.
    :attr str sig_id: (optional) ID of the Spark instance group.
    :attr str id: (optional) ID of the batch.
    :attr str args: (optional) arguments to the tasks.
    :attr str submission_id: (optional) ID of the task.
    :attr str app_id: (optional) ID of the application.
    :attr str master_url: (optional) URL of the Spark.
    :attr str state: (optional) batch state.
    :attr str execution_user_name: (optional) User name.
    """

    def __init__(self,
                 *,
                 user_name: str = None,
                 sig_name: str = None,
                 sig_id: str = None,
                 id: str = None,
                 args: str = None,
                 submission_id: str = None,
                 app_id: str = None,
                 master_url: str = None,
                 state: str = None,
                 execution_user_name: str = None) -> None:
        """
        Initialize a Batch object.

        :param str user_name: (optional) Name of the user who started the task.
        :param str sig_name: (optional) Name of the Spark instance group.
        :param str sig_id: (optional) ID of the Spark instance group.
        :param str id: (optional) ID of the batch.
        :param str args: (optional) arguments to the tasks.
        :param str submission_id: (optional) ID of the task.
        :param str app_id: (optional) ID of the application.
        :param str master_url: (optional) URL of the Spark.
        :param str state: (optional) batch state.
        :param str execution_user_name: (optional) User name.
        """
        self.user_name = user_name
        self.sig_name = sig_name
        self.sig_id = sig_id
        self.id = id
        self.args = args
        self.submission_id = submission_id
        self.app_id = app_id
        self.master_url = master_url
        self.state = state
        self.execution_user_name = execution_user_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Batch':
        """Initialize a Batch object from a json dictionary."""
        args = {}
        if 'userName' in _dict:
            args['user_name'] = _dict.get('userName')
        if 'sigName' in _dict:
            args['sig_name'] = _dict.get('sigName')
        if 'sigId' in _dict:
            args['sig_id'] = _dict.get('sigId')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'args' in _dict:
            args['args'] = _dict.get('args')
        if 'submissionId' in _dict:
            args['submission_id'] = _dict.get('submissionId')
        if 'appId' in _dict:
            args['app_id'] = _dict.get('appId')
        if 'masterURL' in _dict:
            args['master_url'] = _dict.get('masterURL')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'executionUserName' in _dict:
            args['execution_user_name'] = _dict.get('executionUserName')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Batch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_name') and self.user_name is not None:
            _dict['userName'] = self.user_name
        if hasattr(self, 'sig_name') and self.sig_name is not None:
            _dict['sigName'] = self.sig_name
        if hasattr(self, 'sig_id') and self.sig_id is not None:
            _dict['sigId'] = self.sig_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'args') and self.args is not None:
            _dict['args'] = self.args
        if hasattr(self, 'submission_id') and self.submission_id is not None:
            _dict['submissionId'] = self.submission_id
        if hasattr(self, 'app_id') and self.app_id is not None:
            _dict['appId'] = self.app_id
        if hasattr(self, 'master_url') and self.master_url is not None:
            _dict['masterURL'] = self.master_url
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'execution_user_name') and self.execution_user_name is not None:
            _dict['executionUserName'] = self.execution_user_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Batch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Batch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Batch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ClassificationDetDetail():
    """
    ClassificationDetDetail.

    :attr str sample_id: (optional) The sample id.
    :attr str input_path: (optional) The input path.
    :attr bool is_image: (optional) True for image classification.
    :attr List[ClassificationDetResult] results: (optional) The result details.
    """

    def __init__(self,
                 *,
                 sample_id: str = None,
                 input_path: str = None,
                 is_image: bool = None,
                 results: List['ClassificationDetResult'] = None) -> None:
        """
        Initialize a ClassificationDetDetail object.

        :param str sample_id: (optional) The sample id.
        :param str input_path: (optional) The input path.
        :param bool is_image: (optional) True for image classification.
        :param List[ClassificationDetResult] results: (optional) The result
               details.
        """
        self.sample_id = sample_id
        self.input_path = input_path
        self.is_image = is_image
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationDetDetail':
        """Initialize a ClassificationDetDetail object from a json dictionary."""
        args = {}
        if 'sampleId' in _dict:
            args['sample_id'] = _dict.get('sampleId')
        if 'inputPath' in _dict:
            args['input_path'] = _dict.get('inputPath')
        if 'isImage' in _dict:
            args['is_image'] = _dict.get('isImage')
        if 'results' in _dict:
            args['results'] = [ClassificationDetResult.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationDetDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sample_id') and self.sample_id is not None:
            _dict['sampleId'] = self.sample_id
        if hasattr(self, 'input_path') and self.input_path is not None:
            _dict['inputPath'] = self.input_path
        if hasattr(self, 'is_image') and self.is_image is not None:
            _dict['isImage'] = self.is_image
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationDetDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationDetDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationDetDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ClassificationDetResult():
    """
    ClassificationDetResult.

    :attr str label: (optional) The label.
    :attr float prob: (optional) The probability that there is an object in the grid
          cell.
    :attr str bbox: (optional) The bounding box to describe the target location.
    """

    def __init__(self,
                 *,
                 label: str = None,
                 prob: float = None,
                 bbox: str = None) -> None:
        """
        Initialize a ClassificationDetResult object.

        :param str label: (optional) The label.
        :param float prob: (optional) The probability that there is an object in
               the grid cell.
        :param str bbox: (optional) The bounding box to describe the target
               location.
        """
        self.label = label
        self.prob = prob
        self.bbox = bbox

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationDetResult':
        """Initialize a ClassificationDetResult object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'prob' in _dict:
            args['prob'] = _dict.get('prob')
        if 'bbox' in _dict:
            args['bbox'] = _dict.get('bbox')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationDetResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'prob') and self.prob is not None:
            _dict['prob'] = self.prob
        if hasattr(self, 'bbox') and self.bbox is not None:
            _dict['bbox'] = self.bbox
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationDetResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationDetResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationDetResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ComparisonDetail():
    """
    ComparisonDetail.

    :attr str sample_id1: (optional) The first sample id.
    :attr str sample_id2: (optional) The second sample id.
    :attr str input_path: (optional) The input path.
    :attr bool is_image: (optional) True for image classification.
    :attr float distance: (optional) The distance.
    :attr bool is_similar: (optional) True if similar.
    """

    def __init__(self,
                 *,
                 sample_id1: str = None,
                 sample_id2: str = None,
                 input_path: str = None,
                 is_image: bool = None,
                 distance: float = None,
                 is_similar: bool = None) -> None:
        """
        Initialize a ComparisonDetail object.

        :param str sample_id1: (optional) The first sample id.
        :param str sample_id2: (optional) The second sample id.
        :param str input_path: (optional) The input path.
        :param bool is_image: (optional) True for image classification.
        :param float distance: (optional) The distance.
        :param bool is_similar: (optional) True if similar.
        """
        self.sample_id1 = sample_id1
        self.sample_id2 = sample_id2
        self.input_path = input_path
        self.is_image = is_image
        self.distance = distance
        self.is_similar = is_similar

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComparisonDetail':
        """Initialize a ComparisonDetail object from a json dictionary."""
        args = {}
        if 'sampleId1' in _dict:
            args['sample_id1'] = _dict.get('sampleId1')
        if 'sampleId2' in _dict:
            args['sample_id2'] = _dict.get('sampleId2')
        if 'inputPath' in _dict:
            args['input_path'] = _dict.get('inputPath')
        if 'isImage' in _dict:
            args['is_image'] = _dict.get('isImage')
        if 'distance' in _dict:
            args['distance'] = _dict.get('distance')
        if 'isSimilar' in _dict:
            args['is_similar'] = _dict.get('isSimilar')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComparisonDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sample_id1') and self.sample_id1 is not None:
            _dict['sampleId1'] = self.sample_id1
        if hasattr(self, 'sample_id2') and self.sample_id2 is not None:
            _dict['sampleId2'] = self.sample_id2
        if hasattr(self, 'input_path') and self.input_path is not None:
            _dict['inputPath'] = self.input_path
        if hasattr(self, 'is_image') and self.is_image is not None:
            _dict['isImage'] = self.is_image
        if hasattr(self, 'distance') and self.distance is not None:
            _dict['distance'] = self.distance
        if hasattr(self, 'is_similar') and self.is_similar is not None:
            _dict['isSimilar'] = self.is_similar
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComparisonDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComparisonDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComparisonDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Container():
    """
    Container.

    :attr str container_uid: (optional) The uid for container.
    :attr str container_host: (optional) The host for container.
    :attr str container_status: (optional) The status for container.
    :attr int total_task: (optional) The number of all tasks in the container.
    :attr int running_task: (optional) The number of running tasks in the container.
    :attr int finish_task: (optional) The number of finish tasks in the container.
    :attr int failed_task: (optional) The number of failed tasks in the container.
    """

    def __init__(self,
                 *,
                 container_uid: str = None,
                 container_host: str = None,
                 container_status: str = None,
                 total_task: int = None,
                 running_task: int = None,
                 finish_task: int = None,
                 failed_task: int = None) -> None:
        """
        Initialize a Container object.

        :param str container_uid: (optional) The uid for container.
        :param str container_host: (optional) The host for container.
        :param str container_status: (optional) The status for container.
        :param int total_task: (optional) The number of all tasks in the container.
        :param int running_task: (optional) The number of running tasks in the
               container.
        :param int finish_task: (optional) The number of finish tasks in the
               container.
        :param int failed_task: (optional) The number of failed tasks in the
               container.
        """
        self.container_uid = container_uid
        self.container_host = container_host
        self.container_status = container_status
        self.total_task = total_task
        self.running_task = running_task
        self.finish_task = finish_task
        self.failed_task = failed_task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Container':
        """Initialize a Container object from a json dictionary."""
        args = {}
        if 'container_uid' in _dict:
            args['container_uid'] = _dict.get('container_uid')
        if 'container_host' in _dict:
            args['container_host'] = _dict.get('container_host')
        if 'container_status' in _dict:
            args['container_status'] = _dict.get('container_status')
        if 'total_task' in _dict:
            args['total_task'] = _dict.get('total_task')
        if 'running_task' in _dict:
            args['running_task'] = _dict.get('running_task')
        if 'finish_task' in _dict:
            args['finish_task'] = _dict.get('finish_task')
        if 'failed_task' in _dict:
            args['failed_task'] = _dict.get('failed_task')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Container object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'container_uid') and self.container_uid is not None:
            _dict['container_uid'] = self.container_uid
        if hasattr(self, 'container_host') and self.container_host is not None:
            _dict['container_host'] = self.container_host
        if hasattr(self, 'container_status') and self.container_status is not None:
            _dict['container_status'] = self.container_status
        if hasattr(self, 'total_task') and self.total_task is not None:
            _dict['total_task'] = self.total_task
        if hasattr(self, 'running_task') and self.running_task is not None:
            _dict['running_task'] = self.running_task
        if hasattr(self, 'finish_task') and self.finish_task is not None:
            _dict['finish_task'] = self.finish_task
        if hasattr(self, 'failed_task') and self.failed_task is not None:
            _dict['failed_task'] = self.failed_task
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Container object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Container') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Container') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreationResponse():
    """
    CreationResponse.

    :attr str uid: (optional) Unique id of object.
    :attr str href: (optional) Relative endpoint url of the corresponding object.
    """

    def __init__(self,
                 *,
                 uid: str = None,
                 href: str = None) -> None:
        """
        Initialize a CreationResponse object.

        :param str uid: (optional) Unique id of object.
        :param str href: (optional) Relative endpoint url of the corresponding
               object.
        """
        self.uid = uid
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreationResponse':
        """Initialize a CreationResponse object from a json dictionary."""
        args = {}
        if 'uid' in _dict:
            args['uid'] = _dict.get('uid')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'uid') and self.uid is not None:
            _dict['uid'] = self.uid
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DLFramework():
    """
    DLFramework.

    :attr str name: (optional) Name of the deep learning framework.
    :attr List[str] desc: (optional) Description of the deep learning framework.
    :attr str framework_version: (optional) The framework version.
    :attr str distribute_strategy: (optional) The distributed strategies.
    :attr str description: (optional) Description.
    :attr int num_ps: (optional) Number of parameter server workers.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 desc: List[str] = None,
                 framework_version: str = None,
                 distribute_strategy: str = None,
                 description: str = None,
                 num_ps: int = None) -> None:
        """
        Initialize a DLFramework object.

        :param str name: (optional) Name of the deep learning framework.
        :param List[str] desc: (optional) Description of the deep learning
               framework.
        :param str framework_version: (optional) The framework version.
        :param str distribute_strategy: (optional) The distributed strategies.
        :param str description: (optional) Description.
        :param int num_ps: (optional) Number of parameter server workers.
        """
        self.name = name
        self.desc = desc
        self.framework_version = framework_version
        self.distribute_strategy = distribute_strategy
        self.description = description
        self.num_ps = num_ps

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DLFramework':
        """Initialize a DLFramework object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'desc' in _dict:
            args['desc'] = _dict.get('desc')
        if 'frameworkVersion' in _dict:
            args['framework_version'] = _dict.get('frameworkVersion')
        if 'distributeStrategy' in _dict:
            args['distribute_strategy'] = _dict.get('distributeStrategy')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'numPs' in _dict:
            args['num_ps'] = _dict.get('numPs')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DLFramework object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'desc') and self.desc is not None:
            _dict['desc'] = self.desc
        if hasattr(self, 'framework_version') and self.framework_version is not None:
            _dict['frameworkVersion'] = self.framework_version
        if hasattr(self, 'distribute_strategy') and self.distribute_strategy is not None:
            _dict['distributeStrategy'] = self.distribute_strategy
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'num_ps') and self.num_ps is not None:
            _dict['numPs'] = self.num_ps
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DLFramework object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DLFramework') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DLFramework') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DistributeStrategyEnum(str, Enum):
        """
        The distributed strategies.
        """
        MULTIWORKERMIRROREDSTRATEGY = 'MultiWorkerMirroredStrategy'
        PARAMETERSERVERSTRATEGY = 'ParameterServerStrategy'


class DatasetDetail():
    """
    DatasetDetail.

    :attr str name: (optional) The dataset name.
    :attr str dbbackend: (optional) The backend database (e.g. LMDB, Other,
          TFrecords, CSV, ObjectDetection).
    :attr str trainpath: (optional) The dataset training folder path.
    :attr str valpath: (optional) The dataset validation folder path.
    :attr str testpath: (optional) The dataset test folder path.
    :attr str meanfilepath: (optional) The dataset mean file path.
    :attr str status: (optional) The dataset status.
    :attr float runduration: (optional) The application run duration.
    :attr str sigid: (optional) The Spark instance group ID.
    :attr str signame: (optional) The Spark instance group Name.
    :attr str master_url: (optional) The Spark master URL.
    :attr str driverid: (optional) The Spark driver ID.
    :attr str sparkappid: (optional) The Spark Application ID.
    :attr ImageDetail imagedetail: (optional)
    :attr List[List[str]] trainlabels: (optional) The dataset training labels.
    :attr List[List[str]] vallabels: (optional) The dataset validation labels.
    :attr List[List[str]] testlabels: (optional) The dataset test labels.
    :attr str datasourcetype: (optional) Type of source data for creating a new
          dataset.
    :attr str submittedtime: (optional) The application submitted time.
    :attr str create_user: (optional) The user that creates the dataset.
    :attr float size: (optional) The size of the dataset.
    :attr int shards: (optional) The number of shards of the dataset.
    :attr bool byclass: (optional) Whether to generate records by class.
    :attr str plugin: (optional) the csv plugin file path.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 dbbackend: str = None,
                 trainpath: str = None,
                 valpath: str = None,
                 testpath: str = None,
                 meanfilepath: str = None,
                 status: str = None,
                 runduration: float = None,
                 sigid: str = None,
                 signame: str = None,
                 master_url: str = None,
                 driverid: str = None,
                 sparkappid: str = None,
                 imagedetail: 'ImageDetail' = None,
                 trainlabels: List[List[str]] = None,
                 vallabels: List[List[str]] = None,
                 testlabels: List[List[str]] = None,
                 datasourcetype: str = None,
                 submittedtime: str = None,
                 create_user: str = None,
                 size: float = None,
                 shards: int = None,
                 byclass: bool = None,
                 plugin: str = None) -> None:
        """
        Initialize a DatasetDetail object.

        :param str name: (optional) The dataset name.
        :param str dbbackend: (optional) The backend database (e.g. LMDB, Other,
               TFrecords, CSV, ObjectDetection).
        :param str trainpath: (optional) The dataset training folder path.
        :param str valpath: (optional) The dataset validation folder path.
        :param str testpath: (optional) The dataset test folder path.
        :param str meanfilepath: (optional) The dataset mean file path.
        :param str status: (optional) The dataset status.
        :param float runduration: (optional) The application run duration.
        :param str sigid: (optional) The Spark instance group ID.
        :param str signame: (optional) The Spark instance group Name.
        :param str master_url: (optional) The Spark master URL.
        :param str driverid: (optional) The Spark driver ID.
        :param str sparkappid: (optional) The Spark Application ID.
        :param ImageDetail imagedetail: (optional)
        :param List[List[str]] trainlabels: (optional) The dataset training labels.
        :param List[List[str]] vallabels: (optional) The dataset validation labels.
        :param List[List[str]] testlabels: (optional) The dataset test labels.
        :param str datasourcetype: (optional) Type of source data for creating a
               new dataset.
        :param str submittedtime: (optional) The application submitted time.
        :param str create_user: (optional) The user that creates the dataset.
        :param float size: (optional) The size of the dataset.
        :param int shards: (optional) The number of shards of the dataset.
        :param bool byclass: (optional) Whether to generate records by class.
        :param str plugin: (optional) the csv plugin file path.
        """
        self.name = name
        self.dbbackend = dbbackend
        self.trainpath = trainpath
        self.valpath = valpath
        self.testpath = testpath
        self.meanfilepath = meanfilepath
        self.status = status
        self.runduration = runduration
        self.sigid = sigid
        self.signame = signame
        self.master_url = master_url
        self.driverid = driverid
        self.sparkappid = sparkappid
        self.imagedetail = imagedetail
        self.trainlabels = trainlabels
        self.vallabels = vallabels
        self.testlabels = testlabels
        self.datasourcetype = datasourcetype
        self.submittedtime = submittedtime
        self.create_user = create_user
        self.size = size
        self.shards = shards
        self.byclass = byclass
        self.plugin = plugin

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatasetDetail':
        """Initialize a DatasetDetail object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'dbbackend' in _dict:
            args['dbbackend'] = _dict.get('dbbackend')
        if 'trainpath' in _dict:
            args['trainpath'] = _dict.get('trainpath')
        if 'valpath' in _dict:
            args['valpath'] = _dict.get('valpath')
        if 'testpath' in _dict:
            args['testpath'] = _dict.get('testpath')
        if 'meanfilepath' in _dict:
            args['meanfilepath'] = _dict.get('meanfilepath')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'runduration' in _dict:
            args['runduration'] = _dict.get('runduration')
        if 'sigid' in _dict:
            args['sigid'] = _dict.get('sigid')
        if 'signame' in _dict:
            args['signame'] = _dict.get('signame')
        if 'masterUrl' in _dict:
            args['master_url'] = _dict.get('masterUrl')
        if 'driverid' in _dict:
            args['driverid'] = _dict.get('driverid')
        if 'sparkappid' in _dict:
            args['sparkappid'] = _dict.get('sparkappid')
        if 'imagedetail' in _dict:
            args['imagedetail'] = ImageDetail.from_dict(_dict.get('imagedetail'))
        if 'trainlabels' in _dict:
            args['trainlabels'] = _dict.get('trainlabels')
        if 'vallabels' in _dict:
            args['vallabels'] = _dict.get('vallabels')
        if 'testlabels' in _dict:
            args['testlabels'] = _dict.get('testlabels')
        if 'datasourcetype' in _dict:
            args['datasourcetype'] = _dict.get('datasourcetype')
        if 'submittedtime' in _dict:
            args['submittedtime'] = _dict.get('submittedtime')
        if 'createUser' in _dict:
            args['create_user'] = _dict.get('createUser')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'shards' in _dict:
            args['shards'] = _dict.get('shards')
        if 'byclass' in _dict:
            args['byclass'] = _dict.get('byclass')
        if 'plugin' in _dict:
            args['plugin'] = _dict.get('plugin')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatasetDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'dbbackend') and self.dbbackend is not None:
            _dict['dbbackend'] = self.dbbackend
        if hasattr(self, 'trainpath') and self.trainpath is not None:
            _dict['trainpath'] = self.trainpath
        if hasattr(self, 'valpath') and self.valpath is not None:
            _dict['valpath'] = self.valpath
        if hasattr(self, 'testpath') and self.testpath is not None:
            _dict['testpath'] = self.testpath
        if hasattr(self, 'meanfilepath') and self.meanfilepath is not None:
            _dict['meanfilepath'] = self.meanfilepath
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'runduration') and self.runduration is not None:
            _dict['runduration'] = self.runduration
        if hasattr(self, 'sigid') and self.sigid is not None:
            _dict['sigid'] = self.sigid
        if hasattr(self, 'signame') and self.signame is not None:
            _dict['signame'] = self.signame
        if hasattr(self, 'master_url') and self.master_url is not None:
            _dict['masterUrl'] = self.master_url
        if hasattr(self, 'driverid') and self.driverid is not None:
            _dict['driverid'] = self.driverid
        if hasattr(self, 'sparkappid') and self.sparkappid is not None:
            _dict['sparkappid'] = self.sparkappid
        if hasattr(self, 'imagedetail') and self.imagedetail is not None:
            _dict['imagedetail'] = self.imagedetail.to_dict()
        if hasattr(self, 'trainlabels') and self.trainlabels is not None:
            _dict['trainlabels'] = self.trainlabels
        if hasattr(self, 'vallabels') and self.vallabels is not None:
            _dict['vallabels'] = self.vallabels
        if hasattr(self, 'testlabels') and self.testlabels is not None:
            _dict['testlabels'] = self.testlabels
        if hasattr(self, 'datasourcetype') and self.datasourcetype is not None:
            _dict['datasourcetype'] = self.datasourcetype
        if hasattr(self, 'submittedtime') and self.submittedtime is not None:
            _dict['submittedtime'] = self.submittedtime
        if hasattr(self, 'create_user') and self.create_user is not None:
            _dict['createUser'] = self.create_user
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'shards') and self.shards is not None:
            _dict['shards'] = self.shards
        if hasattr(self, 'byclass') and self.byclass is not None:
            _dict['byclass'] = self.byclass
        if hasattr(self, 'plugin') and self.plugin is not None:
            _dict['plugin'] = self.plugin
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatasetDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatasetDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatasetDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DatasourcetypeEnum(str, Enum):
        """
        Type of source data for creating a new dataset.
        """
        LMDB = 'LMDB'
        TFRECORDS = 'TFRECORDS'
        OTHER = 'OTHER'
        IMAGEFORCLASSIFICATION = 'IMAGEFORCLASSIFICATION'
        CSV = 'CSV'
        IMAGEFOROBJECTDETECTION = 'IMAGEFOROBJECTDETECTION'
        IMGTOVECTOR = 'IMGTOVECTOR'


class DriverDetail():
    """
    DriverDetail.

    :attr str id: (optional) The Spark drivers ID.
    :attr str containerid: (optional) The resource orchestrator activity ID that
          starts the Spark drivers.
    :attr str state: (optional) The Spark drivers state.
    :attr str host: (optional) The host on which the Spark drivers run.
    :attr float coresused: (optional) The number of CPU cores allocated.
    :attr float memused: (optional) The amount of memory, in MB that is used by the
          Spark drivers.
    :attr int timestamp: (optional) The time-stamp of the updated Spark drivers.
    :attr str driverstdout: (optional) The path to the Spark drivers stdout log.
    :attr str driverstderr: (optional) The path to the Spark drivers stderr log.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 containerid: str = None,
                 state: str = None,
                 host: str = None,
                 coresused: float = None,
                 memused: float = None,
                 timestamp: int = None,
                 driverstdout: str = None,
                 driverstderr: str = None) -> None:
        """
        Initialize a DriverDetail object.

        :param str id: (optional) The Spark drivers ID.
        :param str containerid: (optional) The resource orchestrator activity ID
               that starts the Spark drivers.
        :param str state: (optional) The Spark drivers state.
        :param str host: (optional) The host on which the Spark drivers run.
        :param float coresused: (optional) The number of CPU cores allocated.
        :param float memused: (optional) The amount of memory, in MB that is used
               by the Spark drivers.
        :param int timestamp: (optional) The time-stamp of the updated Spark
               drivers.
        :param str driverstdout: (optional) The path to the Spark drivers stdout
               log.
        :param str driverstderr: (optional) The path to the Spark drivers stderr
               log.
        """
        self.id = id
        self.containerid = containerid
        self.state = state
        self.host = host
        self.coresused = coresused
        self.memused = memused
        self.timestamp = timestamp
        self.driverstdout = driverstdout
        self.driverstderr = driverstderr

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DriverDetail':
        """Initialize a DriverDetail object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'containerid' in _dict:
            args['containerid'] = _dict.get('containerid')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'coresused' in _dict:
            args['coresused'] = _dict.get('coresused')
        if 'memused' in _dict:
            args['memused'] = _dict.get('memused')
        if 'timestamp' in _dict:
            args['timestamp'] = _dict.get('timestamp')
        if 'driverstdout' in _dict:
            args['driverstdout'] = _dict.get('driverstdout')
        if 'driverstderr' in _dict:
            args['driverstderr'] = _dict.get('driverstderr')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DriverDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'containerid') and self.containerid is not None:
            _dict['containerid'] = self.containerid
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'coresused') and self.coresused is not None:
            _dict['coresused'] = self.coresused
        if hasattr(self, 'memused') and self.memused is not None:
            _dict['memused'] = self.memused
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = self.timestamp
        if hasattr(self, 'driverstdout') and self.driverstdout is not None:
            _dict['driverstdout'] = self.driverstdout
        if hasattr(self, 'driverstderr') and self.driverstderr is not None:
            _dict['driverstderr'] = self.driverstderr
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DriverDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DriverDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DriverDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Envs():
    """
    Envs.

    :attr str name: The name.
    :attr str value: The value.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a Envs object.

        :param str name: The name.
        :param str value: The value.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Envs':
        """Initialize a Envs object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Envs JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Envs JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Envs object from a json dictionary."""
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
        """Return a `str` version of this Envs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Envs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Envs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ExecutorDetail():
    """
    ExecutorDetail.

    :attr str id: (optional) The Spark executor ID.
    :attr str containerid: (optional) The resource orchestrator activity ID that
          starts the Spark executors.
    :attr str state: (optional) The Spark executor state.
    :attr str host: (optional) The host on which the Spark executors run.
    :attr float coresused: (optional) The number of CPU cores that are allocated.
    :attr float memused: (optional) The amount of memory, in MB, that is used by the
          executors.
    :attr int timestamp: (optional) The time-stamp of the updated Spark executors.
    :attr str executorstdout: (optional) The path to the Spark executors stdout log.
    :attr str executorstderr: (optional) The path to the Spark executors stderr log.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 containerid: str = None,
                 state: str = None,
                 host: str = None,
                 coresused: float = None,
                 memused: float = None,
                 timestamp: int = None,
                 executorstdout: str = None,
                 executorstderr: str = None) -> None:
        """
        Initialize a ExecutorDetail object.

        :param str id: (optional) The Spark executor ID.
        :param str containerid: (optional) The resource orchestrator activity ID
               that starts the Spark executors.
        :param str state: (optional) The Spark executor state.
        :param str host: (optional) The host on which the Spark executors run.
        :param float coresused: (optional) The number of CPU cores that are
               allocated.
        :param float memused: (optional) The amount of memory, in MB, that is used
               by the executors.
        :param int timestamp: (optional) The time-stamp of the updated Spark
               executors.
        :param str executorstdout: (optional) The path to the Spark executors
               stdout log.
        :param str executorstderr: (optional) The path to the Spark executors
               stderr log.
        """
        self.id = id
        self.containerid = containerid
        self.state = state
        self.host = host
        self.coresused = coresused
        self.memused = memused
        self.timestamp = timestamp
        self.executorstdout = executorstdout
        self.executorstderr = executorstderr

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExecutorDetail':
        """Initialize a ExecutorDetail object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'containerid' in _dict:
            args['containerid'] = _dict.get('containerid')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'coresused' in _dict:
            args['coresused'] = _dict.get('coresused')
        if 'memused' in _dict:
            args['memused'] = _dict.get('memused')
        if 'timestamp' in _dict:
            args['timestamp'] = _dict.get('timestamp')
        if 'executorstdout' in _dict:
            args['executorstdout'] = _dict.get('executorstdout')
        if 'executorstderr' in _dict:
            args['executorstderr'] = _dict.get('executorstderr')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExecutorDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'containerid') and self.containerid is not None:
            _dict['containerid'] = self.containerid
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'coresused') and self.coresused is not None:
            _dict['coresused'] = self.coresused
        if hasattr(self, 'memused') and self.memused is not None:
            _dict['memused'] = self.memused
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = self.timestamp
        if hasattr(self, 'executorstdout') and self.executorstdout is not None:
            _dict['executorstdout'] = self.executorstdout
        if hasattr(self, 'executorstderr') and self.executorstderr is not None:
            _dict['executorstderr'] = self.executorstderr
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExecutorDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExecutorDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExecutorDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FrameworkDetail():
    """
    FrameworkDetail.

    :attr str name: (optional) The name of the deep learning framework.
    :attr str home: (optional) The home folder of the deep learning framework.
    :attr str backend: (optional) The deep learning framework backend.
    :attr str accelerator: (optional) The deep learning training engine.
    :attr str ps_num: (optional) The psNum.
    :attr str comm_ip_network: (optional) The communication network.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 home: str = None,
                 backend: str = None,
                 accelerator: str = None,
                 ps_num: str = None,
                 comm_ip_network: str = None) -> None:
        """
        Initialize a FrameworkDetail object.

        :param str name: (optional) The name of the deep learning framework.
        :param str home: (optional) The home folder of the deep learning framework.
        :param str backend: (optional) The deep learning framework backend.
        :param str accelerator: (optional) The deep learning training engine.
        :param str ps_num: (optional) The psNum.
        :param str comm_ip_network: (optional) The communication network.
        """
        self.name = name
        self.home = home
        self.backend = backend
        self.accelerator = accelerator
        self.ps_num = ps_num
        self.comm_ip_network = comm_ip_network

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FrameworkDetail':
        """Initialize a FrameworkDetail object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'home' in _dict:
            args['home'] = _dict.get('home')
        if 'backend' in _dict:
            args['backend'] = _dict.get('backend')
        if 'accelerator' in _dict:
            args['accelerator'] = _dict.get('accelerator')
        if 'psNum' in _dict:
            args['ps_num'] = _dict.get('psNum')
        if 'commIPNetwork' in _dict:
            args['comm_ip_network'] = _dict.get('commIPNetwork')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FrameworkDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'home') and self.home is not None:
            _dict['home'] = self.home
        if hasattr(self, 'backend') and self.backend is not None:
            _dict['backend'] = self.backend
        if hasattr(self, 'accelerator') and self.accelerator is not None:
            _dict['accelerator'] = self.accelerator
        if hasattr(self, 'ps_num') and self.ps_num is not None:
            _dict['psNum'] = self.ps_num
        if hasattr(self, 'comm_ip_network') and self.comm_ip_network is not None:
            _dict['commIPNetwork'] = self.comm_ip_network
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FrameworkDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FrameworkDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FrameworkDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AcceleratorEnum(str, Enum):
        """
        The deep learning training engine.
        """
        NATIVE = 'Native'
        ELASTIC = 'Elastic'


class HpoAlgorithmDesc():
    """
    HpoAlgorithmDesc.

    :attr str name: (optional) The hpo algorithm name.
    :attr str path: (optional) The hpo algorithm installation path (only for plugin
          algorithm).
    :attr str conda_home: (optional) The CONDA_HOME used to run hpo algorithm (only
          for plugin algorithm).
    :attr str conda_env: (optional) The conda environment used to run hpo algorithm
          (only for plugin algorithm).
    :attr str createtime: (optional) The creation time of the hpo algorithm (only
          for plugin algorithm).
    :attr str type: (optional) The type of the hpo algorithm.
    :attr bool remote_exec: (optional) The plugin algorithm execution mode is
          remoted or not (only for plugin algorithm).
    :attr str log_level: (optional) The log level for the plugin algorithm (only for
          plugin algorithm).
    """

    def __init__(self,
                 *,
                 name: str = None,
                 path: str = None,
                 conda_home: str = None,
                 conda_env: str = None,
                 createtime: str = None,
                 type: str = None,
                 remote_exec: bool = None,
                 log_level: str = None) -> None:
        """
        Initialize a HpoAlgorithmDesc object.

        :param str name: (optional) The hpo algorithm name.
        :param str path: (optional) The hpo algorithm installation path (only for
               plugin algorithm).
        :param str conda_home: (optional) The CONDA_HOME used to run hpo algorithm
               (only for plugin algorithm).
        :param str conda_env: (optional) The conda environment used to run hpo
               algorithm (only for plugin algorithm).
        :param str createtime: (optional) The creation time of the hpo algorithm
               (only for plugin algorithm).
        :param str type: (optional) The type of the hpo algorithm.
        :param bool remote_exec: (optional) The plugin algorithm execution mode is
               remoted or not (only for plugin algorithm).
        :param str log_level: (optional) The log level for the plugin algorithm
               (only for plugin algorithm).
        """
        self.name = name
        self.path = path
        self.conda_home = conda_home
        self.conda_env = conda_env
        self.createtime = createtime
        self.type = type
        self.remote_exec = remote_exec
        self.log_level = log_level

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoAlgorithmDesc':
        """Initialize a HpoAlgorithmDesc object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'condaHome' in _dict:
            args['conda_home'] = _dict.get('condaHome')
        if 'condaEnv' in _dict:
            args['conda_env'] = _dict.get('condaEnv')
        if 'createtime' in _dict:
            args['createtime'] = _dict.get('createtime')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'remoteExec' in _dict:
            args['remote_exec'] = _dict.get('remoteExec')
        if 'logLevel' in _dict:
            args['log_level'] = _dict.get('logLevel')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoAlgorithmDesc object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'conda_home') and self.conda_home is not None:
            _dict['condaHome'] = self.conda_home
        if hasattr(self, 'conda_env') and self.conda_env is not None:
            _dict['condaEnv'] = self.conda_env
        if hasattr(self, 'createtime') and self.createtime is not None:
            _dict['createtime'] = self.createtime
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'remote_exec') and self.remote_exec is not None:
            _dict['remoteExec'] = self.remote_exec
        if hasattr(self, 'log_level') and self.log_level is not None:
            _dict['logLevel'] = self.log_level
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoAlgorithmDesc object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoAlgorithmDesc') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoAlgorithmDesc') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HpoExperiment():
    """
    HpoExperiment.

    :attr int id: (optional) Experiment id.
    :attr str state: (optional) Experiment state.
    :attr float metric_val: (optional) metric value.
    :attr List[HpoMetric] metrics: (optional)
    :attr int maxiteration: (optional) maximum iteration.
    :attr List[HpoHyperParameter] hyper_params: (optional)
    :attr str app_id: (optional) spark application Id.
    :attr str driver_id: (optional) spark driver Id.
    :attr str start_time: (optional) The start time of experiment training.
    :attr str end_time: (optional) The end time of experiment training.
    """

    def __init__(self,
                 *,
                 id: int = None,
                 state: str = None,
                 metric_val: float = None,
                 metrics: List['HpoMetric'] = None,
                 maxiteration: int = None,
                 hyper_params: List['HpoHyperParameter'] = None,
                 app_id: str = None,
                 driver_id: str = None,
                 start_time: str = None,
                 end_time: str = None) -> None:
        """
        Initialize a HpoExperiment object.

        :param int id: (optional) Experiment id.
        :param str state: (optional) Experiment state.
        :param float metric_val: (optional) metric value.
        :param List[HpoMetric] metrics: (optional)
        :param int maxiteration: (optional) maximum iteration.
        :param List[HpoHyperParameter] hyper_params: (optional)
        :param str app_id: (optional) spark application Id.
        :param str driver_id: (optional) spark driver Id.
        :param str start_time: (optional) The start time of experiment training.
        :param str end_time: (optional) The end time of experiment training.
        """
        self.id = id
        self.state = state
        self.metric_val = metric_val
        self.metrics = metrics
        self.maxiteration = maxiteration
        self.hyper_params = hyper_params
        self.app_id = app_id
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoExperiment':
        """Initialize a HpoExperiment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'metricVal' in _dict:
            args['metric_val'] = _dict.get('metricVal')
        if 'metrics' in _dict:
            args['metrics'] = [HpoMetric.from_dict(x) for x in _dict.get('metrics')]
        if 'maxiteration' in _dict:
            args['maxiteration'] = _dict.get('maxiteration')
        if 'hyperParams' in _dict:
            args['hyper_params'] = [HpoHyperParameter.from_dict(x) for x in _dict.get('hyperParams')]
        if 'appId' in _dict:
            args['app_id'] = _dict.get('appId')
        if 'driverId' in _dict:
            args['driver_id'] = _dict.get('driverId')
        if 'startTime' in _dict:
            args['start_time'] = _dict.get('startTime')
        if 'endTime' in _dict:
            args['end_time'] = _dict.get('endTime')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoExperiment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'metric_val') and self.metric_val is not None:
            _dict['metricVal'] = self.metric_val
        if hasattr(self, 'metrics') and self.metrics is not None:
            _dict['metrics'] = [x.to_dict() for x in self.metrics]
        if hasattr(self, 'maxiteration') and self.maxiteration is not None:
            _dict['maxiteration'] = self.maxiteration
        if hasattr(self, 'hyper_params') and self.hyper_params is not None:
            _dict['hyperParams'] = [x.to_dict() for x in self.hyper_params]
        if hasattr(self, 'app_id') and self.app_id is not None:
            _dict['appId'] = self.app_id
        if hasattr(self, 'driver_id') and self.driver_id is not None:
            _dict['driverId'] = self.driver_id
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['startTime'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['endTime'] = self.end_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoExperiment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoExperiment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoExperiment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HpoHyperParameter():
    """
    HpoHyperParameter.

    :attr str name: Hyperparameter name, the same name will be used in the
          config.json so user model can load it.
    :attr str type: One of Range, Discrete, Fix.
    :attr str data_type: One of int, double, str.
    :attr float min_db_val: (optional) Minimal double value if type=Range and
          datatype=double.
    :attr float max_db_val: (optional) Maximal double value if type=Range and
          datatype=double.
    :attr int min_int_val: (optional) Minimal int value if type=Range and
          datatype=int.
    :attr int max_int_val: (optional) Maximal int value if type=Range and
          datatype=int.
    :attr List[float] discrete_db_val: (optional) Double list like [0.1,0.2] if
          type=Discreate and datatype=double.
    :attr List[int] discrete_int_val: (optional) Int list like [1,2] if
          type=Discreate and datatype=int.
    :attr List[str] discreate_str_val: (optional) str list like ['1','2'] if
          type=Discreate and datatype=double.
    :attr bool user_defined: (optional) whether is user defined parameter.
    :attr str fixed_val: (optional) fixed hyperparameter.
    :attr str step: (optional) A number value in string format, step size to split
          the Range space. ONLY valid when type is Range.
    :attr str power: (optional) A number value in string format, the base value for
          power calculation. ONLY valid when type is Range.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 data_type: str,
                 *,
                 min_db_val: float = None,
                 max_db_val: float = None,
                 min_int_val: int = None,
                 max_int_val: int = None,
                 discrete_db_val: List[float] = None,
                 discrete_int_val: List[int] = None,
                 discreate_str_val: List[str] = None,
                 user_defined: bool = None,
                 fixed_val: str = None,
                 step: str = None,
                 power: str = None) -> None:
        """
        Initialize a HpoHyperParameter object.

        :param str name: Hyperparameter name, the same name will be used in the
               config.json so user model can load it.
        :param str type: One of Range, Discrete, Fix.
        :param str data_type: One of int, double, str.
        :param float min_db_val: (optional) Minimal double value if type=Range and
               datatype=double.
        :param float max_db_val: (optional) Maximal double value if type=Range and
               datatype=double.
        :param int min_int_val: (optional) Minimal int value if type=Range and
               datatype=int.
        :param int max_int_val: (optional) Maximal int value if type=Range and
               datatype=int.
        :param List[float] discrete_db_val: (optional) Double list like [0.1,0.2]
               if type=Discreate and datatype=double.
        :param List[int] discrete_int_val: (optional) Int list like [1,2] if
               type=Discreate and datatype=int.
        :param List[str] discreate_str_val: (optional) str list like ['1','2'] if
               type=Discreate and datatype=double.
        :param bool user_defined: (optional) whether is user defined parameter.
        :param str fixed_val: (optional) fixed hyperparameter.
        :param str step: (optional) A number value in string format, step size to
               split the Range space. ONLY valid when type is Range.
        :param str power: (optional) A number value in string format, the base
               value for power calculation. ONLY valid when type is Range.
        """
        self.name = name
        self.type = type
        self.data_type = data_type
        self.min_db_val = min_db_val
        self.max_db_val = max_db_val
        self.min_int_val = min_int_val
        self.max_int_val = max_int_val
        self.discrete_db_val = discrete_db_val
        self.discrete_int_val = discrete_int_val
        self.discreate_str_val = discreate_str_val
        self.user_defined = user_defined
        self.fixed_val = fixed_val
        self.step = step
        self.power = power

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoHyperParameter':
        """Initialize a HpoHyperParameter object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in HpoHyperParameter JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in HpoHyperParameter JSON')
        if 'dataType' in _dict:
            args['data_type'] = _dict.get('dataType')
        else:
            raise ValueError('Required property \'dataType\' not present in HpoHyperParameter JSON')
        if 'minDbVal' in _dict:
            args['min_db_val'] = _dict.get('minDbVal')
        if 'maxDbVal' in _dict:
            args['max_db_val'] = _dict.get('maxDbVal')
        if 'minIntVal' in _dict:
            args['min_int_val'] = _dict.get('minIntVal')
        if 'maxIntVal' in _dict:
            args['max_int_val'] = _dict.get('maxIntVal')
        if 'discreteDbVal' in _dict:
            args['discrete_db_val'] = _dict.get('discreteDbVal')
        if 'discreteIntVal' in _dict:
            args['discrete_int_val'] = _dict.get('discreteIntVal')
        if 'discreateStrVal' in _dict:
            args['discreate_str_val'] = _dict.get('discreateStrVal')
        if 'userDefined' in _dict:
            args['user_defined'] = _dict.get('userDefined')
        if 'fixedVal' in _dict:
            args['fixed_val'] = _dict.get('fixedVal')
        if 'step' in _dict:
            args['step'] = _dict.get('step')
        if 'power' in _dict:
            args['power'] = _dict.get('power')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoHyperParameter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'data_type') and self.data_type is not None:
            _dict['dataType'] = self.data_type
        if hasattr(self, 'min_db_val') and self.min_db_val is not None:
            _dict['minDbVal'] = self.min_db_val
        if hasattr(self, 'max_db_val') and self.max_db_val is not None:
            _dict['maxDbVal'] = self.max_db_val
        if hasattr(self, 'min_int_val') and self.min_int_val is not None:
            _dict['minIntVal'] = self.min_int_val
        if hasattr(self, 'max_int_val') and self.max_int_val is not None:
            _dict['maxIntVal'] = self.max_int_val
        if hasattr(self, 'discrete_db_val') and self.discrete_db_val is not None:
            _dict['discreteDbVal'] = self.discrete_db_val
        if hasattr(self, 'discrete_int_val') and self.discrete_int_val is not None:
            _dict['discreteIntVal'] = self.discrete_int_val
        if hasattr(self, 'discreate_str_val') and self.discreate_str_val is not None:
            _dict['discreateStrVal'] = self.discreate_str_val
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['userDefined'] = self.user_defined
        if hasattr(self, 'fixed_val') and self.fixed_val is not None:
            _dict['fixedVal'] = self.fixed_val
        if hasattr(self, 'step') and self.step is not None:
            _dict['step'] = self.step
        if hasattr(self, 'power') and self.power is not None:
            _dict['power'] = self.power
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoHyperParameter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoHyperParameter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoHyperParameter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        One of Range, Discrete, Fix.
        """
        RANGE = 'range'
        DISCRETE = 'discrete'
        FIX = 'fix'


    class DataTypeEnum(str, Enum):
        """
        One of int, double, str.
        """
        INT = 'int'
        DOUBLE = 'double'
        STR = 'str'


class HpoMetric():
    """
    HpoMetric.

    :attr str name: (optional) Metric name.
    :attr float min: (optional) Minimal value of the metric.
    :attr float max: (optional) Maximal value of the metric.
    :attr float latest: (optional) Latest value of the metric.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 min: float = None,
                 max: float = None,
                 latest: float = None) -> None:
        """
        Initialize a HpoMetric object.

        :param str name: (optional) Metric name.
        :param float min: (optional) Minimal value of the metric.
        :param float max: (optional) Maximal value of the metric.
        :param float latest: (optional) Latest value of the metric.
        """
        self.name = name
        self.min = min
        self.max = max
        self.latest = latest

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoMetric':
        """Initialize a HpoMetric object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'min' in _dict:
            args['min'] = _dict.get('min')
        if 'max' in _dict:
            args['max'] = _dict.get('max')
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoMetric object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'min') and self.min is not None:
            _dict['min'] = self.min
        if hasattr(self, 'max') and self.max is not None:
            _dict['max'] = self.max
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoMetric object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoMetric') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoMetric') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HpoTaskDetail():
    """
    HpoTaskDetail.

    :attr HpoTaskInput input: (optional)
    :attr SearchGrid search_grid: (optional)
    :attr str state: (optional) The tuning status.
    :attr str creator: (optional) The user who created the tuning task.
    :attr str createtime: (optional) The time the tuning task was created.
    :attr str sig_id: (optional) Spark instance group id.
    :attr str sig_name: (optional) Spark instance group name.
    :attr str consumer_name: (optional) consumer name.
    """

    def __init__(self,
                 *,
                 input: 'HpoTaskInput' = None,
                 search_grid: 'SearchGrid' = None,
                 state: str = None,
                 creator: str = None,
                 createtime: str = None,
                 sig_id: str = None,
                 sig_name: str = None,
                 consumer_name: str = None) -> None:
        """
        Initialize a HpoTaskDetail object.

        :param HpoTaskInput input: (optional)
        :param SearchGrid search_grid: (optional)
        :param str state: (optional) The tuning status.
        :param str creator: (optional) The user who created the tuning task.
        :param str createtime: (optional) The time the tuning task was created.
        :param str sig_id: (optional) Spark instance group id.
        :param str sig_name: (optional) Spark instance group name.
        :param str consumer_name: (optional) consumer name.
        """
        self.input = input
        self.search_grid = search_grid
        self.state = state
        self.creator = creator
        self.createtime = createtime
        self.sig_id = sig_id
        self.sig_name = sig_name
        self.consumer_name = consumer_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoTaskDetail':
        """Initialize a HpoTaskDetail object from a json dictionary."""
        args = {}
        if 'input' in _dict:
            args['input'] = HpoTaskInput.from_dict(_dict.get('input'))
        if 'searchGrid' in _dict:
            args['search_grid'] = SearchGrid.from_dict(_dict.get('searchGrid'))
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'creator' in _dict:
            args['creator'] = _dict.get('creator')
        if 'createtime' in _dict:
            args['createtime'] = _dict.get('createtime')
        if 'sigId' in _dict:
            args['sig_id'] = _dict.get('sigId')
        if 'sigName' in _dict:
            args['sig_name'] = _dict.get('sigName')
        if 'consumerName' in _dict:
            args['consumer_name'] = _dict.get('consumerName')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoTaskDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input.to_dict()
        if hasattr(self, 'search_grid') and self.search_grid is not None:
            _dict['searchGrid'] = self.search_grid.to_dict()
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'creator') and self.creator is not None:
            _dict['creator'] = self.creator
        if hasattr(self, 'createtime') and self.createtime is not None:
            _dict['createtime'] = self.createtime
        if hasattr(self, 'sig_id') and self.sig_id is not None:
            _dict['sigId'] = self.sig_id
        if hasattr(self, 'sig_name') and self.sig_name is not None:
            _dict['sigName'] = self.sig_name
        if hasattr(self, 'consumer_name') and self.consumer_name is not None:
            _dict['consumerName'] = self.consumer_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoTaskDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoTaskDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoTaskDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HpoTaskInput():
    """
    HpoTaskInput.

    :attr str model_name: The deep learning model name.
    :attr str hpo_name: The deep learning tuning name.
    :attr List[HpoHyperParameter] hyper_params: (optional) The deep learning tuning
          hyperparameters.
    :attr ResDef res_def: The deep learning tuning resource definition.
    :attr AlgoDef algo_def: algorithm definition.
    :attr List[SearchExperiment] experiments: (optional) Only valid for
          ExperimentGridSearch algorithm which will submit train with this list of
          experiments.
    """

    def __init__(self,
                 model_name: str,
                 hpo_name: str,
                 res_def: 'ResDef',
                 algo_def: 'AlgoDef',
                 *,
                 hyper_params: List['HpoHyperParameter'] = None,
                 experiments: List['SearchExperiment'] = None) -> None:
        """
        Initialize a HpoTaskInput object.

        :param str model_name: The deep learning model name.
        :param str hpo_name: The deep learning tuning name.
        :param ResDef res_def: The deep learning tuning resource definition.
        :param AlgoDef algo_def: algorithm definition.
        :param List[HpoHyperParameter] hyper_params: (optional) The deep learning
               tuning hyperparameters.
        :param List[SearchExperiment] experiments: (optional) Only valid for
               ExperimentGridSearch algorithm which will submit train with this list of
               experiments.
        """
        self.model_name = model_name
        self.hpo_name = hpo_name
        self.hyper_params = hyper_params
        self.res_def = res_def
        self.algo_def = algo_def
        self.experiments = experiments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoTaskInput':
        """Initialize a HpoTaskInput object from a json dictionary."""
        args = {}
        if 'modelName' in _dict:
            args['model_name'] = _dict.get('modelName')
        else:
            raise ValueError('Required property \'modelName\' not present in HpoTaskInput JSON')
        if 'hpoName' in _dict:
            args['hpo_name'] = _dict.get('hpoName')
        else:
            raise ValueError('Required property \'hpoName\' not present in HpoTaskInput JSON')
        if 'hyperParams' in _dict:
            args['hyper_params'] = [HpoHyperParameter.from_dict(x) for x in _dict.get('hyperParams')]
        if 'resDef' in _dict:
            args['res_def'] = ResDef.from_dict(_dict.get('resDef'))
        else:
            raise ValueError('Required property \'resDef\' not present in HpoTaskInput JSON')
        if 'algoDef' in _dict:
            args['algo_def'] = AlgoDef.from_dict(_dict.get('algoDef'))
        else:
            raise ValueError('Required property \'algoDef\' not present in HpoTaskInput JSON')
        if 'experiments' in _dict:
            args['experiments'] = [SearchExperiment.from_dict(x) for x in _dict.get('experiments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoTaskInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_name') and self.model_name is not None:
            _dict['modelName'] = self.model_name
        if hasattr(self, 'hpo_name') and self.hpo_name is not None:
            _dict['hpoName'] = self.hpo_name
        if hasattr(self, 'hyper_params') and self.hyper_params is not None:
            _dict['hyperParams'] = [x.to_dict() for x in self.hyper_params]
        if hasattr(self, 'res_def') and self.res_def is not None:
            _dict['resDef'] = self.res_def.to_dict()
        if hasattr(self, 'algo_def') and self.algo_def is not None:
            _dict['algoDef'] = self.algo_def.to_dict()
        if hasattr(self, 'experiments') and self.experiments is not None:
            _dict['experiments'] = [x.to_dict() for x in self.experiments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoTaskInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoTaskInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoTaskInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HpoTaskState():
    """
    HpoTaskState.

    :attr str hpo_name: (optional) The name of hyperparameter optimization(HPO)
          task.
    :attr str state: (optional) The state of HPO task.
    :attr str progress: (optional) The progress of HPO task.
    :attr str duration: (optional) The duration of HPO task.
    :attr str creator: (optional) The creator of HPO task.
    :attr str createtime: (optional) The create time of HPO task.
    :attr HpoExperiment best: (optional) The best hyper parameters of HPO.
    :attr List[HpoExperiment] experiments: (optional) All experiments of HPO.
    """

    def __init__(self,
                 *,
                 hpo_name: str = None,
                 state: str = None,
                 progress: str = None,
                 duration: str = None,
                 creator: str = None,
                 createtime: str = None,
                 best: 'HpoExperiment' = None,
                 experiments: List['HpoExperiment'] = None) -> None:
        """
        Initialize a HpoTaskState object.

        :param str hpo_name: (optional) The name of hyperparameter
               optimization(HPO) task.
        :param str state: (optional) The state of HPO task.
        :param str progress: (optional) The progress of HPO task.
        :param str duration: (optional) The duration of HPO task.
        :param str creator: (optional) The creator of HPO task.
        :param str createtime: (optional) The create time of HPO task.
        :param HpoExperiment best: (optional) The best hyper parameters of HPO.
        :param List[HpoExperiment] experiments: (optional) All experiments of HPO.
        """
        self.hpo_name = hpo_name
        self.state = state
        self.progress = progress
        self.duration = duration
        self.creator = creator
        self.createtime = createtime
        self.best = best
        self.experiments = experiments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HpoTaskState':
        """Initialize a HpoTaskState object from a json dictionary."""
        args = {}
        if 'hpoName' in _dict:
            args['hpo_name'] = _dict.get('hpoName')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'duration' in _dict:
            args['duration'] = _dict.get('duration')
        if 'creator' in _dict:
            args['creator'] = _dict.get('creator')
        if 'createtime' in _dict:
            args['createtime'] = _dict.get('createtime')
        if 'best' in _dict:
            args['best'] = HpoExperiment.from_dict(_dict.get('best'))
        if 'experiments' in _dict:
            args['experiments'] = [HpoExperiment.from_dict(x) for x in _dict.get('experiments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HpoTaskState object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hpo_name') and self.hpo_name is not None:
            _dict['hpoName'] = self.hpo_name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'creator') and self.creator is not None:
            _dict['creator'] = self.creator
        if hasattr(self, 'createtime') and self.createtime is not None:
            _dict['createtime'] = self.createtime
        if hasattr(self, 'best') and self.best is not None:
            _dict['best'] = self.best.to_dict()
        if hasattr(self, 'experiments') and self.experiments is not None:
            _dict['experiments'] = [x.to_dict() for x in self.experiments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HpoTaskState object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HpoTaskState') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HpoTaskState') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HyperParameter():
    """
    HyperParameter.

    :attr float learningrate: (optional) The learning rate hyperparameter.
    :attr float momentum: (optional) The momentum hyperparameter.
    :attr float weightdecay: (optional) The Caffe and PyTorch weight decay
          hyperparameter.
    :attr float decayrate: (optional) The TensorFlow learning rate decay
          hyperparameter.
    :attr float decaysteps: (optional) The TensorFlow decaysteps hyperparameter.
    :attr str staircase: (optional) The TensorFlow staircase hyperparameter.
    :attr int maxiteration: (optional) The Caffe and TensorFlow maximum iteration
          hyperparameter.
    :attr int epoch: (optional) The PyTorch maximum iteration hyperparameter.
    :attr str solvertype: (optional) The solver or optimizer type hyperparameter.
          "Cf" marks a valid parameter for Caffe, "TF" for TensorFlow, "PT" for PyTorch.
    :attr str lrpolicy: (optional) The learning rate policy. "Cf" marks a valid
          parameter for Caffe, and "TF" for TensorFlow.
    :attr int stepsize: (optional) The Caffe and PyTorch model stepsize
          hyperparameter.
    :attr str stepvalues: (optional) The Caffe model stepvalue hyperparameter, a
          list of step values separated by comma.
    :attr float gamma: (optional) The Caffe and PyTorch model gamma hyperparameter.
    :attr float power: (optional) The Caffe and TensorFlow model power
          hyperparameter.
    :attr bool cycle: (optional) The TensorFlow model power hyperparameter.
    :attr int hiddenstatesize: (optional) The TensorFlow LSTM model hidden state
          size hyperparameter.
    :attr float optdecay: (optional) The TensorFlow model optdecay hyperparameter.
    :attr float epsilon: (optional) The TensorFlow and PyTorch model epsilon
          hyperparameter.
    :attr float accumulator: (optional) The TensorFlow and PyTorch model accumulator
          hyperparameter.
    :attr float l1_regularization: (optional) The TensorFlow model l1_regularization
          hyperparameter.
    :attr float l2_regularization: (optional) The TensorFlow model l2_regularization
          hyperparameter.
    :attr float beta1: (optional) The TensorFlow model beta1 hyperparameter.
    :attr float beta2: (optional) The TensorFlow model beta2 hyperparameter.
    :attr float lr_power: (optional) The TensorFlow model lr_power hyperparameter.
    :attr float end_learning_rate: (optional) The TensorFlow model end_learning_rate
          hyperparameter.
    :attr float rho: (optional) The PyTorch model rho hyperparameter.
    :attr float lr_decay: (optional) The PyTorch model lr_decay hyperparameter.
    :attr bool amsgrad: (optional) The PyTorch model amsgrad hyperparameter.
    :attr float lambd: (optional) The PyTorch model lambd hyperparameter.
    :attr float alpha: (optional) The PyTorch model alpha hyperparameter.
    :attr float t0: (optional) The PyTorch model t0 hyperparameter.
    :attr bool centered: (optional) The PyTorch model centered hyperparameter.
    :attr float dampening: (optional) The PyTorch model dampening hyperparameter.
    :attr bool nesterov: (optional) The PyTorch model nesterov hyperparameter.
    :attr int t_max: (optional) The PyTorch model t_max hyperparameter.
    :attr float eta_min: (optional) The PyTorch model eta_min hyperparameter.
    :attr str mode: (optional) The PyTorch model mode hyperparameter, value is one
          of min, max.
    :attr float factor: (optional) The PyTorch model factor hyperparameter.
    :attr int patience: (optional) The PyTorch model patience hyperparameter.
    :attr float threshold: (optional) The PyTorch model threshold hyperparameter.
    :attr str threshold_mode: (optional) The PyTorch model threshold_mode
          hyperparameter, value is one of rel, abs.
    :attr int cooldown: (optional) The PyTorch model cooldown hyperparameter.
    :attr float eps: (optional) The PyTorch model eps hyperparameter.
    """

    def __init__(self,
                 *,
                 learningrate: float = None,
                 momentum: float = None,
                 weightdecay: float = None,
                 decayrate: float = None,
                 decaysteps: float = None,
                 staircase: str = None,
                 maxiteration: int = None,
                 epoch: int = None,
                 solvertype: str = None,
                 lrpolicy: str = None,
                 stepsize: int = None,
                 stepvalues: str = None,
                 gamma: float = None,
                 power: float = None,
                 cycle: bool = None,
                 hiddenstatesize: int = None,
                 optdecay: float = None,
                 epsilon: float = None,
                 accumulator: float = None,
                 l1_regularization: float = None,
                 l2_regularization: float = None,
                 beta1: float = None,
                 beta2: float = None,
                 lr_power: float = None,
                 end_learning_rate: float = None,
                 rho: float = None,
                 lr_decay: float = None,
                 amsgrad: bool = None,
                 lambd: float = None,
                 alpha: float = None,
                 t0: float = None,
                 centered: bool = None,
                 dampening: float = None,
                 nesterov: bool = None,
                 t_max: int = None,
                 eta_min: float = None,
                 mode: str = None,
                 factor: float = None,
                 patience: int = None,
                 threshold: float = None,
                 threshold_mode: str = None,
                 cooldown: int = None,
                 eps: float = None) -> None:
        """
        Initialize a HyperParameter object.

        :param float learningrate: (optional) The learning rate hyperparameter.
        :param float momentum: (optional) The momentum hyperparameter.
        :param float weightdecay: (optional) The Caffe and PyTorch weight decay
               hyperparameter.
        :param float decayrate: (optional) The TensorFlow learning rate decay
               hyperparameter.
        :param float decaysteps: (optional) The TensorFlow decaysteps
               hyperparameter.
        :param str staircase: (optional) The TensorFlow staircase hyperparameter.
        :param int maxiteration: (optional) The Caffe and TensorFlow maximum
               iteration hyperparameter.
        :param int epoch: (optional) The PyTorch maximum iteration hyperparameter.
        :param str solvertype: (optional) The solver or optimizer type
               hyperparameter. "Cf" marks a valid parameter for Caffe, "TF" for
               TensorFlow, "PT" for PyTorch.
        :param str lrpolicy: (optional) The learning rate policy. "Cf" marks a
               valid parameter for Caffe, and "TF" for TensorFlow.
        :param int stepsize: (optional) The Caffe and PyTorch model stepsize
               hyperparameter.
        :param str stepvalues: (optional) The Caffe model stepvalue hyperparameter,
               a list of step values separated by comma.
        :param float gamma: (optional) The Caffe and PyTorch model gamma
               hyperparameter.
        :param float power: (optional) The Caffe and TensorFlow model power
               hyperparameter.
        :param bool cycle: (optional) The TensorFlow model power hyperparameter.
        :param int hiddenstatesize: (optional) The TensorFlow LSTM model hidden
               state size hyperparameter.
        :param float optdecay: (optional) The TensorFlow model optdecay
               hyperparameter.
        :param float epsilon: (optional) The TensorFlow and PyTorch model epsilon
               hyperparameter.
        :param float accumulator: (optional) The TensorFlow and PyTorch model
               accumulator hyperparameter.
        :param float l1_regularization: (optional) The TensorFlow model
               l1_regularization hyperparameter.
        :param float l2_regularization: (optional) The TensorFlow model
               l2_regularization hyperparameter.
        :param float beta1: (optional) The TensorFlow model beta1 hyperparameter.
        :param float beta2: (optional) The TensorFlow model beta2 hyperparameter.
        :param float lr_power: (optional) The TensorFlow model lr_power
               hyperparameter.
        :param float end_learning_rate: (optional) The TensorFlow model
               end_learning_rate hyperparameter.
        :param float rho: (optional) The PyTorch model rho hyperparameter.
        :param float lr_decay: (optional) The PyTorch model lr_decay
               hyperparameter.
        :param bool amsgrad: (optional) The PyTorch model amsgrad hyperparameter.
        :param float lambd: (optional) The PyTorch model lambd hyperparameter.
        :param float alpha: (optional) The PyTorch model alpha hyperparameter.
        :param float t0: (optional) The PyTorch model t0 hyperparameter.
        :param bool centered: (optional) The PyTorch model centered hyperparameter.
        :param float dampening: (optional) The PyTorch model dampening
               hyperparameter.
        :param bool nesterov: (optional) The PyTorch model nesterov hyperparameter.
        :param int t_max: (optional) The PyTorch model t_max hyperparameter.
        :param float eta_min: (optional) The PyTorch model eta_min hyperparameter.
        :param str mode: (optional) The PyTorch model mode hyperparameter, value is
               one of min, max.
        :param float factor: (optional) The PyTorch model factor hyperparameter.
        :param int patience: (optional) The PyTorch model patience hyperparameter.
        :param float threshold: (optional) The PyTorch model threshold
               hyperparameter.
        :param str threshold_mode: (optional) The PyTorch model threshold_mode
               hyperparameter, value is one of rel, abs.
        :param int cooldown: (optional) The PyTorch model cooldown hyperparameter.
        :param float eps: (optional) The PyTorch model eps hyperparameter.
        """
        self.learningrate = learningrate
        self.momentum = momentum
        self.weightdecay = weightdecay
        self.decayrate = decayrate
        self.decaysteps = decaysteps
        self.staircase = staircase
        self.maxiteration = maxiteration
        self.epoch = epoch
        self.solvertype = solvertype
        self.lrpolicy = lrpolicy
        self.stepsize = stepsize
        self.stepvalues = stepvalues
        self.gamma = gamma
        self.power = power
        self.cycle = cycle
        self.hiddenstatesize = hiddenstatesize
        self.optdecay = optdecay
        self.epsilon = epsilon
        self.accumulator = accumulator
        self.l1_regularization = l1_regularization
        self.l2_regularization = l2_regularization
        self.beta1 = beta1
        self.beta2 = beta2
        self.lr_power = lr_power
        self.end_learning_rate = end_learning_rate
        self.rho = rho
        self.lr_decay = lr_decay
        self.amsgrad = amsgrad
        self.lambd = lambd
        self.alpha = alpha
        self.t0 = t0
        self.centered = centered
        self.dampening = dampening
        self.nesterov = nesterov
        self.t_max = t_max
        self.eta_min = eta_min
        self.mode = mode
        self.factor = factor
        self.patience = patience
        self.threshold = threshold
        self.threshold_mode = threshold_mode
        self.cooldown = cooldown
        self.eps = eps

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HyperParameter':
        """Initialize a HyperParameter object from a json dictionary."""
        args = {}
        if 'learningrate' in _dict:
            args['learningrate'] = _dict.get('learningrate')
        if 'momentum' in _dict:
            args['momentum'] = _dict.get('momentum')
        if 'weightdecay' in _dict:
            args['weightdecay'] = _dict.get('weightdecay')
        if 'decayrate' in _dict:
            args['decayrate'] = _dict.get('decayrate')
        if 'decaysteps' in _dict:
            args['decaysteps'] = _dict.get('decaysteps')
        if 'staircase' in _dict:
            args['staircase'] = _dict.get('staircase')
        if 'maxiteration' in _dict:
            args['maxiteration'] = _dict.get('maxiteration')
        if 'epoch' in _dict:
            args['epoch'] = _dict.get('epoch')
        if 'solvertype' in _dict:
            args['solvertype'] = _dict.get('solvertype')
        if 'lrpolicy' in _dict:
            args['lrpolicy'] = _dict.get('lrpolicy')
        if 'stepsize' in _dict:
            args['stepsize'] = _dict.get('stepsize')
        if 'stepvalues' in _dict:
            args['stepvalues'] = _dict.get('stepvalues')
        if 'gamma' in _dict:
            args['gamma'] = _dict.get('gamma')
        if 'power' in _dict:
            args['power'] = _dict.get('power')
        if 'cycle' in _dict:
            args['cycle'] = _dict.get('cycle')
        if 'hiddenstatesize' in _dict:
            args['hiddenstatesize'] = _dict.get('hiddenstatesize')
        if 'optdecay' in _dict:
            args['optdecay'] = _dict.get('optdecay')
        if 'epsilon' in _dict:
            args['epsilon'] = _dict.get('epsilon')
        if 'accumulator' in _dict:
            args['accumulator'] = _dict.get('accumulator')
        if 'l1_regularization' in _dict:
            args['l1_regularization'] = _dict.get('l1_regularization')
        if 'l2_regularization' in _dict:
            args['l2_regularization'] = _dict.get('l2_regularization')
        if 'beta1' in _dict:
            args['beta1'] = _dict.get('beta1')
        if 'beta2' in _dict:
            args['beta2'] = _dict.get('beta2')
        if 'lr_power' in _dict:
            args['lr_power'] = _dict.get('lr_power')
        if 'end_learning_rate' in _dict:
            args['end_learning_rate'] = _dict.get('end_learning_rate')
        if 'rho' in _dict:
            args['rho'] = _dict.get('rho')
        if 'lr_decay' in _dict:
            args['lr_decay'] = _dict.get('lr_decay')
        if 'amsgrad' in _dict:
            args['amsgrad'] = _dict.get('amsgrad')
        if 'lambd' in _dict:
            args['lambd'] = _dict.get('lambd')
        if 'alpha' in _dict:
            args['alpha'] = _dict.get('alpha')
        if 't0' in _dict:
            args['t0'] = _dict.get('t0')
        if 'centered' in _dict:
            args['centered'] = _dict.get('centered')
        if 'dampening' in _dict:
            args['dampening'] = _dict.get('dampening')
        if 'nesterov' in _dict:
            args['nesterov'] = _dict.get('nesterov')
        if 't_max' in _dict:
            args['t_max'] = _dict.get('t_max')
        if 'eta_min' in _dict:
            args['eta_min'] = _dict.get('eta_min')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        if 'factor' in _dict:
            args['factor'] = _dict.get('factor')
        if 'patience' in _dict:
            args['patience'] = _dict.get('patience')
        if 'threshold' in _dict:
            args['threshold'] = _dict.get('threshold')
        if 'threshold_mode' in _dict:
            args['threshold_mode'] = _dict.get('threshold_mode')
        if 'cooldown' in _dict:
            args['cooldown'] = _dict.get('cooldown')
        if 'eps' in _dict:
            args['eps'] = _dict.get('eps')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HyperParameter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'learningrate') and self.learningrate is not None:
            _dict['learningrate'] = self.learningrate
        if hasattr(self, 'momentum') and self.momentum is not None:
            _dict['momentum'] = self.momentum
        if hasattr(self, 'weightdecay') and self.weightdecay is not None:
            _dict['weightdecay'] = self.weightdecay
        if hasattr(self, 'decayrate') and self.decayrate is not None:
            _dict['decayrate'] = self.decayrate
        if hasattr(self, 'decaysteps') and self.decaysteps is not None:
            _dict['decaysteps'] = self.decaysteps
        if hasattr(self, 'staircase') and self.staircase is not None:
            _dict['staircase'] = self.staircase
        if hasattr(self, 'maxiteration') and self.maxiteration is not None:
            _dict['maxiteration'] = self.maxiteration
        if hasattr(self, 'epoch') and self.epoch is not None:
            _dict['epoch'] = self.epoch
        if hasattr(self, 'solvertype') and self.solvertype is not None:
            _dict['solvertype'] = self.solvertype
        if hasattr(self, 'lrpolicy') and self.lrpolicy is not None:
            _dict['lrpolicy'] = self.lrpolicy
        if hasattr(self, 'stepsize') and self.stepsize is not None:
            _dict['stepsize'] = self.stepsize
        if hasattr(self, 'stepvalues') and self.stepvalues is not None:
            _dict['stepvalues'] = self.stepvalues
        if hasattr(self, 'gamma') and self.gamma is not None:
            _dict['gamma'] = self.gamma
        if hasattr(self, 'power') and self.power is not None:
            _dict['power'] = self.power
        if hasattr(self, 'cycle') and self.cycle is not None:
            _dict['cycle'] = self.cycle
        if hasattr(self, 'hiddenstatesize') and self.hiddenstatesize is not None:
            _dict['hiddenstatesize'] = self.hiddenstatesize
        if hasattr(self, 'optdecay') and self.optdecay is not None:
            _dict['optdecay'] = self.optdecay
        if hasattr(self, 'epsilon') and self.epsilon is not None:
            _dict['epsilon'] = self.epsilon
        if hasattr(self, 'accumulator') and self.accumulator is not None:
            _dict['accumulator'] = self.accumulator
        if hasattr(self, 'l1_regularization') and self.l1_regularization is not None:
            _dict['l1_regularization'] = self.l1_regularization
        if hasattr(self, 'l2_regularization') and self.l2_regularization is not None:
            _dict['l2_regularization'] = self.l2_regularization
        if hasattr(self, 'beta1') and self.beta1 is not None:
            _dict['beta1'] = self.beta1
        if hasattr(self, 'beta2') and self.beta2 is not None:
            _dict['beta2'] = self.beta2
        if hasattr(self, 'lr_power') and self.lr_power is not None:
            _dict['lr_power'] = self.lr_power
        if hasattr(self, 'end_learning_rate') and self.end_learning_rate is not None:
            _dict['end_learning_rate'] = self.end_learning_rate
        if hasattr(self, 'rho') and self.rho is not None:
            _dict['rho'] = self.rho
        if hasattr(self, 'lr_decay') and self.lr_decay is not None:
            _dict['lr_decay'] = self.lr_decay
        if hasattr(self, 'amsgrad') and self.amsgrad is not None:
            _dict['amsgrad'] = self.amsgrad
        if hasattr(self, 'lambd') and self.lambd is not None:
            _dict['lambd'] = self.lambd
        if hasattr(self, 'alpha') and self.alpha is not None:
            _dict['alpha'] = self.alpha
        if hasattr(self, 't0') and self.t0 is not None:
            _dict['t0'] = self.t0
        if hasattr(self, 'centered') and self.centered is not None:
            _dict['centered'] = self.centered
        if hasattr(self, 'dampening') and self.dampening is not None:
            _dict['dampening'] = self.dampening
        if hasattr(self, 'nesterov') and self.nesterov is not None:
            _dict['nesterov'] = self.nesterov
        if hasattr(self, 't_max') and self.t_max is not None:
            _dict['t_max'] = self.t_max
        if hasattr(self, 'eta_min') and self.eta_min is not None:
            _dict['eta_min'] = self.eta_min
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'factor') and self.factor is not None:
            _dict['factor'] = self.factor
        if hasattr(self, 'patience') and self.patience is not None:
            _dict['patience'] = self.patience
        if hasattr(self, 'threshold') and self.threshold is not None:
            _dict['threshold'] = self.threshold
        if hasattr(self, 'threshold_mode') and self.threshold_mode is not None:
            _dict['threshold_mode'] = self.threshold_mode
        if hasattr(self, 'cooldown') and self.cooldown is not None:
            _dict['cooldown'] = self.cooldown
        if hasattr(self, 'eps') and self.eps is not None:
            _dict['eps'] = self.eps
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HyperParameter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HyperParameter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HyperParameter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SolvertypeEnum(str, Enum):
        """
        The solver or optimizer type hyperparameter. "Cf" marks a valid parameter for
        Caffe, "TF" for TensorFlow, "PT" for PyTorch.
        """
        ADAGRAD_CF = 'AdaGrad (Cf)'
        ADADELTA_CF = 'AdaDelta (Cf)'
        ADAM_CF_TF_AND_PT = 'Adam (Cf, TF and PT)'
        MOMENTUM_TF = 'Momentum (TF)'
        RMSPROP_CF_TF_AND_PT = 'RMSProp (Cf, TF and PT)'
        SGD_CF_AND_PT = 'SGD (Cf and PT)'
        ASGD_PT = 'ASGD (PT)'
        NESTEROV_CF = 'Nesterov (Cf)'
        GRADIENTDESCENT_TF = 'GradientDescent (TF)'
        ADADELTA_TF_AND_PT = 'Adadelta (TF and PT)'
        ADAGRAD_TF_AND_PT = 'Adagrad (TF and PT)'
        ADAGRADDA_TF = 'AdagradDA (TF)'
        FTRL_TF = 'Ftrl (TF)'
        SPARSEADAM_PT = 'SparseAdam (PT)'
        ADAMAX_PT = 'Adamax (PT)'
        RPROP_PT = 'Rprop (PT)'
        PROXIMALGRADIENTDESCENT_TF = 'ProximalGradientDescent (TF)'
        PROXIMALADAGRAD_TF = 'ProximalAdagrad (TF)'


    class LrpolicyEnum(str, Enum):
        """
        The learning rate policy. "Cf" marks a valid parameter for Caffe, and "TF" for
        TensorFlow.
        """
        FIXED_CF_TF_AND_PT = 'fixed (Cf, TF and PT)'
        STEP_CF_AND_PT = 'step (Cf and PT)'
        MULTISTEP_CF_AND_PT = 'multistep (Cf and PT)'
        EXP_CF = 'exp (Cf)'
        INV_CF = 'inv (Cf)'
        POLY_CF = 'poly (Cf)'
        SIGMOID_CF = 'sigmoid (Cf)'
        EXPONENTIAL_TF_AND_PT = 'exponential (TF and PT)'
        INVERSETIME_TF = 'inversetime (TF)'
        NATURALEXP_TF = 'naturalexp (TF)'
        PIECEWISE_TF = 'piecewise (TF)'
        POLYNOMIAL_TF = 'polynomial (TF)'
        COSINEANNEALING_PT = 'cosineannealing (PT)'
        REDUCELRONPLATEAU_PT = 'reducelronplateau (PT)'


class IaSInstanceParam():
    """
    IaSInstanceParam.

    :attr str name: The name for Elastic Distributed Inference model.
    :attr str state: (optional) The state for Elastic Distributed Inference model.
    :attr Instance instance: (optional)
    """

    def __init__(self,
                 name: str,
                 *,
                 state: str = None,
                 instance: 'Instance' = None) -> None:
        """
        Initialize a IaSInstanceParam object.

        :param str name: The name for Elastic Distributed Inference model.
        :param str state: (optional) The state for Elastic Distributed Inference
               model.
        :param Instance instance: (optional)
        """
        self.name = name
        self.state = state
        self.instance = instance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IaSInstanceParam':
        """Initialize a IaSInstanceParam object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in IaSInstanceParam JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'instance' in _dict:
            args['instance'] = Instance.from_dict(_dict.get('instance'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IaSInstanceParam object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'instance') and self.instance is not None:
            _dict['instance'] = self.instance.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IaSInstanceParam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IaSInstanceParam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IaSInstanceParam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IaSModelDescription():
    """
    IaSModelDescription.

    :attr str schema_version: (optional) The version of Elastic Distributed
          Inference model.
    :attr str name: The name of the Elastic Distributed Inference model.
    :attr str tag: (optional) The tag of the Elastic Distributed Inference model.
    :attr str weight_path: (optional) The model weight which used for inference.
    :attr str model_path: (optional) The inference model path.
    :attr str creator: (optional) The creator of the Elastic Distributed Inference
          model.
    :attr str runtime: (optional) The runtime of Elastic Distributed Inference
          model.
    :attr str kernel_path: (optional) The execution kernel for inference model.
    :attr str mk_resource_req: (optional) The kernel resource request of the Elastic
          Distributed Inference model.
    :attr str mk_umask: (optional) The kernel umask of Elastic Distributed Inference
          model.
    :attr List[Attr] attributes: (optional) Key-value of attributes can be accessed
          in model kernel.
    :attr List[Envs] mk_environments: (optional) Additional environment variables to
          run model kernel.
    :attr str service_uri: (optional) Rest Service URL.
    :attr int size: (optional) The size of the Elastic Distributed Inference model.
    :attr int mk_instance_min: (optional) The minimal number of instance.
    :attr int mk_instance_max: (optional) The maximal number of instance.
    :attr str create_time: (optional) The create time of the Elastic Distributed
          Inference model.
    :attr str last_update_time: (optional) The last update time of the Elastic
          Distributed Inference model.
    :attr str state: (optional) The state of Elastic Distributed Inference model.
    """

    def __init__(self,
                 name: str,
                 *,
                 schema_version: str = None,
                 tag: str = None,
                 weight_path: str = None,
                 model_path: str = None,
                 creator: str = None,
                 runtime: str = None,
                 kernel_path: str = None,
                 mk_resource_req: str = None,
                 mk_umask: str = None,
                 attributes: List['Attr'] = None,
                 mk_environments: List['Envs'] = None,
                 service_uri: str = None,
                 size: int = None,
                 mk_instance_min: int = None,
                 mk_instance_max: int = None,
                 create_time: str = None,
                 last_update_time: str = None,
                 state: str = None) -> None:
        """
        Initialize a IaSModelDescription object.

        :param str name: The name of the Elastic Distributed Inference model.
        :param str schema_version: (optional) The version of Elastic Distributed
               Inference model.
        :param str tag: (optional) The tag of the Elastic Distributed Inference
               model.
        :param str weight_path: (optional) The model weight which used for
               inference.
        :param str model_path: (optional) The inference model path.
        :param str creator: (optional) The creator of the Elastic Distributed
               Inference model.
        :param str runtime: (optional) The runtime of Elastic Distributed Inference
               model.
        :param str kernel_path: (optional) The execution kernel for inference
               model.
        :param str mk_resource_req: (optional) The kernel resource request of the
               Elastic Distributed Inference model.
        :param str mk_umask: (optional) The kernel umask of Elastic Distributed
               Inference model.
        :param List[Attr] attributes: (optional) Key-value of attributes can be
               accessed in model kernel.
        :param List[Envs] mk_environments: (optional) Additional environment
               variables to run model kernel.
        :param str service_uri: (optional) Rest Service URL.
        :param int size: (optional) The size of the Elastic Distributed Inference
               model.
        :param int mk_instance_min: (optional) The minimal number of instance.
        :param int mk_instance_max: (optional) The maximal number of instance.
        :param str create_time: (optional) The create time of the Elastic
               Distributed Inference model.
        :param str last_update_time: (optional) The last update time of the Elastic
               Distributed Inference model.
        :param str state: (optional) The state of Elastic Distributed Inference
               model.
        """
        self.schema_version = schema_version
        self.name = name
        self.tag = tag
        self.weight_path = weight_path
        self.model_path = model_path
        self.creator = creator
        self.runtime = runtime
        self.kernel_path = kernel_path
        self.mk_resource_req = mk_resource_req
        self.mk_umask = mk_umask
        self.attributes = attributes
        self.mk_environments = mk_environments
        self.service_uri = service_uri
        self.size = size
        self.mk_instance_min = mk_instance_min
        self.mk_instance_max = mk_instance_max
        self.create_time = create_time
        self.last_update_time = last_update_time
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IaSModelDescription':
        """Initialize a IaSModelDescription object from a json dictionary."""
        args = {}
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in IaSModelDescription JSON')
        if 'tag' in _dict:
            args['tag'] = _dict.get('tag')
        if 'weight_path' in _dict:
            args['weight_path'] = _dict.get('weight_path')
        if 'model_path' in _dict:
            args['model_path'] = _dict.get('model_path')
        if 'creator' in _dict:
            args['creator'] = _dict.get('creator')
        if 'runtime' in _dict:
            args['runtime'] = _dict.get('runtime')
        if 'kernel_path' in _dict:
            args['kernel_path'] = _dict.get('kernel_path')
        if 'mk_resource_req' in _dict:
            args['mk_resource_req'] = _dict.get('mk_resource_req')
        if 'mk_umask' in _dict:
            args['mk_umask'] = _dict.get('mk_umask')
        if 'attributes' in _dict:
            args['attributes'] = [Attr.from_dict(x) for x in _dict.get('attributes')]
        if 'mk_environments' in _dict:
            args['mk_environments'] = [Envs.from_dict(x) for x in _dict.get('mk_environments')]
        if 'service_uri' in _dict:
            args['service_uri'] = _dict.get('service_uri')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'mk_instance_min' in _dict:
            args['mk_instance_min'] = _dict.get('mk_instance_min')
        if 'mk_instance_max' in _dict:
            args['mk_instance_max'] = _dict.get('mk_instance_max')
        if 'create_time' in _dict:
            args['create_time'] = _dict.get('create_time')
        if 'last_update_time' in _dict:
            args['last_update_time'] = _dict.get('last_update_time')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IaSModelDescription object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tag') and self.tag is not None:
            _dict['tag'] = self.tag
        if hasattr(self, 'weight_path') and self.weight_path is not None:
            _dict['weight_path'] = self.weight_path
        if hasattr(self, 'model_path') and self.model_path is not None:
            _dict['model_path'] = self.model_path
        if hasattr(self, 'creator') and self.creator is not None:
            _dict['creator'] = self.creator
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime
        if hasattr(self, 'kernel_path') and self.kernel_path is not None:
            _dict['kernel_path'] = self.kernel_path
        if hasattr(self, 'mk_resource_req') and self.mk_resource_req is not None:
            _dict['mk_resource_req'] = self.mk_resource_req
        if hasattr(self, 'mk_umask') and self.mk_umask is not None:
            _dict['mk_umask'] = self.mk_umask
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x.to_dict() for x in self.attributes]
        if hasattr(self, 'mk_environments') and self.mk_environments is not None:
            _dict['mk_environments'] = [x.to_dict() for x in self.mk_environments]
        if hasattr(self, 'service_uri') and self.service_uri is not None:
            _dict['service_uri'] = self.service_uri
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'mk_instance_min') and self.mk_instance_min is not None:
            _dict['mk_instance_min'] = self.mk_instance_min
        if hasattr(self, 'mk_instance_max') and self.mk_instance_max is not None:
            _dict['mk_instance_max'] = self.mk_instance_max
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = self.create_time
        if hasattr(self, 'last_update_time') and self.last_update_time is not None:
            _dict['last_update_time'] = self.last_update_time
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IaSModelDescription object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IaSModelDescription') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IaSModelDescription') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IaSProfileParam():
    """
    IaSProfileParam.

    :attr str name: The name for Elastic Distributed Inference model.
    :attr str create_time: (optional) The create time for Elastic Distributed
          Inference model.
    :attr str update_time: (optional) The update time for Elastic Distributed
          Inference model.
    :attr int replica: (optional) The replication number for inference model
          instance.
    :attr str type: (optional) The type for Elastic Distributed Inference model.
    :attr str schema_version: (optional) The schema version for Elastic Distributed
          Inference model.
    :attr Policy policy: (optional)
    :attr Kernel kernel: (optional)
    :attr ResourceAllocation resource_allocation: (optional)
    :attr List[Envs] envs: (optional) Additional environment variables to run model
          kernel.
    """

    def __init__(self,
                 name: str,
                 *,
                 create_time: str = None,
                 update_time: str = None,
                 replica: int = None,
                 type: str = None,
                 schema_version: str = None,
                 policy: 'Policy' = None,
                 kernel: 'Kernel' = None,
                 resource_allocation: 'ResourceAllocation' = None,
                 envs: List['Envs'] = None) -> None:
        """
        Initialize a IaSProfileParam object.

        :param str name: The name for Elastic Distributed Inference model.
        :param str create_time: (optional) The create time for Elastic Distributed
               Inference model.
        :param str update_time: (optional) The update time for Elastic Distributed
               Inference model.
        :param int replica: (optional) The replication number for inference model
               instance.
        :param str type: (optional) The type for Elastic Distributed Inference
               model.
        :param str schema_version: (optional) The schema version for Elastic
               Distributed Inference model.
        :param Policy policy: (optional)
        :param Kernel kernel: (optional)
        :param ResourceAllocation resource_allocation: (optional)
        :param List[Envs] envs: (optional) Additional environment variables to run
               model kernel.
        """
        self.name = name
        self.create_time = create_time
        self.update_time = update_time
        self.replica = replica
        self.type = type
        self.schema_version = schema_version
        self.policy = policy
        self.kernel = kernel
        self.resource_allocation = resource_allocation
        self.envs = envs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IaSProfileParam':
        """Initialize a IaSProfileParam object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in IaSProfileParam JSON')
        if 'create_time' in _dict:
            args['create_time'] = _dict.get('create_time')
        if 'update_time' in _dict:
            args['update_time'] = _dict.get('update_time')
        if 'replica' in _dict:
            args['replica'] = _dict.get('replica')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        if 'policy' in _dict:
            args['policy'] = Policy.from_dict(_dict.get('policy'))
        if 'kernel' in _dict:
            args['kernel'] = Kernel.from_dict(_dict.get('kernel'))
        if 'resource_allocation' in _dict:
            args['resource_allocation'] = ResourceAllocation.from_dict(_dict.get('resource_allocation'))
        if 'envs' in _dict:
            args['envs'] = [Envs.from_dict(x) for x in _dict.get('envs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IaSProfileParam object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = self.create_time
        if hasattr(self, 'update_time') and self.update_time is not None:
            _dict['update_time'] = self.update_time
        if hasattr(self, 'replica') and self.replica is not None:
            _dict['replica'] = self.replica
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'policy') and self.policy is not None:
            _dict['policy'] = self.policy.to_dict()
        if hasattr(self, 'kernel') and self.kernel is not None:
            _dict['kernel'] = self.kernel.to_dict()
        if hasattr(self, 'resource_allocation') and self.resource_allocation is not None:
            _dict['resource_allocation'] = self.resource_allocation.to_dict()
        if hasattr(self, 'envs') and self.envs is not None:
            _dict['envs'] = [x.to_dict() for x in self.envs]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IaSProfileParam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IaSProfileParam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IaSProfileParam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IaSReadmeParam():
    """
    IaSReadmeParam.

    :attr str readme: (optional) The readme for Elastic Distributed Inference model.
    """

    def __init__(self,
                 *,
                 readme: str = None) -> None:
        """
        Initialize a IaSReadmeParam object.

        :param str readme: (optional) The readme for Elastic Distributed Inference
               model.
        """
        self.readme = readme

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IaSReadmeParam':
        """Initialize a IaSReadmeParam object from a json dictionary."""
        args = {}
        if 'readme' in _dict:
            args['readme'] = _dict.get('readme')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IaSReadmeParam object from a json dictionary."""
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
        """Return a `str` version of this IaSReadmeParam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IaSReadmeParam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IaSReadmeParam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IaSTestResultParam():
    """
    IaSTestResultParam.

    :attr str model_name: (optional) The name of inference model.
    :attr bool reslove: (optional) Whether or not the inference result can be
          resolved.
    :attr str other: (optional) Return value for inference result can not be
          resolved.
    :attr List[PredictResult] results: (optional) The result for the inference.
    """

    def __init__(self,
                 *,
                 model_name: str = None,
                 reslove: bool = None,
                 other: str = None,
                 results: List['PredictResult'] = None) -> None:
        """
        Initialize a IaSTestResultParam object.

        :param str model_name: (optional) The name of inference model.
        :param bool reslove: (optional) Whether or not the inference result can be
               resolved.
        :param str other: (optional) Return value for inference result can not be
               resolved.
        :param List[PredictResult] results: (optional) The result for the
               inference.
        """
        self.model_name = model_name
        self.reslove = reslove
        self.other = other
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IaSTestResultParam':
        """Initialize a IaSTestResultParam object from a json dictionary."""
        args = {}
        if 'modelName' in _dict:
            args['model_name'] = _dict.get('modelName')
        if 'reslove' in _dict:
            args['reslove'] = _dict.get('reslove')
        if 'other' in _dict:
            args['other'] = _dict.get('other')
        if 'results' in _dict:
            args['results'] = [PredictResult.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IaSTestResultParam object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_name') and self.model_name is not None:
            _dict['modelName'] = self.model_name
        if hasattr(self, 'reslove') and self.reslove is not None:
            _dict['reslove'] = self.reslove
        if hasattr(self, 'other') and self.other is not None:
            _dict['other'] = self.other
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IaSTestResultParam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IaSTestResultParam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IaSTestResultParam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageDetail():
    """
    ImageDetail.

    :attr bool isusingtext: (optional) Whether using text or not.
    :attr str traintextpath: (optional) The train text path.
    :attr str valtextpath: (optional) The validation text path.
    :attr str testtextpath: (optional) The test text path.
    :attr str labeltextpath: (optional) The label text path.
    :attr str trainimagepath: (optional) The train image path.
    :attr str valimagepath: (optional) The validation image path.
    :attr str testimagepath: (optional) The test image path.
    :attr str imagetype: (optional) The image type.
    :attr int height: (optional) The height of the image.
    :attr int width: (optional) The width of the image.
    :attr str resizetransformation: (optional) The resize transformation.
    :attr int valpercentage: (optional) The percentage for validation.
    :attr int testpercentage: (optional) The percentage for test.
    :attr str splitalgorithm: (optional) The algorithm for splitting images.
    """

    def __init__(self,
                 *,
                 isusingtext: bool = None,
                 traintextpath: str = None,
                 valtextpath: str = None,
                 testtextpath: str = None,
                 labeltextpath: str = None,
                 trainimagepath: str = None,
                 valimagepath: str = None,
                 testimagepath: str = None,
                 imagetype: str = None,
                 height: int = None,
                 width: int = None,
                 resizetransformation: str = None,
                 valpercentage: int = None,
                 testpercentage: int = None,
                 splitalgorithm: str = None) -> None:
        """
        Initialize a ImageDetail object.

        :param bool isusingtext: (optional) Whether using text or not.
        :param str traintextpath: (optional) The train text path.
        :param str valtextpath: (optional) The validation text path.
        :param str testtextpath: (optional) The test text path.
        :param str labeltextpath: (optional) The label text path.
        :param str trainimagepath: (optional) The train image path.
        :param str valimagepath: (optional) The validation image path.
        :param str testimagepath: (optional) The test image path.
        :param str imagetype: (optional) The image type.
        :param int height: (optional) The height of the image.
        :param int width: (optional) The width of the image.
        :param str resizetransformation: (optional) The resize transformation.
        :param int valpercentage: (optional) The percentage for validation.
        :param int testpercentage: (optional) The percentage for test.
        :param str splitalgorithm: (optional) The algorithm for splitting images.
        """
        self.isusingtext = isusingtext
        self.traintextpath = traintextpath
        self.valtextpath = valtextpath
        self.testtextpath = testtextpath
        self.labeltextpath = labeltextpath
        self.trainimagepath = trainimagepath
        self.valimagepath = valimagepath
        self.testimagepath = testimagepath
        self.imagetype = imagetype
        self.height = height
        self.width = width
        self.resizetransformation = resizetransformation
        self.valpercentage = valpercentage
        self.testpercentage = testpercentage
        self.splitalgorithm = splitalgorithm

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDetail':
        """Initialize a ImageDetail object from a json dictionary."""
        args = {}
        if 'isusingtext' in _dict:
            args['isusingtext'] = _dict.get('isusingtext')
        if 'traintextpath' in _dict:
            args['traintextpath'] = _dict.get('traintextpath')
        if 'valtextpath' in _dict:
            args['valtextpath'] = _dict.get('valtextpath')
        if 'testtextpath' in _dict:
            args['testtextpath'] = _dict.get('testtextpath')
        if 'labeltextpath' in _dict:
            args['labeltextpath'] = _dict.get('labeltextpath')
        if 'trainimagepath' in _dict:
            args['trainimagepath'] = _dict.get('trainimagepath')
        if 'valimagepath' in _dict:
            args['valimagepath'] = _dict.get('valimagepath')
        if 'testimagepath' in _dict:
            args['testimagepath'] = _dict.get('testimagepath')
        if 'imagetype' in _dict:
            args['imagetype'] = _dict.get('imagetype')
        if 'height' in _dict:
            args['height'] = _dict.get('height')
        if 'width' in _dict:
            args['width'] = _dict.get('width')
        if 'resizetransformation' in _dict:
            args['resizetransformation'] = _dict.get('resizetransformation')
        if 'valpercentage' in _dict:
            args['valpercentage'] = _dict.get('valpercentage')
        if 'testpercentage' in _dict:
            args['testpercentage'] = _dict.get('testpercentage')
        if 'splitalgorithm' in _dict:
            args['splitalgorithm'] = _dict.get('splitalgorithm')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'isusingtext') and self.isusingtext is not None:
            _dict['isusingtext'] = self.isusingtext
        if hasattr(self, 'traintextpath') and self.traintextpath is not None:
            _dict['traintextpath'] = self.traintextpath
        if hasattr(self, 'valtextpath') and self.valtextpath is not None:
            _dict['valtextpath'] = self.valtextpath
        if hasattr(self, 'testtextpath') and self.testtextpath is not None:
            _dict['testtextpath'] = self.testtextpath
        if hasattr(self, 'labeltextpath') and self.labeltextpath is not None:
            _dict['labeltextpath'] = self.labeltextpath
        if hasattr(self, 'trainimagepath') and self.trainimagepath is not None:
            _dict['trainimagepath'] = self.trainimagepath
        if hasattr(self, 'valimagepath') and self.valimagepath is not None:
            _dict['valimagepath'] = self.valimagepath
        if hasattr(self, 'testimagepath') and self.testimagepath is not None:
            _dict['testimagepath'] = self.testimagepath
        if hasattr(self, 'imagetype') and self.imagetype is not None:
            _dict['imagetype'] = self.imagetype
        if hasattr(self, 'height') and self.height is not None:
            _dict['height'] = self.height
        if hasattr(self, 'width') and self.width is not None:
            _dict['width'] = self.width
        if hasattr(self, 'resizetransformation') and self.resizetransformation is not None:
            _dict['resizetransformation'] = self.resizetransformation
        if hasattr(self, 'valpercentage') and self.valpercentage is not None:
            _dict['valpercentage'] = self.valpercentage
        if hasattr(self, 'testpercentage') and self.testpercentage is not None:
            _dict['testpercentage'] = self.testpercentage
        if hasattr(self, 'splitalgorithm') and self.splitalgorithm is not None:
            _dict['splitalgorithm'] = self.splitalgorithm
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InferenceDetail():
    """
    InferenceDetail.

    :attr str modelname: (optional) The deep learning model name.
    :attr str predictname: (optional) The prediction name.
    :attr str inputpath: (optional) The input directory path.
    :attr str inputfiles: (optional) The input files.
    :attr str output: (optional) The output directory path.
    :attr str threshold: (optional) The probability threshold for classification.
    :attr str resultfile: (optional) The result file name.
    :attr PredictParameters result: (optional)
    :attr str status: (optional) The inference status.
    :attr str sigid: (optional) The Spark instance group ID.
    :attr str signame: (optional) The Spark instance group name.
    :attr str master_url: (optional) The Spark master URL.
    :attr str driverid: (optional) The Spark driver ID.
    :attr str appid: (optional) The Spark application ID.
    :attr str app_url: (optional) The Spark application URL.
    :attr str create_time: (optional) The time the inference was created.
    :attr str user: (optional) The user who created the inference.
    :attr str history_server_url: (optional) The Spark history server URL.
    """

    def __init__(self,
                 *,
                 modelname: str = None,
                 predictname: str = None,
                 inputpath: str = None,
                 inputfiles: str = None,
                 output: str = None,
                 threshold: str = None,
                 resultfile: str = None,
                 result: 'PredictParameters' = None,
                 status: str = None,
                 sigid: str = None,
                 signame: str = None,
                 master_url: str = None,
                 driverid: str = None,
                 appid: str = None,
                 app_url: str = None,
                 create_time: str = None,
                 user: str = None,
                 history_server_url: str = None) -> None:
        """
        Initialize a InferenceDetail object.

        :param str modelname: (optional) The deep learning model name.
        :param str predictname: (optional) The prediction name.
        :param str inputpath: (optional) The input directory path.
        :param str inputfiles: (optional) The input files.
        :param str output: (optional) The output directory path.
        :param str threshold: (optional) The probability threshold for
               classification.
        :param str resultfile: (optional) The result file name.
        :param PredictParameters result: (optional)
        :param str status: (optional) The inference status.
        :param str sigid: (optional) The Spark instance group ID.
        :param str signame: (optional) The Spark instance group name.
        :param str master_url: (optional) The Spark master URL.
        :param str driverid: (optional) The Spark driver ID.
        :param str appid: (optional) The Spark application ID.
        :param str app_url: (optional) The Spark application URL.
        :param str create_time: (optional) The time the inference was created.
        :param str user: (optional) The user who created the inference.
        :param str history_server_url: (optional) The Spark history server URL.
        """
        self.modelname = modelname
        self.predictname = predictname
        self.inputpath = inputpath
        self.inputfiles = inputfiles
        self.output = output
        self.threshold = threshold
        self.resultfile = resultfile
        self.result = result
        self.status = status
        self.sigid = sigid
        self.signame = signame
        self.master_url = master_url
        self.driverid = driverid
        self.appid = appid
        self.app_url = app_url
        self.create_time = create_time
        self.user = user
        self.history_server_url = history_server_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InferenceDetail':
        """Initialize a InferenceDetail object from a json dictionary."""
        args = {}
        if 'modelname' in _dict:
            args['modelname'] = _dict.get('modelname')
        if 'predictname' in _dict:
            args['predictname'] = _dict.get('predictname')
        if 'inputpath' in _dict:
            args['inputpath'] = _dict.get('inputpath')
        if 'inputfiles' in _dict:
            args['inputfiles'] = _dict.get('inputfiles')
        if 'output' in _dict:
            args['output'] = _dict.get('output')
        if 'threshold' in _dict:
            args['threshold'] = _dict.get('threshold')
        if 'resultfile' in _dict:
            args['resultfile'] = _dict.get('resultfile')
        if 'result' in _dict:
            args['result'] = PredictParameters.from_dict(_dict.get('result'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'sigid' in _dict:
            args['sigid'] = _dict.get('sigid')
        if 'signame' in _dict:
            args['signame'] = _dict.get('signame')
        if 'masterUrl' in _dict:
            args['master_url'] = _dict.get('masterUrl')
        if 'driverid' in _dict:
            args['driverid'] = _dict.get('driverid')
        if 'appid' in _dict:
            args['appid'] = _dict.get('appid')
        if 'appURL' in _dict:
            args['app_url'] = _dict.get('appURL')
        if 'createTime' in _dict:
            args['create_time'] = _dict.get('createTime')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'historyServerUrl' in _dict:
            args['history_server_url'] = _dict.get('historyServerUrl')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InferenceDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'modelname') and self.modelname is not None:
            _dict['modelname'] = self.modelname
        if hasattr(self, 'predictname') and self.predictname is not None:
            _dict['predictname'] = self.predictname
        if hasattr(self, 'inputpath') and self.inputpath is not None:
            _dict['inputpath'] = self.inputpath
        if hasattr(self, 'inputfiles') and self.inputfiles is not None:
            _dict['inputfiles'] = self.inputfiles
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output
        if hasattr(self, 'threshold') and self.threshold is not None:
            _dict['threshold'] = self.threshold
        if hasattr(self, 'resultfile') and self.resultfile is not None:
            _dict['resultfile'] = self.resultfile
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'sigid') and self.sigid is not None:
            _dict['sigid'] = self.sigid
        if hasattr(self, 'signame') and self.signame is not None:
            _dict['signame'] = self.signame
        if hasattr(self, 'master_url') and self.master_url is not None:
            _dict['masterUrl'] = self.master_url
        if hasattr(self, 'driverid') and self.driverid is not None:
            _dict['driverid'] = self.driverid
        if hasattr(self, 'appid') and self.appid is not None:
            _dict['appid'] = self.appid
        if hasattr(self, 'app_url') and self.app_url is not None:
            _dict['appURL'] = self.app_url
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['createTime'] = self.create_time
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'history_server_url') and self.history_server_url is not None:
            _dict['historyServerUrl'] = self.history_server_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InferenceDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InferenceDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InferenceDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Instance():
    """
    Instance.

    :attr str name: (optional) The name of the Elastic Distributed Inference model.
    :attr str state: (optional) The state of the instance.
    :attr List[Isd] instances: (optional) The instance detail for an instance
          deamon.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 state: str = None,
                 instances: List['Isd'] = None) -> None:
        """
        Initialize a Instance object.

        :param str name: (optional) The name of the Elastic Distributed Inference
               model.
        :param str state: (optional) The state of the instance.
        :param List[Isd] instances: (optional) The instance detail for an instance
               deamon.
        """
        self.name = name
        self.state = state
        self.instances = instances

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Instance':
        """Initialize a Instance object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'instances' in _dict:
            args['instances'] = [Isd.from_dict(x) for x in _dict.get('instances')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Instance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'instances') and self.instances is not None:
            _dict['instances'] = [x.to_dict() for x in self.instances]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Instance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Isd():
    """
    Isd.

    :attr str isd_uid: (optional) The uid of the instance.
    :attr int client_number: (optional) The number of the instance client.
    :attr int pending_number: (optional) The number of the pending instance.
    :attr int request_per_sec: (optional) The number of request dealing with per
          second.
    :attr int data_size_per_sec: (optional) The size of data dealing with per
          second.
    :attr List[Container] isd_container: (optional) The container detail for an
          instance deamon.
    """

    def __init__(self,
                 *,
                 isd_uid: str = None,
                 client_number: int = None,
                 pending_number: int = None,
                 request_per_sec: int = None,
                 data_size_per_sec: int = None,
                 isd_container: List['Container'] = None) -> None:
        """
        Initialize a Isd object.

        :param str isd_uid: (optional) The uid of the instance.
        :param int client_number: (optional) The number of the instance client.
        :param int pending_number: (optional) The number of the pending instance.
        :param int request_per_sec: (optional) The number of request dealing with
               per second.
        :param int data_size_per_sec: (optional) The size of data dealing with per
               second.
        :param List[Container] isd_container: (optional) The container detail for
               an instance deamon.
        """
        self.isd_uid = isd_uid
        self.client_number = client_number
        self.pending_number = pending_number
        self.request_per_sec = request_per_sec
        self.data_size_per_sec = data_size_per_sec
        self.isd_container = isd_container

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Isd':
        """Initialize a Isd object from a json dictionary."""
        args = {}
        if 'isd_uid' in _dict:
            args['isd_uid'] = _dict.get('isd_uid')
        if 'client_number' in _dict:
            args['client_number'] = _dict.get('client_number')
        if 'pending_number' in _dict:
            args['pending_number'] = _dict.get('pending_number')
        if 'request_per_sec' in _dict:
            args['request_per_sec'] = _dict.get('request_per_sec')
        if 'data_size_per_sec' in _dict:
            args['data_size_per_sec'] = _dict.get('data_size_per_sec')
        if 'isd_container' in _dict:
            args['isd_container'] = [Container.from_dict(x) for x in _dict.get('isd_container')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Isd object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'isd_uid') and self.isd_uid is not None:
            _dict['isd_uid'] = self.isd_uid
        if hasattr(self, 'client_number') and self.client_number is not None:
            _dict['client_number'] = self.client_number
        if hasattr(self, 'pending_number') and self.pending_number is not None:
            _dict['pending_number'] = self.pending_number
        if hasattr(self, 'request_per_sec') and self.request_per_sec is not None:
            _dict['request_per_sec'] = self.request_per_sec
        if hasattr(self, 'data_size_per_sec') and self.data_size_per_sec is not None:
            _dict['data_size_per_sec'] = self.data_size_per_sec
        if hasattr(self, 'isd_container') and self.isd_container is not None:
            _dict['isd_container'] = [x.to_dict() for x in self.isd_container]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Isd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Isd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Isd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Kernel():
    """
    Kernel.

    :attr str working_directory: (optional) Working Directory.
    :attr int connection_timeout: (optional) The kernel connection timeout.
    :attr str log_directory: (optional) Log Directory.
    :attr str run_as: (optional) The kernel run as.
    :attr str umask: (optional) The kernel umask.
    :attr str gpu: (optional) Nvidia GPU policy, including no, shared, exclusive.
    :attr Envs envs: (optional)
    """

    def __init__(self,
                 *,
                 working_directory: str = None,
                 connection_timeout: int = None,
                 log_directory: str = None,
                 run_as: str = None,
                 umask: str = None,
                 gpu: str = None,
                 envs: 'Envs' = None) -> None:
        """
        Initialize a Kernel object.

        :param str working_directory: (optional) Working Directory.
        :param int connection_timeout: (optional) The kernel connection timeout.
        :param str log_directory: (optional) Log Directory.
        :param str run_as: (optional) The kernel run as.
        :param str umask: (optional) The kernel umask.
        :param str gpu: (optional) Nvidia GPU policy, including no, shared,
               exclusive.
        :param Envs envs: (optional)
        """
        self.working_directory = working_directory
        self.connection_timeout = connection_timeout
        self.log_directory = log_directory
        self.run_as = run_as
        self.umask = umask
        self.gpu = gpu
        self.envs = envs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Kernel':
        """Initialize a Kernel object from a json dictionary."""
        args = {}
        if 'working_directory' in _dict:
            args['working_directory'] = _dict.get('working_directory')
        if 'connection_timeout' in _dict:
            args['connection_timeout'] = _dict.get('connection_timeout')
        if 'log_directory' in _dict:
            args['log_directory'] = _dict.get('log_directory')
        if 'run_as' in _dict:
            args['run_as'] = _dict.get('run_as')
        if 'umask' in _dict:
            args['umask'] = _dict.get('umask')
        if 'gpu' in _dict:
            args['gpu'] = _dict.get('gpu')
        if 'envs' in _dict:
            args['envs'] = Envs.from_dict(_dict.get('envs'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Kernel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'working_directory') and self.working_directory is not None:
            _dict['working_directory'] = self.working_directory
        if hasattr(self, 'connection_timeout') and self.connection_timeout is not None:
            _dict['connection_timeout'] = self.connection_timeout
        if hasattr(self, 'log_directory') and self.log_directory is not None:
            _dict['log_directory'] = self.log_directory
        if hasattr(self, 'run_as') and self.run_as is not None:
            _dict['run_as'] = self.run_as
        if hasattr(self, 'umask') and self.umask is not None:
            _dict['umask'] = self.umask
        if hasattr(self, 'gpu') and self.gpu is not None:
            _dict['gpu'] = self.gpu
        if hasattr(self, 'envs') and self.envs is not None:
            _dict['envs'] = self.envs.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Kernel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Kernel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Kernel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ModelDetail():
    """
    ModelDetail.

    :attr str name: (optional) The name of the deep learning model.
    :attr str path: (optional) The path of the deep learning model.
    :attr str description: (optional) The description of the deep learning model.
    :attr str templatename: (optional) The deep learning model template name.
    :attr str framework: (optional) The deep learning model framework.
    :attr str accelerator: (optional) The deep learning model training engine.
    :attr HyperParameter hyperparameter: (optional)
    :attr str dataset: (optional) The name of the the dataset associated with the
          deep learning model.
    :attr int batchsize: (optional) The batch size.
    :attr str solverprototxtpath: (optional) The path to *solver.prototxt
          configuration file.
    :attr str traintestprototxtpath: (optional) The path to *train_test.prototxt
          configuration file.
    :attr str inferenceprototxtpath: (optional) The path for inference configuration
          file.
    :attr str dimimage: (optional) The dimimage.
    :attr str solver_content: (optional) The content of the *solver.prototxt
          configuration file.
    :attr str train_test_content: (optional) The content of the *train_test.prototxt
          configuration file.
    :attr str inference_content: (optional) The content of the inference
          configuration file.
    :attr str tfmainpath: (optional) The main executor file path.
    :attr str tfmain_content: (optional) The contents of the main.py file.
    :attr str sig: (optional) The Spark instance group id.
    :attr str signame: (optional) The Spark instance group name.
    :attr str tmpfile_path: (optional) The path of the temporary file.
    :attr str tmpfile_content: (optional) Contents of the temporary file.
    :attr str wfinit: (optional) The initial weight file.
    :attr str wtfolder: (optional) The folder that contains the weight file.
    :attr str type: (optional) The type of the model, indicates whether it is
          inference model or training model.
    :attr str user: (optional) The user who created the model.
    :attr str create_time: (optional) The time the model was created.
    :attr str framework_version: (optional) The framework version.
    :attr str distribute_strategy: (optional) The distribution strategy.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 path: str = None,
                 description: str = None,
                 templatename: str = None,
                 framework: str = None,
                 accelerator: str = None,
                 hyperparameter: 'HyperParameter' = None,
                 dataset: str = None,
                 batchsize: int = None,
                 solverprototxtpath: str = None,
                 traintestprototxtpath: str = None,
                 inferenceprototxtpath: str = None,
                 dimimage: str = None,
                 solver_content: str = None,
                 train_test_content: str = None,
                 inference_content: str = None,
                 tfmainpath: str = None,
                 tfmain_content: str = None,
                 sig: str = None,
                 signame: str = None,
                 tmpfile_path: str = None,
                 tmpfile_content: str = None,
                 wfinit: str = None,
                 wtfolder: str = None,
                 type: str = None,
                 user: str = None,
                 create_time: str = None,
                 framework_version: str = None,
                 distribute_strategy: str = None) -> None:
        """
        Initialize a ModelDetail object.

        :param str name: (optional) The name of the deep learning model.
        :param str path: (optional) The path of the deep learning model.
        :param str description: (optional) The description of the deep learning
               model.
        :param str templatename: (optional) The deep learning model template name.
        :param str framework: (optional) The deep learning model framework.
        :param str accelerator: (optional) The deep learning model training engine.
        :param HyperParameter hyperparameter: (optional)
        :param str dataset: (optional) The name of the the dataset associated with
               the deep learning model.
        :param int batchsize: (optional) The batch size.
        :param str solverprototxtpath: (optional) The path to *solver.prototxt
               configuration file.
        :param str traintestprototxtpath: (optional) The path to
               *train_test.prototxt configuration file.
        :param str inferenceprototxtpath: (optional) The path for inference
               configuration file.
        :param str dimimage: (optional) The dimimage.
        :param str solver_content: (optional) The content of the *solver.prototxt
               configuration file.
        :param str train_test_content: (optional) The content of the
               *train_test.prototxt configuration file.
        :param str inference_content: (optional) The content of the inference
               configuration file.
        :param str tfmainpath: (optional) The main executor file path.
        :param str tfmain_content: (optional) The contents of the main.py file.
        :param str sig: (optional) The Spark instance group id.
        :param str signame: (optional) The Spark instance group name.
        :param str tmpfile_path: (optional) The path of the temporary file.
        :param str tmpfile_content: (optional) Contents of the temporary file.
        :param str wfinit: (optional) The initial weight file.
        :param str wtfolder: (optional) The folder that contains the weight file.
        :param str type: (optional) The type of the model, indicates whether it is
               inference model or training model.
        :param str user: (optional) The user who created the model.
        :param str create_time: (optional) The time the model was created.
        :param str framework_version: (optional) The framework version.
        :param str distribute_strategy: (optional) The distribution strategy.
        """
        self.name = name
        self.path = path
        self.description = description
        self.templatename = templatename
        self.framework = framework
        self.accelerator = accelerator
        self.hyperparameter = hyperparameter
        self.dataset = dataset
        self.batchsize = batchsize
        self.solverprototxtpath = solverprototxtpath
        self.traintestprototxtpath = traintestprototxtpath
        self.inferenceprototxtpath = inferenceprototxtpath
        self.dimimage = dimimage
        self.solver_content = solver_content
        self.train_test_content = train_test_content
        self.inference_content = inference_content
        self.tfmainpath = tfmainpath
        self.tfmain_content = tfmain_content
        self.sig = sig
        self.signame = signame
        self.tmpfile_path = tmpfile_path
        self.tmpfile_content = tmpfile_content
        self.wfinit = wfinit
        self.wtfolder = wtfolder
        self.type = type
        self.user = user
        self.create_time = create_time
        self.framework_version = framework_version
        self.distribute_strategy = distribute_strategy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelDetail':
        """Initialize a ModelDetail object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'templatename' in _dict:
            args['templatename'] = _dict.get('templatename')
        if 'framework' in _dict:
            args['framework'] = _dict.get('framework')
        if 'accelerator' in _dict:
            args['accelerator'] = _dict.get('accelerator')
        if 'hyperparameter' in _dict:
            args['hyperparameter'] = HyperParameter.from_dict(_dict.get('hyperparameter'))
        if 'dataset' in _dict:
            args['dataset'] = _dict.get('dataset')
        if 'batchsize' in _dict:
            args['batchsize'] = _dict.get('batchsize')
        if 'solverprototxtpath' in _dict:
            args['solverprototxtpath'] = _dict.get('solverprototxtpath')
        if 'traintestprototxtpath' in _dict:
            args['traintestprototxtpath'] = _dict.get('traintestprototxtpath')
        if 'inferenceprototxtpath' in _dict:
            args['inferenceprototxtpath'] = _dict.get('inferenceprototxtpath')
        if 'dimimage' in _dict:
            args['dimimage'] = _dict.get('dimimage')
        if 'solverContent' in _dict:
            args['solver_content'] = _dict.get('solverContent')
        if 'trainTestContent' in _dict:
            args['train_test_content'] = _dict.get('trainTestContent')
        if 'inferenceContent' in _dict:
            args['inference_content'] = _dict.get('inferenceContent')
        if 'tfmainpath' in _dict:
            args['tfmainpath'] = _dict.get('tfmainpath')
        if 'tfmainContent' in _dict:
            args['tfmain_content'] = _dict.get('tfmainContent')
        if 'sig' in _dict:
            args['sig'] = _dict.get('sig')
        if 'signame' in _dict:
            args['signame'] = _dict.get('signame')
        if 'tmpfilePath' in _dict:
            args['tmpfile_path'] = _dict.get('tmpfilePath')
        if 'tmpfileContent' in _dict:
            args['tmpfile_content'] = _dict.get('tmpfileContent')
        if 'wfinit' in _dict:
            args['wfinit'] = _dict.get('wfinit')
        if 'wtfolder' in _dict:
            args['wtfolder'] = _dict.get('wtfolder')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'createTime' in _dict:
            args['create_time'] = _dict.get('createTime')
        if 'frameworkVersion' in _dict:
            args['framework_version'] = _dict.get('frameworkVersion')
        if 'distributeStrategy' in _dict:
            args['distribute_strategy'] = _dict.get('distributeStrategy')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'templatename') and self.templatename is not None:
            _dict['templatename'] = self.templatename
        if hasattr(self, 'framework') and self.framework is not None:
            _dict['framework'] = self.framework
        if hasattr(self, 'accelerator') and self.accelerator is not None:
            _dict['accelerator'] = self.accelerator
        if hasattr(self, 'hyperparameter') and self.hyperparameter is not None:
            _dict['hyperparameter'] = self.hyperparameter.to_dict()
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'batchsize') and self.batchsize is not None:
            _dict['batchsize'] = self.batchsize
        if hasattr(self, 'solverprototxtpath') and self.solverprototxtpath is not None:
            _dict['solverprototxtpath'] = self.solverprototxtpath
        if hasattr(self, 'traintestprototxtpath') and self.traintestprototxtpath is not None:
            _dict['traintestprototxtpath'] = self.traintestprototxtpath
        if hasattr(self, 'inferenceprototxtpath') and self.inferenceprototxtpath is not None:
            _dict['inferenceprototxtpath'] = self.inferenceprototxtpath
        if hasattr(self, 'dimimage') and self.dimimage is not None:
            _dict['dimimage'] = self.dimimage
        if hasattr(self, 'solver_content') and self.solver_content is not None:
            _dict['solverContent'] = self.solver_content
        if hasattr(self, 'train_test_content') and self.train_test_content is not None:
            _dict['trainTestContent'] = self.train_test_content
        if hasattr(self, 'inference_content') and self.inference_content is not None:
            _dict['inferenceContent'] = self.inference_content
        if hasattr(self, 'tfmainpath') and self.tfmainpath is not None:
            _dict['tfmainpath'] = self.tfmainpath
        if hasattr(self, 'tfmain_content') and self.tfmain_content is not None:
            _dict['tfmainContent'] = self.tfmain_content
        if hasattr(self, 'sig') and self.sig is not None:
            _dict['sig'] = self.sig
        if hasattr(self, 'signame') and self.signame is not None:
            _dict['signame'] = self.signame
        if hasattr(self, 'tmpfile_path') and self.tmpfile_path is not None:
            _dict['tmpfilePath'] = self.tmpfile_path
        if hasattr(self, 'tmpfile_content') and self.tmpfile_content is not None:
            _dict['tmpfileContent'] = self.tmpfile_content
        if hasattr(self, 'wfinit') and self.wfinit is not None:
            _dict['wfinit'] = self.wfinit
        if hasattr(self, 'wtfolder') and self.wtfolder is not None:
            _dict['wtfolder'] = self.wtfolder
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['createTime'] = self.create_time
        if hasattr(self, 'framework_version') and self.framework_version is not None:
            _dict['frameworkVersion'] = self.framework_version
        if hasattr(self, 'distribute_strategy') and self.distribute_strategy is not None:
            _dict['distributeStrategy'] = self.distribute_strategy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrameworkEnum(str, Enum):
        """
        The deep learning model framework.
        """
        CAFFE = 'Caffe'
        TENSORFLOW = 'TensorFlow'
        PYTORCH = 'PyTorch'


    class AcceleratorEnum(str, Enum):
        """
        The deep learning model training engine.
        """
        SINGLE = 'Single'
        NATIVE = 'Native'
        ELASTIC = 'Elastic'


    class TypeEnum(str, Enum):
        """
        The type of the model, indicates whether it is inference model or training model.
        """
        TRAINING = 'Training'
        INFERENCE = 'Inference'


class ModelTemplateDetail():
    """
    ModelTemplateDetail.

    :attr str name: (optional) The name of the model template.
    :attr str path: (optional) The path of the model template.
    :attr str description: (optional) The description.
    :attr HyperParameter hyperparameter: (optional)
    :attr str framework: (optional) The deep learning framework name.
    :attr str solverprototxtpath: (optional) The path to Caffe *solver.prototxt
          configuration file.
    :attr str traintestprototxtpath: (optional) The path to Caffe
          *train_test.prototxt configuration file.
    :attr str inferenceprototxtpath: (optional) The path to inference prototxt
          configuration file.
    :attr str solver_content: (optional) The solverContent.
    :attr str train_test_content: (optional) The trainTestContent.
    :attr str inference_content: (optional) The inferenceContent.
    :attr str tfmainpath: (optional) The main executor file path.
    :attr str tfmain_content: (optional) The contents of the main.py.
    :attr str framework_version: (optional) The framework version.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 path: str = None,
                 description: str = None,
                 hyperparameter: 'HyperParameter' = None,
                 framework: str = None,
                 solverprototxtpath: str = None,
                 traintestprototxtpath: str = None,
                 inferenceprototxtpath: str = None,
                 solver_content: str = None,
                 train_test_content: str = None,
                 inference_content: str = None,
                 tfmainpath: str = None,
                 tfmain_content: str = None,
                 framework_version: str = None) -> None:
        """
        Initialize a ModelTemplateDetail object.

        :param str name: (optional) The name of the model template.
        :param str path: (optional) The path of the model template.
        :param str description: (optional) The description.
        :param HyperParameter hyperparameter: (optional)
        :param str framework: (optional) The deep learning framework name.
        :param str solverprototxtpath: (optional) The path to Caffe
               *solver.prototxt configuration file.
        :param str traintestprototxtpath: (optional) The path to Caffe
               *train_test.prototxt configuration file.
        :param str inferenceprototxtpath: (optional) The path to inference prototxt
               configuration file.
        :param str solver_content: (optional) The solverContent.
        :param str train_test_content: (optional) The trainTestContent.
        :param str inference_content: (optional) The inferenceContent.
        :param str tfmainpath: (optional) The main executor file path.
        :param str tfmain_content: (optional) The contents of the main.py.
        :param str framework_version: (optional) The framework version.
        """
        self.name = name
        self.path = path
        self.description = description
        self.hyperparameter = hyperparameter
        self.framework = framework
        self.solverprototxtpath = solverprototxtpath
        self.traintestprototxtpath = traintestprototxtpath
        self.inferenceprototxtpath = inferenceprototxtpath
        self.solver_content = solver_content
        self.train_test_content = train_test_content
        self.inference_content = inference_content
        self.tfmainpath = tfmainpath
        self.tfmain_content = tfmain_content
        self.framework_version = framework_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelTemplateDetail':
        """Initialize a ModelTemplateDetail object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'hyperparameter' in _dict:
            args['hyperparameter'] = HyperParameter.from_dict(_dict.get('hyperparameter'))
        if 'framework' in _dict:
            args['framework'] = _dict.get('framework')
        if 'solverprototxtpath' in _dict:
            args['solverprototxtpath'] = _dict.get('solverprototxtpath')
        if 'traintestprototxtpath' in _dict:
            args['traintestprototxtpath'] = _dict.get('traintestprototxtpath')
        if 'inferenceprototxtpath' in _dict:
            args['inferenceprototxtpath'] = _dict.get('inferenceprototxtpath')
        if 'solverContent' in _dict:
            args['solver_content'] = _dict.get('solverContent')
        if 'trainTestContent' in _dict:
            args['train_test_content'] = _dict.get('trainTestContent')
        if 'inferenceContent' in _dict:
            args['inference_content'] = _dict.get('inferenceContent')
        if 'tfmainpath' in _dict:
            args['tfmainpath'] = _dict.get('tfmainpath')
        if 'tfmainContent' in _dict:
            args['tfmain_content'] = _dict.get('tfmainContent')
        if 'frameworkVersion' in _dict:
            args['framework_version'] = _dict.get('frameworkVersion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelTemplateDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'hyperparameter') and self.hyperparameter is not None:
            _dict['hyperparameter'] = self.hyperparameter.to_dict()
        if hasattr(self, 'framework') and self.framework is not None:
            _dict['framework'] = self.framework
        if hasattr(self, 'solverprototxtpath') and self.solverprototxtpath is not None:
            _dict['solverprototxtpath'] = self.solverprototxtpath
        if hasattr(self, 'traintestprototxtpath') and self.traintestprototxtpath is not None:
            _dict['traintestprototxtpath'] = self.traintestprototxtpath
        if hasattr(self, 'inferenceprototxtpath') and self.inferenceprototxtpath is not None:
            _dict['inferenceprototxtpath'] = self.inferenceprototxtpath
        if hasattr(self, 'solver_content') and self.solver_content is not None:
            _dict['solverContent'] = self.solver_content
        if hasattr(self, 'train_test_content') and self.train_test_content is not None:
            _dict['trainTestContent'] = self.train_test_content
        if hasattr(self, 'inference_content') and self.inference_content is not None:
            _dict['inferenceContent'] = self.inference_content
        if hasattr(self, 'tfmainpath') and self.tfmainpath is not None:
            _dict['tfmainpath'] = self.tfmainpath
        if hasattr(self, 'tfmain_content') and self.tfmain_content is not None:
            _dict['tfmainContent'] = self.tfmain_content
        if hasattr(self, 'framework_version') and self.framework_version is not None:
            _dict['frameworkVersion'] = self.framework_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelTemplateDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelTemplateDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelTemplateDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Pictures():
    """
    Pictures.

    :attr str name: (optional) The name of the image.
    :attr str path: (optional) The path of the image.
    :attr str labels: (optional) The labels of the image.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 path: str = None,
                 labels: str = None) -> None:
        """
        Initialize a Pictures object.

        :param str name: (optional) The name of the image.
        :param str path: (optional) The path of the image.
        :param str labels: (optional) The labels of the image.
        """
        self.name = name
        self.path = path
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pictures':
        """Initialize a Pictures object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pictures object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pictures object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pictures') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pictures') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Policy():
    """
    Policy.

    :attr str name: (optional) The name of the policy.
    :attr int schedule_intervel: (optional) The intervel of schedule.
    :attr int kernel_min: (optional) The minimal number of model kernel.
    :attr int kernel_max: (optional) The maximal number of model kernel.
    :attr int kernel_delay_release_time: (optional) The idle time to wait to release
          the kernel.
    :attr int task_execution_timeout: (optional) The task execution timeout.
    :attr int task_batch_size: (optional) The maximal number of task which single
          model can handle each time.
    :attr int stream_number_per_group: (optional) The number of stream task per
          group.
    :attr bool stream_discard_slow_tasks: (optional) Discard stream slow task if set
          true.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 schedule_intervel: int = None,
                 kernel_min: int = None,
                 kernel_max: int = None,
                 kernel_delay_release_time: int = None,
                 task_execution_timeout: int = None,
                 task_batch_size: int = None,
                 stream_number_per_group: int = None,
                 stream_discard_slow_tasks: bool = None) -> None:
        """
        Initialize a Policy object.

        :param str name: (optional) The name of the policy.
        :param int schedule_intervel: (optional) The intervel of schedule.
        :param int kernel_min: (optional) The minimal number of model kernel.
        :param int kernel_max: (optional) The maximal number of model kernel.
        :param int kernel_delay_release_time: (optional) The idle time to wait to
               release the kernel.
        :param int task_execution_timeout: (optional) The task execution timeout.
        :param int task_batch_size: (optional) The maximal number of task which
               single model can handle each time.
        :param int stream_number_per_group: (optional) The number of stream task
               per group.
        :param bool stream_discard_slow_tasks: (optional) Discard stream slow task
               if set true.
        """
        self.name = name
        self.schedule_intervel = schedule_intervel
        self.kernel_min = kernel_min
        self.kernel_max = kernel_max
        self.kernel_delay_release_time = kernel_delay_release_time
        self.task_execution_timeout = task_execution_timeout
        self.task_batch_size = task_batch_size
        self.stream_number_per_group = stream_number_per_group
        self.stream_discard_slow_tasks = stream_discard_slow_tasks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Policy':
        """Initialize a Policy object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'schedule_intervel' in _dict:
            args['schedule_intervel'] = _dict.get('schedule_intervel')
        if 'kernel_min' in _dict:
            args['kernel_min'] = _dict.get('kernel_min')
        if 'kernel_max' in _dict:
            args['kernel_max'] = _dict.get('kernel_max')
        if 'kernel_delay_release_time' in _dict:
            args['kernel_delay_release_time'] = _dict.get('kernel_delay_release_time')
        if 'task_execution_timeout' in _dict:
            args['task_execution_timeout'] = _dict.get('task_execution_timeout')
        if 'task_batch_size' in _dict:
            args['task_batch_size'] = _dict.get('task_batch_size')
        if 'stream_number_per_group' in _dict:
            args['stream_number_per_group'] = _dict.get('stream_number_per_group')
        if 'stream_discard_slow_tasks' in _dict:
            args['stream_discard_slow_tasks'] = _dict.get('stream_discard_slow_tasks')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Policy object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'schedule_intervel') and self.schedule_intervel is not None:
            _dict['schedule_intervel'] = self.schedule_intervel
        if hasattr(self, 'kernel_min') and self.kernel_min is not None:
            _dict['kernel_min'] = self.kernel_min
        if hasattr(self, 'kernel_max') and self.kernel_max is not None:
            _dict['kernel_max'] = self.kernel_max
        if hasattr(self, 'kernel_delay_release_time') and self.kernel_delay_release_time is not None:
            _dict['kernel_delay_release_time'] = self.kernel_delay_release_time
        if hasattr(self, 'task_execution_timeout') and self.task_execution_timeout is not None:
            _dict['task_execution_timeout'] = self.task_execution_timeout
        if hasattr(self, 'task_batch_size') and self.task_batch_size is not None:
            _dict['task_batch_size'] = self.task_batch_size
        if hasattr(self, 'stream_number_per_group') and self.stream_number_per_group is not None:
            _dict['stream_number_per_group'] = self.stream_number_per_group
        if hasattr(self, 'stream_discard_slow_tasks') and self.stream_discard_slow_tasks is not None:
            _dict['stream_discard_slow_tasks'] = self.stream_discard_slow_tasks
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Policy object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Policy') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Policy') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PredictParameters():
    """
    PredictParameters.

    :attr str predict_item: (optional) Prediction item.
    :attr PredictParams predict_results: (optional)
    """

    def __init__(self,
                 *,
                 predict_item: str = None,
                 predict_results: 'PredictParams' = None) -> None:
        """
        Initialize a PredictParameters object.

        :param str predict_item: (optional) Prediction item.
        :param PredictParams predict_results: (optional)
        """
        self.predict_item = predict_item
        self.predict_results = predict_results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PredictParameters':
        """Initialize a PredictParameters object from a json dictionary."""
        args = {}
        if 'predictItem' in _dict:
            args['predict_item'] = _dict.get('predictItem')
        if 'predictResults' in _dict:
            args['predict_results'] = PredictParams.from_dict(_dict.get('predictResults'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PredictParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'predict_item') and self.predict_item is not None:
            _dict['predictItem'] = self.predict_item
        if hasattr(self, 'predict_results') and self.predict_results is not None:
            _dict['predictResults'] = self.predict_results.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PredictParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PredictParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PredictParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PredictParams():
    """
    PredictParams.

    :attr str index: (optional) The prediction item index.
    :attr str name: (optional) The prediction item name.
    :attr float proba: (optional) The prediction item probability.
    """

    def __init__(self,
                 *,
                 index: str = None,
                 name: str = None,
                 proba: float = None) -> None:
        """
        Initialize a PredictParams object.

        :param str index: (optional) The prediction item index.
        :param str name: (optional) The prediction item name.
        :param float proba: (optional) The prediction item probability.
        """
        self.index = index
        self.name = name
        self.proba = proba

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PredictParams':
        """Initialize a PredictParams object from a json dictionary."""
        args = {}
        if 'index' in _dict:
            args['index'] = _dict.get('index')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'proba' in _dict:
            args['proba'] = _dict.get('proba')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PredictParams object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'proba') and self.proba is not None:
            _dict['proba'] = self.proba
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PredictParams object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PredictParams') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PredictParams') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PredictResult():
    """
    PredictResult.

    :attr str type: (optional) The type of the prediction.
    :attr List[ClassificationDetDetail] classification_results: (optional) The
          results of classification.
    :attr List[ClassificationDetDetail] det_results: (optional) Det results.
    :attr List[ComparisonDetail] comparison_results: (optional) Comparison results.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 classification_results: List['ClassificationDetDetail'] = None,
                 det_results: List['ClassificationDetDetail'] = None,
                 comparison_results: List['ComparisonDetail'] = None) -> None:
        """
        Initialize a PredictResult object.

        :param str type: (optional) The type of the prediction.
        :param List[ClassificationDetDetail] classification_results: (optional) The
               results of classification.
        :param List[ClassificationDetDetail] det_results: (optional) Det results.
        :param List[ComparisonDetail] comparison_results: (optional) Comparison
               results.
        """
        self.type = type
        self.classification_results = classification_results
        self.det_results = det_results
        self.comparison_results = comparison_results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PredictResult':
        """Initialize a PredictResult object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'classificationResults' in _dict:
            args['classification_results'] = [ClassificationDetDetail.from_dict(x) for x in _dict.get('classificationResults')]
        if 'detResults' in _dict:
            args['det_results'] = [ClassificationDetDetail.from_dict(x) for x in _dict.get('detResults')]
        if 'comparisonResults' in _dict:
            args['comparison_results'] = [ComparisonDetail.from_dict(x) for x in _dict.get('comparisonResults')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PredictResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'classification_results') and self.classification_results is not None:
            _dict['classificationResults'] = [x.to_dict() for x in self.classification_results]
        if hasattr(self, 'det_results') and self.det_results is not None:
            _dict['detResults'] = [x.to_dict() for x in self.det_results]
        if hasattr(self, 'comparison_results') and self.comparison_results is not None:
            _dict['comparisonResults'] = [x.to_dict() for x in self.comparison_results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PredictResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PredictResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PredictResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RAKernel():
    """
    RAKernel.

    :attr str type: (optional) Resource manager for model kernel, currently only
          support ego.
    :attr str resource_group: (optional) Ego resource group for model kernel.
    :attr str consumer: (optional) Ego consumer for model kernel.
    :attr str resreq: (optional) Ego resource filter for model kernel.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 resource_group: str = None,
                 consumer: str = None,
                 resreq: str = None) -> None:
        """
        Initialize a RAKernel object.

        :param str type: (optional) Resource manager for model kernel, currently
               only support ego.
        :param str resource_group: (optional) Ego resource group for model kernel.
        :param str consumer: (optional) Ego consumer for model kernel.
        :param str resreq: (optional) Ego resource filter for model kernel.
        """
        self.type = type
        self.resource_group = resource_group
        self.consumer = consumer
        self.resreq = resreq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RAKernel':
        """Initialize a RAKernel object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        if 'consumer' in _dict:
            args['consumer'] = _dict.get('consumer')
        if 'resreq' in _dict:
            args['resreq'] = _dict.get('resreq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RAKernel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'consumer') and self.consumer is not None:
            _dict['consumer'] = self.consumer
        if hasattr(self, 'resreq') and self.resreq is not None:
            _dict['resreq'] = self.resreq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RAKernel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RAKernel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RAKernel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RAService():
    """
    RAService.

    :attr str type: (optional) Resource manager for Elastic Distributed Inference,
          currently only support ego.
    :attr str resource_group: (optional) Ego resource group for Elastic Distributed
          Inference.
    :attr str consumer: (optional) Ego consumer for Elastic Distributed Inference.
    :attr str resreq: (optional) Ego resource filter for Elastic Distributed
          Inference.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 resource_group: str = None,
                 consumer: str = None,
                 resreq: str = None) -> None:
        """
        Initialize a RAService object.

        :param str type: (optional) Resource manager for Elastic Distributed
               Inference, currently only support ego.
        :param str resource_group: (optional) Ego resource group for Elastic
               Distributed Inference.
        :param str consumer: (optional) Ego consumer for Elastic Distributed
               Inference.
        :param str resreq: (optional) Ego resource filter for Elastic Distributed
               Inference.
        """
        self.type = type
        self.resource_group = resource_group
        self.consumer = consumer
        self.resreq = resreq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RAService':
        """Initialize a RAService object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        if 'consumer' in _dict:
            args['consumer'] = _dict.get('consumer')
        if 'resreq' in _dict:
            args['resreq'] = _dict.get('resreq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RAService object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'consumer') and self.consumer is not None:
            _dict['consumer'] = self.consumer
        if hasattr(self, 'resreq') and self.resreq is not None:
            _dict['resreq'] = self.resreq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RAService object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RAService') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RAService') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceAllocation():
    """
    ResourceAllocation.

    :attr RAService service: (optional)
    :attr RAKernel kernel: (optional)
    """

    def __init__(self,
                 *,
                 service: 'RAService' = None,
                 kernel: 'RAKernel' = None) -> None:
        """
        Initialize a ResourceAllocation object.

        :param RAService service: (optional)
        :param RAKernel kernel: (optional)
        """
        self.service = service
        self.kernel = kernel

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceAllocation':
        """Initialize a ResourceAllocation object from a json dictionary."""
        args = {}
        if 'service' in _dict:
            args['service'] = RAService.from_dict(_dict.get('service'))
        if 'kernel' in _dict:
            args['kernel'] = RAKernel.from_dict(_dict.get('kernel'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceAllocation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service.to_dict()
        if hasattr(self, 'kernel') and self.kernel is not None:
            _dict['kernel'] = self.kernel.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceAllocation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceAllocation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceAllocation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SigAppInstanceDetail():
    """
    SigAppInstanceDetail.

    :attr str uuid: (optional) The unique ID of the Spark instance group.
    :attr str name: (optional) The name of the Spark instance group.
    :attr str version: (optional) The Spark version of the Spark instance group.
    :attr str master_url: (optional) The URL of the Spark instance group master.
    :attr str execution_user: (optional) The execution user of the Spark instance
          group.
    :attr str state: (optional) The state of the Spark instance group.
    :attr str history_server_url: (optional) The Spark history server URL.
    """

    def __init__(self,
                 *,
                 uuid: str = None,
                 name: str = None,
                 version: str = None,
                 master_url: str = None,
                 execution_user: str = None,
                 state: str = None,
                 history_server_url: str = None) -> None:
        """
        Initialize a SigAppInstanceDetail object.

        :param str uuid: (optional) The unique ID of the Spark instance group.
        :param str name: (optional) The name of the Spark instance group.
        :param str version: (optional) The Spark version of the Spark instance
               group.
        :param str master_url: (optional) The URL of the Spark instance group
               master.
        :param str execution_user: (optional) The execution user of the Spark
               instance group.
        :param str state: (optional) The state of the Spark instance group.
        :param str history_server_url: (optional) The Spark history server URL.
        """
        self.uuid = uuid
        self.name = name
        self.version = version
        self.master_url = master_url
        self.execution_user = execution_user
        self.state = state
        self.history_server_url = history_server_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SigAppInstanceDetail':
        """Initialize a SigAppInstanceDetail object from a json dictionary."""
        args = {}
        if 'uuid' in _dict:
            args['uuid'] = _dict.get('uuid')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'masterUrl' in _dict:
            args['master_url'] = _dict.get('masterUrl')
        if 'executionUser' in _dict:
            args['execution_user'] = _dict.get('executionUser')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'historyServerUrl' in _dict:
            args['history_server_url'] = _dict.get('historyServerUrl')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SigAppInstanceDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'uuid') and self.uuid is not None:
            _dict['uuid'] = self.uuid
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'master_url') and self.master_url is not None:
            _dict['masterUrl'] = self.master_url
        if hasattr(self, 'execution_user') and self.execution_user is not None:
            _dict['executionUser'] = self.execution_user
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'history_server_url') and self.history_server_url is not None:
            _dict['historyServerUrl'] = self.history_server_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SigAppInstanceDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SigAppInstanceDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SigAppInstanceDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SparkApplicationDetail():
    """
    SparkApplicationDetail.

    :attr str sparkinstancegroupid: (optional) The Spark instance group ID.
    :attr str applicationid: (optional) The Spark application ID.
    :attr str applicationname: (optional) The Spark application name.
    :attr str type: (optional) The Spark application type.
    :attr str state: (optional) The Spark application state.
    :attr str uiport: (optional) The port number on which to access the Spark
          application UI.
    :attr DriverDetail driver: (optional)
    :attr List[ExecutorDetail] executors: (optional) A list of Spark executors.
    :attr int slots: (optional) The number of slots that are used by the Spark
          instance group.
    :attr int demandslots: (optional) The number of demanded slots that is being
          used by the Spark application.
    :attr int hosts: (optional) The number of hosts on which Spark applications run.
    :attr float coresused: (optional) The number of CPU cores that are allocated to
          the Spark application.
    :attr float memused: (optional) The amount of memory, in MB, that is used by the
          Spark application.
    :attr str username: (optional) The user that executes the Spark application.
    :attr str driverexecutionuser: (optional) The execution user for the Spark
          drivers.
    :attr str executorexecutionuser: (optional) The execution user for the Spark
          executors.
    :attr int timestamp: (optional) The time-stamp of the updated Spark application.
    :attr int submittedtime: (optional) The Spark application submitted time.
    :attr str master_url: (optional) The Spark master URL.
    :attr int endtime: (optional) The Spark application finish time.
    :attr str schedule_name: (optional) The application schedule name.
    :attr str issharedapp: (optional) Specifies whether the Spark application shares
          RDD.
    :attr float apprunduration: (optional) The application run duration.
    :attr int master_seq_no: (optional) The master sequence number.
    :attr str master_service: (optional) The master service name.
    :attr str model: (optional) The deep learning model name.
    :attr str dataset: (optional) The deep learning dataset name.
    :attr str dltype: (optional) The deep learning framework name (e.g Caffe or
          TensorFlow).
    :attr str tunningname: (optional) The deep learning tuning name.
    :attr str sig_name: (optional) The Spark instance group name.
    :attr str history_server_url: (optional) The Spark history server URL.
    """

    def __init__(self,
                 *,
                 sparkinstancegroupid: str = None,
                 applicationid: str = None,
                 applicationname: str = None,
                 type: str = None,
                 state: str = None,
                 uiport: str = None,
                 driver: 'DriverDetail' = None,
                 executors: List['ExecutorDetail'] = None,
                 slots: int = None,
                 demandslots: int = None,
                 hosts: int = None,
                 coresused: float = None,
                 memused: float = None,
                 username: str = None,
                 driverexecutionuser: str = None,
                 executorexecutionuser: str = None,
                 timestamp: int = None,
                 submittedtime: int = None,
                 master_url: str = None,
                 endtime: int = None,
                 schedule_name: str = None,
                 issharedapp: str = None,
                 apprunduration: float = None,
                 master_seq_no: int = None,
                 master_service: str = None,
                 model: str = None,
                 dataset: str = None,
                 dltype: str = None,
                 tunningname: str = None,
                 sig_name: str = None,
                 history_server_url: str = None) -> None:
        """
        Initialize a SparkApplicationDetail object.

        :param str sparkinstancegroupid: (optional) The Spark instance group ID.
        :param str applicationid: (optional) The Spark application ID.
        :param str applicationname: (optional) The Spark application name.
        :param str type: (optional) The Spark application type.
        :param str state: (optional) The Spark application state.
        :param str uiport: (optional) The port number on which to access the Spark
               application UI.
        :param DriverDetail driver: (optional)
        :param List[ExecutorDetail] executors: (optional) A list of Spark
               executors.
        :param int slots: (optional) The number of slots that are used by the Spark
               instance group.
        :param int demandslots: (optional) The number of demanded slots that is
               being used by the Spark application.
        :param int hosts: (optional) The number of hosts on which Spark
               applications run.
        :param float coresused: (optional) The number of CPU cores that are
               allocated to the Spark application.
        :param float memused: (optional) The amount of memory, in MB, that is used
               by the Spark application.
        :param str username: (optional) The user that executes the Spark
               application.
        :param str driverexecutionuser: (optional) The execution user for the Spark
               drivers.
        :param str executorexecutionuser: (optional) The execution user for the
               Spark executors.
        :param int timestamp: (optional) The time-stamp of the updated Spark
               application.
        :param int submittedtime: (optional) The Spark application submitted time.
        :param str master_url: (optional) The Spark master URL.
        :param int endtime: (optional) The Spark application finish time.
        :param str schedule_name: (optional) The application schedule name.
        :param str issharedapp: (optional) Specifies whether the Spark application
               shares RDD.
        :param float apprunduration: (optional) The application run duration.
        :param int master_seq_no: (optional) The master sequence number.
        :param str master_service: (optional) The master service name.
        :param str model: (optional) The deep learning model name.
        :param str dataset: (optional) The deep learning dataset name.
        :param str dltype: (optional) The deep learning framework name (e.g Caffe
               or TensorFlow).
        :param str tunningname: (optional) The deep learning tuning name.
        :param str sig_name: (optional) The Spark instance group name.
        :param str history_server_url: (optional) The Spark history server URL.
        """
        self.sparkinstancegroupid = sparkinstancegroupid
        self.applicationid = applicationid
        self.applicationname = applicationname
        self.type = type
        self.state = state
        self.uiport = uiport
        self.driver = driver
        self.executors = executors
        self.slots = slots
        self.demandslots = demandslots
        self.hosts = hosts
        self.coresused = coresused
        self.memused = memused
        self.username = username
        self.driverexecutionuser = driverexecutionuser
        self.executorexecutionuser = executorexecutionuser
        self.timestamp = timestamp
        self.submittedtime = submittedtime
        self.master_url = master_url
        self.endtime = endtime
        self.schedule_name = schedule_name
        self.issharedapp = issharedapp
        self.apprunduration = apprunduration
        self.master_seq_no = master_seq_no
        self.master_service = master_service
        self.model = model
        self.dataset = dataset
        self.dltype = dltype
        self.tunningname = tunningname
        self.sig_name = sig_name
        self.history_server_url = history_server_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SparkApplicationDetail':
        """Initialize a SparkApplicationDetail object from a json dictionary."""
        args = {}
        if 'sparkinstancegroupid' in _dict:
            args['sparkinstancegroupid'] = _dict.get('sparkinstancegroupid')
        if 'applicationid' in _dict:
            args['applicationid'] = _dict.get('applicationid')
        if 'applicationname' in _dict:
            args['applicationname'] = _dict.get('applicationname')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'uiport' in _dict:
            args['uiport'] = _dict.get('uiport')
        if 'driver' in _dict:
            args['driver'] = DriverDetail.from_dict(_dict.get('driver'))
        if 'executors' in _dict:
            args['executors'] = [ExecutorDetail.from_dict(x) for x in _dict.get('executors')]
        if 'slots' in _dict:
            args['slots'] = _dict.get('slots')
        if 'demandslots' in _dict:
            args['demandslots'] = _dict.get('demandslots')
        if 'hosts' in _dict:
            args['hosts'] = _dict.get('hosts')
        if 'coresused' in _dict:
            args['coresused'] = _dict.get('coresused')
        if 'memused' in _dict:
            args['memused'] = _dict.get('memused')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'driverexecutionuser' in _dict:
            args['driverexecutionuser'] = _dict.get('driverexecutionuser')
        if 'executorexecutionuser' in _dict:
            args['executorexecutionuser'] = _dict.get('executorexecutionuser')
        if 'timestamp' in _dict:
            args['timestamp'] = _dict.get('timestamp')
        if 'submittedtime' in _dict:
            args['submittedtime'] = _dict.get('submittedtime')
        if 'masterUrl' in _dict:
            args['master_url'] = _dict.get('masterUrl')
        if 'endtime' in _dict:
            args['endtime'] = _dict.get('endtime')
        if 'scheduleName' in _dict:
            args['schedule_name'] = _dict.get('scheduleName')
        if 'issharedapp' in _dict:
            args['issharedapp'] = _dict.get('issharedapp')
        if 'apprunduration' in _dict:
            args['apprunduration'] = _dict.get('apprunduration')
        if 'masterSeqNo' in _dict:
            args['master_seq_no'] = _dict.get('masterSeqNo')
        if 'masterService' in _dict:
            args['master_service'] = _dict.get('masterService')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        if 'dataset' in _dict:
            args['dataset'] = _dict.get('dataset')
        if 'dltype' in _dict:
            args['dltype'] = _dict.get('dltype')
        if 'tunningname' in _dict:
            args['tunningname'] = _dict.get('tunningname')
        if 'sigName' in _dict:
            args['sig_name'] = _dict.get('sigName')
        if 'historyServerUrl' in _dict:
            args['history_server_url'] = _dict.get('historyServerUrl')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SparkApplicationDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sparkinstancegroupid') and self.sparkinstancegroupid is not None:
            _dict['sparkinstancegroupid'] = self.sparkinstancegroupid
        if hasattr(self, 'applicationid') and self.applicationid is not None:
            _dict['applicationid'] = self.applicationid
        if hasattr(self, 'applicationname') and self.applicationname is not None:
            _dict['applicationname'] = self.applicationname
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'uiport') and self.uiport is not None:
            _dict['uiport'] = self.uiport
        if hasattr(self, 'driver') and self.driver is not None:
            _dict['driver'] = self.driver.to_dict()
        if hasattr(self, 'executors') and self.executors is not None:
            _dict['executors'] = [x.to_dict() for x in self.executors]
        if hasattr(self, 'slots') and self.slots is not None:
            _dict['slots'] = self.slots
        if hasattr(self, 'demandslots') and self.demandslots is not None:
            _dict['demandslots'] = self.demandslots
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = self.hosts
        if hasattr(self, 'coresused') and self.coresused is not None:
            _dict['coresused'] = self.coresused
        if hasattr(self, 'memused') and self.memused is not None:
            _dict['memused'] = self.memused
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'driverexecutionuser') and self.driverexecutionuser is not None:
            _dict['driverexecutionuser'] = self.driverexecutionuser
        if hasattr(self, 'executorexecutionuser') and self.executorexecutionuser is not None:
            _dict['executorexecutionuser'] = self.executorexecutionuser
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = self.timestamp
        if hasattr(self, 'submittedtime') and self.submittedtime is not None:
            _dict['submittedtime'] = self.submittedtime
        if hasattr(self, 'master_url') and self.master_url is not None:
            _dict['masterUrl'] = self.master_url
        if hasattr(self, 'endtime') and self.endtime is not None:
            _dict['endtime'] = self.endtime
        if hasattr(self, 'schedule_name') and self.schedule_name is not None:
            _dict['scheduleName'] = self.schedule_name
        if hasattr(self, 'issharedapp') and self.issharedapp is not None:
            _dict['issharedapp'] = self.issharedapp
        if hasattr(self, 'apprunduration') and self.apprunduration is not None:
            _dict['apprunduration'] = self.apprunduration
        if hasattr(self, 'master_seq_no') and self.master_seq_no is not None:
            _dict['masterSeqNo'] = self.master_seq_no
        if hasattr(self, 'master_service') and self.master_service is not None:
            _dict['masterService'] = self.master_service
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'dltype') and self.dltype is not None:
            _dict['dltype'] = self.dltype
        if hasattr(self, 'tunningname') and self.tunningname is not None:
            _dict['tunningname'] = self.tunningname
        if hasattr(self, 'sig_name') and self.sig_name is not None:
            _dict['sigName'] = self.sig_name
        if hasattr(self, 'history_server_url') and self.history_server_url is not None:
            _dict['historyServerUrl'] = self.history_server_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SparkApplicationDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SparkApplicationDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SparkApplicationDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The Spark application type.
        """
        BATCH = 'BATCH'
        NOTEBOOK = 'NOTEBOOK'


class StringMap():
    """
    StringMap.

    :attr str example_key: (optional)
    """

    def __init__(self,
                 *,
                 example_key: str = None) -> None:
        """
        Initialize a StringMap object.

        :param str example_key: (optional)
        """
        self.example_key = example_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StringMap':
        """Initialize a StringMap object from a json dictionary."""
        args = {}
        if 'example_key' in _dict:
            args['example_key'] = _dict.get('example_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StringMap object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'example_key') and self.example_key is not None:
            _dict['example_key'] = self.example_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StringMap object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StringMap') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StringMap') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TrainDetail():
    """
    TrainDetail.

    :attr str model: (optional) The deep learning model name.
    :attr str dataset: (optional) The dataset name.
    :attr TrainingParameters training_parameters: (optional)
    """

    def __init__(self,
                 *,
                 model: str = None,
                 dataset: str = None,
                 training_parameters: 'TrainingParameters' = None) -> None:
        """
        Initialize a TrainDetail object.

        :param str model: (optional) The deep learning model name.
        :param str dataset: (optional) The dataset name.
        :param TrainingParameters training_parameters: (optional)
        """
        self.model = model
        self.dataset = dataset
        self.training_parameters = training_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainDetail':
        """Initialize a TrainDetail object from a json dictionary."""
        args = {}
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        if 'dataset' in _dict:
            args['dataset'] = _dict.get('dataset')
        if 'trainingParameters' in _dict:
            args['training_parameters'] = TrainingParameters.from_dict(_dict.get('trainingParameters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        if hasattr(self, 'dataset') and self.dataset is not None:
            _dict['dataset'] = self.dataset
        if hasattr(self, 'training_parameters') and self.training_parameters is not None:
            _dict['trainingParameters'] = self.training_parameters.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TrainingParameters():
    """
    TrainingParameters.

    :attr str sig_id: (optional) The Spark instance group ID.
    :attr str sig_name: (optional) The Spark instance group name.
    :attr str sig_master_url: (optional) The Spark instance group master URL.
    :attr str driverid: (optional) The Spark driver ID.
    :attr str cmd: (optional) The training command.
    :attr str train_name: (optional) The deep learning training name.
    :attr str dl_framework: (optional) The deep learning framework name.
    :attr str status: (optional) The training status.
    :attr str appid: (optional) The Spark application ID.
    :attr str app_url: (optional) The Spark application URL.
    :attr str wt_url: (optional) The training weight file URL.
    :attr str wfinit: (optional) The initial weight file for training.
    :attr str wtfolder: (optional) The training weight file folder name.
    :attr int gpu_ratio: (optional) The gpu ratio.
    :attr str create_time: (optional) The time the training task was created.
    :attr str user: (optional) The user who created the training task.
    :attr int cluster_size: (optional) The number of workers in the cluster.
    :attr int test_interval: (optional) Number of training runs that are run in a
          test interval. At each test interval the model is run against the test dataset
          to verify that the accuracy is enough.
    :attr int test_iteration: (optional) Number of times that the model runs against
          the test dataset in each interval. For example, if the test interval is set to
          100 and the test iteration is set to 10, on the hundredth training run, the
          model will run against the test dataset 10 times.
    :attr str sync_mode: (optional) The gradient synchronization mode in elastic
          distributed training. This parameter specifies whether the training is a
          synchronous or asynchronous.
    :attr int progress: (optional) The progress.
    :attr str history_server_url: (optional) The Spark history server URL.
    """

    def __init__(self,
                 *,
                 sig_id: str = None,
                 sig_name: str = None,
                 sig_master_url: str = None,
                 driverid: str = None,
                 cmd: str = None,
                 train_name: str = None,
                 dl_framework: str = None,
                 status: str = None,
                 appid: str = None,
                 app_url: str = None,
                 wt_url: str = None,
                 wfinit: str = None,
                 wtfolder: str = None,
                 gpu_ratio: int = None,
                 create_time: str = None,
                 user: str = None,
                 cluster_size: int = None,
                 test_interval: int = None,
                 test_iteration: int = None,
                 sync_mode: str = None,
                 progress: int = None,
                 history_server_url: str = None) -> None:
        """
        Initialize a TrainingParameters object.

        :param str sig_id: (optional) The Spark instance group ID.
        :param str sig_name: (optional) The Spark instance group name.
        :param str sig_master_url: (optional) The Spark instance group master URL.
        :param str driverid: (optional) The Spark driver ID.
        :param str cmd: (optional) The training command.
        :param str train_name: (optional) The deep learning training name.
        :param str dl_framework: (optional) The deep learning framework name.
        :param str status: (optional) The training status.
        :param str appid: (optional) The Spark application ID.
        :param str app_url: (optional) The Spark application URL.
        :param str wt_url: (optional) The training weight file URL.
        :param str wfinit: (optional) The initial weight file for training.
        :param str wtfolder: (optional) The training weight file folder name.
        :param int gpu_ratio: (optional) The gpu ratio.
        :param str create_time: (optional) The time the training task was created.
        :param str user: (optional) The user who created the training task.
        :param int cluster_size: (optional) The number of workers in the cluster.
        :param int test_interval: (optional) Number of training runs that are run
               in a test interval. At each test interval the model is run against the test
               dataset to verify that the accuracy is enough.
        :param int test_iteration: (optional) Number of times that the model runs
               against the test dataset in each interval. For example, if the test
               interval is set to 100 and the test iteration is set to 10, on the
               hundredth training run, the model will run against the test dataset 10
               times.
        :param str sync_mode: (optional) The gradient synchronization mode in
               elastic distributed training. This parameter specifies whether the training
               is a synchronous or asynchronous.
        :param int progress: (optional) The progress.
        :param str history_server_url: (optional) The Spark history server URL.
        """
        self.sig_id = sig_id
        self.sig_name = sig_name
        self.sig_master_url = sig_master_url
        self.driverid = driverid
        self.cmd = cmd
        self.train_name = train_name
        self.dl_framework = dl_framework
        self.status = status
        self.appid = appid
        self.app_url = app_url
        self.wt_url = wt_url
        self.wfinit = wfinit
        self.wtfolder = wtfolder
        self.gpu_ratio = gpu_ratio
        self.create_time = create_time
        self.user = user
        self.cluster_size = cluster_size
        self.test_interval = test_interval
        self.test_iteration = test_iteration
        self.sync_mode = sync_mode
        self.progress = progress
        self.history_server_url = history_server_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingParameters':
        """Initialize a TrainingParameters object from a json dictionary."""
        args = {}
        if 'sigId' in _dict:
            args['sig_id'] = _dict.get('sigId')
        if 'sigName' in _dict:
            args['sig_name'] = _dict.get('sigName')
        if 'sigMasterUrl' in _dict:
            args['sig_master_url'] = _dict.get('sigMasterUrl')
        if 'driverid' in _dict:
            args['driverid'] = _dict.get('driverid')
        if 'cmd' in _dict:
            args['cmd'] = _dict.get('cmd')
        if 'trainName' in _dict:
            args['train_name'] = _dict.get('trainName')
        if 'dlFramework' in _dict:
            args['dl_framework'] = _dict.get('dlFramework')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'appid' in _dict:
            args['appid'] = _dict.get('appid')
        if 'appURL' in _dict:
            args['app_url'] = _dict.get('appURL')
        if 'wtURL' in _dict:
            args['wt_url'] = _dict.get('wtURL')
        if 'wfinit' in _dict:
            args['wfinit'] = _dict.get('wfinit')
        if 'wtfolder' in _dict:
            args['wtfolder'] = _dict.get('wtfolder')
        if 'gpuRatio' in _dict:
            args['gpu_ratio'] = _dict.get('gpuRatio')
        if 'createTime' in _dict:
            args['create_time'] = _dict.get('createTime')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'clusterSize' in _dict:
            args['cluster_size'] = _dict.get('clusterSize')
        if 'testInterval' in _dict:
            args['test_interval'] = _dict.get('testInterval')
        if 'testIteration' in _dict:
            args['test_iteration'] = _dict.get('testIteration')
        if 'syncMode' in _dict:
            args['sync_mode'] = _dict.get('syncMode')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'historyServerUrl' in _dict:
            args['history_server_url'] = _dict.get('historyServerUrl')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sig_id') and self.sig_id is not None:
            _dict['sigId'] = self.sig_id
        if hasattr(self, 'sig_name') and self.sig_name is not None:
            _dict['sigName'] = self.sig_name
        if hasattr(self, 'sig_master_url') and self.sig_master_url is not None:
            _dict['sigMasterUrl'] = self.sig_master_url
        if hasattr(self, 'driverid') and self.driverid is not None:
            _dict['driverid'] = self.driverid
        if hasattr(self, 'cmd') and self.cmd is not None:
            _dict['cmd'] = self.cmd
        if hasattr(self, 'train_name') and self.train_name is not None:
            _dict['trainName'] = self.train_name
        if hasattr(self, 'dl_framework') and self.dl_framework is not None:
            _dict['dlFramework'] = self.dl_framework
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'appid') and self.appid is not None:
            _dict['appid'] = self.appid
        if hasattr(self, 'app_url') and self.app_url is not None:
            _dict['appURL'] = self.app_url
        if hasattr(self, 'wt_url') and self.wt_url is not None:
            _dict['wtURL'] = self.wt_url
        if hasattr(self, 'wfinit') and self.wfinit is not None:
            _dict['wfinit'] = self.wfinit
        if hasattr(self, 'wtfolder') and self.wtfolder is not None:
            _dict['wtfolder'] = self.wtfolder
        if hasattr(self, 'gpu_ratio') and self.gpu_ratio is not None:
            _dict['gpuRatio'] = self.gpu_ratio
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['createTime'] = self.create_time
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'cluster_size') and self.cluster_size is not None:
            _dict['clusterSize'] = self.cluster_size
        if hasattr(self, 'test_interval') and self.test_interval is not None:
            _dict['testInterval'] = self.test_interval
        if hasattr(self, 'test_iteration') and self.test_iteration is not None:
            _dict['testIteration'] = self.test_iteration
        if hasattr(self, 'sync_mode') and self.sync_mode is not None:
            _dict['syncMode'] = self.sync_mode
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'history_server_url') and self.history_server_url is not None:
            _dict['historyServerUrl'] = self.history_server_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SyncModeEnum(str, Enum):
        """
        The gradient synchronization mode in elastic distributed training. This parameter
        specifies whether the training is a synchronous or asynchronous.
        """
        SYNC = 'SYNC'
        ASYNC = 'ASYNC'


class ValidateDetail():
    """
    ValidateDetail.

    :attr str modelname: (optional) The deep learning model name.
    :attr str data_set: (optional) The deep learning dataset name.
    :attr str status: (optional) The deep learning validation status.
    :attr str driver_id: (optional) The Spark driver ID.
    :attr str appid: (optional) The Spark application ID.
    :attr str app_url: (optional) The Spark application URL.
    :attr str history_server_url: (optional) The Spark history server URL.
    :attr ValidateParameters val_parameters: (optional)
    :attr ValidateOutPair out_pairs: (optional)
    """

    def __init__(self,
                 *,
                 modelname: str = None,
                 data_set: str = None,
                 status: str = None,
                 driver_id: str = None,
                 appid: str = None,
                 app_url: str = None,
                 history_server_url: str = None,
                 val_parameters: 'ValidateParameters' = None,
                 out_pairs: 'ValidateOutPair' = None) -> None:
        """
        Initialize a ValidateDetail object.

        :param str modelname: (optional) The deep learning model name.
        :param str data_set: (optional) The deep learning dataset name.
        :param str status: (optional) The deep learning validation status.
        :param str driver_id: (optional) The Spark driver ID.
        :param str appid: (optional) The Spark application ID.
        :param str app_url: (optional) The Spark application URL.
        :param str history_server_url: (optional) The Spark history server URL.
        :param ValidateParameters val_parameters: (optional)
        :param ValidateOutPair out_pairs: (optional)
        """
        self.modelname = modelname
        self.data_set = data_set
        self.status = status
        self.driver_id = driver_id
        self.appid = appid
        self.app_url = app_url
        self.history_server_url = history_server_url
        self.val_parameters = val_parameters
        self.out_pairs = out_pairs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValidateDetail':
        """Initialize a ValidateDetail object from a json dictionary."""
        args = {}
        if 'modelname' in _dict:
            args['modelname'] = _dict.get('modelname')
        if 'dataSet' in _dict:
            args['data_set'] = _dict.get('dataSet')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'driverId' in _dict:
            args['driver_id'] = _dict.get('driverId')
        if 'appid' in _dict:
            args['appid'] = _dict.get('appid')
        if 'appURL' in _dict:
            args['app_url'] = _dict.get('appURL')
        if 'historyServerUrl' in _dict:
            args['history_server_url'] = _dict.get('historyServerUrl')
        if 'valParameters' in _dict:
            args['val_parameters'] = ValidateParameters.from_dict(_dict.get('valParameters'))
        if 'outPairs' in _dict:
            args['out_pairs'] = ValidateOutPair.from_dict(_dict.get('outPairs'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValidateDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'modelname') and self.modelname is not None:
            _dict['modelname'] = self.modelname
        if hasattr(self, 'data_set') and self.data_set is not None:
            _dict['dataSet'] = self.data_set
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'driver_id') and self.driver_id is not None:
            _dict['driverId'] = self.driver_id
        if hasattr(self, 'appid') and self.appid is not None:
            _dict['appid'] = self.appid
        if hasattr(self, 'app_url') and self.app_url is not None:
            _dict['appURL'] = self.app_url
        if hasattr(self, 'history_server_url') and self.history_server_url is not None:
            _dict['historyServerUrl'] = self.history_server_url
        if hasattr(self, 'val_parameters') and self.val_parameters is not None:
            _dict['valParameters'] = self.val_parameters.to_dict()
        if hasattr(self, 'out_pairs') and self.out_pairs is not None:
            _dict['outPairs'] = self.out_pairs.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ValidateDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValidateDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValidateDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ValidateOutPair():
    """
    ValidateOutPair.

    :attr str name: (optional) The validation result pair name.
    :attr str value: (optional) The validation result pair value.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None) -> None:
        """
        Initialize a ValidateOutPair object.

        :param str name: (optional) The validation result pair name.
        :param str value: (optional) The validation result pair value.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValidateOutPair':
        """Initialize a ValidateOutPair object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValidateOutPair object from a json dictionary."""
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
        """Return a `str` version of this ValidateOutPair object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValidateOutPair') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValidateOutPair') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ValidateParameters():
    """
    ValidateParameters.

    :attr str val_name: (optional) The deep learning validation name.
    :attr str sig_id: (optional) Spark instance group ID.
    :attr str sig_name: (optional) Spark instance group name.
    :attr str sig_master_url: (optional) URL of the Spark master for the Spark
          instance group.
    :attr str create_time: (optional) The time the validation was created.
    :attr str user: (optional) The user who created the validation.
    :attr str train_name: (optional) Name of the training to validate.
    :attr List[str] metrics: (optional) The list of metrics.
    """

    def __init__(self,
                 *,
                 val_name: str = None,
                 sig_id: str = None,
                 sig_name: str = None,
                 sig_master_url: str = None,
                 create_time: str = None,
                 user: str = None,
                 train_name: str = None,
                 metrics: List[str] = None) -> None:
        """
        Initialize a ValidateParameters object.

        :param str val_name: (optional) The deep learning validation name.
        :param str sig_id: (optional) Spark instance group ID.
        :param str sig_name: (optional) Spark instance group name.
        :param str sig_master_url: (optional) URL of the Spark master for the Spark
               instance group.
        :param str create_time: (optional) The time the validation was created.
        :param str user: (optional) The user who created the validation.
        :param str train_name: (optional) Name of the training to validate.
        :param List[str] metrics: (optional) The list of metrics.
        """
        self.val_name = val_name
        self.sig_id = sig_id
        self.sig_name = sig_name
        self.sig_master_url = sig_master_url
        self.create_time = create_time
        self.user = user
        self.train_name = train_name
        self.metrics = metrics

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValidateParameters':
        """Initialize a ValidateParameters object from a json dictionary."""
        args = {}
        if 'valName' in _dict:
            args['val_name'] = _dict.get('valName')
        if 'sigId' in _dict:
            args['sig_id'] = _dict.get('sigId')
        if 'sigName' in _dict:
            args['sig_name'] = _dict.get('sigName')
        if 'sigMasterUrl' in _dict:
            args['sig_master_url'] = _dict.get('sigMasterUrl')
        if 'createTime' in _dict:
            args['create_time'] = _dict.get('createTime')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'trainName' in _dict:
            args['train_name'] = _dict.get('trainName')
        if 'metrics' in _dict:
            args['metrics'] = _dict.get('metrics')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValidateParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'val_name') and self.val_name is not None:
            _dict['valName'] = self.val_name
        if hasattr(self, 'sig_id') and self.sig_id is not None:
            _dict['sigId'] = self.sig_id
        if hasattr(self, 'sig_name') and self.sig_name is not None:
            _dict['sigName'] = self.sig_name
        if hasattr(self, 'sig_master_url') and self.sig_master_url is not None:
            _dict['sigMasterUrl'] = self.sig_master_url
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['createTime'] = self.create_time
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'train_name') and self.train_name is not None:
            _dict['trainName'] = self.train_name
        if hasattr(self, 'metrics') and self.metrics is not None:
            _dict['metrics'] = self.metrics
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ValidateParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValidateParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValidateParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AlgoDef():
    """
    algorithm definition.

    :attr str algorithm: The tuning algorithm. it can be build in algorithms like
          Random, Bayesian, Tpe, Hyperband and ExperimentGridSearch, or user installed
          algorithms.
    :attr int max_run_time: (optional) Max running time of the hpo task in munites,
          default -1(unlimited).
    :attr int max_job_num: (optional) Max number of training job to submitted for
          hpo task, default -1(unlimited).
    :attr int max_paralle_job_num: (optional) Max number of training job to run in
          parallel, default 1.
    :attr float hyperband_eta: (optional) hyperband eta value.
    :attr str objective: (optional) Optimize policy, one of minimize and maximize.
    :attr List[AlgoParams] algo_params: (optional) optional, additional algorithm
          parameters and it could be different for each algorithm.
    """

    def __init__(self,
                 algorithm: str,
                 *,
                 max_run_time: int = None,
                 max_job_num: int = None,
                 max_paralle_job_num: int = None,
                 hyperband_eta: float = None,
                 objective: str = None,
                 algo_params: List['AlgoParams'] = None) -> None:
        """
        Initialize a AlgoDef object.

        :param str algorithm: The tuning algorithm. it can be build in algorithms
               like Random, Bayesian, Tpe, Hyperband and ExperimentGridSearch, or user
               installed algorithms.
        :param int max_run_time: (optional) Max running time of the hpo task in
               munites, default -1(unlimited).
        :param int max_job_num: (optional) Max number of training job to submitted
               for hpo task, default -1(unlimited).
        :param int max_paralle_job_num: (optional) Max number of training job to
               run in parallel, default 1.
        :param float hyperband_eta: (optional) hyperband eta value.
        :param str objective: (optional) Optimize policy, one of minimize and
               maximize.
        :param List[AlgoParams] algo_params: (optional) optional, additional
               algorithm parameters and it could be different for each algorithm.
        """
        self.algorithm = algorithm
        self.max_run_time = max_run_time
        self.max_job_num = max_job_num
        self.max_paralle_job_num = max_paralle_job_num
        self.hyperband_eta = hyperband_eta
        self.objective = objective
        self.algo_params = algo_params

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlgoDef':
        """Initialize a AlgoDef object from a json dictionary."""
        args = {}
        if 'algorithm' in _dict:
            args['algorithm'] = _dict.get('algorithm')
        else:
            raise ValueError('Required property \'algorithm\' not present in AlgoDef JSON')
        if 'maxRunTime' in _dict:
            args['max_run_time'] = _dict.get('maxRunTime')
        if 'maxJobNum' in _dict:
            args['max_job_num'] = _dict.get('maxJobNum')
        if 'maxParalleJobNum' in _dict:
            args['max_paralle_job_num'] = _dict.get('maxParalleJobNum')
        if 'hyperbandEta' in _dict:
            args['hyperband_eta'] = _dict.get('hyperbandEta')
        if 'objective' in _dict:
            args['objective'] = _dict.get('objective')
        if 'algoParams' in _dict:
            args['algo_params'] = [AlgoParams.from_dict(x) for x in _dict.get('algoParams')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlgoDef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'algorithm') and self.algorithm is not None:
            _dict['algorithm'] = self.algorithm
        if hasattr(self, 'max_run_time') and self.max_run_time is not None:
            _dict['maxRunTime'] = self.max_run_time
        if hasattr(self, 'max_job_num') and self.max_job_num is not None:
            _dict['maxJobNum'] = self.max_job_num
        if hasattr(self, 'max_paralle_job_num') and self.max_paralle_job_num is not None:
            _dict['maxParalleJobNum'] = self.max_paralle_job_num
        if hasattr(self, 'hyperband_eta') and self.hyperband_eta is not None:
            _dict['hyperbandEta'] = self.hyperband_eta
        if hasattr(self, 'objective') and self.objective is not None:
            _dict['objective'] = self.objective
        if hasattr(self, 'algo_params') and self.algo_params is not None:
            _dict['algoParams'] = [x.to_dict() for x in self.algo_params]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AlgoDef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlgoDef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlgoDef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ObjectiveEnum(str, Enum):
        """
        Optimize policy, one of minimize and maximize.
        """
        MAXIMIZE = 'Maximize'
        MINIMIZE = 'Minimize'


class AlgoParams():
    """
    AlgoParams.

    :attr str name: Name of the search algorithm parameter name.
    :attr str value: Value for the corresponding algirhtm parameter.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a AlgoParams object.

        :param str name: Name of the search algorithm parameter name.
        :param str value: Value for the corresponding algirhtm parameter.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlgoParams':
        """Initialize a AlgoParams object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in AlgoParams JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AlgoParams JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlgoParams object from a json dictionary."""
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
        """Return a `str` version of this AlgoParams object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlgoParams') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlgoParams') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CsvDetail():
    """
    CsvDetail.

    :attr List[str] columns: (optional) A list of the column name.
    :attr List[str] index: (optional) A list of the index.
    :attr List[List[float]] data: (optional) The data.
    :attr str json_string: (optional) The Json string of the csv data.
    """

    def __init__(self,
                 *,
                 columns: List[str] = None,
                 index: List[str] = None,
                 data: List[List[float]] = None,
                 json_string: str = None) -> None:
        """
        Initialize a CsvDetail object.

        :param List[str] columns: (optional) A list of the column name.
        :param List[str] index: (optional) A list of the index.
        :param List[List[float]] data: (optional) The data.
        :param str json_string: (optional) The Json string of the csv data.
        """
        self.columns = columns
        self.index = index
        self.data = data
        self.json_string = json_string

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CsvDetail':
        """Initialize a CsvDetail object from a json dictionary."""
        args = {}
        if 'columns' in _dict:
            args['columns'] = _dict.get('columns')
        if 'index' in _dict:
            args['index'] = _dict.get('index')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        if 'JSONString' in _dict:
            args['json_string'] = _dict.get('JSONString')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CsvDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'columns') and self.columns is not None:
            _dict['columns'] = self.columns
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'json_string') and self.json_string is not None:
            _dict['JSONString'] = self.json_string
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CsvDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CsvDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CsvDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FixedHyperParam():
    """
    FixedHyperParam.

    :attr str name: Hyperparameter name, the same name will be used in the
          config.json so user model can load it.
    :attr str data_type: one of int, double, str.
    :attr str fixed_val: The same type with datatype specified, if dataTye=double,
          need fixedVal type doulbe.
    """

    def __init__(self,
                 name: str,
                 data_type: str,
                 fixed_val: str) -> None:
        """
        Initialize a FixedHyperParam object.

        :param str name: Hyperparameter name, the same name will be used in the
               config.json so user model can load it.
        :param str data_type: one of int, double, str.
        :param str fixed_val: The same type with datatype specified, if
               dataTye=double, need fixedVal type doulbe.
        """
        self.name = name
        self.data_type = data_type
        self.fixed_val = fixed_val

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FixedHyperParam':
        """Initialize a FixedHyperParam object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in FixedHyperParam JSON')
        if 'dataType' in _dict:
            args['data_type'] = _dict.get('dataType')
        else:
            raise ValueError('Required property \'dataType\' not present in FixedHyperParam JSON')
        if 'fixedVal' in _dict:
            args['fixed_val'] = _dict.get('fixedVal')
        else:
            raise ValueError('Required property \'fixedVal\' not present in FixedHyperParam JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FixedHyperParam object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'data_type') and self.data_type is not None:
            _dict['dataType'] = self.data_type
        if hasattr(self, 'fixed_val') and self.fixed_val is not None:
            _dict['fixedVal'] = self.fixed_val
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FixedHyperParam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FixedHyperParam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FixedHyperParam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResDef():
    """
    The deep learning tuning resource definition.

    :attr str framework: The deep learning framework.
    :attr str init_weight_path: (optional) Weight file path.
    :attr str maxiteration: The maximum iteration count.
    :attr str miniteration: (optional) The minimum iteration count, optional for
          hyperband, default value 1.
    :attr int batchsize: The batch size tuning parameter.
    :attr int gpu_num: (optional) The gpu number.
    :attr int worker_num: (optional) The number of workers in the cluster.
    :attr bool distribute: (optional) Whether using distribute mode.
    :attr str sync_mode: (optional) The gradient synchronization mode in elastic
          distributed training. This parameter to specify whether the training is a
          synchronous training, or an asynchronous training.
    :attr str resource_instance_id: (optional) Instance group id.
    """

    def __init__(self,
                 framework: str,
                 maxiteration: str,
                 batchsize: int,
                 *,
                 init_weight_path: str = None,
                 miniteration: str = None,
                 gpu_num: int = None,
                 worker_num: int = None,
                 distribute: bool = None,
                 sync_mode: str = None,
                 resource_instance_id: str = None) -> None:
        """
        Initialize a ResDef object.

        :param str framework: The deep learning framework.
        :param str maxiteration: The maximum iteration count.
        :param int batchsize: The batch size tuning parameter.
        :param str init_weight_path: (optional) Weight file path.
        :param str miniteration: (optional) The minimum iteration count, optional
               for hyperband, default value 1.
        :param int gpu_num: (optional) The gpu number.
        :param int worker_num: (optional) The number of workers in the cluster.
        :param bool distribute: (optional) Whether using distribute mode.
        :param str sync_mode: (optional) The gradient synchronization mode in
               elastic distributed training. This parameter to specify whether the
               training is a synchronous training, or an asynchronous training.
        :param str resource_instance_id: (optional) Instance group id.
        """
        self.framework = framework
        self.init_weight_path = init_weight_path
        self.maxiteration = maxiteration
        self.miniteration = miniteration
        self.batchsize = batchsize
        self.gpu_num = gpu_num
        self.worker_num = worker_num
        self.distribute = distribute
        self.sync_mode = sync_mode
        self.resource_instance_id = resource_instance_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResDef':
        """Initialize a ResDef object from a json dictionary."""
        args = {}
        if 'framework' in _dict:
            args['framework'] = _dict.get('framework')
        else:
            raise ValueError('Required property \'framework\' not present in ResDef JSON')
        if 'initWeightPath' in _dict:
            args['init_weight_path'] = _dict.get('initWeightPath')
        if 'maxiteration' in _dict:
            args['maxiteration'] = _dict.get('maxiteration')
        else:
            raise ValueError('Required property \'maxiteration\' not present in ResDef JSON')
        if 'miniteration' in _dict:
            args['miniteration'] = _dict.get('miniteration')
        if 'batchsize' in _dict:
            args['batchsize'] = _dict.get('batchsize')
        else:
            raise ValueError('Required property \'batchsize\' not present in ResDef JSON')
        if 'gpuNum' in _dict:
            args['gpu_num'] = _dict.get('gpuNum')
        if 'workerNum' in _dict:
            args['worker_num'] = _dict.get('workerNum')
        if 'distribute' in _dict:
            args['distribute'] = _dict.get('distribute')
        if 'syncMode' in _dict:
            args['sync_mode'] = _dict.get('syncMode')
        if 'resourceInstanceId' in _dict:
            args['resource_instance_id'] = _dict.get('resourceInstanceId')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResDef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'framework') and self.framework is not None:
            _dict['framework'] = self.framework
        if hasattr(self, 'init_weight_path') and self.init_weight_path is not None:
            _dict['initWeightPath'] = self.init_weight_path
        if hasattr(self, 'maxiteration') and self.maxiteration is not None:
            _dict['maxiteration'] = self.maxiteration
        if hasattr(self, 'miniteration') and self.miniteration is not None:
            _dict['miniteration'] = self.miniteration
        if hasattr(self, 'batchsize') and self.batchsize is not None:
            _dict['batchsize'] = self.batchsize
        if hasattr(self, 'gpu_num') and self.gpu_num is not None:
            _dict['gpuNum'] = self.gpu_num
        if hasattr(self, 'worker_num') and self.worker_num is not None:
            _dict['workerNum'] = self.worker_num
        if hasattr(self, 'distribute') and self.distribute is not None:
            _dict['distribute'] = self.distribute
        if hasattr(self, 'sync_mode') and self.sync_mode is not None:
            _dict['syncMode'] = self.sync_mode
        if hasattr(self, 'resource_instance_id') and self.resource_instance_id is not None:
            _dict['resourceInstanceId'] = self.resource_instance_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResDef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResDef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResDef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrameworkEnum(str, Enum):
        """
        The deep learning framework.
        """
        CAFFE = 'Caffe'
        TENSORFLOW = 'TensorFlow'
        PYTORCH = 'PyTorch'
        PYTORCHONELASTIC = 'PyTorchOnElastic'


    class SyncModeEnum(str, Enum):
        """
        The gradient synchronization mode in elastic distributed training. This parameter
        to specify whether the training is a synchronous training, or an asynchronous
        training.
        """
        SYNC = 'SYNC'
        ASYNC = 'ASYNC'


class SearchExperiment():
    """
    SearchExperiment.

    :attr int id: experiment id.
    :attr List[FixedHyperParam] fixed_hyper_params: List of hyperparameters used in
          this experiment training.
    """

    def __init__(self,
                 id: int,
                 fixed_hyper_params: List['FixedHyperParam']) -> None:
        """
        Initialize a SearchExperiment object.

        :param int id: experiment id.
        :param List[FixedHyperParam] fixed_hyper_params: List of hyperparameters
               used in this experiment training.
        """
        self.id = id
        self.fixed_hyper_params = fixed_hyper_params

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchExperiment':
        """Initialize a SearchExperiment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SearchExperiment JSON')
        if 'fixedHyperParams' in _dict:
            args['fixed_hyper_params'] = [FixedHyperParam.from_dict(x) for x in _dict.get('fixedHyperParams')]
        else:
            raise ValueError('Required property \'fixedHyperParams\' not present in SearchExperiment JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchExperiment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'fixed_hyper_params') and self.fixed_hyper_params is not None:
            _dict['fixedHyperParams'] = [x.to_dict() for x in self.fixed_hyper_params]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchExperiment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchExperiment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchExperiment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchGrid():
    """
    SearchGrid.

    :attr List[HpoExperiment] experiments: (optional)
    :attr HpoExperiment best: (optional)
    :attr int running: (optional) The total number of parallel running jobs.
    :attr int complete: (optional) The number of completed jobs.
    :attr int failed: (optional) The number of failed jobs.
    :attr str progress: (optional) The progress.
    :attr str duration: (optional) Run duration of this task.
    """

    def __init__(self,
                 *,
                 experiments: List['HpoExperiment'] = None,
                 best: 'HpoExperiment' = None,
                 running: int = None,
                 complete: int = None,
                 failed: int = None,
                 progress: str = None,
                 duration: str = None) -> None:
        """
        Initialize a SearchGrid object.

        :param List[HpoExperiment] experiments: (optional)
        :param HpoExperiment best: (optional)
        :param int running: (optional) The total number of parallel running jobs.
        :param int complete: (optional) The number of completed jobs.
        :param int failed: (optional) The number of failed jobs.
        :param str progress: (optional) The progress.
        :param str duration: (optional) Run duration of this task.
        """
        self.experiments = experiments
        self.best = best
        self.running = running
        self.complete = complete
        self.failed = failed
        self.progress = progress
        self.duration = duration

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchGrid':
        """Initialize a SearchGrid object from a json dictionary."""
        args = {}
        if 'experiments' in _dict:
            args['experiments'] = [HpoExperiment.from_dict(x) for x in _dict.get('experiments')]
        if 'best' in _dict:
            args['best'] = HpoExperiment.from_dict(_dict.get('best'))
        if 'running' in _dict:
            args['running'] = _dict.get('running')
        if 'complete' in _dict:
            args['complete'] = _dict.get('complete')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'duration' in _dict:
            args['duration'] = _dict.get('duration')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchGrid object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'experiments') and self.experiments is not None:
            _dict['experiments'] = [x.to_dict() for x in self.experiments]
        if hasattr(self, 'best') and self.best is not None:
            _dict['best'] = self.best.to_dict()
        if hasattr(self, 'running') and self.running is not None:
            _dict['running'] = self.running
        if hasattr(self, 'complete') and self.complete is not None:
            _dict['complete'] = self.complete
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchGrid object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchGrid') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchGrid') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
