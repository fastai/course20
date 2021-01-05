# Use FastAI with Scaleway GPU Instances!
This repository has examples showing you how to use FastAI Scaleway GPU Instances.

# Pricing
Scaleway's "RENDER-S" [GPU Instances](https://www.scaleway.com/en/gpu-instances/) are billed at €1.00 per hour. They come with the following specifications: 

* Dedicated NVIDIA Tesla P100 16GB PCIe
* 10 Intel Xeon Gold 6148 cores (2.4 GHz)
* 45 GB RAM
* 400 GB SSD storage
* 1 Gbit/s of bandwidth

# Step 1: Signing up

Create your account on [console.scaleway.com](https://console.scaleway.com/register). You require a valid email address to confirm your account. 

# Step 2: Register your credit or debit card

Scaleway's services are postpaid. This means you receive a monthly invoice for your resource consumption. To be able to deploy resources, you have to register a valid credit or debit card in your account. 

> **Note:** When you register your card, a €2.00 transaction is made. This transaction comes with a validation code. It is required to validate the card in your Scaleway Console - once validated; the amount will be refunded to your card. 

## Step 3: Creating an SSH key.

You require an SSH key to access your GPU instance. An SSH key allows you to authenticate passwordless on **S**ecure **SH**ell connections. On computers running Linux or MacOS, you can create the SSH key direcly from a terminal: Type the following command `ssh-keygen -o -b 4096` and press Enter to generate the new key.

On computers running Windows, or if you prefer a graphical user interface, you can use a tool such as PuTTYgen to generate the key.

1 . Download [PuTTYgen]http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html to your local computer

2 . Launch [PuTTYgen by double-clicking on the application:

<img src="/images/scaleway/puttygenapp.webp" width="80" alt="" class="screenshot">

3 . Select **RSA**, set the number of bits in the key to **4096** and click the **Generate** button:

<img src="/images/scaleway/puttygen.webp" width="350" alt="" class="screenshot">

4 . Move the mouse around the blank area, as indicated, to generate some randomness:

<img src="/images/scaleway/puttygen_randomness.gif" width="350" alt="" class="screenshot">

5 . Two keys are generated (a public key that will be transferred on your instances, and a private key that you must keep secret):

<img src="/images/scaleway/puttygen_key.webp" width="350" alt="" class="screenshot">


* Fill-in the **Key-comment** field with a name to help you identify this key pair.
* Click the **Save public key** button and save it in the folder of your choice.
* Click the **Save private key** button and save it the same folder.
* Select the public key content. Copy it (below _Public key for pasting into OpenSSH authorized_keys file_) into your clipboard which is required for the following step.

6 . Go to your Scaleway Elements console and add the key to your Project.

Uoplad the content of the public key by clicking on Add a new SSH key on the Credentials tab of the Project Dashboard.

<img src="/images/scaleway/ssh-keys-settings.webp" width="700" alt="" class="screenshot">

A pop up appears. Paste the key in the indicated box, add a description, and click on **Add a SSH key**.

<img src="/images/scaleway/new-ssh-key.png" width="500" alt="" class="screenshot">

## Step 4: Requesting a GPU Instance quota increase

By default, your quota for "RENDER-S" instances is set to 0, and you will need to request a quota increase in order to create a GPU Instance. To increase your quota contact Scaleway's Trust&Safety Team by [ticket](https://console.scaleway.com/support/create).

## Step 5: Deploying your GPU Instance

1 . In the **Compute** section of the side menu in the Scaleway Elements console, click **Instances**. If you do not have an instance already created, the product presentation displays.

2 . Click **Create an instance**.

3 . Choose the Region for your GPU Instance. 

4 . Choose an Image for your instance: Click on the **GPU OS** tab and select **Ubuntu Bionic ML 10.2**

5 . Select an instance type: Click on the **GPU** tab and select **RENDER-S**

6 . Optionally, enter a custom name for your instance.

7 . Click **Create** to deploy your GPU Instance

## Step 6: Launching Jupyter Notebook

8 . Once your GPU instance is ready, connect to it using SSH to launch the Jupyter Notebook application:

```
ssh root@gpu-instance-ip
```
Start the Jupyter Notebook application by running the following command:

```
jupyter notebook --no-browser --port=8888 --allow-root
``` 

The flag `--no-browser` prevents opening the notebook in a browser after startup. The flag `--port=8888` specifies the port on which the notebook listens. It is possible to change this value to another port number if required.

If you start the application for the first time, a link with an authentication token displays. Keep a note of this link as you need it in a later stop:

```
Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=da97d8dfc8e409f2045da6ccb8685407644a409c2d51bc6e
```

9 . Open a local terminal and run the following command:

```
ssh -N -L localhost:7777:localhost:8888 root@gpu-instance-ip
```

The command above configures the port forwarding of the local port `7777` to the port `8888` on the GPU instance. This allows access to the Jupyter Notebook with a web browser from the local computer.

> Optional: Use the option `-f` in the command above to move SSH into the background, so the local terminal remains usable.

10 . Open a web browser and go to `http://localhost:7777`. Enter the authentication token and click login. The Jupyter Dashboard displays.


## Step 7: Download the course material

You can get your course material by cloning the GitHub repository. To do so, open a new terminal in Jupyter Notebook by clicking on **New** -> **Terminal**:

<img src="/images/scaleway/jupyter_terminal.png" width="700" alt="" class="screenshot">

Type the following command in the terminal to get the 2020 version of the course 'git clone https://github.com/fastai/course20'

<img src="/images/scaleway/jupyter_git.png" width="700" alt="" class="screenshot">

> **Note:** Alternatively, you can also run the command in a "classic" SSH terminal. 

## Step 8: Stopping your instance

To manage your expenses, you can archive your GPU instance when you are not using it. When the GPU instance is archived, only storage and your flexible IP address are billed. You can do this either from the Scaleway control panel by clicking the power button or by using the Scaleway [Command Line Interface](https://github.com/scaleway/scaleway-cli/): 

```
scw instance server stop <instance_id>
```

When you have finished the course; you can delete the GPU instance einter from the Scaleway Elements Console or by using the CLI: 

```
scw instance server delete <instance_id>
```