# you can find the age of the year...

def main():
  name_a=input("enter your name:" )
  age_a=int(input("enter your D.O.B:"))
  age_b=int(input("enter your age to find year :"))
  age=age_a+age_b
  print("------------------------------------------------------")
  print(name_a,"you entered age is",age_a,"the year is ",age)
  print("------------------------------------------------------")
ques=input("you want try it (yes/no):")
while(ques=="yes"):
  main()
  ques1=input("you try again (yes/no):")
  if(ques1=="yes"):
    main()
  else:
    exit()