# Deploy Fastai model to AWS Sagemaker with BentoML

This guide demonstrates how to deploy a chest X-ray image
classification model from [tutorial 61](https://github.com/fastai/fastai/blob/master/nbs/61_tutorial.medical_imaging.ipynb) to AWS Sagemaker with BentoML.

## Prerequisites

* An active AWS account configured on the machine with AWS CLI installed and configured
  * Install instruction: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
  * Configure AWS account instruction: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
* Docker is installed and running on the machine.
  * Install instruction: https://docs.docker.com/install
* Python 3.6 or above and required PyPi package: `bentoml`
  * `pip install bentoml`

## Build Fastai model server with BentoML

You can follow this tutorial [here](https://github.com/bentoml/gallery/blob/master/fast-ai/fastai2_medical/medical_imaging.ipynb).

Model serving with BentoML comes after a model is trained. The first step is creating a prediction service class,
which defines the models required and the inference APIs which contains the serving logic code.

```
# medical_image_service.py

from bentoml.frameworks.fastai import FastaiModelArtifact
from bentoml.adapters import FileInput
from fastcore.utils import tuplify, detuplify

import bentoml
import datablock_utils

@bentoml.artifacts([FastaiModelArtifact('learner')])
@bentoml.env(infer_pip_packages=True)
class FastaiMedicalImagingService(bentoml.BentoService):

    @bentoml.api(input=FileInput(), batch=False)
    def predict(self, file):
        files = [i.read() for i in files]
        dl = self.artifacts.learner.dls.test_dl([file.read()], rm_type_tfms=None, num_workers=0)
        inp, preds, _, dec_preds = self.artifacts.learner.get_preds(dl=dl, with_input=True, with_decoded=True)
        i = getattr(self.artifacts.learner.dls, 'n_inp', -1)
        inp = (inp,)
        dec_list = self.artifacts.learner.dls.decode_batch(inp + tuplify(dec_preds))
        res = []
        for dec in dec_list:
            dec_inp, dec_targ = map(detuplify, [dec[:i], dec[i:]])
            res.append(dec_targ)
        return res
```

The `@artifact(...)` here defines the required trained models to be packed with this prediction service.
BentoML model artifacts are pre-built wrappers for persisting, loading and running a trained model. For Fastai model use the `FastaiModelArtifact`.

The `@api` decorator defines an inference API, which is the entry point for accessing the prediction service. The input=FileInput() means this inference API callback function defined by the user, is expecting files as its input.

### Save model server for distribution

The following code packages the trained model with the prediction service class `FastaiMedicalImagingService` defined above, and then saves the `FastaiMedicalImagingService` instance to disk in the BentoML format for distribution and deployment:

```
# import the FastaiMedicalImagingService defined above
from medical_image_service import FastaiMedicalImagingService

# create a service instance
svc = FastaiMedicalImagingService()

# Pack the trained model artifact
svc.pack('leaner', learner)

# Save the model server to disk for model serving
saved_path = svc.save()
```

## Deploy to AWS Sagemaker

You need to provide the deployment name, BentoService information in the format of `name:version` and the API name to the deploy command `bentoml sagemaker deploy`.

BentoML handles containerizing the model, Sagemaker model creation, endpoint configuration and other operations for you.

*Example:*

```bash
$ bentoml sagemaker deploy my-first-deployment \
  -b FastaiMedicalImagingService:20201013153437_51E59E \
  --api-name predict

#Output
Deploying Sagemaker deployment
....
[2020-10-13 15:44:54,626] INFO - Successfully built 1efba0843a79
[2020-10-13 15:44:54,636] INFO - Successfully tagged 192023623294.dkr.ecr.us-west-2.amazonaws.com/fastaimedicalimagingservice-sagemaker:20201013153437_51E59E
|[2020-10-13 15:52:10,619] INFO - ApplyDeployment (my-first-deployment, namespace dev) succeeded
Successfully created AWS Sagemaker deployment my-first-deployment
{
  "namespace": "dev",
  "name": "my-first-deployment",
  "spec": {
    "bentoName": "FastaiMedicalImagingService",
    "bentoVersion": "20201013153437_51E59E",
    "operator": "AWS_SAGEMAKER",
    "sagemakerOperatorConfig": {
      "region": "us-west-2",
      "instanceType": "ml.m4.xlarge",
      "instanceCount": 1,
      "apiName": "predict",
      "timeout": 60
    }
  },
  "state": {
    "infoJson": {
      "EndpointName": "dev-my-first-deployment",
      "EndpointArn": "arn:aws:sagemaker:us-west-2:192023623294:endpoint/dev-my-first-deployment",
      "EndpointConfigName": "dev-my-first-dep-FastaiMedicalImaging-20201013153437-51E59E",
      "EndpointStatus": "Running",
      "CreationTime": "2020-10-13 15:52:10.554000-07:00",
      "LastModifiedTime": "2020-10-13 15:52:10.554000-07:00",
      "ResponseMetadata": {
        "RequestId": "b7eee60c-e621-4cde-b422-e774c0d11180",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
          "x-amzn-requestid": "b7eee60c-e621-4cde-b422-e774c0d11180",
          "content-type": "application/x-amz-json-1.1",
          "content-length": "311",
          "date": "Tue, 13 Oct 2020 23:02:08 GMT"
        },
        "RetryAttempts": 0
      }
    },
    "timestamp": "2020-10-13T23:02:08.898372Z"
  },
  "createdAt": "2020-10-13T22:38:16.868660Z",
  "lastUpdatedAt": "2020-10-13T22:38:16.868703Z"
}
```

## Update AWS Sagemaker deployment with BentoML

You can update the Sagemaker deployment with the latest trained model or change any of the configurations with `bentoml sagemaker update` command.

*Example:*

```
$ bentoml sagemaker update my-first-deployment \
  --instance-count 2
```

## Get deployments with BentoML

You can use `bentoml sagemaker get` to find out detailed information of the deployment.

Example:

```bash
$ bentoml sagemaker get my-first-deployment
```

Use `bentoml sagemaker list` to see all of the Sagemaker deployments

*Example:*

```bash
$ bentoml sagemaker list

#output
NAME                 NAMESPACE    PLATFORM       BENTO_SERVICE                                      STATUS    AGE
my-first-deployment  dev          aws-sagemaker  FastaiMedicalImagingService:20201013153437_51E59E  running     32 minutes and 38.48 seconds
```

## Clean up Sagemaker deployment with BentoML

BentoML cleans up resources when you want to delete your deployment.

*Example:*
```
$ bentoml sagemaker delete my-first-deployment
```
