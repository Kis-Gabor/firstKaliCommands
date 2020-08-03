import os

def osCommands():
    commands = ['sudo echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list',
                "sudo apt-get update -y",
                "sudo apt-get upgrade -y",
                "sudo apt-get dist-upgrade -y",
                "sudo apt-get install tor -y",
                "sudo apt-get install git -y"]

    for command in commands:
        print("\n[+]",command,"\n")
        os.system(command)

if __name__ == "__main__":
    osCommands()