```zsh
az vm create \
  --resource-group Azuredevops \
  --name myTestVM \
  --image myPackerImage \
  --admin-username azureuser \
  --admin-password 'myTestVM@123' \
  --public-ip-sku Standard

az vm open-port \
  --resource-group Azuredevops \
  --name myTestVM \
  --port 22


ssh azureuser@<publicIp> # 172.211.43.120

# Copied from dev portal
# make sure you use the link below to download, the one given is wrong
mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://download.agent.dev.azure.com/agent/4.258.1/vsts-agent-linux-x64-4.258.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284939/ --work _work --projectname 'Udacity' --auth PAT --token EeeNoQHatFOUSPrmLRuIq7ZhQusFm2T9h6874KmKtdqX3vH8X07iJQQJ99BGACAAAAAPDBwgAAASAZDO3e8l --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284939/ --work _work --projectname 'Udacity' --auth PAT --token EeeNoQHatFOUSPrmLRuIq7ZhQusFm2T9h6874KmKtdqX3vH8X07iJQQJ99BGACAAAAAPDBwgAAASAZDO3e8l; ./run.sh; fi

# 108.143.104.254

```