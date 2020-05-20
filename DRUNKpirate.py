import turtle

pirate = turtle.Turtle()
pirate.speed(10)

def Drunk_pirate():
    pirate.fd(160)
    pirate.rt(20)

    pirate.fd(-43)
    pirate.lt(10)

    pirate.fd(270)
    pirate.rt(8)

    pirate.fd(-43)
    pirate.rt(12)

Drunk_pirate()

turtle.mainloop()