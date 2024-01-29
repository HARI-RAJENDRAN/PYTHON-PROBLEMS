#create a guide for new gym guys.............

#its create in a weight limit..........

print("--------------------------------------")
user_a=int(input("enter your age:"))
user_b=int(input("enter the weight:"))
print("--------------------------------------")

#its for age 12 to 18-----------------
print("----------------------------------------------------------------------------")
if(40 <= user_b <= 70 and 12<=user_a <=18):
    print("its a perfect workout for you")
    print("1. Cardiovascular Exercise (3-5 times per week)\n"
           "2. Strength Training (2-3 times per week)\n"
            "3.Cardiovascular Exercise (3-5 times per week) - 30-60 minutes\n"
            "4,Strength Training (2-3 times per week) - 45-60 minutes\n"
            "5.Flexibility and Stretching (Daily) - 10-15 minutes\n"
            "6.Balance and Stability Exercises (2-3 times per week) - 20-30 minutes\n"
            "7.Rest and Recovery - Varies (Ensure adequate rest)\n"
            "8.Stay Hydrated - Throughout the day\n"
            "9.Warm-up and Cool Down - 10-15 minutes each\n")
    print("--------------------------------------------------------------------------------")
    

    
#its for age 18 to 25--------------------------


if(50 <= user_b <= 80 and 18<=user_a <=25):
    print("--------------------------------------------------------------------------------")
    print("its a perfect workout for you")
    print("1. Cardiovascular Exercise (3-5 times per week) - 30-60 minutes\n"
          "2. High-Intensity Interval Training (HIIT) (1-2 times per week) - 20-30 minutes\n"
          "3. Strength Training (3-4 times per week) - 45-60 minutes\n"
          "4. Flexibility and Mobility Training (2-3 times per week) - 15-30 minutes\n"
          "5. Functional Training and Core Workouts (2-3 times per week) - 30-45 minutes\n"
          "6. Active Recreation or Sports (1-2 times per week) - Varies\n"
          "7. Rest and Recovery - Varies (Ensure at least 1-2 rest days per week)\n")
    print("----------------------------------------------------------------------------")



#its for age 25 to 40

if( 60 <= user_b <=90 and 25<=user_a <=40):
    print("----------------------------------------------------------------------------")
    print("its a perfect workout for you")
    print("1. Cardiovascular Exercise (3-5 times per week) - 30-60 minutes\n"
            "2. Strength Training (3-4 times per week) - 45-60 minutes\n"
            "3. High-Intensity Interval Training (HIIT) or Circuit Training (1-2 times per week) - 20-30 minutes\n"
            "4. Flexibility and Mobility Training (2-3 times per week) - 15-30 minutes\n"
            "5. Yoga or Pilates (1-2 times per week) - 30-45 minutes\n"
            "6. Outdoor Activities or Sports (1-2 times per week) - Varies\n"
            "7. Rest and Recovery - Varies (Ensure at least 1-2 rest days per week)")
    
    print("----------------------------------------------------------------------------")

    
#its for age 40 to 60

elif(50 <=user_b<=90 and 40<=user_a <=60):
    print("----------------------------------------------------------------------------")
    print("its a perfect workout for you")
    print("1. Cardiovascular Exercise (3-5 times per week) - 30-60 minutes\n"
        "2. Strength Training (2-4 times per week) - 45-60 minutes\n"
        "3. Low-Impact Aerobic Exercise (2-3 times per week) - 20-45 minutes\n"
        "4. Flexibility and Mobility Training (3-4 times per week) - 15-30 minutes\n"
        "5. Functional Training and Balance Exercises (2-3 times per week) - 30-45 minutes\n"
        "6. Mind-Body Exercises (e.g., Tai Chi, Yoga) (1-2 times per week) - 30-60 minutes\n"
        "7. Rest and Recovery - Varies (Ensure at least 1-2 rest days per week)")
    print("----------------------------------------------------------------------------")
    
else:
    print("go for runing")
    