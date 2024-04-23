# aws_pulumi_yaml

This project deploys AWS infrastructure resources using Pulumi + Yaml


## Prerequisits

- Linux OS
- AWS account
- AWS user role with permission to create an EKS cluster (id (arn) of this role will be provided by eks_arn variable)
- created account at app.pulumi.com for remote backend
- manually created pulumi project and its directory should exist
```
mkdir pulumi-yaml-project
cd pulumi-yaml-project
# following templates can be used
pulumi new aws-yaml --name pulumi-yaml-project --description "yaml project" --stack initialstack 
```


## Install Pulumi

```
./install.sh
```


## Deploy project

```
cp deploy_project.py pulumi-yaml-project/
cd pulumi-yaml-project
pulumi login
export CUSTOMER=myapp
# to deploy ec2 vms in 3 stages test, dev, prod run the wrapper
python deploy_project.py --resource ec2
```


## Destroy project

```
pulumi stack select test
pulumi destroy
pulumi stack select dev
pulumi destroy
pulumi stack select prod
pulumi destroy
```


## Tested with

pulumi version v3.111.1  

