provider "azurerm" {
  tenant_id       = "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = "southcentralus"
  lifecycle {
    prevent_destroy = true
  }
}


terraform {
  backend "azurerm" {
    storage_account_name = "tfstate1192918862"
    container_name       = "tfstate"
    key                  = "test.terraform.tfstate"
    access_key           = "mckkPt9bkMx97OH71LL+FzJpHpskATYTZTBIY1kPIho8LnyAzMNu0DPo/4HCbcaJpmUc8/0rGKm/+AStkfo/aw=="
  }
}

module "network" {
  source               = "../../modules/network"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  virtual_network_name = "${var.virtual_network_name}"
  application_type     = "${var.application_type}"
  resource_type        = "NET"
  resource_group       = azurerm_resource_group.main.name
  address_prefix_test  = "${var.address_prefix_test}"
}

module "nsg-test" {
  source           = "../../modules/networksecuritygroup"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "NSG"
  resource_group   = azurerm_resource_group.main.name
  subnet_id        = "${module.network.subnet_id_test}"
  address_prefix_test = "${var.address_prefix_test}"
}
module "appservice" {
  source           = "../../modules/appservice"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "AppService"
  resource_group   = azurerm_resource_group.main.name
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "publicip"
  resource_group   = azurerm_resource_group.main.name
}

module "vm" {
  source           = "../../modules/vm"
  location         = "${var.location}"
  resource_group   = azurerm_resource_group.main.name
  subnet_id        = "${module.network.subnet_id_test}" 
  vm_count         = "${var.vm_count}"
  prefix           = "${var.prefix}"
  tag_name         = "${var.tag_name}"
  tag_value        = "${var.tag_value}"
  admin_username   = "${var.admin_username}"
  public_key       = "${var.public_key}" 
}