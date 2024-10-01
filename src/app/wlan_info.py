from psutil import *
import psutil
import socket

result = {"Interface": None, "MAC": None, "IP": None}

def get_wlan_info():
    """Get wlan Info"""
    machine_interface = net_if_addrs()
    #interface_stats = net_if_stats()

    for interface, addrs in machine_interface.items():
        if "wl" in interface.lower() or "wlan0" in interface.lower():
            result["Interface"] = interface

        for  addr in addrs:   
            if addr.family == psutil.AF_LINK:
                result["MAC"] = addr.address

            if addr.family == socket.AF_INET:
                result["IP"] = addr.address

    return result["IP"]