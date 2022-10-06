from turtle import width


print(                 "Geometry Calculator" )
print("")
# asking user to enter required parameters
w= int(input(" Please Enter width: "))
h= int(input(" Please Enter height: "))
# asking user to Select any options
def menu():
    print("[1] Area of triangle: ")
    print("[2] Area of rectangle: ")
    print("[3] Area of circle: ")
    print("[4] Quit")

menu()
option = int(input(" Please Select any option (1-4): "))

# area of triangle
if option == 1:
    # formula for area of triangle
    triangle = h*w / 2  
    print("Area of triangle is: ", triangle)

# area of rectangle    
elif option == 2:
    # formula  for area of rectangle
    rectangle = h * w   
    print("Area of Rectangle is: ",rectangle)
# area of circle 
elif option == 3:
    #asking user to provide radius 
    radius = int(input(" Please Enter Radius of circle: ")) 
    #formula for area of circle 
    #3.14= value of pi
    circle = 3.14 * radius * radius
    print("Area of Circle is: ",circle)
elif option == 4:
    menu()
    option = int(input(" Please Select any option (1-4): "))

else:
  print("Invalid Selection")
