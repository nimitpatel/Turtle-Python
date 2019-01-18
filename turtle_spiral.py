import turtle
  
win = turtle.Screen()
my_turtle = turtle.Turtle() 
my_turtle.color("lightblue")

my_turtle.penup()              
size = 20

for i in range(50):
   my_turtle.stamp()             
   size = size + 1.5           
   my_turtle.forward(size)    
   my_turtle.right(25)           

win.mainloop()