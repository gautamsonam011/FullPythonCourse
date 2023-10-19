import pickle

l = [10,34,56,34]

file = open("pickle.txt","wb")
pickle.dump(l,file)
file.close()


file1 = open("pickle.txt","rb")
l1 = pickle.load(file1)
print(l1)