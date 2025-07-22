# Udacity Cloud DevOps using Microsoft Azure
## Project 3: Ensuring Quality Releases

### Description
This repo ..............

### Dependencies
- Azure account
- Azure CLI
- Terraform CLI
- JMeter
- Postman




# Configurations - Dev
## Python virtual environment
```zsh
python -m venv myvenv
source myvenv/bin/activate
```
## Selenium
```bash
pip install selenium
sudo ap-get install -y chromium-browser
```
or if on Mac
```zsh
pip install selenium
brew install chromium --no-quarantine
```

## Azure
```zsh
az login
```

## SSH Keys
```zsh
ssh-keygen -t rsa -f ~/.ssh/udacity_rsa 
cat ~/.ssh/udacity_rsa.pub
```
Then update ```terraform/modules/vm.tf``` as follows:
Local development
```zsh
admin_ssh_key {
  username = "adminuser"
  public_key = file("~/.ssh/id_rsa.pub")
}
```
Within the pipeline
```zsh
admin_ssh_key {
  username = "adminuser"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfy9OZMaglxczcucEIXRS/t2MEZvpi34YxcQaFlsYyoYqNKyGaJLeCaaCWWRE12LphaEi9+NOxgtgczluZcQFqoCue+lM0utuZWISv1A1oSuEsiPM92kdHsEvnbM6kEku4LkFFgT/w62ig2iZmQhDXip4/7H0JSbdYIx+xoDM4AQBHI9KWM/5TzkmT5njdN5xzmqxuDM4yy5apjuJbuhf63hj4Z3EMec095tgRFSv0K3uAaslW9c7woadTzLVEjqjJ8/cTfX1m1P92KI+a1w5vzDc5AIYJgI3yWNq/j/8XL3e62fZ8igFgoDIsH8DkXhHCjizWsz0o2Gd2Hsm4BHgRbltOPEX8SPW40OWQb+ytmywjqdmaGI6w4N9sNprB7qSMeTDLVO3jYr3olmG85/cJc/5MKKloOcdW4ZObUOgZxuNONO4SdOXGHh2ASC5mOsJ1g1VuwhYigt/e9InRIFnpVuoDkQ94NSaXej0tLqoQHHx9ZcF4LzOcxPcr7j6XysU= masonkeresty@Masons-MacBook-Pro.local"
}
```

## Env variables
Fill in load.sh
```zsh
source load_env.sh
```


## Storage Account
```zsh
## For Mac/Linux
## Assuming you are in the terraform/ directory in the starter code
chmod +x configure-tfstate-storage-account.sh
./configure-tfstate-storage-account.sh
```
Then copy the output values over to ```main.tf```
Example:
```zsh
    terraform {
        backend "azurerm" {
              storage_account_name = "tstate9592"
              container_name       = "tfstate"
              key                  = "test.terraform.tfstate"
              access_key           = "xxxxxx"
        }
	}
```
*Note: You cannot use ```terraform.tfvars``` for these values.*

## Terraform
Ensure all variables are set in ```terraform.tfvars``` then:
```zsh
## Assuming you are in the terraform/environments/test/ directory
terraform init
terraform import azurerm_resource_group.main /subscriptions/<subsription_id>/resourceGroups/Azuredevops
## Run "terraform init -upgrade" if you have changed the file contents/path
terraform plan -out "solution.plan"
terraform apply "solution.plan"
terraform state rm azurerm_resource_group.main
terraform destroy
```

~~*Note: In ```main.tf``` you will see the resource group location hard coded as ```southcentralus``` and that is because the Udacity Azure Cloud Portal set the location of the resource group, but the other resources would not deploy in the same location, so I used ```East US``` for all other resources.*~~


## Create Packer Image
Edit vars in ```packer.json```
 ```packer build ./packer.json```


## Do all steps from project 2

## Then
1. Install terraform extension
2. add storage account key in variables