import turtle
import os
import math
import random
# import time
# import sys





#set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("Backg.gif")


turtle.register_shape("sp_enemy.gif")
turtle.register_shape("sp_player.gif")
#border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pendown()
border_pen.pensize(1)
for side in range(4):
	border_pen.fd(500)
	border_pen.lt(90)
border_pen.hideturtle()

#set score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-250,265)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
#create the player

player = turtle.Turtle()
player.color("red")
player.shape("sp_player.gif")
player.penup()
player.speed(0)
player.setposition(0, -220)
player.setheading(90)

playerspeed = 20

# choose number of enemies
number_of_enemies = 5

#create an empty list
enemies = []

#Add enemies to the ist
for i in range(number_of_enemies):
	#invaders
	enemies.append(turtle.Turtle())

for enemy in enemies:	
	enemy.color("green")
	enemy.shape("sp_enemy.gif")
	enemy.shapesize(10,10,5)
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-180, 180)
	y = random.randint(100, 230)
	enemy.setposition(x, y)

enemyspeed = 1

#create the laser bullet
laser = turtle.Turtle()
laser.color("white")
laser.shape("triangle")
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.shapesize(0.5,0.5)
laser.hideturtle()

laserspeed = 15

#define laser state
# ready - ready to fire
#fire - laser is firing

laserstate = "ready"





#left movement

def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -230:
		x = -230
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 230:
		x = 230
	player.setx(x)


def fire_laser():
	#declare laser as a global if it needs changed
	global laserstate
	if laserstate == "ready":
		laserstate = "fire"
		#move the laser just above the player
		x = player.xcor()
		y = player.ycor()
		laser.setposition(x,y+10)
		laser.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#keyboard binding

turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkey(fire_laser,"space")
turtle.listen()



#main loop
while True:
	#move the  enemy
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#move the enemy back and down
		if enemy.xcor() > 230:
			for e in enemies:
				y = e.ycor()
				y -= 25
				e.sety(y)
			enemyspeed *= -1

		if enemy.xcor() < -230:
			for e in enemies:
				y = e.ycor()
				y -= 25
				e.sety(y)
			enemyspeed *= -1
		#check for collision between laser and enemy
		if isCollision(laser, enemy):
			#reset the bullet
			laser.hideturtle()
			laserstate = "ready"
			laser.setposition(0, -400)
			#reset the enemy
			enemy.setposition(0, 220)
			#update score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over!!")
			break
		
	#move laser	
	if laserstate == "fire":
		y = laser.ycor()
		y += laserspeed
		laser.sety(y)

	#stop laser at the top
	if laser.ycor()>245:
		laser.hideturtle()
		laserstate = "ready"

	




win.exitonclick()