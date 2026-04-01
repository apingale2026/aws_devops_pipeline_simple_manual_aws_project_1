#!/bin/bash
# Pull latest image from ECR
ImageName=mypythonapp 
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin 533267311092.dkr.ecr.us-east-1.amazonaws.com

docker pull 533267311092.dkr.ecr.us-east-1.amazonaws.com/$ImageName:latest

# Run container
docker run -d --name myapp -p 80:80 533267311092.dkr.ecr.us-east-1.amazonaws.com/$ImageName:latest
