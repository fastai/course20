---
title: Returning to Sagemaker
keywords: 
sidebar: home_sidebar
---

To return to your notebook, the basic steps will be:

1. Start your instance
1. When done, shut down your instance

Your instance will run a script when started to update the fastai library and get the latest notebooks from the GitHub repository [here](https://github.com/fastai/course-v4).

## Step by step guide

### Start your instance

Log in to the [AWS console](https://aws.amazon.com/console/) then click on the Sagemaker link (it should be in your history, otherwise find it in the 'Services' on the left or type sagemaker in the search bar). Once on this page, select 'Notebook instances' on the left menu.

<img alt="" src="/images/sagemaker/notebooks.png" class="screenshot">

Tick the box of the notebook you want to start, then click on 'Start'.

<img alt="" src="/images/sagemaker/start.png" class="screenshot">


You will have to wait a little bit for your instance to be ready while the light under instance state is orange.

<img alt="pending" src="/images/sagemaker/16.png" class="screenshot">

When it turns green, just click on 'Open' and you'll be back to your notebooks.

<img alt="ready" src="/images/sagemaker/17.png" class="screenshot">

### Updating start script
Every time the Notebook instance is started it will run a [Lifecycle Configuration](https://aws.amazon.com/blogs/machine-learning/customize-your-amazon-sagemaker-notebook-instances-with-lifecycle-configurations-and-the-option-to-disable-internet-access/) script. To update the start script, select 'Lifecycle configurations', it's on the sidebar under notebooks, name that starts with *fastai-v4LifecycleConfig*. Select the **Edit** button and now you will be able to update the **Start notebook** script to perform custom actions.

### Stop your instance
When you finish working you must go back to your [AWS console](https://us-west-2.console.aws.amazon.com/sagemaker) and stop your instance manually to avoid getting extra charges. Just pick the notebook you want to stop and click on the 'Stop' button next to its name. You can configure your lifecycle configuration to automatically stop your notebook after some idle time. To do so add this [lifecycle config](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/blob/master/scripts/auto-stop-idle/on-start.sh) to the 'Start notebook' script.

<img alt="stop" src="/images/sagemaker/23.png" class="screenshot">

 **NOTE: you *will* be charged for the time that your instance is running.**
