import os
import numpy as np
import moviepy.editor as mpy


filenames = os.listdir()
filenames = [int(fn.replace('.png', '')) for fn in filenames if '.png' in fn]
filenames = np.sort(filenames)
filenames = [str(fn) + '.png' for fn in filenames]

clip = mpy.ImageSequenceClip(filenames, fps=48)
clip.write_videofile('00test.webm', codec='libvpx', fps=48)