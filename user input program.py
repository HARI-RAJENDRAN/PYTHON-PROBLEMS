#python basic(user input method)

value_a=int(input("enter the first value to calculate: "))
value_b=int(input("enter the second value to calculate: "))
value_c=input("enter any operator ( + , - , * , / ): ")
if(value_c == "+"):
  print(value_a + value_b)
elif(value_c=="-"):
  print(value_a - value_b)
elif(value_c=="/"):
  print(value_a / value_b)
elif(value_c=="*"):
  print(value_a * value_b)
else:
  print("go learn maths first")
