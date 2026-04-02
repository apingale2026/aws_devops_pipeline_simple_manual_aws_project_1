# 📖 Project Overview
A simple yet practical DevOps project where we:
- Build a containerized web application (Flask-based To-Do app with CRUD functionality).
- Push the Docker image to **Amazon ECR** for secure storage.
- Deploy the application on **Amazon EC2**, pulling the image directly from ECR.
- Automate the process using **AWS CodePipeline, CodeBuild, and CodeDeploy** for CI/CD.
- 
##  Step1 Create a Repo locally, make directory a git directory and set username and email id and 


```bash
  # mkdir aws_devops_pipeline_simple_manual_aws_project_1
  # cd aws_devops_pipeline_simple_manual_aws_project_1
  # git init 
  # git config --global user.name "username"
  # git config --global user.email "username@gmail.com"
  # git remote add origin https://github.com/account_id/git_remote_repo.git
  #  git push -u origin main --> add token and authenticate
```
##  Step2 add app.py for simple todo list app 
##  Step3 Create Dockerfile to build images
##  Step4 Create IAM user with programmatic access
##  Step5 Create ECR Repo on AWS Console
##  Step6 Configure aws with credential and login to ECR
```bash
  # aws configure
  # aws ecr get-login-password --region us-east-1 \
| docker login --username AWS --password-stdin <account_id>.dkr.ecr.us-east-1.amazonaws.com
  # docker build -t python_app:to_do-v1 .
  # docker tag todo_list_app:latest 533267311092.dkr.ecr.us-east-1.amazonaws.com/devops/python_app:to_do-v1
  # docker push 533267311092.dkr.ecr.us-east-1.amazonaws.com/devops/python_app:to_do-v1
```
## Step7 Create EC2 Instance with userdata script added to install docker,codedeployagent and awscli 
## Step8 Create AWS CodePipeline for three stage 
### Stage1: Source Stage
- Add provider as Github app and create connection to your github account, it will install **AWS Connector for GitHub** in your github for integration
- Then select repository and branch name
- select output artifacts path
- create trigger via webhook for pipeline trigger after every push events
### Stage2: Build Stage 
- First in codeBuild create a build project in that select environment for your build work
- In pipeline build stage add filename for build i.e buildspec.yml
- Add input and output artifacts path to fetch and store artifacts respectively
### Stage3: Deploy Stage
- First in CodeDeploy create application and deployment group
- In deployment group add your instances key and value to add that instance in deployment group
- In pipeline deploy stage add application ,deployment group and Input artifacts source
- Add appspec.yml in your repo, so it will deploy based on it
## Step9 For every new update to repo pipeline is triggered 

# 🚀 Project Output
### 1. CI/CD Pipeline
Below is the screenshot of the AWS CodePipeline execution showing the automated build and deployment process:
<img width="957" height="451" alt="image" src="https://github.com/user-attachments/assets/72fe9df2-49d9-49a8-b9d7-6b453e5c1516" />
### 2. Final Deployed Web Application
Here is the final deployed To-Do web application with full CRUD functionality:
<img width="602" height="314" alt="image" src="https://github.com/user-attachments/assets/cc493854-ffbb-4310-b9e9-e8cd74088e07" />

