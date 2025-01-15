Trainning and fine tuning a transformer model with the persian_common_voice_17_0 and cv-corpus-20.0-2024-12-06-fa datasets from 


link to the datesets:

1:
https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0
to get and use the dataset you can:
git lfs install
git clone https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0

if you want to clone the pointers to the data set (not the large files) 
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0

2:
https://commonvoice.mozilla.org/fa/datasets
https://storage.googleapis.com/common-voice-prod-prod-datasets/cv-corpus-20.0-delta-2024-12-06/cv-corpus-20.0-delta-2024-12-06-fa.tar.gz?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gke-prod%40moz-fx-common-voice-prod.iam.gserviceaccount.com%2F20250111%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250111T060830Z&X-Goog-Expires=43200&X-Goog-SignedHeaders=host&X-Goog-Signature=272d00b915eab049149bd9a651f6b1fcc743d9d2afb82582c6fdd9c44d10cac184801fda931cf566a69e747901e983a94c8caab6610360ce0f6ade530bbd26e6686221eef6c1de7e435f00a74957d5234733944b00f987abe4ba8c060958b37324d849a345d2d4ff45f3ac76150e025da51dbde67875b8f4b8909ccbc9ef20e73e0a2d9ab5caa5912a20fdb8bd3b2087f775c2450d4935d54c6eaa95e5967978102ecfc07ccf9003687ecd28a72bbbcde92541d8ced12d8ae2d79080c2cb59536d81e7c9a01a365d70e1953ce2a3f5b54f870ad92054ccebd42bdded825d05a595c41a5a752053f708159c58191bc6383f2655e1d0984c27b7592d37cfb656cb
this one's a straight forward download

firt step =>  pre processing the data:
extracting spectograms from the voice files.
you are provided with the code to get the spectograms of the voices in the data set. for more info on how the code works checkout the link below:

"https://github.com/musikalkemist/AudioSignalProcessingForML/blob/master/16%20-%20Extracting%20Spectrograms%20from%20Audio%20with%20Python/Extracting%20Spectrograms%20from%20Audio%20with%20Python.ipynb"

the code is optimized to run on machines with low memory (at least 8GB) anything under and you'll get 'OOM (out of memory)' error.