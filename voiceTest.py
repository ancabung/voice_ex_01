import librosa
import sounddevice as sd
import soundfile as sf
import time

with open('paragraph.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

sentences=f_contents.split('.')

def record(filename, duration, fs, channels):
    print('Recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')

record('test.wav', 10, 22000, 2)