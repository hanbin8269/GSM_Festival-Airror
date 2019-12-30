from flask_opencv_streamer.streamer import Streamer
import cv2
from mss import mss
from PIL import Image
import numpy as np
mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

sct = mss()

port = 3030
require_login = False
streamer = Streamer(port, require_login)

# Open video device 0
video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    
    streamer.update_frame(np.array(img))

    if not streamer.is_streaming:
        streamer.start_streaming()

    cv2.waitKey(30)