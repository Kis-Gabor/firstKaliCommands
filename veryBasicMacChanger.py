#!/usr/bin/env python3
import platform, optparse, subprocess, time

def checkOS():
    if "kali" in platform.release():
        return True
    else:
        return False

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not options.new_mac:
        parser.error("[-] Please specify a new mac address, use --help for more info")
    return options
    

def macChanger(interface_name, new_mac):
    # interface down
    subprocess.call(["sudo", "ifconfig", interface_name, "down"])
    time.sleep(1)
    #mac address changing
    subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", new_mac])
    time.sleep(1)
    #interface up
    subprocess.call(["sudo", "ifconfig", interface_name, "up"])


if __name__ == "__main__":
    ch = checkOS()
    if ch:
        options = get_arguments()
        macChanger(options.interface, options.new_mac)
    else:
        print("[-] Your OS is not Kali linux!")