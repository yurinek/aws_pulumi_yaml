# to run this script:
# cp deploy_project.py dir_of_pulumi_project/
# cd dir_of_pulumi_project
# pulumi login
# export CUSTOMER=myapp
# python deploy_project.py --resource ec2

import os
import sys
import argparse
import shutil

# we use arguments to pass the value of types of aws resources to deploy
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--resource', help='resource to deploy in aws e.g. ec2')
# parse arguments otherwise show help
arg_value = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
print("deploying {}".format(arg_value.resource))


# we use var CUSTOMER instead of var PROJECT because projects already have their life in pulumi
try:  
   os.environ["CUSTOMER"]
except KeyError: 
   print ("Please set the environment variable CUSTOMER")
   sys.exit(1)

customer = os.environ["CUSTOMER"]
print("CUSTOMER: " + os.environ["CUSTOMER"])


# copy source code files
source = "../boilerplates/{}.yaml".format(arg_value.resource)
destination = "Pulumi.yaml"
shutil.copy(source, destination)


# Create infrastructure for every stage
stages = ["test", "dev", "prod"]
for stage in stages:
    print("########## Processing infrastructure for the following stage: " + stage + " ...")  

    os.system('pulumi stack init %s' % stage)
    os.system('pulumi stack select %s' % stage)
    os.system('pulumi stack ls')
    # config values are stored in Pulumi.<STACKNAME>.yaml
    os.system('pulumi config set customer %s' % customer)
    os.system('pulumi config set ami ami-080e1f13689e07408')
    # set config namespace to aws for standard aws vars
    os.system('pulumi config set aws:region us-east-1')
    os.system('pulumi preview')
    os.system('pulumi up --yes')
    os.system('pulumi stack')


