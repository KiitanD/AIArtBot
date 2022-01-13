import moviepy.video.io.ImageSequenceClip as mp
import os
from pathlib import Path

image_folder=os.path.join('../DownloadTest','swin')
fps=5
image_files = [os.path.join(image_folder,img)
               for img in sorted(os.listdir(image_folder))]
clip = mp.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('../DownloadTest/process.mp4')
