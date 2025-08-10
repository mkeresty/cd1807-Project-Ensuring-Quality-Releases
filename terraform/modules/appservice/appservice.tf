resource "azurerm_app_service_plan" "test" {
  name                = "service-plan"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_windows_web_app" "test" {
  name                = var.host_name
  location            = var.location
  resource_group_name = var.resource_group
  service_plan_id     = azurerm_app_service_plan.test.id


  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
  }

    site_config {
    always_on = false
  }

}
