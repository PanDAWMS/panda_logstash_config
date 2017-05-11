# Installation Filebeat 5.4

* Download and install the public signing key: 
```
sudo rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
```

* Create a file with a .repo extension (for example, beats.repo) in your /etc/yum.repos.d/directory and add the following lines:
```
[elastic-5.x]
name=Elastic repository for 5.x packages
baseurl=https://artifacts.elastic.co/packages/5.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

* Your repository is ready to use. For example, you can install Filebeat by running:
```
sudo yum install filebeat
```
* If you need to force the specific repository, e.g. in case some other repo is overwriting the versions:
```
yum repolist
yum --disablerepo=* --enablerepo=elastic-5.x install filebeat
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

# Installation Logstash 5.4
* Download and install the public signing key: 
```
sudo rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
```

* Create a file with a .repo extension (for example logstash.repo) in your /etc/yum.repos.d/directory and add the following lines:
```
[elastic-5.x]
name=Elastic repository for 5.x packages
baseurl=https://artifacts.elastic.co/packages/5.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
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
For start:
sudo initctl start logstash 
For stop:
sudo initctl stop logstash
For configtest:
/usr/share/logstash/bin/logstash -t -f /etc/logstash/conf.d
```
