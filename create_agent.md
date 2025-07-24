```zsh
az vm create \
  --resource-group Azuredevops \
  --name myLinuxVM \
  --image Ubuntu2204 \
  --admin-username devopsagent \
  --admin-password 'DevOpsAgent@123' \
  --public-ip-sku Standard \
  --size Standard_DS1_v2

az vm open-port \
  --resource-group Azuredevops \
  --name myLinuxVM \
  --port 22


ssh devopsagent@<publicIp> #4.150.13.18
sudo snap install docker
python3 --version
sudo groupadd docker
sudo usermod -aG docker $USER

# go to dev portal then click new agent in the pool settings
curl -O https://download.agent.dev.azure.com/agent/4.258.1/vsts-agent-linux-x64-4.258.1.tar.gz
mkdir myagent && cd myagent
tar -xzvf ../vsts-agent-linux-x64-4.258.1.tar.gz
./config.sh
# enter dev portal url : ex: https://dev.azure.com/odluser284917
# enter access token
# enter myPool name
# use default vm myLinuxVM
# use default work folder

sudo ./svc.sh install
sudo ./svc.sh start

sudo apt-get update
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get install python3.10-venv
sudo apt-get install python3-pip
sudo apt-get install python3.10-distutils
sudo apt-get -y install zip
pip install pylint==3.2.6
export PATH=$HOME/.local/bin:$PATH
```