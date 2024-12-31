trainning and fine tuning a transformer model with the persian_common_voice data set from hugging face


link to the dateset:
https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0

to get and use the dataset you can:
git lfs install
git clone https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0

if you want to clone the pointers to the data set (not the large files) 
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/Ashegh-Sad-Warrior/Persian_Common_Voice_17_0


firt step=>  pre processing the data:
extracting spectograms from the voice files.