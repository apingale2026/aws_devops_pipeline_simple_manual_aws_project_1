# AWS Simple Devops pipeline manually Project-1 

A simple devops pipeline where we will build an app and push it to ECR and then on EC2 we will pull and deploy this app

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

