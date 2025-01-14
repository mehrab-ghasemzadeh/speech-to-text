import pandas as pd
from os import listdir
from os.path import join, isfile
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import csv
from memory_profiler import memory_usage

def plot_spectrogram(Y, sr, hop_length, y_axis="log", fileName = '_'):
  try:
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.savefig(join('speech_to_text\spectogramOutputs\mozilla', f"{fileName}.png"))
    plt.close('all')
    plt.cla()
    plt.clf()
  except:
    print(f"couldn't create spectogram with the voice : {fileName}")

def create_spectogram(voice, name):
    try:
      file , sr = librosa.load(voice)
      FRAME_SIZE = 2048
      HOP_SIZE = 512
      s_file = librosa.stft(file, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
      Y_file = np.abs(s_file) ** 2
      Y_log_file = librosa.power_to_db(Y_file)
      plot_spectrogram(Y=Y_log_file, sr= sr, hop_length= HOP_SIZE, y_axis="log", fileName = name)
      del file, sr
      print(memory_usage())
    except:
      print(f"error on voice : {name}")

if __name__ == "__main__":    
  tsvPath = 'speech_to_text\common_voice_mozilla'
  tsvFiles = [f for f in listdir(tsvPath)[2:]]
  print(tsvFiles)
  i = 0
  for file in tsvFiles:
    try:
        df = pd.read_csv(join(tsvPath,file), sep='\t',quoting=csv.QUOTE_NONE)
        voicePaths = df.path
        nameIds = df.sentence_id
        del df, file
        for voicePath, nameId in zip( voicePaths, nameIds):
          create_spectogram(join('speech_to_text\common_voice_mozilla\clips',voicePath), f"{i}-{nameId}")
          print(i)
          i+=1
        del voicePaths, nameIds
    except:
      print(f"error on : {file}")
