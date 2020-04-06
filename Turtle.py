import turtle

my_turtle = turtle.Turtle()
my_turtle.color("green")
my_turtle.speed(5) #speed of drawing object

def circle(n,angle): # n for size of object  
    for i in range(4): #lines of object
        my_turtle.forward(n)
        my_turtle.right(angle)

for i in range(100): #range mean how many times object you want to draw
    circle(200,90)  #here 90 is angle of object that means 90 is square object 
    my_turtle.right(11) #11 is angle (first object drawn then create angle of 11 and drawn again second time and so on...)
