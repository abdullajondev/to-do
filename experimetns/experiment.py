"""contents = ['All carrots are to be sliced',
            'The carrots were reportedly sliced',
            'the slicing process was well presented']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"textfiles/{filename}", "w")
    file.write(content)"""


file = open("textfiles/new.txt", "r")
words = file.readlines()

for num, word in enumerate(words):
    upperwords = word.title()
    row = f"{num}-{upperwords}"
    print(row)

"""file = open("textfiles/new.txt", 'r')
content = file.read()
print(content.title())"""
