import pandas as pd
from os import listdir
from os.path import join, isfile
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import io
from memory_profiler import memory_usage

def plot_spectrogram(Y, sr, hop_length, y_axis="log", fileName = '_'):
  try:
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.savefig(join('speech_to_text\spectogramOutputs\hugging_face', f"{fileName}.png"))
    plt.close('all')
    plt.cla()
    plt.clf()
  except:
    print(f"couldn't create spectogram with the voice : {fileName}")

def create_spectogram(voice, name):
    try:
      file , sr = librosa.load(io.BytesIO(voice['bytes']))
      FRAME_SIZE = 2048
      HOP_SIZE = 512
      s_file = librosa.stft(file, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
      Y_file = np.abs(s_file) ** 2
      Y_log_file = librosa.power_to_db(Y_file)
      plot_spectrogram(Y=Y_log_file, sr= sr, hop_length= HOP_SIZE, y_axis="log", fileName = name)
      del file, sr
      # print(memory_usage())
    except:
      print(f"error on voice : {name}")

if __name__ == "__main__":    
  path = 'speech_to_text\Persian_Common_Voice_17_0\data'
  files = [f for f in listdir(path)]
  i=0
  fileIter = iter(files)
  # for f in files:
  try:
    while True:
      f = next(fileIter)
      df = pd.read_parquet(join(path,f))
      audios = df.audio
      sentences = df.sentence
      print(f)
      del df, f
      for audio, sentence in zip(audios, sentences):
        create_spectogram(audio, f"{i}-{sentence}")
        print(i)
        i+=1
      del audios, sentences
  except:
    print(f"error on : file")