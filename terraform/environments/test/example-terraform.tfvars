# You don't need a terraform.tfvars file in the variables 
# are defined as env variables with the TF_VAR_ prefix.

# Azure subscription vars
subscription_id = ""
client_id = ""
client_secret = ""
tenant_id = ""

# Resource Group/Location
location = "East US"
resource_group_name = "Azuredevops"
application_type = "myApplication"

# Network
virtual_network_name = "myVirtualNetwork"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

public_key = "ssh-rsa AAAAB3Nz..."
image_name="/subscriptions/4123456/resourceGroups/AZUREDEVOPS/providers/Microsoft.Compute/images/myPackerImage"

