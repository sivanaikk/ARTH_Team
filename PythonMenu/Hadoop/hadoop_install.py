import os

# Install jdk-8u171-linux-x64.rpm  and  hadoop-1.2.1-1.x86_64.rpm 

javaFileID = '1SzsGGHsthag_AD8QWhzk1pW2JEAsaItI'
javaSoftware = 'Copy\ of\ jdk-8u171-linux-x64.rpm'
hadoopLink = 'https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm'
hadoopSoftware = 'hadoop-1.2.1-1.x86_64.rpm'
os.system("sudo yum install python3 -y")
os.system("sudo yum install python3-pip -y")
os.system("pip3 install gdown")
os.system("gdown --id  {0}".format(javaFileID))
os.system("sudo yum install wget -y")
os.system("wget {0}".format(hadoopLink))
os.system("sudo rpm -ivh {0}".format(javaSoftware))
os.system("sudo rpm -ivh {0} --force".format(hadoopSoftware))

