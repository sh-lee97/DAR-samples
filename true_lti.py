import numpy as np
import soundfile as sf
import glob
from scipy import signal

dirs = glob.glob('audio/fdn/*p/*')

for dir_folder in dirs:
    lti_ir_dir = glob.glob(dir_folder + '/*true_lti_estimation.wav')[0]
    deco_str = lti_ir_dir[-28:-23]
    print(deco_str)
    lti_ir, sr = sf.read(lti_ir_dir)
    dspeech, _ = sf.read(glob.glob(dir_folder + '/*dry_speech.wav')[0])
    lti_cspeech = signal.convolve(dspeech, lti_ir)
    sf.write(dir_folder + '/' + deco_str + 'true_lti_convolved_speech.wav', lti_cspeech, sr)
