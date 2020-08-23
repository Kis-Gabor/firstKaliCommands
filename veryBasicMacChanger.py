#!/usr/bin/env python3
import platform, subprocess, time

def checkOS():
    if "kali" in platform.release():
        return True
    else:
        return False

def mac_addr_input():
    new_mac = input("Enter the new mac address => ")

    if ":" in new_mac:
        if len(new_mac) == 17:
            return new_mac
        else:
            exit("[-] Wrong mac address!")
    else:
        exit("[-] Wrong mac address!") 

def macChanger():
    subprocess.call("ifconfig", shell=True)
    #inputs
    interface_name= input("Interface name => ")
    new_mac = mac_addr_input()
    # interface down
    subprocess.call("sudo ifconfig " + interface_name + " down", shell=True)
    time.sleep(1)
    #mac address changing
    subprocess.call("sudo ifconfig " + interface_name + " hw ether " + new_mac, shell=True)
    time.sleep(1)
    #interface up
    subprocess.call("sudo ifconfig " + interface_name + " up", shell=True)
    subprocess.call("ifconfig", shell=True)


if __name__ == "__main__":
    ch = checkOS()
    if ch:
        macChanger()
    else:
        print("[-] Your OS is not Kali linux!")