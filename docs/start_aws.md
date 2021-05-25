---

title: AWS EC2
keywords:
sidebar: home_sidebar


---
# Welcome to AWS EC2

AWS EC2 provides preconfigured machine images called [DLAMI](https://aws.amazon.com/machine-learning/amis/), which are servers hosted by Amazon that are specially dedicated to Deep Learning tasks. Setting up an AWS EC2 instance, even with DLAMI, can be daunting. But don't worry, we got you covered. In fact, Amazon has a sweet [step by step guide](https://aws.amazon.com/getting-started/tutorials/get-started-dlami/) to set it up and we are going to draw heavily from their tutorial.

If you are returning to work and have previously completed the steps below, please go to the [returning to work](https://course.fast.ai/update_aws.html) section.

## Pricing
A `p2.xlarge` instance in Amazon which is what we suggest, is [$0.9 an hour](https://aws.amazon.com/ec2/instance-types/p2/).

## Step 1: Sign in or sign up

Visit the [AWS webpage](https://aws.amazon.com/) and click on 'Sign In to the Console'. If you do not have an account, the button to press will say 'Sign up' instead of 'Sign in to the Console'.

Next, enter your credentials if you are signing in, or e-mail, account name and password if you need to sign up. If you are signing up you will also need to set your credit card details. This will be the credit card to which all the charges of the instance usage will be applied (if you have free credits you will not be charged until they are over). Note that you will also need to provide a phone number that will be called to verify your identity.

## Step 2: Request service limit

If you just created your account, you'll need to ask for an increase limit in the instance type we need for the course (default is 0). First click on 'Services' and then 'EC2'.

<img alt="amiubuntu" src="/images/aws/ec2.png" class="screenshot">

Then on the left bar, choose Limits, then scroll through the list until you find g4dn.xlarge. You can skip this step if your limit is already 1 or more, otherwise click on 'Request limit increase'. Selecting 'Service Limit Increase', choose 'EC2 instance', your region, then 'g4dn.xlarge' and ask for a new limit of 1. Type the message '[FastAI] Limit Increase Request' in the use case description box, then select your preferred language and contact method before clicking 'Submit'. You should have an automatic reply telling you they'll look in your case, then an approval notice (hopefully in just a couple of hours).

<img alt="limit" src="/images/aws/increase_limit2.png" class="screenshot">

While you wait, get on with the third step.

## Step 3: Create an ssh key and upload it to AWS

For this step, you'll need a terminal. On Windows we strongly recommend using WSL for your terminal, which can be installed by following [these steps](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Once in your terminal, type 'ssh-keygen' then press return three times. This will create a directory named .ssh/ with two files in it, 'id_rsa' and 'id_rsa.pub'. The first one is your private key and you should keep it safe, the second one is your public key, that you will transmit to people you want to securely communicate with (in our case AWS).

On Windows, you will need to copy this public key in a Windows directory to easily access it (since it's created in the WSL home folder). The following line will copy it in 'C:\Temp', feel free to replace Temp with any directory you prefer.

``` bash
cp .ssh/id_rsa.pub /mnt/c/Temp/
```

Once you have made your ssh key, go back to the AWS console and make sure you are in the region in which you have requested your service limit increase. You can tell where you are by looking at the web address of your console. For example https://us-west-2.console.aws.amazon.com/ is the Oregon region, while https://ap-south-1.console.aws.amazon.com/ is the Mumbai region. You can change your region by choosing from the dropdown list to the right of your username in the top right corner of your screen.

Again, click on 'Services' and then 'EC2'.

<img alt="amiubuntu" src="/images/aws/ec2.png" class="screenshot">

You can also search for EC2 in the querry bar. Scroll in the left menu until you find 'Key pairs' then click on it.

<img alt="key pair" src="/images/aws/key_pair.png" class="screenshot">

On the new screen:

1. Click on the 'Import Key Pair' button
1. Browse to select the file id_rsa.pub from where you put it (either the '.ssh' folder of your home directory or the folder to where you copied it)
1. Customize the name of the key if you want, then click 'Import'

<img alt="import key" src="/images/aws/import_key.png" class="screenshot">

## Step 4: Launch an instance

Note that this step will fail at the end if you didn't get the approval for GPU instances, so you may have to wait a bit before starting it.

Log in to the AWS console then search for EC2 in the query bar or click 'EC2' in the services. Once on the EC2 screen, click launch instance.

<img alt="launch instance" src="/images/aws/launch_instance.png" class="screenshot">

Select Ubuntu 20.04.

Scroll down until you find 'g4dn.xlarge' and select it. Click "Next" until you get to the screen where you can choose your main partition size; change it from 8GB to at least 100GB. Finally, continue to the 'Review' tab press 'Launch'.

<img alt="launch" src="/images/aws/launch.png" class="screenshot">

In the pop-up window's first drop-down menu, select the key you created in step 2 then tick the box to acknowledge you have access to the selected private key file then click on 'Launch Instance'

<img alt="key" src="/images/aws/key.png" class="screenshot">

## Step 5: Connect to your instance

In the next window scroll down then click on 'View Instances'. You will see that you have an instance that says 'running' under 'Instance State'. Amazon charges you by the amount of seconds an instance has been running so you should **always stop an instance when you finish** using it to avoid getting extra charges. More on this, on Step 7.

You will have to wait a little bit for your instance to be ready while the light under instance state is orange.

<img alt="pending" src="/images/aws/pending.png" class="screenshot">

When it turns green, copy your instance IP in the IPv4 column.

<img alt="pubdns" src="/images/aws/pubdns.png" class="screenshot">

It's time to connect! Open your command line [terminal](/terminal_tutorial_) and type the following command:

    ssh ubuntu@<your-IP>

(Replace '\<your-IP\>' with your the IP address of your instance as shown before.)

You may be prompted about trusting this address, to which you should reply 'yes'.

## Step 6: Setup server

Now that you're logged in to your server, we can get it set up. First, we'll have it run some basic steps to secure and configure Ubuntu:

```
sudo apt update && sudo apt -y install git
git clone https://github.com/fastai/fastsetup.git
cd fastsetup
sudo ./ubuntu-initial.sh
```

Reboot when prompted. Then reconnect using ssh, but with an additional `-L` flag which will allow you to connect to Jupyter Notebook once it's installed:

    ssh -L localhost:8888:localhost:8888 ubuntu@<your-IP>

Install miniconda:

```
cd fastsetup
./setup-conda.sh
source ~/.bashrc
conda install -yq mamba
```

Next, find out which NVIDIA drivers you need:

    ubuntu-drivers devices

...and install them -- choose the "recommended" option, plus the `-server` suffix:

```
# "460" might be a different number, based on `ubuntu-drivers` output above
sudo apt-fast install -y nvidia-driver-460-server
sudo modprobe nvidia
nvidia-smi
```

Now you're ready to install all needed packages for the fast.ai course:

    mamba install -y fastbook

To download the notebooks, run:

    cd
    git clone https://github.com/fastai/fastbook

Next move into the directory where you will find the materials for the course by running:

    cd fastbook

Finally run

    jupyter notebook

You can access the notebook by clicking on the URL that is printed in your terminal, or by copying it and pasting it into your browser.

Go to the `app_jupyter.ipynb` to run the jupyter notebook tutorial. *Don't forget to stop your instance* when you're done, with the next step.

## Step 7: Stop your instance when you are done

When you finish working you must go back to your AWS console and stop your instance manually to avoid getting extra charges. A good practice is setting a reminder for yourself (when you close your computer or log off) so you never forget to do it!

<img alt="stop" src="/images/aws/stop.png" class="screenshot">

Note that you should press *Stop*, not *Terminate*. If you press *Terminate* it will remove your instance entirely and you will lose your work.
