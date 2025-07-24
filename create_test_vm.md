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


ssh azureuser@<publicIp> # 20.225.176.199

# Copied from dev portal
mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://download.agent.dev.azure.com/agent/4.258.1/vsts-agent-linux-x64-4.258.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284917/ --work _work --projectname 'Udacity' --auth PAT --token 9YoPRrhuRTTupoBnjPprkGKryNeAPG9iQfdFM83pPrvpTxEneDTNJQQJ99BGACAAAAAPDBwgAAASAZDO1DKf --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284917/ --work _work --projectname 'Udacity' --auth PAT --token 9YoPRrhuRTTupoBnjPprkGKryNeAPG9iQfdFM83pPrvpTxEneDTNJQQJ99BGACAAAAAPDBwgAAASAZDO1DKf; ./run.sh; fi
```