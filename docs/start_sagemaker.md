# Amazon SageMaker

This is a quick guide to starting v4 of the fast.ai course Practical Deep Learning for Coders using Amazon SageMaker. It assumes you already have an AWS account setup. If you do not then [follow the instructions here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) to create and activate your AWS account.

We will use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to provision all of the SageMaker resources including the Notebook instance, Notebook Lifecyle configuration and IAM role. By default it will provision a SageMaker notebook instance of type *ml.p2.xlarge* which has the Nvidia K80 GPU and 50 GB of EBS disk space.

## Pricing

The default instance type, ml.p2.xlarge, is $1.26 an hour. The hourly rate is dependent on the instance type selected, see all available types [here](https://aws.amazon.com/sagemaker/pricing/). You will need to explicitely request a service limit increase to use ml.p2.xlarge or the ml.p3.2xlarge instance, [here](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). Select limit type SageMaker and  in the request select the region you want to work in, SageMaker Notebooks & the instance type you are planning to use. Select a new limit value of 1, add a description and submit on the bottom right of the page. Instances must be stopped to end billing.

 <img alt="limitincrease" src="/images/aws/increase_limit_sagemaker.png" class="screenshot">

## Getting Set Up

### Creating the SageMaker Notebook Instance

1. We will create a [SageMaker Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) providing us the Jupyter notebook to run the course exercises by using [AWS CloudFormation](https://aws.amazon.com/cloudformation/). To launch the CloudFormation stack click the Launch Stack link for the closest region to where you live in the table below. 

    Region | Name | Launch link
    --- | --- | ---
    US West (Oregon) Region | us-west-2 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    US East (N. Virginia) Region | us-east-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    US East (Ohio) Region | us-east-2 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    US West (N. California) Region | us-west-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://us-west-1.console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)    
    Asia Pacific (Tokyo) Region | ap-northeast-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ap-northeast-1.console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    Asia Pacific (Seoul) Region | ap-northeast-2 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ap-northeast-2.console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    Asia Pacific (Sydney) Region | ap-southeast-2 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ap-southeast-2.console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    Asia Pacific (Mumbai) Region | ap-south-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ap-south-1.console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack) 
    Asia Pacific (Singapore) Region | ap-southeast-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)           
    Canada (central) Region | ca-central-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://ca-central-1.console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)       
    EU (Ireland) Region | eu-west-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    EU (Frankfurt) Region | eu-central-1 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://eu-central-1.console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)
    EU (London) Region | eu-west-2 | [![CloudFormation](/images/aws/cfn-launch-stack.png)](https://eu-west-2.console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/create/review?filter=active&templateURL=https://fastai-cfn.s3.amazonaws.com/sagemaker-cfn-course-v4.yml&stackName=FastaiSageMakerStack)    

1. This will open the AWS CloudFormation web console with the template to create the AWS resources as per the screenshot below. Take a look at the input parameters and either accept the defaults or update them as necessary. Select the option box **I acknowledge that AWS CloudFormation might create IAM resources.** and then click the **Create** button to create the stack.

    <img alt="create stack" src="/images/sagemaker/create_stack.png" class="screenshot">


1. You should be taken to the CloudFormation page where it shows that the stack status is CREATE_IN_PROGRESS. Wait for the stack status to change to **CREATE_COMPLETE**. After the stack has been created, open the SageMaker web console by selecting the Services menu item at the top left hand side of your AWS web console and entering the text “Sage” and then selecting the option Amazon SageMaker like the screenshot below.

   <img alt="sage" src="/images/sagemaker/01.png" class="screenshot">

1. On the left navigation bar, choose Notebook instances. This is where we create, manage, and access our notebook instances. You should see that your notebook instance named **fastai-v4** status has the status InService as per the screenshot below.

   <img alt="openjupyter" src="/images/sagemaker/open_juypter.png" class="screenshot">
   
   The first time the notebook instance is created it will install the fastai libraries and dependencies for the course which can take around 10 min.
   
### Working with the fastai course material

Once you click the Open Jupyter link you will be redirected to the Jupyter notebook web interface with the notebooks of the fastai course already installed.

<img alt="coursenotebooks" src="/images/sagemaker/course_notebooks.png" class="screenshot">

The first time you open any of the notebooks you will be asked to select the Jupyter kernel. Select the kernel named fastai in the drop down selection like the screenshot below and click the Set Kernel button.

<img alt="selectfastaikernel" src="/images/sagemaker/selectkernel.png" class="screenshot">

If you do not see the option fastai, then the libraries and dependencies have not yet finished installing. Wait up to 10 min for this to complete, refresh the page and try to select the fastai kernel.

### Shutting down your instance

- When you're done, close the notebook tab, and **remember to click stop!** If you don't, you'll keep getting charged until you click the *stop* button.

    <img alt="stop" src="/images/sagemaker/stop_instance.png" class="screenshot">


### Returning back to work

When you want to go back to the notebook exercises just select your notebook instance you can select the action Start, wait a few min and pick up where you left off. It will take less time to setup as the fastai libraries have already been installed and the notebooks will be saved.


## More help

For questions or issues related to course content, we recommend posting in the [fast.ai forum](http://forums.fast.ai/).
