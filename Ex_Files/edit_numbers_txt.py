file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

print(lines)

for x in range(len(lines)):
  try:
    number = float(lines[x]) * 2
    lines[x] = f"{number}\n"
  except Exception as e:
    pass

print(lines)

file = open("numbers.txt", "w")
file.writelines(lines)
file.close()


# edit = open("numbers.txt", "w")
# edit.write(str(read))
# edit.close()