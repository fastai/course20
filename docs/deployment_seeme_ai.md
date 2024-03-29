# SeeMe.ai Deployment.

<div class="provider-logo">
  <img alt="SeeMe.ai" width="600" src="images/seeme_ai/seeme_ai.svg">
</div>

This is a quick guide to deploy your trained vision models in just a few steps using [SeeMe.ai](https://seeme.ai).

**NB**: SeeMe.ai is currently in pre-release. You can register for an account by following the steps below, and get 1000 predictions per month. However note that unreleased services like this one may be unstable, or may change in substantial ways, including major changes to pricing or quotas. SeeMe.ai has not announced any pricing plans as yet.

## Before you begin

If you prefer to have these steps in a Jupyter Notebook, have a look at the [Fast.ai Quick guide on Github](https://github.com/SeeMe-ai/fastai-quick-guides/blob/master/seeme-quick-guide-fastai-v2.ipynb).

## Setup

### Install the SDK

All you need to deploy your model is the Python SDK:

```bash
pip install --upgrade seeme
```

### Create a client

```Python
from seeme import Client

client = Client()
```

### Register an account

If you have not done so already, create an account

```Python
my_password =  # example: "supersecurepassword"
my_username =  # example: "janvdp"
my_email =  # example: "jan.vandepoel@seeme.ai"
my_firstname =  # example: "Jan"
my_name =  # example: "Van de Poel"

client.register(
  username=my_username,
  email=my_email,
  password=my_password,
  firstname=my_firstname,
  name=my_name
)
```

### Log in

```Python
client.login(my_username, my_password)
```

## Deploy your model

### Export your model for deployment

```Python
# Put your model in eval model
learn.model.eval()

# Export your model (by default your model will be exported to `export.pkl`)
learn.export()
```

### Get the application_id for your framework (version).
application_id = client.get_application_id(
    base_framework="pytorch",
    framework="fastai",
    base_framework_version=str(torch.__version__),
    framework_version=str(fastai.__version__),
    application="image_classification"
)

### Create a model
Create your model on SeeMe.ai

```Python
model_name = "My Model name"
description = "Created to be used..."

my_model = client.create_full_model({
    "name": model_name,
    "description": description,
    "application_id": application_id,
    "auto_convert": True
})
```

### Upload your model

```Python
client.upload_model(my_model["id"], str(learn.path))
```

## Use your model

Once your model is deployed, you can use it in a number of ways:

- [Web app](https://app.seeme.ai)
- [iOS - App Store](https://apps.apple.com/us/app/id1443724639)
- [Android - Play Store](https://play.google.com/store/apps/details?id=ai.seeme)
- [Python SDK](https://pypi.org/project/seeme/)

### On the web

You can also open the web app via [app.seeme.ai](https://app.seeme.ai/#/?filter=owned) and log in with your credentials.

You will see an overview of all your models as well as the public models that can be used by anyone.

Click on the model to start making predictions.

![seeme-ai-your-first-model-cats-dogs](images/seeme_ai/seeme-ai-first-model-cats-dogs-edit.png)

Here is what the detail screen looks like:

![SeeMe.ai first model detail screen](images/seeme_ai/seeme-ai-model-detail-screen.png)

Next:

- click on `select image`
- find an image you would like to classify
- click on analyze
- Look at `result` and `confidence` to see what the prediction is.

![SeeMe.ai model prediction example](images/seeme_ai/seeme-ai-model-prediction-example.png)

### iOS/Android

When you upload your trained model, SeeMe.ai automatically converts it to [ONNX](https://onnx.ai/), [TensorFlow Lite](https://www.tensorflow.org/lite) and [Core ML](https://developer.apple.com/documentation/coreml). This enables you to install and use your AI Model on your device, even when you are offline.

You can install the apps from the [iOS App Store](https://apps.apple.com/us/app/id1443724639) and [Android Play Store](https://play.google.com/store/apps/details?id=ai.seeme).

![SeeMe.ai mobile list of models](images/seeme_ai/seeme-ai-mobile-list-of-models.png)

On the model detail, you can take pictures with the camera or select from the gallery:

![SeeMe.ai model detail](images/seeme_ai/seeme-ai-mobile-model-detail.png)

And see what your model thinks:

![SeeMe.ai model prediction](images/seeme_ai/seeme-ai-model-prediction.png)

Once your model has made a prediction, you will see a green button name "Action". When clicking that button, you have a number of choices:

* search Google for your prediction
* search Wikipedia for your prediction
* Report a wrong prediction

![SeeMe.ai follow up action](images/seeme_ai/seeme-ai-mobile-action-selection.png)

When the model is available to be installed, you will see the install button on the top right:

![SeeMe.ai install model offline](images/seeme_ai/seeme-ai-mobile-model-install-offline.png)

Once installed, you can still switch between using the offline or online version of your model:

![SeeMe.ai switch between online and offline model](images/seeme_ai/seeme-ai-mobile-switch-online-offline.png)

### Python SDK

You can also use the [Python SDK](https://pypi.org/project/seeme/) to make predictions from basically anywhere, provided you have:

- SeeMe SDK installed
- Login credentials
- The 'id' of a deployed model
- An image to classiy

```Python
image_location = "data/images/image_to_predict.png"

result = client.inference(my_model["id"], image_location)
```

Print the results

```Python
print(result["prediction"])
print(result["confidence"])
```

## Share your model

Once you have tested your model, it is time to share it with friends.

Go back to the home page, and click the `edit` icon.

![SeeMe.ai edit your model](images/seeme_ai/seeme-ai-first-model-cats-dogs-edit.png)

You will go to the model detail screen:

![SeeMe.ai Model detail](images/seeme_ai/seeme-ai-model-detail.png)

There you can invite people by entering their email address.

Once invited, they will receive an email to either register (if that email is not yet associated to an account) or to notify them of your model being shared with them.

## Pricing

For pricing details, check the [pricing page](https://www.seeme.ai/pricing/).

## Status Page

An overview of the current status of SeeMe.ai: [status page](https://status.seeme.ai/). 

## Support / Feedback

Check out the [docs](https://docs.seeme.ai) for more details, managing models and datasets, and/or other supported applications.

For feedback, questions or problems, send an email to [support@seeme.ai](mailto:support@seeme.ai).
