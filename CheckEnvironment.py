import sys
import os
import platform
import pygame
import cv2

print(f"---------------------------")
print(f"Python Version: {sys.version}")
print(f"Executable Path: {sys.executable}")
print(f"Current Working Directory: {os.getcwd()}")
print(f"Platform: {platform.platform()}")
print(f"Python Path: {sys.path}")
print(f"---------------------------")
print(f"Pygame Version: {pygame.version.ver}")
print(f"OpenCV Version: {cv2.__version__}")
print(f"---------------------------")
