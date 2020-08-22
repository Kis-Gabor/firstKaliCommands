import platform
import os

def checkOS():
    if "kali" in platform.release():
        return True
    else:
        return False

def osCommands():
    commands = ['sudo echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list',
                "sudo apt-get update -y",
                "sudo apt-get upgrade -y",
                "sudo apt-get dist-upgrade -y",
                "sudo gedit /etc/proxychains.conf",
                "sudo apt-get install tor -y",
                "sudo apt-get install git -y",
                "sudo apt-get install ncat -y",
                "sudo apt-get install mc -y",
                "sudo apt-get install links -y",
                "sudo apt-get install gcc -y",
                "sudo apt-get install rainbowcrack -y",
                "sudo apt-get install beef-xss -y",
                "sudo searchsploit --update",
                "sudo apt-get install pyrit -y",
                "sudo apt-get install hcxdumptool -y",
                "sudo apt-get install libssl-dev -y",
                "sudo apt-get install libz-dev -y",
                "sudo apt-get install libcurl4-openssl-dev -y",
                "sudo apt-get install libnetfilter-queue-dev -y",
                "sudo apt-get install libnfnetlink-dev -y",
                "sudo apt-get install foremost -y",
                "sudo apt-get install libimage-exiftool-perl -y",
                "sudo apt-get install edb-debugger -y",
                "sudo apt-get install dsniff -y"]

    for command in commands:
        print("\n[+]",command,"\n")
        os.system(command)

if __name__ == "__main__":
    ch = checkOS()
    if ch:
        osCommands()
    else:
        print("[-] Your OS is not Kali linux!")