#!/bin/bash 
sudo mkdir /namenode
sudo sed '/<configuration>/a <property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>' -i /etc/hadoop/core-site.xml
#/etc.hadoop/hdfs-site.xml
sudo sed '/<configuration>/a <property>\n<name>dfs.name.dir</name>\n<value>/namenode</value>\n</property>' -i /etc/hadoop/hdfs-site.xml

sudo hadoop namenode -format
sudo hadoop-daemon.sh start datanode
