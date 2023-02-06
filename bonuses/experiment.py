from parser import parse

user_input = input("Enter feet and inches")


def convert(feet, inches):
    meters = feet * 0.3848 + inches * 0.0254
    return meters

parsed = parse(user_input)

result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']} : feet , {parsed['inches']} is iqual to {result}")

print(result)