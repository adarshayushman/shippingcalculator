print("""

SHIPPING CALCULATOR

Bienvenue! This program will take the weight of a package and determine the cheapest way to ship that package.

There are several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you are not charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping:
- For packages 2 lb or less: $1.50 per pound plus a $20.00 flat charge.
- For packages over 2 lb but less than or equal to 6 lb: $3.00 per pound plus a $20.00 flat charge.
- For packages over 6 lb but less than or equal to 10 lb: $4.00 per pound plus a $20.00 flat charge.
- For packages over 10 lb: $4.75 per pound plus a $20.00 flat charge.

Ground Shipping Premium:
- Flat charge of $125.00 regardless of package weight.

Drone Shipping:
- For packages 2 lb or less: $4.50 per pound with no flat charge.
- For packages over 2 lb but less than or equal to 6 lb: $9.00 per pound with no flat charge.
- For packages over 6 lb but less than or equal to 10 lb: $12.00 per pound with no flat charge.
- For packages over 10 lb: $14.25 per pound with no flat charge.

""")

weight = float(input("Please enter the weight of your desired package in lbs: "))
ground_weight = weight
drone_weight = weight

#Ground Shipping
if ground_weight <= 2: 
  cost_ground = (ground_weight * 1.5) + 20
elif ground_weight > 2 and ground_weight <= 6: 
  cost_ground = (ground_weight * 3) + 20
elif ground_weight > 6 and ground_weight <= 10: 
  cost_ground = (ground_weight * 4) + 20
elif ground_weight > 10: 
  cost_ground = (ground_weight * 4.75) + 20 
print("The cost of your package via GROUND SHIPPING will be " +  str(cost_ground) + "dollars. \n")

#Ground Shipping Premium
cost_ground_premium = 125
print("The cost of your package via GROUND SHIPPING PREMIUM will be " + str(cost_ground_premium) + "dollars. \n")  

#Drone Shipping
if drone_weight <= 2: 
  cost_drone = drone_weight * 4.5
elif drone_weight > 2 and drone_weight <= 6: 
  cost_drone = drone_weight * 9
elif drone_weight > 6 and drone_weight <= 10: 
  cost_drone = drone_weight * 12
elif drone_weight > 10: 
  cost_drone = drone_weight * 14.25
print("The cost of your package via DRONE SHIPPING will be " + str(cost_drone) + "dollars. \n") 

if cost_ground < cost_drone and cost_ground < cost_ground_premium: 
  print("GROUND SHIPPING is the cheapest option. ")
elif cost_drone < cost_ground and cost_drone < cost_ground_premium: 
  print("DRONE SHIPPING is the cheapest option. ")
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone: 
  print("GROUND SHIPPING PREMIUM is the cheapest option. ")  
else: 
  print("There are multiple options available at the same price. ")  

