import pyarrow.parquet as pq
# import pandas as pd
from os import listdir
from os.path import join
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import io

def plot_spectrogram(Y, sr, hop_length, y_axis="log", fileName = '_'):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.savefig(join('./dataSetSpectogramOutputs', f"{fileName}.png"))

def create_spectogram(filename: str) -> None:
  df = pq.read_table(source=filename).to_pandas() or None
  for audio,clientId in zip(df.audio, df.client_id):
    try:
      file, sr = librosa.load(io.BytesIO(audio['bytes']))
      FRAME_SIZE = 2048
      HOP_SIZE = 512
      s_file = librosa.stft(file, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
      Y_file = np.abs(s_file) ** 2
      Y_log_file = librosa.power_to_db(Y_file)
      plot_spectrogram(Y_log_file, sr, HOP_SIZE,'log', fileName= clientId)
    except:
      print(f"error on voice : {clientId}")
    del df

if __name__ == "__main__":    
  path = '.\Persian_Common_Voice_17_0\data'
  for file in listdir(path):
    try:
      create_spectogram(join(path,file))
    except:
      print(f'error on file : "{join(path,file)}"')