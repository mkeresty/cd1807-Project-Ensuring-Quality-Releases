# Udacity Cloud DevOps using Microsoft Azure
## Project 3: Ensuring Quality Releases

### Description
This repo ..............

### Dependencies
- Azure account
- Azure CLI
- [Azure DevOps Portal](https://app.vssps.visualstudio.com/_signin)
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



# Production

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
```zsh
admin_ssh_key {
  username = "adminuser"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfy9OZMaglxczcucEIXRS/t2MEZvpi34YxcQaFlsYyoYqNKyGaJLeCaaCWWRE12LphaEi9+NOxgtgczluZcQFqoCue+lM0utuZWISv1A1oSuEsiPM92kdHsEvnbM6kEku4LkFFgT/w62ig2iZmQhDXip4/7H0JSbdYIx+xoDM4AQBHI9KWM/5TzkmT5njdN5xzmqxuDM4yy5apjuJbuhf63hj4Z3EMec095tgRFSv0K3uAaslW9c7woadTzLVEjqjJ8/cTfX1m1P92KI+a1w5vzDc5AIYJgI3yWNq/j/8XL3e62fZ8igFgoDIsH8DkXhHCjizWsz0o2Gd2Hsm4BHgRbltOPEX8SPW40OWQb+ytmywjqdmaGI6w4N9sNprB7qSMeTDLVO3jYr3olmG85/cJc/5MKKloOcdW4ZObUOgZxuNONO4SdOXGHh2ASC5mOsJ1g1VuwhYigt/e9InRIFnpVuoDkQ94NSaXej0tLqoQHHx9ZcF4LzOcxPcr7j6XysU= masonkeresty@Masons-MacBook-Pro.local"
}
```

## 


## Env variables
Fill in ``load_env.sh`` and rerun this command whenever you modify variables in it
```zsh
source load_env.sh
```
*Note the ``Azuredevops`` resource group location in the Azure developer portal*


## Storage Account
```zsh
## For Mac/Linux
## Assuming you are in the terraform/ directory in the starter code
chmod +x configure-tfstate-storage-account.sh
./configure-tfstate-storage-account.sh
```
Then copy the output values over to ```main.tf``` and to ```load_env.sh```
Example:
```zsh
    terraform {
        backend "azurerm" {
              storage_account_name = "tstate9592"
              container_name       = "tfstate"
              key                  = "test.terraform.tfstate"
        }
	}
```
*Note: You cannot use ```terraform.tfvars``` for these values.*

## Terraform
Ensure all variables are set in ```terraform.tfvars``` then:
```zsh
## Assuming you are in the terraform/environments/test/ directory
terraform init # add -reconfigure if you need to restart
terraform import azurerm_resource_group.main "/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP_NAME}"
## Run "terraform init -upgrade" if you have changed the file contents/path
terraform plan -out "solution.plan"
terraform apply "solution.plan"
terraform state rm azurerm_resource_group.main
terraform destroy
```


## Create Packer Image
Edit vars in ```packer.json```
 ```packer build ./packer.json```


## Azure DevOps Setup
- Go to [dev.azure.com](https://go.microsoft.com/fwlink/?LinkId=307137) and create a new project called `udacity_project`
- Go to **Project Settings** then **Service Connections** and **Azure Resource Manager**
- Click **App registration (automatic)** and fill in the required fields. Make sure you grant it access to all pipelines.
- In **User Settings** create a Personal Access Token and give it full access, then fill in and reload ```load_env.sh```
- Create new agent pool in **Project Settings > Agent pools** with type **self-hosted** and check **grant access permissions to all pipelines**
- Follow the steps in ```create_agent.md```. You will now see your agent online in the Dev Portal ![Agent Online](./screenshots/12_agent_online.png)
- Install Terraform extension from the marketplace
- Click **Create Pipeline** and then **Existing Azure Pipelines YAML file**
- Add ```ARM_ACCESS_KEY``` storage account key in pipeline variables NOT library
- Create a new pipeline environment virtual Linux machine and copy the command it provides, then follow the steps in ```create_test_vm.md```