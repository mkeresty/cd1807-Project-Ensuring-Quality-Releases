resource "azurerm_app_service_plan" "test" {
  name                = "service-plan"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "test" {
  name                = "${var.host_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  app_service_plan_id     = azurerm_service_plan.test.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
  site_config {
    always_on = false
  }
}