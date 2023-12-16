from moviepy.editor import *
from moviepy import *

# Load videos
video1 = VideoFileClip('/Users/gagewillette/_projects/pyshorts/familyguy.mp4').subclip(10, 20)
video2 = VideoFileClip('/Users/gagewillette/_projects/pyshorts/gta.mp4').subclip(10, 20)

# Resize videos
video1_resized = video1.resize(height=960) 
video2_resized = video2.resize(height=960)

# Combine videos
final_video = clips_array([[video1_resized], [video2_resized]])

# Export
final_video.write_videofile('output_video.mp4', codec='libx264')



