from os import listdir
from os.path import join
import pandas as pd
import csv

filename = 'data.csv'
with open(filename, 'w',encoding='utf-8', newline='') as f:
  w = csv.DictWriter(f,['id','spectogram_path','sentence'])
  w.writeheader()

folderPaths = 'speech_to_text\spectogramOutputs'
id_counter = 0
for folder in listdir(folderPaths):
    for file in listdir(join(folderPaths, folder)):
        with open(filename, 'a',encoding='utf-8', newline='') as f:
          w = csv.DictWriter(f,['id','spectogram_path','sentence'])
          fp = join(folderPaths,folder,file)
          fs = file.split('-')[1]
          ins = {}
          ins['id'] = id_counter
          ins['spectogram_path'] = fp
          ins['sentence'] = fs.replace('.png','')
          w.writerow(ins)
          del ins,fp,fs
          id_counter += 1