# Deploying to Heroku with Voila

[Voila](https://voila.readthedocs.io/) is one of the quickest and easiest ways for you as a beginner to deploy your work. 
It works by transforming your Jupyter notebook into something like a webpage.

It is an option on various deployment platforms, one of which is [Heroku](http://www.heroku.com). 

Heroku gives you different options for how to create your web application, including proper web applications in Python, Ruby, PHP, Node.js etc. 
In this guide we are simply going to create a free account and deploy your first model using Voila and your Jupyter notebook.

# Prerequisites

You should have an exported model and a Jupyter notebook which functions as your demo. Chapter 2 of the fastai book discusses how to use Jupyter widgets to create a UI for your classifier demo.

# Getting started on Heroku

Create an account at [signup.heroku.com](http://signup.heroku.com/)...

# Creating your repo. What files do you need? What goes where?

You project needs to be in a [GitHub](https://github.com/) repo as Heroku will copy it from there, and the simplest way is to have everything you need in your repo. However, Heroku limits the size of the final "slug" (server image) to 500 MB, and that includes all of the libraries you use and their dependancies, so what you thought was quite a small project, may well be closer to the limit than you expect.

One way to reduce the size of your server image if you're having issues, is to store your model export (and any other large files your demo needs) on Google Drive or Dropbox or somewhere similar, and load them across from there.

``` Python
import urllib.request

MODEL_URL = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
urllib.request.urlretrieve(MODEL_URL, "model.pkl")

learner = load_learner(Path("."), "model.pkl")
```

The minimum you need in your repo is as follows:
- notebook.ipynb
- Procfile
- requirements.txt
