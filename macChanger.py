#!/usr/bin/env python3
import platform, optparse, subprocess, re

def checkOS():
    if "Linux" in platform.system():
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
    
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)) #pythex.org

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return False

def macChanger(interface_name, new_mac):
    subprocess.call(["sudo", "ifconfig", interface_name, "down"])
    subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface_name, "up"])


if __name__ == "__main__":
    ch = checkOS()
    if ch:
        options = get_arguments()
        current_mac = get_current_mac(options.interface)
        if current_mac != False:
            print("[i] Current MAC: " + current_mac)
            macChanger(options.interface, options.new_mac)
            current_mac = get_current_mac(options.interface)
            if current_mac == options.new_mac:
                print("[+] MAC address was successfully changed to " + current_mac)
            else:
                print("[-] MAC address did not get changed!")
        else:
            print("[-] Could not read MAC address!")
    else:
        print("[-] Your OS is not linux!")