# Azure GUIDS
variable "subscription_id" {
    description = "The Azure subscription ID"
}
variable "client_id" {
    description = "The Azure client ID"
}
variable "client_secret" {
    description = "The Azure client secret"
}
variable "tenant_id" {
    description = "The Azure tenant ID"
}

# Resource Group/Location
variable "location" {
    description = "The Azure location for resources"
    default = "southcentralus"
}

variable "resource_group_name" {
    description = "The name of the Azure resource group"
    default = "Azuredevops"
}

variable "application_type" {
    description = "The type of application being deployed"
    default = "myApplication"
}

# Network
variable virtual_network_name {
    description = "The name of the virtual network"
    default = "myVirtualNetwork"
}

variable address_space {
    description = "Value for address space"
    default = ["10.5.0.0/16"]
    type = list(string)
}

variable address_prefix_test {
    description = "Value for address prefix test"
    default = "10.5.1.0/24"
}


variable "prefix" {
  description = "The prefix which should be used for all resources."
  default = "ud"
}

variable "vm_count" {
  description = "Number of virtual machines to be deployed."
  default = 1
}

variable "tag_name" {
  description = "Tag name required on all resources."
  default = "project"
}

variable "tag_value" {
  description = "Tag value required on all resources."
  default = "project_3"
}

variable "admin_username" {
  description = "The administrator username for the virtual machines."
  default = "adminuser"
}

variable "public_key" {
  description = "The public SSH key for the administrator user."
}

variable "image_name" {
  description = "The ID of the source image to use for the virtual machines."
  default = "/subscriptions/456cc604-544c-45f8-99d0-c1b73aeec440/resourceGroups/AZUREDEVOPS/providers/Microsoft.Compute/images/myPackerImage"
}

