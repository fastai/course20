# Deploying to Heroku with Voila

[Voila](https://voila.readthedocs.io/) is one of the quickest and easiest ways for you as a beginner to deploy your work. 
It works by transforming your Jupyter notebook into something like a webpage.

It is an option on various deployment platforms, one of which is [Heroku](http://www.heroku.com). Heroku gives you different options for how 
to create your web application, including proper web applications in Python, Ruby, PHP, etc but in this guide we are simply going to create a 
free account and deploy your first model using Voila and your Jupyter notebook.

## Prerequisites

You should have an exported model and a Jupyter notebook which functions as your demo. Chapter 2 of the fastai book discusses how to use Jupyter widgets to create a UI for your classifier demo. You will also need a [GitHub](https://github.com/) account so if you don't have one yet, go and sign up.

## Creating your GitHub repo. What do you need?

You project needs to be in a GitHub repository as we're going to tell Heroku to copy it from there, and the simplest way to get your demo deployed is to have *everything* you need in your repo (unless you start getting close to the size limit which we will discuss at the end).

The minimum you need in your repo is as follows:
- yournotebook.ipynb
- requirements.txt
- Procfile

But let's assume for now that you will not have any size issues and also include:
- Your model.pkl
- Any other files you use (eg: images to make your demo UI pretty)

### requirements.txt

When you deploy your application, Heroku builds a server image, essentially one giant file that it can quickly copy onto a server when someone wants to run your app. All of the packages you need must be specified in your requirements.txt. That means all of the things you `pip install` at the top of your notebook should be moved to here (plus any packages you use which your particular platform makes available by default).

The one big "gotcha" here is that you should use the CPU only versions of Pytorch for inference in your demo, because the GPU versions are *much* larger and do not fit within your 500 MB limit.

This is the minimum you should have in your requirements.txt file (I'm assuming that you are using Jupyter widgets for your UI).

```
https://download.pytorch.org/whl/cpu/torch-1.6.0%2Bcpu-cp36-cp36m-linux_x86_64.whl
https://download.pytorch.org/whl/cpu/torchvision-0.7.0%2Bcpu-cp36-cp36m-linux_x86_64.whl
fastai
voila
ipywidgets
```

NB: If you're still using fastai version 1 you can use `fastai==1.0.61` here instead.

### Procfile

Your Procfile (process file) only needs to contain 1 line, and it tells Heroku what kind of application to create. You have two choices when using Voila.

One specific notebook (if you only have one thing to deploy right now you want this one):
```
web: voila --port=$PORT --no-browser --enable_nbextensions=True yournotebook.ipynb
```

All the notebooks in your repo:
```
web: voila --port=$PORT --no-browser --enable_nbextensions=True
```

If you use the first option and specify a notebook name, your Heroku app will automatically load and run that notebook. If you want to host multiple demos at the same time, use the second option. If you do this then when somebody goes to the root of your Heroku app they will simply see a list of notebooks which they can click to run, but if you want to make this more inviting you can always provide a "homepage" named something obvious like README.ipynb or default.ipynb.


## Getting started on Heroku

Now you've got everything you need in GitHub, lets get it onto Heroku.

- Create an account at [signup.heroku.com](http://signup.heroku.com/)
- Once logged in you will be taken to your [dashboard](https://dashboard.heroku.com/apps), click `Create new app`
- Give it a name (this will be part of your URL), pick the region closest to you and click `Create app`
- On the next screen ignore the pipeline section at the top, and under "Deployment method" choose `GitHub` and then click the purple `Connect to GitHub` button which appears underneath.
- Once connected it will ask you for a repository to connect to. Enter your repo name here, click `Search` and then `Connect`
- You should then see a section titled "App connected to GitHub", followed by 2 sections where you can choose between automatic or manual deployment of a particular branch. If you are a beginner, we recommend automatic deployment of your master branch. This means it will automatically update your Heroku app if you make changes to your notebook in GitHub.

If you choose automatic deployment or press the `Deploy Branch` button now you'll see a build progress list as it gathers all of the libraries you need and compliles the server image we talked about earlier. Expect this to take a couple of minutes. Eventually you should see "https://yourappname.herokuapp.com/ deployed to Heroku" and your app is now ready to share with the world.

## 500 MB "slug" limit

Heroku limits the size of the final "slug" as they call it (the server image they create) to 500 MB, and that includes all of the libraries you use along with all of *their* dependancies, so what you thought was quite a small project, may well be closer to the limit than you expected. 

Most basic beginner projects should be fine but if you do need to reduce the size of your server image (especially once you start hosting multiple demo projects), you can store your model exports (and any other large files) on Google Drive or Dropbox or somewhere similar, and load them across from there.

``` Python
import urllib.request

MODEL_URL = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
urllib.request.urlretrieve(MODEL_URL, "model.pkl")

learner = load_learner(Path("."), "model.pkl")
```

## And finally

Don't forget to post your work on the [forum](https://forums.fast.ai/) in the [Share your V2 projects here](https://forums.fast.ai/t/share-your-v2-projects-here/65757/224) thread!
