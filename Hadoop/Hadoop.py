import os

dataNodeIPs = []
dataNodeUsers = [] 
count = 0 
keyPath = " "
nameNodeIP = " " #Just to declare Variables
nameNodeUser = " "


def Hadoop_Install(nodeIP,user):
    print("Installing Hadoop....")
    os.system("scp -i {2} ./Hadoop/hadoop_install.py {0}@{1}:/home/{0}/ ".format(user,nodeIP,keyPath))
    os.system("ssh -i {2}  {0}@{1} sudo yum install python3 -y   ".format(user,nodeIP,keyPath))
    os.system("ssh -i {2}  {0}@{1} python3 /home/{0}/hadoop_install.py ".format(user,nodeIP,keyPath))
    print("Hadoop Installed.")

def ConfigNamenode(nodeIP,user):
    print("Configuring Namenode....")
    os.system("ssh -i {2} {0}@{1} export MASTER_IP={3}".format(user,nodeIP,keyPath,nameNodeIP))
    os.system("ssh -i {2} {0}@{1} echo \"export MASTER_IP={3}\" >> ~/.bashrc".format(user,nodeIP,keyPath,nameNodeIP))
    os.system("scp  -i {2} ./Hadoop/config_files_nn.sh {0}@{1}:/home/{0}/".format(user,nodeIP,keyPath))
    os.system("ssh -i {2} {0}@{1} sudo chmod +x /home/(0)/config_files_nn.sh ".format(user,nodeIP,keyPath))
    os.system("ssh -i {2} {0}@{1} source /home/{0}/config_files_nn.sh".format(user,nodeIP,keyPath))

def ConfigDatanode(nodeIP,user):
    print("Configuring Datanode {0} ... ".format(nodeIP))
    os.system("ssh -i {2} {0}@{1} export MASTER_IP={3}".format(user,nodeIP,keyPath,nameNodeIP))
    os.system("ssh -i {2} {0}@{1} echo \"export MASTER_IP={3}\" >> ~/.bashrc".format(user,nodeIP,keyPath,nameNodeIP))
    os.system("scp  -i {2} ./Hadoop/config_files_dn.sh {0}@{1}:/home/{0}/ ".format(user,nodeIP,keyPath))
    os.system("ssh -i {2} {0}@{1} sudo chmod +x /home/{0}/config_files_dn.sh ".format(user,nodeIP,keyPath))
    os.system("ssh  -i {2}  {0}@{1} source /home/{0}/config_files_dn.sh ".format(user,nodeIP,keyPath))

def Hadoop():
    import os
    os.system("tput setaf 1")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system("tput setaf 4")
    name = "\"HADOOP TUI\""
    os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
    os.system("tput setaf 118 ")
    os.system("echo   HADOOP TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
    os.system("tput setaf 10")
    print("\t\t\t\t\t\t\t\t...Do things of Hadoop with a click")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system(" tput setaf 11 ")
    print("...Hadoop Main Menu...")
    print(
    """
    Enter 1: To configure Complete Cluster
    Enter 2: To configure Namenode
    Enter 3: To configure Datanode\n\n
    Enter -2: To exit to Main Menu
    Enter 0: To Terminate\n
    """)
    os.system("tput setaf 4")
    hadoop = int(input("Select the Option : "))
    os.system("tput setaf 7")
    if hadoop == 1:
        nameNodeIP = input("Enter Namenode IP : ")
        nameNodeUser = input("Enter Namenode UserName : ")
        dataNodeCount = int(input("Enter Number of Datanodes : "))
        for count in range(dataNodeCount):
            dataNodeIP = input("Enter Datanode {0} IP : ".format(count))
            dataNodeIPs.append(dataNodeIP)
            print(dataNodeIPs)
            dataNodeUser = input("Enter Datanode {0} Username : ".format(count))
            dataNodeUsers.append(dataNodeUser)
            print(dataNodeUsers)

        keyPath = input("Enter the SSH Key Path : ")
        Hadoop_Install(nameNodeIP,nameNodeUser) #Install Hadoop in Namenode
        ConfigNamenode(nameNodeIP,nameNodeUser) #Configure Namenode
        count = 0
        for count in range(dataNodeCount):
            print("Installing Hadoop in Datanode {0}...".format(count))
            Hadoop_Install(dataNodeIPs[count],dataNodeUsers[count]) #Install Hadoop in Datanode
            ConfigDatanode(dataNodeIPs[count],dataNodeUsers[count]) #Configure Namenode
    elif hadoop == 2:
        nameNodeIP = input("Enter Namenode IP : ")
        nameNodeUser = input("Enter Namenode UserName : ")
        Hadoop_Install(nameNodeIP,nameNodeUser) #Install Hadoop in Namenode
        ConfigNamenode(nameNodeIP,nameNodeUser) #Configure Namenode
    elif hadoop == 3:
        for count in range(dataNodeCount):
            dataNodeIP = input("Enter Datanode {0} IP : ".format(count))
            dataNodeIPs.append(dataNodeIP)
            print(dataNodeIPs)
            dataNodeUser = input("Enter Datanode {0} Username : ".format(count))
            dataNodeUsers.append(dataNodeUser)
            print(dataNodeUsers)
        count = 0
        for count in range(dataNodeCount):
            print("Installing Hadoop in Datanode {0}...".format(count))
            Hadoop_Install(dataNodeIPs[count],dataNodeUsers[count]) #Install Hadoop in Datanode
            ConfigDatanode(dataNodeIPs[count],dataNodeUsers[count]) #Configure Namenode
    elif(hadoop == -2):
        import main
        print("Returning to Main Menu...\n")
        input("Press: Enter to clear Screen")
        os.system("clear")
        main.main()
    elif(hadoop == 0):
        exit()

