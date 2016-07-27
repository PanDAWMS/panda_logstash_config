#Installation Filebeat

* Download and install the public signing key: 
```
sudo rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
```

* Create a file with a .repo extension (for example, beats.repo) in your /etc/yum.repos.d/directory and add the following lines:
```
[beats]
name=Elastic Beats Repository
baseurl=https://packages.elastic.co/beats/yum/el/$basearch
enabled=1
gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch
gpgcheck=1
```

* Your repository is ready to use. For example, you can install Filebeat by running:
```
sudo yum install filebeat
```
!!! If this command does not work - check you /etc/yum.conf file. And (if needed) add string reposdir=/etc/yum.repos.d/  at the end of a file. !!!
To configure the beat to start automatically during boot, run:
```
sudo chkconfig --add filebeat
```

* Download the filebeat configuration files into 
```
/etc/filebeat/filebeat.yml
```

* Manage the filebeat daemon
```
service filebeat stop/start/status
```

#Installation Logstash
* Download and install the public signing key: 
```
sudo rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
```

* Create a file with a .repo extension (for example logstash.repo) in your /etc/yum.repos.d/directory and add the following lines:
```
[logstash-2.3]
name=Logstash repository for 2.3.x packages
baseurl=https://packages.elastic.co/logstash/2.3/centos
gpgcheck=1
gpgkey=https://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
```

* Your repository is ready to use. For example, you can install Logstash by running:
```
sudo yum install logstash
```
!!! If this command does not work - check you /etc/yum.conf file. And (if needed) add string reposdir=/etc/yum.repos.d/  at the end of a file. !!!

* Download the logstash configuration files and filters into 
```
/etc/logstash/conf.d/*.conf
```

* Manage the logstash daemon
```
service logstash configtest/stop/start/status
Better not to use: /opt/logstash/bin/logstash -f /etc/logstash/conf.d &
```
