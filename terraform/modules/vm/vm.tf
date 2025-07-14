resource "azurerm_network_interface" "main" {
  count               = var.vm_count
  name                = "${var.prefix}-nic-${count.index}"
  resource_group_name = "${var.resource_group}"
  location            = "${var.location}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    
  }
  tags = {
    "${var.tag_name}" = "${var.tag_value}"
  }
}
resource "azurerm_linux_virtual_machine" "main" {
  count                           = var.vm_count
  name                            = "${var.prefix}-vm-${count.index}"
  resource_group_name             = "${var.resource_group}"
  location                        = "${var.location}"
  size                = "Standard_B1s"
  admin_username      = "${var.admin_username}"
  network_interface_ids = [
    azurerm_network_interface.main[count.index].id,
  ]
    admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "${var.public_key}"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
