import turtle
import time
 
#绘制月亮
def drawMoon():            
	turtle.penup()
	turtle.goto(-150, 0)
	turtle.fillcolor((255, 215, 0))
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(112)
	turtle.end_fill()
 
 
#绘制云朵
def drawCloud():           
   turtle.penup()
   turtle.goto(-500, 200)
   turtle.fillcolor((245, 245, 245))
   turtle.pencolor((255, 255, 255))
   turtle.pensize(5)
   turtle.pendown()
   turtle.forward(250)
   def cloud(mode='right'):
      for i in range(90):
         turtle.pensize((i+1)*0.2+5)
         turtle.right(1) if mode == 'right' else turtle.left(1)
         turtle.forward(0.5)
      for i in range(90):
         turtle.pensize(90*0.2+5-0.2*(i+1))
         turtle.right(1) if mode == 'right' else turtle.left(1)
         turtle.forward(0.5)
   cloud()
   turtle.forward(100)
   cloud('left')
   turtle.forward(600)
 
 
#绘制山川
def drawMountain():          
   turtle.penup()
   turtle.goto(-500, -250)
   turtle.pensize(4)
   turtle.fillcolor((128, 138, 135))
   turtle.pencolor((31, 28, 24))
   turtle.pendown()
   turtle.begin_fill()
   turtle.left(20)
   turtle.forward(400)
   turtle.right(45)
   turtle.forward(200)
   turtle.left(60)
   turtle.forward(300)
   turtle.right(70)
   turtle.forward(300)
   turtle.goto(500, -300)
   turtle.goto(-500, -300)
   turtle.end_fill()
 
 
#画嫦娥
def draw_ChangE():
    lx, ly = -30, 50
    # 左手
    print("ok")
    turtle.penup()
    turtle.color("#ffffeb")
    turtle.width(4)
    turtle.goto(lx, ly)
    turtle.seth(50)
    turtle.pendown()
    turtle.fd(10)
    turtle.circle(-3, 180)
    turtle.right(170)
    turtle.circle(-6, 180)
    turtle.circle(-50, 20)
    # 左袖
    turtle.penup()
    turtle.color('red')
    turtle.goto(lx, ly)
    turtle.seth(-140)
    turtle.pendown()
    turtle.fd(16)
    turtle.penup()
    turtle.goto(lx, ly)
    turtle.seth(-50)
    turtle.pendown()
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(10)
    turtle.circle(-50, 40)
    # 衣服
    turtle.color('#f3dd64')
    turtle.penup()
    turtle.right(90)
    turtle.fd(10)
    turtle.right(180)
    turtle.pendown()
    turtle.circle(-100, 8)
    turtle.circle(-20, 80)
    turtle.circle(-100, 11)
    # 衣服2
    turtle.penup()
    turtle.circle(-100, -11)
    turtle.circle(-20, -80)
    turtle.fd(8)
    turtle.pendown()
    turtle.circle(-100, 6)
    turtle.circle(-15, 82)
    turtle.circle(-40, 35)
    # 衣服-裙
    turtle.color('red')
    turtle.penup()
    turtle.circle(-40, -35)
    turtle.circle(-15, -82)
    turtle.fd(10)
    turtle.right(10)
    turtle.pendown()
    turtle.circle(-100, 60)
    turtle.right(60)
    turtle.circle(-100, 60)
    turtle.right(60)
    turtle.circle(-200, 2)
    # 右袖
    turtle.penup()
    turtle.circle(-200, -2)
    turtle.right(-60)
    turtle.circle(-100, -60)
    turtle.right(-60)
    turtle.circle(-100, -60)
    turtle.right(-10)
    turtle.fd(-6)
    turtle.circle(-100, -6)
    turtle.fd(-8)
    turtle.circle(-20, 80)
    turtle.circle(-100, 12)
    turtle.right(110)
    turtle.fd(10)
    turtle.right(180)
    turtle.pendown()
    turtle.circle(-50, 50)
    turtle.right(70)
    turtle.circle(-50, 40)
    turtle.right(57)
    turtle.circle(-200, 10)
    # 右手
    turtle.penup()
    turtle.circle(-200, -10)
    turtle.right(-57)
    turtle.circle(-50, -4)
    turtle.color("#ffffeb")
    turtle.left(80)
    turtle.circle(10, 15)
    turtle.pendown()
    turtle.circle(10, 190)
    # 下方飘带
    turtle.penup()
    turtle.circle(10, -90)
    turtle.seth(-140)
    turtle.color('#f3dd64')
    turtle.circle(-10, 10)
    turtle.pendown()
    turtle.circle(-10, 100)
    turtle.circle(-40, 20)
    turtle.circle(40, 70)
    turtle.left(80)
    turtle.circle(60, 40)
    turtle.left(60)
    turtle.circle(-30, 50)
    turtle.circle(20, 80)
    turtle.fd(25)
    # 脸
    turtle.penup()
    turtle.goto(lx, ly)
    turtle.seth(-140)
    turtle.fd(16)
    turtle.seth(-100)
    turtle.color("#ffffeb")
    turtle.pendown()
    turtle.circle(-30, 100)
    turtle.color('black')
    turtle.begin_fill()
    turtle.circle(-30, 30)
    # 耳朵
    turtle.left(100)
    turtle.circle(-10, 180)
    turtle.circle(-2, 60)
    turtle.circle(-40, 20)
    # 头发
    turtle.left(150)
    turtle.circle(-10, 90)
    turtle.circle(80, 10)
    turtle.circle(30, 60)
    turtle.right(100)
    turtle.circle(-20, 70)
    turtle.circle(3, 160)
    turtle.circle(25, 90)
    turtle.left(20)
    turtle.fd(20)
    turtle.right(80)
    turtle.circle(20, 150)
    turtle.right(80)
    turtle.circle(8, 180)
    turtle.right(90)
    turtle.fd(10)
    turtle.right(110)
    turtle.circle(10, 100)
    turtle.right(110)
    turtle.fd(12)
    turtle.circle(8, 110)
    turtle.right(50)
    turtle.circle(12, 70)
    turtle.circle(2, 50)
    turtle.circle(180, 25)
    turtle.end_fill()
    # 发髻
    turtle.penup()
    turtle.circle(180, -25)
    turtle.circle(2, -50)
    turtle.circle(12, -70)
    turtle.right(-50)
    turtle.circle(8, -110)
    turtle.fd(-12)
    turtle.right(-110)
    turtle.circle(10, -100)
    turtle.right(-110)
    turtle.fd(-10)
    turtle.right(-90)
    turtle.circle(8, -180)
    turtle.fd(-25)
    turtle.left(20)
    turtle.color('yellow')
    turtle.width(1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fd(8)
    turtle.right(90)
    turtle.circle(-4, 180)
    turtle.end_fill()
    # 脸
    turtle.penup()
    turtle.width(1)
    turtle.goto(lx, ly)
    turtle.seth(-140)
    turtle.fd(16)
    turtle.seth(-100)
    turtle.color("#ffffeb")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(-30, 130)
    turtle.left(100)
    turtle.circle(-10, 180)
    turtle.circle(-2, 60)
    turtle.circle(-40, 20)
    turtle.left(150)
    turtle.circle(-10, 90)
 
    turtle.circle(80, 10)
    turtle.circle(30, 60)
    turtle.right(100)
    turtle.circle(-20, 70)
    turtle.left(3)
    turtle.circle(-200, 9)
    turtle.end_fill()
    # 眼睛
    turtle.penup()
    turtle.width(6)
    turtle.goto(lx, ly)
    turtle.color('black')
    turtle.seth(170)
    turtle.fd(25)
    turtle.pendown()
    turtle.seth(120)
    turtle.fd(4)
    turtle.penup()
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.pendown()
    turtle.fd(4)
    # 嘴
    turtle.penup()
    turtle.circle(100, 10)
    turtle.width(4)
    turtle.left(40)
    turtle.color('red')
    turtle.pendown()
    turtle.circle(100, 3)
    turtle.circle(15, 90)
    turtle.circle(100, 3)
 
 
def initTurtle():
   turtle.hideturtle()
   turtle.setup(1000, 600)
   turtle.title('中秋月饼')
   turtle.colormode(255)
   turtle.bgcolor((8, 46, 84))
   turtle.speed(100)
 
 
#写诗
def writePoetry():
	turtle.penup()
	turtle.goto(400, -150)
	turtle.pencolor((250, 240, 230))
	# 诗句
	potery = ["\n明\n月\n几\n时\n有\n", "把\n酒\n问\n青\n天\n"]
	coordinates = [(300, -150), (200, -150), (100, -150)]
	for i, p in enumerate(potery):
		turtle.write(p, align="center", font=("STXingkai", 50, "bold"))
		if (i + 1) != len(potery):
			time.sleep(2)
			turtle.goto(coordinates[i])
 
def add_moon_palace():
  draw_ChangE()
 
def main():
    initTurtle()
    turtle.speed(100)
    drawMoon()
    drawCloud()
    drawMountain()
    writePoetry()
    add_moon_palace()
    turtle.done()
 
if __name__ == '__main__':
    main()