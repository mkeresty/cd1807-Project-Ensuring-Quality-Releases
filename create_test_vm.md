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


ssh azureuser@<publicIp> # 104.211.47.142

# Copied from dev portal
# make sure you use the link below to download, the one given is wrong


mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://download.agent.dev.azure.com/agent/4.259.0/vsts-agent-linux-x64-4.259.0.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser285335/ --work _work --projectname 'udproject' --auth PAT --token 123456 --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser285335/ --work _work --projectname 'udproject' --auth PAT --token 123456; ./run.sh; fi
```