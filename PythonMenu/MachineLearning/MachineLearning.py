def MachineLearning():
    import os
    os.system("tput setaf 1")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system("tput setaf 4")
    name = "\"Machine Learning TUI\""
    os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/ ".format(name))
    os.system("tput setaf 118 ")
    os.system("echo ML TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
    os.system("tput setaf 10")
    print("\t\t\t\t\t\t\t\t...Do things of Machine Learning with a click")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system(" tput setaf 11 ")
    print("""
    Enter 1: To configure Jupyter Notebook 
    Enter 2: To configure Jupyter Notebook in Docker container

    Enter -2: To navigate to main Manu 
    Enter 0: To Terminate  
    """)

    os.system("tput setaf 4")
    ml = int(input("Select Option : "))
    os.system("tput setaf 7")
    if ml == 1:
        print("Configuring...")
    elif ml == 2:
        print("Configuring...")
    elif ml == -2:
        print("Enter to clear Screen..")
        os.system("clear")
        import main
    elif ml == 0:
        exit()
