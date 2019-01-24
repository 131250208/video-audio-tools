import subprocess

# Input video/audio file: a.mp4
# Output audio or path: b.wav or Audio/b.wav

# The output format can be .wav or .mp3

command = "ffmpeg -i a.mp3 -ab 160k -ac 2 -ar 44100 -vn b.wav"

subprocess.call(command, shell=True)
