from scapy.all import *
import psutil
from collections import defaultdict
from threading import Thread
import pandas as pd
import time
import os


all_macs = {iface.mac for iface in ifaces.values()}

connection2pid = {}
pid2traffuc = defaultdict(lambda: [0, 0])
global_df = None
is_program_running = True
UPDATE_DELAY = 1

def get_size(bytes):

    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters()

bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    time.sleep(UPDATE_DELAY)
    io_2 = psutil.net_io_counters()

    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

    print(f"Upload: {get_size(io_2.bytes_sent)}   "
          f", Download: {get_size(io_2.bytes_recv)}   "
          f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
          f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
    
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv