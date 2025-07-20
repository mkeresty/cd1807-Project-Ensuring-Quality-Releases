az vm create \
  --resource-group Azuredevops \
  --name myTestVM \
  --image Ubuntu2204 \
  --generate-ssh-keys \
  --admin-username azureuser \
  --public-ip-sku Standard

ssh azureuser@<publicIp> # 4.150.41.65

mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://download.agent.dev.azure.com/agent/4.258.1/vsts-agent-linux-x64-4.258.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "test-vm" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284835/ --work _work --projectname 'Project 3 - Ensuring Quality Releases' --auth PAT --token 3QzWmOVsrzuFoE1ixocWpcB8QAw7zS2tIpq4zLbcvWWQot8oaDoNJQQJ99BGACAAAAAPDBwgAAASAZDOOogO --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "test-vm" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser284835/ --work _work --projectname 'Project 3 - Ensuring Quality Releases' --auth PAT --token 3QzWmOVsrzuFoE1ixocWpcB8QAw7zS2tIpq4zLbcvWWQot8oaDoNJQQJ99BGACAAAAAPDBwgAAASAZDOOogO; ./run.sh; fi