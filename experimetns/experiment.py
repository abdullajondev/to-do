"""contents = ['All carrots are to be sliced',
            'The carrots were reportedly sliced',
            'the slicing process was well presented']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"textfiles/{filename}", "w")
    file.write(content)"""

"""file = open("textfiles/new.txt", "r")
words = file.readlines()

for num, word in enumerate(words):
    upperwords = word.title()
    row = f"{num}-{upperwords}"
    print(row)"""

"""file = open("textfiles/new.txt", 'r')
content = file.read()
print(content.title())"""







##LIST comprehension

"""filenames = ['1.doc', '2.report', '3.presentation']

filenames = [file.replace('.', '-') + ".txt" for file in filenames]
print(filenames)"""

"""names = ["john smith", "jay santi", "eva kuki"]

names = [i.title() for i in names]
print(names)"""



"""date = input("Enter today's date: ")
mood = input("how do you rate your mood today from 1 to 10: ")
thoughts = input("let your thoughts flow: ")

with open(f"textfiles/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thoughts)"""

"""while True:
    with open("textfiles/sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("textfiles/sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")"""
while True:
    with open("textfiles/file.txt", 'r') as file:
        words = file.readlines()
        user_input = input("say somthing: ")
        words.append(user_input)

    with open("textfiles/file.txt", "w") as file:
        words = file.writelines(user_input)


