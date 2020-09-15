# Use FastAI with Azure Machine Learning!
This repository has examples showing you how to use FastAI on Azure ML.

# Pricing
The suggested VM size is **Standard_NC6**, which costs $0.90/hour. The Standard NC6 is equipped with a on Nvidia K80 GPU. Read more about Azure Machine Learning pricing [here](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/). VMs are pay as you go, so you must [stop the VM](#Shutting-down-your-compute) to end the billing. In addition to the above costs for a VM, three additional resources will be deployed for the Azure Machine Learning Studio that will incur additional charges, [Azure Container Registry Basic account](https://azure.microsoft.com/en-ca/pricing/details/container-registry/), [Azure Block Blob Storage (general purpose v1)](https://azure.microsoft.com/en-ca/pricing/details/storage/blobs/) and [Key Vault](https://azure.microsoft.com/en-ca/pricing/details/key-vault/).

For those looking to use [Azure Spot Instance](https://docs.microsoft.com/en-us/azure/virtual-machines/spot-vms) instead of the Azure Machine Learning Studio mentioned below, follow these [instructions](https://forums.fast.ai/t/platform-azure/65527)

# Create an ML workspace
The [Azure Machine Learning workspace](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio) is the top-level resource for the service. It provides you with a centralized place to work with all the artifacts you create. 

You can create an ML workspace by clicking here - **specify a unique resource group name for your Azure subscription!**:

[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzureML-fastai%2Fmain%2F.cloud%2Fazuredeploy.json)

More details about deployment in the button used above, Check out [ARM JSON definition](https://github.com/Azure/AzureML-fastai/blob/main/.cloud/azuredeploy.json) and [Azure Machine Learning VM sizes](https://azure.microsoft.com/en-ca/pricing/details/machine-learning/)

# Quick FastAI Environment setup
1) Go to the Azure ML studio (https://ml.azure.com) and find your ML workspace.

2) On the left side, select **Notebooks**. Select any notebook located in the User files section on the left-hand side. If you don't have any notebooks there, first **create a notebook**

![Notebook](images/aml/click_notebook.png)

3) Select the Open terminal icon.
![Open Terminal](images/aml/open_terminal_full.png)

4) If you don't see the icon, select the ... to the right of the compute target and then select Open terminal .
![Open Terminal Mini](images/aml/open_terminal.png)

> **PRO-TIP: Copy and Paste in Terminal**
> * Windows: `Ctrl-c` to copy is supported but use `Shift-insert` to paste.
> * FireFox/IE may not support clipboard permissions properly.
> *    Mac OS: `Cmd-c` to copy and `Cmd-v` to paste.

5) Copy the following command to clipboard:
```shell
wget https://raw.githubusercontent.com/Azure/AzureML-fastai/main/fastaionAMLCI.sh
bash fastaionAMLCI.sh
```
If you don't already have fastai, then you have to wait for the libraries and dependencies to install. **Wait up to 10 mins** for this to complete and continue to the next step.

All of the notebook samples should now be cloned into the fastai folder and ready to run!

6) Refresh File Explorer to see all new files.

![Refresh File Explorer](images/aml/refresh_file_explorer.png)


7) If you didn't run into any errors, proceed to [Running FastAI Notebook section](#Running-FastAI-Notebooks)

# Manual FastAI Environment Setup
1) Use the terminal window to create a new environment. For example, the code below creates fastaienv and activate the environment:

```shell
conda create -y --name fastaienv
conda activate fastaienv
```

2) Install fastai, nbdev, pip and ipykernel package to the new environment and create a kernel for that conda env:
```shell
conda install -y pip
conda install -y ipykernel
conda install -y -c fastai -c pytorch fastai
conda install -y -c fastai fastbook
conda install -y -c fastai nbdev
```
If you don't already have fastai, then you have to wait for the libraries and dependencies to install. Wait up to 10 mins for this to complete and continue to the next step.

3) Create a kernel for that conda env:
```shell
python -m ipykernel install --user --name fastaienv --display-name "Python (fastaienv)"
```

4) Clone the [Fast AI Repo](https://github.com/fastai/fastai) with below snippet:
```shell
git clone https://github.com/fastai/fastai.git
```

All of the notebook samples should now be cloned into the fastai folder and ready to run!

5) Refresh File Explorer to see all new files.

![Refresh File Explorer](images/aml/refresh_file_explorer.png)

# Running FastAI Notebooks
1) Open a notebook in `fastai/nbs` you just cloned:

![Open Notebooks](images/aml/opennotebooks.png)

2) Always make sure you select the `Python (fastaienv)` Kernel:

![Fast AI Kernel](images/aml/select_fastaikernel.png)

3) Run all cells in Notebook:

![Run All](images/aml/run_all.png)

# Shutting down your compute
When you're down make sure you **stop your compute**! If you don't you'll keep getting charged until you click the stop compute button.
![Shutdown Compute](images/aml/shutdowncompute.png)

# Returning back to work
When you want to go back to your notebook exercises, just find the notebook in the AzureML Studio and hit **Play** on any cell.

It will take a few mins to reboot your compute and run you cell. Make sure you have selected the `Python (fastaienv)` kernel when you notebook is running.
