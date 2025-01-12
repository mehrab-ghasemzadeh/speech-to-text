import pandas as pd
from os import listdir
from os.path import join, isfile
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
# import io
from memory_profiler import memory_usage

def plot_spectrogram(Y, sr, hop_length, y_axis="log", fileName = '_'):
  try:
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.savefig(join('./speech_to_text\spectogramOutputs', f"{fileName}.png"))
    plt.close('all')
    plt.cla()
    plt.clf()
  except:
    print(f"couldn't create spectogram with the voice : {fileName}")

def create_spectogram(voice, name):
    try:
      # file , sr = librosa.load(io.BytesIO(voice['bytes']))
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
  tsvFileList = [
          'clip_durations.tsv',
          'dev.tsv',
          'invalidated.tsv',
          'other.tsv',
          'reported.tsv',
          'test.tsv',
          'train.tsv',
          'unvalidated_sentences.tsv',
          'validated.tsv',
          'validated_sentences.tsv'
        ]
  for file in listdir(tsvPath)[1:]:
    try:
        df = pd.read_csv(join(tsvPath,file), sep='\t')
        print(df)
  #     df = pd.read_parquet(join(path,file))
  #     audios = df.audio
  #     clientIds = df.client_id
  #     sentences = df.sentence
  #     print(file)
  #     del df, file
  #     for audio, clientId, sentence in zip(audios, clientIds, sentences):
  #       create_spectogram(audio, f"{i}-{clientId}")
  #       print(i)
  #       i+=1
  #     del audios, clientIds, sentences
    except:
      print(f"error on : {file}")
