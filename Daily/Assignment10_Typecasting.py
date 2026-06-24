#Typecasting



# Assignment: Create a simple  bill of Grocery. take 3-4 inputs and print the fina; bill

Brownsugar =40
Nescoffee = 250
BasmatiRice=100
SunflowerOil=150
CowMilk = 80

sugar_q = float(input("Enter sugar quantity in kg-"))
coffe_q = float(input("Enter coffe quantity in kg-"))
rice_q = float(input("Enter rice quantity in kg-"))
milk_q = float(input("Enter milk quantity in lit-"))
oil_q = float(input("Enter oil quantity in kg-"))


sug = Brownsugar*sugar_q
coff = Nescoffee*coffe_q
rice = BasmatiRice*rice_q
milk = CowMilk*milk_q
oil = SunflowerOil*oil_q
Total = sug+coff+rice+milk+oil

print("Bill details:   ")
print("Sugar:" ,sug)
print("Coffe: ",coff)
print("Rice: ",rice)
print("Milk:",milk)
print("Oil: ",oil)
print("---------------------------------------")
print("Toatal Amount: ",Total)

