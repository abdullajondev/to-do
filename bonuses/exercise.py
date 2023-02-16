from bonuses.state import calculate

while True:
    user_input = float(input("please enter your water state: "))

    result = calculate(user_input)
    print(result)



