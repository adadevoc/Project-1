class Car:
 

    def __init__(self):
        self.doors = 4
        self.tyres = 4
        self.name = " "
        
    def title(self):
       self.name = input("Enter Driver's name")
    

    
    def output(self):
        print(self.doors, self.tyres, self.name)
  
       
c = Car()
c.title()
user_input = 1
while user_input ==1:
        c.output()
        user_input = int(input("Do you want to continue? if so enter 1 to continue if not enter 0"))
        if user_input!=1:
            print("Thank you for playing")


#print("Fire")   






 


  

   ## print(x)
