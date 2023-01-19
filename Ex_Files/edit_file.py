# read the lines in, edit them, then write them back in

#read
file = open("cheese.txt", "r")
lines = file.readlines()
file.close()

# edit
# file = open("cheese.txt", "w")
lines.insert(0, "Using insert function\n")
lines[1] = "Hello, this is another way to insert an edit\n"
lines[-1] = lines[-1] + "\n"
lines.append("Goodbye!")

print(lines)


# write
# lines = "Hello,\nthis is an edit"
file = open("cheese.txt", "w")
file.writelines(lines)
file.close()
