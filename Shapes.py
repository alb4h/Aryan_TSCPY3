# Space Arena!
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

import turtle
import math
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(width=SCREEN_WIDTH + 220, height=SCREEN_HEIGHT + 20)
wn.title("Space Arena! by #TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

radar_pen = turtle.Turtle()
radar_pen.speed(0)
radar_pen.shape("square")
radar_pen.color("white")
radar_pen.penup()
radar_pen.hideturtle()

# Splash screen
pen.goto(0, 200)
pen.write("SPACE ARENA!", align="center", font=("Courier", 30, "normal"))
pen.goto(0, 150)
pen.write("Kill the red enemies with your missiles. You have 3 to begin with.", align="center",
          font=("Courier", 15, "normal"))
pen.goto(0, 100)
pen.write("Collect the blue powerups to increase the number, power,", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 50)
pen.write("speed, and range of your missiles.", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 0)
pen.write("Use the arrows to rotate and accelerate. Space to fire.", align="center", font=("Courier", 15, "normal"))
wn.update()
time.sleep(0)


class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame = 0
        self.show_radar = False

    def toggle_radar(self):
        self.show_radar = not self.show_radar

    def render_info(self, pen, score, active_enemies):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(stretch_wid=10, stretch_len=32, outline=None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color("white")
        pen.goto(400, 250)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        pen.goto(400, 230)
        pen.write("Enemies: {}".format(active_enemies), align="center", font=("Courier", 18, "normal"))

    def render_border(self, pen, x_offset, y_offset, screen_width, screen_height):
        pen.color("white")
        pen.width(3)
        pen.penup()
        left = -self.width / 2.0 - x_offset
        right = self.width / 2.0 - x_offset
        top = self.height / 2.0 - y_offset
        bottom = -self.height / 2.0 - y_offset

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()


class Sprite():

    @staticmethod
    def is_collision(sprite1, sprite2, threshold):
        d = math.sqrt((sprite1.x - sprite2.x) ** 2 + (sprite1.y - sprite2.y) ** 2)
        if d < threshold:
            return True
        else:
            return False

    @staticmethod
    def is_on_screen(sprite, screen_width, screen_height, x_offset, y_offset):
        if sprite.x + 120 - x_offset < screen_width / 2 and sprite.x - x_offset > -screen_width / 2 \
                and sprite.y - y_offset < screen_height / 2 and sprite.y - y_offset > - screen_height / 2:
            return True
        else:
            return False

    def __init__(self, x, y, shape="square", color="white"):
        self.shape = shape
        self.color = color
        self.width = 20.0
        self.height = 20.0
        self.heading = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.da = 0.0
        self.thrust = 0.0
        self.max_d = 2.0
        self.x = x
        self.y = y
        self.state = "active"

    def update(self):
        self.heading += self.da
        self.heading %= 360.0

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.border_check()

    def border_check(self):
        if self.x > game.width / 2.0 - 10.0:
            self.x = game.width / 2.0 - 10.0
            self.dx *= -1.0
        elif self.x < -game.width / 2.0 + 10.0:
            self.x = -game.width / 2.0 + 10.0
            self.dx *= -1.0

        if self.y > game.height / 2.0 - 10.0:
            self.y = game.height / 2.0 - 10.0
            self.dy *= -1.0
        elif self.y < -game.height / 2.0 + 10.0:
            self.y = -game.height / 2.0 + 10.0
            self.dy *= -1.0

    def render(self, pen, x_offset=0, y_offset=0):
        # Check if active
        if self.state == "active":
            # Check if it is on the screen
            screen_x = self.x - x_offset
            screen_y = self.y - y_offset

            if (
                    screen_x > -game.width / 2.0 and screen_x < game.width / 2.0 and screen_y > -game.height / 2.0 and screen_y < game.width / 2.0):
                pen.goto(self.x - x_offset, self.y - y_offset)
                pen.shape(self.shape)
                pen.color(self.color)
                pen.shapesize(stretch_wid=1, stretch_len=1, outline=None)
                pen.setheading(self.heading)
                pen.stamp()


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, 0.0, 0.0, "triangle")
        self.da = 0.0
        self.heading = 90.0
        self.score = 0
        self.max_health = 40
        self.health = self.max_health
        self.sensor_range = 500

    def rotate_left(self):
        self.da = 10.0

    def rotate_right(self):
        self.da = -10.0

    def stop_rotation(self):
        self.da = 0.0

    def accelerate(self):
        self.thrust += 0.2

    def decelerate(self):
        self.thrust = 0.0

    def fire(self):
        for missile in missiles:
            if missile.state == "ready":
                missile.x = player.x
                missile.y = player.y
                missile.dx = player.dx
                missile.dy = player.dy
                missile.heading = player.heading
                missile.dx += math.cos(math.radians(self.heading)) * missile.thrust
                missile.dy += math.sin(math.radians(self.heading)) * missile.thrust
                missile.state = "active"

                self.dx -= missile.dx * 0.05
                self.dy -= missile.dy * 0.05
                break

    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.heading = 90.0
        self.health = self.max_health

    def render(self, pen, x_offset=0, y_offset=0):
        pen.shapesize(stretch_wid=0.5, stretch_len=1, outline=None)
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()

        # Draw health
        pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)
        pen.width(3.0)
        pen.pendown()
        pen.setheading(0.0)
        try:
            if self.health / self.max_health < 0.3:
                pen.color("red")
            elif self.health / self.max_health < 0.7:
                pen.color("yellow")
            else:
                pen.color("green")
            pen.fd(20.0 * (self.health / self.max_health))
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health - self.health) / self.max_health))
        except:
            pass

        pen.penup()


class Enemy(Sprite):
    def __init__(self, x, y, shape="square", color="red"):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = random.randint(10, 30)
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])
        self.max_dx = 3.0
        self.max_dy = 3.0
        self.sensor_range = random.randint(40, 60)

        if self.type == "hunter":
            self.color = "red"
            self.sensor_range = random.randint(100, 200)

        elif self.type == "mine":
            self.color = "orange"
            self.sensor_range = random.randint(100, 200)

        elif self.type == "surveillance":
            self.color = "pink"
            self.sensor_range = random.randint(200, 400)

    def update(self):

        if self.health <= 0:
            self.state = "inactive"

        self.heading += self.da
        self.heading %= 360.0

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        # Change movement based on type
        if self.type == "hunter":
            if Sprite.is_collision(player, self, self.sensor_range):
                if self.x < player.x:
                    self.dx += 0.05
                else:
                    self.dx -= 0.05

                if self.y < player.y:
                    self.dy += 0.05
                else:
                    self.dy -= 0.05

        elif self.type == "mine":
            self.dx = 0.0
            self.dy = 0.0

            if Sprite.is_collision(player, self, self.sensor_range):
                self.type = "hunter"
                self.color = "red"

        elif self.type == "surveillance":
            if Sprite.is_collision(player, self, self.sensor_range):
                if self.x > player.x:
                    self.dx += 0.03
                else:
                    self.dx -= 0.03

                if self.y > player.y:
                    self.dy += 0.03
                else:
                    self.dy -= 0.03

        # Check max velocity
        if self.dx > self.max_dx:
            self.dx = self.max_dx
        elif self.dx < -self.max_dx:
            self.dx = -self.max_dx

        if self.dy > self.max_dy:
            self.dy = self.max_dy
        elif self.dy < -self.max_dy:
            self.dy = -self.max_dy

        self.border_check()

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(stretch_wid=1, stretch_len=1, outline=None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.setheading(self.heading)
            pen.stamp()

            # Draw health
            pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)
            pen.width(2)
            pen.pendown()
            pen.setheading(0.0)
            try:
                if self.health / self.max_health < 0.3:
                    pen.color("red")
                elif self.health / self.max_health < 0.7:
                    pen.color("yellow")
                else:
                    pen.color("green")
                pen.fd(20.0 * (self.health / self.max_health))
                pen.color("grey")
                pen.fd(20.0 * ((self.max_health - self.health) / self.max_health))
            except:
                pass

            pen.penup()


class Missile(Sprite):
    def __init__(self, x, y, shape="triangle", color="yellow"):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 5.0
        self.max_fuel = 200.0
        self.fuel = 200.0
        self.damage = 5.0

    def update(self):
        self.heading += self.da
        self.heading %= 360.0

        self.x += self.dx
        self.y += self.dy

        self.border_check()

        self.fuel -= self.thrust
        if self.fuel < 0:
            self.state = "ready"
            self.fuel = self.max_fuel

    def reset(self):
        self.state = "ready"
        self.fuel = self.max_fuel

