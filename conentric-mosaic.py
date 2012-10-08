#!/usr/bin/python

import pygame
from pygame.locals import *
import numpy as np
import cv2
import cv2.cv as cv

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Concentric Mosaic')
font = pygame.font.SysFont(None, 48)

frames = []
camera = cv2.VideoCapture(0)

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			running = False
		# if
	# for

	screen.fill((0, 0, 0))

	frame = camera.read()[1]
	if frame is not None:
		# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# self.finder.detect(gray_frame)

		pyimage = cv.CreateImage(cv.GetSize(cv.fromarray(frame)), 8, 3)
		cv.CvtColor(cv.fromarray(frame), pyimage, cv.CV_BGR2RGB)
		frame = pygame.image.frombuffer(pyimage.tostring(), cv.GetSize(pyimage), 'RGB')

		screen.blit(frame, (0, 0))
	# if

	pygame.display.flip()
	cv2.waitKey(10)
# while