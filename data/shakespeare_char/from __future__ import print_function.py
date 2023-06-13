from __future__ import print_function
import io
import os
os.rename
with io.open(r'C:\Users\tansi\Downloads\nanoGPT-master\data\shakespeare_char\input.txt','r',encoding='utf-8',errors='ignore') as infile, \
     io.open(r'C:\Users\tansi\Downloads\nanoGPT-master\data\shakespeare_char\input.txt','w',encoding='ascii',errors='ignore') as outfile:
    for line in infile:
        print(*line.split(), file=outfile)