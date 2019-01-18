import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main(draw):
	pygame.init()
	display = (800,800)
	# double buffer双缓存区
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
	# 透视参数
	gluPerspective(45,1,0,50)
	# 摆放位置
	glTranslatef(0,0,-6)
	# 初始旋转角度
	glRotatef(0,0,0,0)

	x_rotate = 0
	y_rotate = 0
	speed = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					y_rotate = -1
					speed = 1
				if event.key == pygame.K_RIGHT:
					y_rotate = 1
					speed = 1
				if event.key == pygame.K_UP:
					x_rotate = -1
					speed = 1
				if event.key == pygame.K_DOWN:
					x_rotate = 1
					speed = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					y_rotate = 0
					speed = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					x_rotate = 0
					speed = 0
		glRotatef(speed,x_rotate,y_rotate,0)
		# 清除颜色缓冲和深度缓冲
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		draw()
		pygame.display.flip()
		pygame.time.wait(10)

