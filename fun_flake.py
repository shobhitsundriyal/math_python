from turtle import * 

speed(0) 
pencolor('white') 
bgcolor('black') 

x = 0 
up() 
rt(45) 
fd(90) 
rt(135) 
down() 

def fd_rt(n=6):
     j = int(360/n) 
     for i in range(n):
        fd(120)
        rt(j)  

while x < 120: 
    fd_rt(1)
    rt(11.1111) 
    x = x+1 
exitonclick() 