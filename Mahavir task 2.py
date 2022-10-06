print(                 "Geometry Calculator" )
print("")

while True:
    print("[1] Want to Find Parimeter: ")
    print("[2] Want to Find Area: ")
    option1 = int(input("Please select your option: "))
     
    if option1 == 1:
    
     print("[1] triangle: ")
     print("[2] rectangle: ")
     print("[3] circle: ")
     print("[4] Quit")
     option2 = int(input("Please Enter your choice: "))
     
     if option2 == 1:
        x = int(input("Please Enter A side: "))
        y  = int(input("Please Enter B side: "))
        z = int(input("Please Enter C side: "))        
        PT = x+y+z 
        print("Parimeter of Triangle is ",PT)
     elif option2 == 2:
        h = int(input("Enter Height: "))
        w = int(input("Enter width:")) 
        PR = 2 * h + w 
        print("Perimeter of Rectangle is ",PR)
     elif option2 == 3:
        radius = int(input("Enter radius:"))
        PC = 2 * 3.14 * radius
        print("Perimeter of Circle is ",PC)
     else:
        print(" Please Enter valid option ")
        break
    elif option1 == 2:
     print("[1] triangle: ")
     print("[2] rectangle: ")
     print("[3] circle: ")
     print("[4] Quit")
     option3 = int(input("Please Enter your choice: "))
     
     if option3 == 1:
        h = int(input("Please Enter height:"))
        w = int(input("Please Enter width:"))                
        AT = h * w / 2  
        print("Area of Triangle is ",AT)
     elif option3 == 2:
        h = int(input("Please Enter Height: "))
        w = int(input("Please Enter width:")) 
        AR = h * w  
        print("Area of Rectangle is ",AR)
     elif option3 == 3:
        radius = int(input("Please Enter radius:"))
        AC = 3.14 * radius * radius
        print("Area of Circle is ",AC)
     else:
        print("Enter valid option ")

