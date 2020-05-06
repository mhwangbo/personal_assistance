# LibROSA and SciPy: python libraries for processing audio signals
import os
import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import warnings

warnings.filterwarnings("ignore")

# Specifying training materials
train_audio_path = '../input/audio/'
samples, sample_rate = librosa.load(train_audio_path+'')