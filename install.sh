#!/bin/bash


echo "########## installing Pulumi..."

# This will install the pulumi CLI to ~/.pulumi/bin and add it to your path. 
curl -fsSL https://get.pulumi.com | sh



# or download binary
# Extract the tarball and move the binaries in the pulumi directory to a directory included in your systems $PATH


pulumi version

# You dont have to install anything else to write Pulumi programs in YAML.
