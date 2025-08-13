import scapy.all as scapy
from mac_vendor_lookup import MacLookup
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

mac_lookup = MacLookup()

def update_vendor_database():
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Updating MAC vendor database...")
    try:
        mac_lookup.update_vendors()
        print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Vendor database updated successfully.\n")
    except Exception as e:
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Could not update vendor database: {e}\n")

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        mac = element[1].hwsrc
        try:
            vendor = mac_lookup.lookup(mac)
        except:
            vendor = "Unknown Vendor"
        devices_list.append({"ip": element[1].psrc, "mac": mac, "vendor": vendor})
    return devices_list

def display(devices, previous_devices):
    print(f"\nCurrent Devices ({len(devices)} total) at {datetime.now().strftime('%H:%M:%S')}:")
    print("IP Address         MAC Address        Vendor")
    print("-" * 60)

    current_macs = {d["mac"] for d in devices}
    previous_macs = {d["mac"] for d in previous_devices}

    for device in devices:
        line = f"{device['ip']:<17} {device['mac']:<17} {device['vendor']}"
        if device["mac"] not in previous_macs:
            print(Fore.GREEN + line + Style.RESET_ALL)  # New device
        else:
            print(line)

    for old_device in previous_devices:
        if old_device["mac"] not in current_macs:
            line = f"{old_device['ip']:<17} {old_device['mac']:<17} {old_device['vendor']}"
            print(Fore.RED + line + Style.RESET_ALL)  # Removed device

def main():
    update_vendor_database()
    previous_devices = []
    while True:
        devices = scan("192.168.229.1/24")  # Change to your subnet
        display(devices, previous_devices)
        previous_devices = devices
        time.sleep(30)  # Sleep for 30 seconds, change if needed.

if __name__ == "__main__":
    main()
# netwatcher.py - A simple network watcher to monitor devices on a local network