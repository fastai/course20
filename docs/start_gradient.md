# Paperspace Gradient

![image](images/gradient/fastaiv4-gradient-new.jpg)

This is a quick guide to getting started with Deep Learning for Coders on Paperspace Gradient. With [Gradient](https://gradient.paperspace.com/), you get access to a Jupyter Notebook instance backed by a free GPU in less than 60 seconds, without any complicated installs or configuration. [Gradient](https://gradient.paperspace.com/) is built on top of [Paperspace](https://www.paperspace.com/), a GPU-accelerated cloud platform.

## Pricing

**Paperspace has a [Free Tier of free GPU and CPU instances](https://docs.paperspace.com/gradient/instances/free-instances).** To use them, choose *Free-GPU* or *Free-P5000* (recommended) in step 3.3 Create Notebook.

Note: Additional capacity and more powerful GPUs are available with paid instance types. Paid instances are billed while they're running and the rate is dependent on the [Instance Type](https://gradient.paperspace.com/instances) selected. Notebooks must be stopped to end billing.

## Step 1: Create an account

To get started, create an account [here](https://console.paperspace.com/signup?gradient=true) and confirm your account by clicking the verification link in your inbox.

## Step 2: Create a Project

In the sign up workflow you will be asked to create a project. Projects are used to organize all of the Gradient resources in one place. 

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/ProjectCreate.png)

## Step 3: Create Notebook

1. Open the project you created by clicking on the project tile. You can then click the Create button to start your first notebook. 

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/NoebookCreate.png)

2. Select the _Paperspace + Fast.AI_ base container in the Select a runtime section.

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/RuntimeSelector.png)

3. Select the type of machine you want to run on in the Select a machine section. You will be able to change this once you start the notebook meaning you can start out running on an inexpensive or free instance, and then, whenever you want, switch to a much more powerful instance to execute code as efficiently as possible. When you return to your notebook, the instance type will self-select to the instance type you most recently used. See the Stopping your Notebook section below for more information about choosing a new instance.

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/InstanceSelector.png)

4. Enter your payment details (if using a paid instance type). _Even if you have a promo or referral code, all paid instances require a valid credit card on file._

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/Payment.png)

5. Select an autoshutdown time period. This is how long the notebook instance will stay running before it shutsdown. All work will be saved when the instance is offline but cells can only be run when the instance is on. Note: All free instances have a max autoshutdown period of 6 hours. 

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/Autoshutdown.png)

6. Click Start Notebook. Your Notebook will then appear on your screen. Wait for the status at the top of the page to go from Setting up Image to Running, and then you will be ready to go :star2:.

![image](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/SettingUpNotebook.png)

Note: When you use paid instances, clicking Create Notebook will start your Notebook and your billing session will begin. To stop billing, you must stop your Notebook. 

## Step 4: Start learning Fast.ai!

From here it is as simple as clicking into the file in the file manager that you would like to run in the fast.ai course and begin or continue your journey.

If you would like to run the experience in Jupyter, then it is as easy as clicking the Jupyter icon at the bottom of the left-side menu when your notebook is online. To return to the Gradient platform from Jupyter just go back in your browser.

Go back to the [first page](https://course.fast.ai/index.html) to see how to use this notebook and run the notebook tutorial. Come back here once you're finished and _don't forget to stop your instance_ with the next step.

## Step 5: Stopping your Notebook

There are two ways to stop your notebook.

1. Click the Stop Instance button at the top of your notebook.

![stop1](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/StopNotebook.png)

2. Go to the Instance tab on the left menu and click stop instance. Note: Once your instance has stopped you can choose a new instance type to start your notebook on. Try something more powerful out to see how it impacts your notebook!

![stop2](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/StopInstance-menu.png)

Note: When using paid instances, you _will_ be charged for the time that your notebook is running. You must stop the notebook to stop incurring charges.

## Additional considerations:

### Managing Data

The `/storage` folder is your [Persistent Storage](https://docs.paperspace.com/gradient/data/storage#persistent-storage). Files placed here are available across all Notebooks, Jobs, and Linux VMs (currently free of charge). This repository is perfect for storing datasets, models etc. Note: Persistent Storage is region specific (you'll see the storage region options when creating Notebooks and Jobs).

### Sharing your notebook

Gradient Notebooks can be shared publicly so others can view and/or fork your work.  Just click the "share" button in the top right corner to get a shareable url.

![share](https://s3.amazonaws.com/ps.public.resources/img/fastai-v5/ShareNotebook.png)


### Viewing a stopped notebook

Gradient Notebooks can be viewed without running them. Just click open to view a static version of the notebook. Note: you may not see all of the files in your Notebook until you start the instance.

### Where to get help

Questions or issues related to course content, we recommend posting in the [fast.ai forum](http://forums.fast.ai/). 

For Paperspace-specific support, check out the rest of the [Gradient Docs](https://docs.paperspace.com/gradient/) or submit a support ticket with [this form](https://support.paperspace.com/hc/en-us/requests/new).

## Developing fastai on Gradient

If you would like to follow the [Developer guide for fastai](http://docs.fast.ai/dev-setup) and help develop the fastai library from your Gradient instance,
read this section first for some Gradient-specific recommendations.

> The Gradient terminal is easier to use if you first type `bash` after opening the terminal window. This will let you use the up/down arrows to explore command history, as well as use tab for text completion. To paste text into the prompt, use `ctrl-shift-v` in the terminal window. 

### Things to keep in mind before working through the section [Setting up access and `gh`](http://docs.fast.ai/dev-setup#Setting-up-access-and-gh):

Start with the _Paperspace + Fast.AI_ base container instance that you've already created.

Your gradient instance has miniconda, not anaconda, so follow the miniconda-specific instructions in the developer guide. For example, the first command of the developer guide should be `conda install -y -c fastai -c pytorch fastai gh nbdev`

If you are working through the Github SSH keygen tutorials and the `ssh-keygen` command doesn't work, you first need to install openssh-client on your Gradient instance. Type the commands 

    apt-get update
    apt-get upgrade
    apt-get install openssh-client

and then continue with the GitHub tutorial.

### Things to keep in mind before working through the section [Set up `fastcore`](http://docs.fast.ai/dev-setup#Set-up-fastcore):

Run these `clone` commands from the `/notebooks` directory, so the repos end up here next to the other ones.
