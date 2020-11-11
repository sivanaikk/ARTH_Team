#!/bin/bash

sudo mkdir /datanode

# core-site.xml
sudo sed "/<configuration>/a <property>\n<name>fs.default.name</name>\n<value>hdfs://$MASTER_IP:9001</value>\n</property>" -i /etc/hadoop/core-site.xml

# hdfs-site.xml
sudo sed '/<configuration>/a <property>\n<name>dfs.data.dir</name>\n<value>/datanode</value>\n</property>' -i /etc/hadoop/hdfs-site.xml 

sudo hadoop-daemon.sh start namenode
