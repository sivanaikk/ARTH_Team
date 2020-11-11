import os


os.system("echo 'Welcome to Python Menu' | figlet -f cybermedium -d ./figletfonts40/ ")

from Docker import Docker 
from Ansible import Ansible
from AWS import AWS
from MachineLearning import MachineLearning
from Hadoop import Hadoop

os.system("echo   MAIN MENU | figlet -f wideterm -d ./figletfonts40/ ")

os.system("tput setaf 10")
print("Enter 1: Ansible \nEnter 2: AWS  \nEnter 3: Docker \nEnter 4: Hadoop \nEnter 5: Machine Learning \nEnter 6: Exit")

technology = int(input("Select Technology : "))

def main():
    if technology == 1:
        Ansible.Ansible()
    elif technology == 2:
        AWS.AWS()
    elif technology == 3:
        Docker.Docker()
    elif technology == 4:
        Hadoop.Hadoop()
    elif technology == 5:
        MachineLearning.MachineLearning()
    elif technology == 6:
        exit()
    else :
        print("Enter Correct Technology...")

if __name__ == "__main__":
    main()
