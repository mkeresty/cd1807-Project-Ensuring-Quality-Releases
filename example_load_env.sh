# Azure variables
export RESOURCE_GROUP_NAME=""
export SUBSCRIPTION_ID=""
export TENANT_ID=""
export APPLICATION_ID=""
export SECRET_KEY=""

# Terraform variables
export TF_VAR_subscription_id=$SUBSCRIPTION_ID
export TF_VAR_client_id=$APPLICATION_ID
export TF_VAR_client_secret=$SECRET_KEY
export TF_VAR_tenant_id=$TENANT_ID
export TF_VAR_resource_group_name=$RESOURCE_GROUP_NAME
export TF_VAR_application_type=""
export TF_VAR_virtual_network_name=""
export TF_VAR_address_space='[ "" ]'
export TF_VAR_address_prefix_test=""
export TF_VAR_public_key=""
export TF_VAR_location=""

# Storage account variables
export STORAGE_ACCOUNT_NAME=""
export CONTAINER_NAME=""
export ARM_ACCESS_KEY=""

# Azure DevOps Service Connection variables
export AZURE_TOKEN=""
export AZURE_TOKEN_NAME=""

# Packer variables
export ARM_CLIENT_ID=$APPLICATION_ID
export ARM_CLIENT_SECRET=$SECRET_KEY
export ARM_SUBSCRIPTION_ID=$SUBSCRIPTION_ID
export ARM_LOCATION=$TF_VAR_location
export ARM_RESOURCE_GROUP_NAME=$RESOURCE_GROUP_NAME
export MANAGED_IMAGE_NAME=""