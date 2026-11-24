# Ask for temperature
temperature = input("enter the temperature in celsius ")
temperature = int(temperature)

if temperature < 20: 
    outfit = "jacket"
    print("it is cold today ")
    print("wear a " , outfit )

else :
    outfit = "t-shirt"
    print("it is warm today ")
    print("wear a " , outfit )

is_raining = input("is it raining today yes/no ")

if is_raining == "yes" :
   print("bring an umbrella")

wind_speed = int(input ("enter the wind speed in km/h " ))

if wind_speed > 30 :
  winds_breaker_needed = "yes"
  print("it is windy today ") 
  print("wear a wind breaker today " ,winds_breaker_needed )

else :  
     winds_breaker_needed = "no"
     print("it is calm today ")
     print("wear a wind breaker today " , winds_breaker_needed )
  
