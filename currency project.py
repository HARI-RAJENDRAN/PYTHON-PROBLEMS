
#currency converter....

# In this code have some country calclulation and only  ruppees to convert ....

# Its have only three currency dollar,euro,pounds,dirham.......

print("----------------------------------------")
value_c=input("what currency you have: ")
if(value_c !="rupees"):
  exit("invalid")
print("----------------------------------------")
value_cur=int(input("enter the currency: "))
value_con=input("enter the currency name: ")
if(value_con !="dollar","euro","pounds","emirates","dirham","emirates dirham" ):
  print("invalid currency")
print("-----------------------------------------")

if(value_con=="rupees"):
  print("its denote on rupees")
elif(value_c=="rupees" and value_con=="dollar"):
  print(value_cur*0.012,"dollar")
  print("---------------------------------------")

if(value_con=="rupees"):
  print("its denote on rupees")
elif(value_c=="rupees" and value_con=="euro"):
  print(value_cur*0.011,"euro")
  print("---------------------------------------")
  
if(value_con=="rupees"):
  print("its denote on rupees")
elif(value_c=="rupees" and value_con=="pounds"):
  print(value_cur*0.0095,"pounds")
  print("---------------------------------------")

if(value_con=="rupees"):
  print("its denote on rupees")
elif(value_c=="rupees" and value_con=="emirates" or value_con=="dirham" or value_con=="emirates dirham" ):
  print(value_cur*0.044265 ,"emirates dirham")
  print("---------------------------------------")
