resource "azurerm_service_plan" "test" {
  name                = "service-plan"
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  os_type             = "Windows"
  sku_name            = "S1" 
}

resource "azurerm_windows_web_app" "test" {
  name                = var.host_name
  location            = var.location
  resource_group_name = var.resource_group
  service_plan_id     = azurerm_service_plan.test.id


  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
  }

    site_config {
    always_on = false
  }

}
