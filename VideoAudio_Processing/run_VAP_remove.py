'''Function (Python3): Remove audio from video with FFmpeg.

Author: He Zhang @ University of Exeter
Date: April 17th 2019 (Update: April 17th 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/JJY_HZY360P.mp4"
OUTPUT_FILE = "Media/JJY_HZY360P_noS.mp4"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -y -i " + INPUT_VIDEO + " -an -vcodec copy " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
