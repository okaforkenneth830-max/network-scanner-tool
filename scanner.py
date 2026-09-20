#!/usr/bin/env python3
"""
Simple Network Scanner Tool
By: Kenneth Okafor - Cybersecurity Enthusiast
"""

import socket
import sys
from datetime import datetime

def scan_ports(target, ports):
    print(f"\n[+] Scanning {target}")
    print(f"[+] Time started: {datetime.now()}")
    print("-" * 50)
    
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"[OPEN] Port {port}: {service}")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] You stopped the scan")
        sys.exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("[!] Could not connect to server")
        sys.exit()

if __name__ == "__main__":
    target = input("Enter target IP/domain: ")
    # Common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    scan_ports(target, common_ports)
    print("\n[+] Scan completed!")
