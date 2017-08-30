from random import randint
from time import sleep
from InstagramAPI import InstagramAPI

import sys
import os
import datetime
import cv2
import numpy as np


# Define tag messages list.
messages = [ "calismalar tum hizi ile suruyor",
              "calismalar tam gaz devam ediyor",
              "calismaya devam"
              ]

# SoftTech Hackathon tags
tag = "#SoftTechHackathon5 @softtechas "

# Get random tag messages from messages list.
def getRandomTagMessage():

     # Get current time
     currentTime = datetime.datetime.now()

     tagMessage = "Saat : " + str(currentTime.hour) + ":" + str(currentTime.minute)
     tagMessage = tag + tagMessage + " " + messages[randint(0, len(messages) - 1)]
     return tagMessage


newSize = 500, 500
fileName = "frame.jpeg"

# Take frame from video capture.
def takeFrame():

     # Define a video capture.
     capture = cv2.VideoCapture()

     # Open Video Capture
     capture.open(0)

     # Check capture is opened ?
     if capture.isOpened():

         # Read a frame from capture
         ret,frame = capture.read()

         # Resize frame
         cv2.resize(frame,newSize)

         # Save
         cv2.imwrite(fileName, frame)

         # Release capture
         capture.release()

# Upload photo to instagram
def uploadPhoto():

    # Take frame from capture
    takeFrame()

    # Get random tag message.
    tagMessage = getRandomTagMessage()

    # Check taken frame is exist.
    returnValue = os.path.isfile(fileName)
    if returnValue:
        instagramAPI = InstagramAPI("USER NAME", "PASSWORD")
        instagramAPI.login()
        instagramAPI.uploadPhoto(fileName,tagMessage)

timeInterval = 2
while True:
    uploadPhoto()
    sleep(60 * timeInterval)
