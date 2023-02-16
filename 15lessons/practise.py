import random
while True:
    user_input1 = int(input("Enter your first number: "))
    user_input2 = int(input("Enter your second number: "))

    if user_input2 < user_input1:
        print("pls enter lower number first")
    else:
        result = random.randint(user_input1, user_input2)
        print(result)
        break
