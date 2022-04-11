import time
import cv2 as cv
import numpy as np
import mediapipe as mp
import math

class HandDetector :
  def __init__(self ,mode=False ,maxHand=2 , detectCon=0.5 ,trackcon=0.5):
    

