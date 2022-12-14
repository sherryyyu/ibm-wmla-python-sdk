[![Build Status](https://travis.ibm.com/CloudEngineering/python-sdk-template.svg?token=eW5FVD71iyte6tTby8gr&branch=master)](https://travis.ibm.com/CloudEngineering/python-sdk-template)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# IBM Watson Machine Learning Accelerator Elastic Distributed Inference Python SDK 

Python client library for IBM Watson Machine Learning Accelerator [IBM Watson Machine Learning Accelerator Inference APIs](https://www.ibm.com/docs/en/wmla/2.3?topic=workload-inference).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The Watson Machine Learning Accelerator Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[wmla](htt) | ElasticDistributedInferenceV2

## Compatibility: 

Version 0.0.1 is compatible with WMLA REST API 2.3.0

Version 0.1.x is compatible with WMLA REST API 2.3.7

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* Python 3.5.3 or above.

## Installation 

### Install with `pip`

```bash
pip install ibm-wmla
```

### Install from source

To install the package, clone this repository and 

```bash
cd ibm-wmla-python-sdk
pip install requirements.txt
pip install .
```

To debug,

```bash
cd ibm-wmla-python-sdk
pip install -r requirements.txt
python setup.py develop
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

## Setting up EDI service
```python
from ibm_wmla_client import Connection

service_url = "YOUR_SERVICE_URL:PORT"
service_instance = "YOUR_INSTANCE_NAME"
username = "YOUR_UNAME"
password = "YOUR_PW"

edi_connection = Connection(service_url, service_instance, wmla_v1=True, edi=True,
                 apikey=None, username=username, password=password, user_access_token = None)

edi_connection.connect()

conn = edi_connection.service_edi

# List models
response = conn.get_models()
print(response.result)

```

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](<github-repo-url>/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/master/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/master/LICENSE).
