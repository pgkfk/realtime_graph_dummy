#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time
from time import gmtime, strftime
from contextlib import closing

JSAPP_HOST = "127.0.0.1"
JSAPP_PORT = 8081
j = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
time.sleep(1)

base_time = time.time()

temp_arrays = [[]]
temp_arrays = [[
    36.0, 36.0, 36.5, 36.0, 36.0, 
    36.0, 36.0, 36.5, 36.0, 36.0, 
    36.0, 36.0, 36.0, 36.5, 36.5, 
    36.5, 36.0, 36.0, 36.5, 36.5, 
    36.0, 36.0, 36.5, 36.5, 36.5, 
    36.0, 36.0, 36.5, 36.0, 36.0, 
    36.0, 36.0, 37.5, 38.0, 39.0,
    39.0, 39.0, 39.0, 39.5, 39.5,],
[
    37.0, 37.5, 37.0, 37.0, 37.0, 
    37.0, 37.5, 37.5, 37.0, 37.0, 
    37.5, 37.0, 37.0, 37.5, 37.5, 
    37.5, 37.0, 37.0, 37.5, 37.5, 
    37.0, 37.5, 37.5, 37.0, 37.0, 
    37.0, 37.0, 37.0, 37.0, 37.0, 
    37.0, 37.0, 37.5, 37.0, 37.0,
    37.0, 37.0, 37.0, 37.5, 38.0,],
[
    35.5, 36.0, 35.5, 36.0, 36.0, 
    36.0, 36.5, 36.0, 35.5, 36.0, 
    36.0, 36.0, 36.0, 37.5, 37.5, 
    37.5, 37.0, 37.0, 37.5, 37.5, 
    37.0, 37.0, 37.5, 37.5, 37.5, 
    37.0, 37.0, 37.5, 37.0, 37.0, 
    37.0, 37.0, 37.5, 37.0, 37.0,
    37.0, 37.0, 37.0, 37.5, 37.5,
]
]

cnt = 0
###for html display
while True :
   id = 0
   for temp_array in temp_arrays:
      data = str(temp_array[min(cnt,39)]) + '_' + str(id)
      j.sendto(data, (JSAPP_HOST,JSAPP_PORT))
      id += 1
   # print temp_str
   time.sleep(1)
   cnt += 1

print "\ndone"
