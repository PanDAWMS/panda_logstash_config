# Installation Curator
* For installaion enter this command:
```
pip install elasticsearch-curator
```
* If Curator already installed and necessary update it, enter this command:
```
pip install -U elasticsearch-curator
```
# Configuration Curator
* Create a config file with a .yml extension (Default path for the config file /etc/curator/) for connection to ES server. And add the following code:
```
client:
  hosts:
    - es-atlas.cern.ch
  port: 9203
  url_prefix:
  use_ssl: True
  certificate:
  client_cert:
  client_key:
  aws_key:
  aws_secret_key:
  aws_region:
  ssl_no_validate: True
  http_auth: es-atlas:'********'
  timeout: 30
  master_only: False

logging:
  loglevel: INFO
  logfile:
  logformat: default
  blacklist: ['elasticsearch', 'urllib3']
```
* Create a action file with a .yml extension (Default path for the action file /etc/curator/). And add actions using the following template:
```
actions:
  1:
    action: ACTION1
    description: OPTIONAL DESCRIPTION
    options:
      option1: value1
      ...
      optionN: valueN
      continue_if_exception: False
      disable_action: True
    filters:
    - filtertype: *first*
      filter_element1: value1
      ...
      filter_elementN: valueN
    - filtertype: *second*
      filter_element1: value1
      ...
      filter_elementN: valueN
  2:
    action: ACTION2
    description: OPTIONAL DESCRIPTION
    options:
      option1: value1
      ...
      optionN: valueN
      continue_if_exception: False
      disable_action: True
    filters:
    - filtertype: *first*
      filter_element1: value1
      ...
      filter_elementN: valueN
    - filtertype: *second*
      filter_element1: value1
      ...
      filter_elementN: valueN
  3:
    action: ACTION3
    ...
  4:
    action: ACTION4
    ...
```
* All examples for each type of action you can find here: https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actions.html

# Using Curator

* You can start Curator and your action by running:
```
curator --config /etc/curator/config.yml /etc/curator/delete_indicies.yml    
```
* Note: If you are not too sure about the outcome of this execution, it is recommended to use the --dry-run option, which will simulate the actions taken but will not change anything in your cluster. Example:
```
curator --config /etc/curator/config.yml --dry-run /etc/curator/delete_indicies.yml
```
* If you want to automatically start the actions - use crontab. Add into path /etc/cron.d a new file for example 'curator' or into /etc/crontab file, the following line:
```
00 02 * * * root /usr/bin/curator --config /etc/curator/config.yml /etc/curator/delete_indicies.yml
```
