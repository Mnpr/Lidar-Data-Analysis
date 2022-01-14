"""
convert txt files to bin format
"""

import os
import sys
import os.path
import pickle
import struct

data_dir = '../data/pcd_txt/velodynevlp16/data_ascii/'
save_dir = '../data/npy_bin/bin/'


for file_name in os.listdir(data_dir):
 
    
    if file_name.split('.')[-1]!='txt':
        continue
    
    print(F'Processing {file_name} ... ')

    bin_filename=file_name.split('.txt')[0] +'.bin'
   
    txt_file=open(data_dir + file_name,'r') 
    bin_file=open(save_dir + bin_filename,'wb')

    lines=txt_file.readlines()
    
    for j,line in enumerate(lines):
        if j == 0:
            continue
        
        curLine=line.split(',')[1:4]                    # txt [1:4]  x,y,z
        curLine.append(line.split(',')[5])              # txt [5] intensity
        
        for i in range(len(curLine)):
            if len(curLine[i])==0:
                continue
            
            if i == 3:                                                # intensity
                parsedata = struct.pack("f",float(curLine[i]))        ## 这里可选择intensity用浮点数形式还是整型格式  you can choose intensity in float or int format
                # parsedata = struct.pack("i",int(curLine[i]))

                bin_file.write(parsedata)
            else:                                                     
                parsedata = struct.pack("f",float(curLine[i]))         
                bin_file.write(parsedata)

    bin_file.close()
    txt_file.close()
    
print(' ... Finished Processing')
