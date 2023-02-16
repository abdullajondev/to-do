from bonuses.converters import convert
from parser import parse

user_input = input("Enter feet and inches")

parsed = parse(user_input)

result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']}:feet , {parsed['inches']}; inches is iqual to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")