```zsh
az vm create \
  --resource-group Azuredevops \
  --name myTestVM \
  --image myPackerImage \
  --generate-ssh-keys \
  --admin-username azureuser \
  --admin-password 'myTestVM@123' \
  --public-ip-sku Standard

az vm open-port \
  --resource-group Azuredevops \
  --name myTestVM \
  --port 22


ssh azureuser@<publicIp> # 172.206.205.204

# Copied from dev portal
mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://download.agent.dev.azure.com/agent/4.258.1/vsts-agent-linux-x64-4.258.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284907/ --work _work --projectname 'Udacity Final' --auth PAT --token 2gVmKChNbWjJM3ToAHb1XD2DSpFYVji3MHwQcjuAD2rlfXcigIYTJQQJ99BGACAAAAAPDBwgAAASAZDO1oHd --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "myEnvironment" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284907/ --work _work --projectname 'Udacity Final' --auth PAT --token 2gVmKChNbWjJM3ToAHb1XD2DSpFYVji3MHwQcjuAD2rlfXcigIYTJQQJ99BGACAAAAAPDBwgAAASAZDO1oHd; ./run.sh; fi
```