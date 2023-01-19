import sys

total = 1
for argument in sys.argv:
  try:
    number = int(argument)
    total *= number
  except Exception as e:
    pass


# print(total)

# file_name = sys.argv[1]
# print(file_name)
# file = open("file.txt", "w")
# file.write(file_name)
# file.close()

file = open("file.txt", "r")
file_text = file.readlines()
print(file_text)
file.close()