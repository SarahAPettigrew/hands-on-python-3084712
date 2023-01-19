import pickle

age = 33

file = open("pickle_text.txt", "wb")
pickle.dump(age, file)
file.close()