# Here We are going to learn about Sets in python 
# Sets {} - unordered collection of unique elements(no duplicates)
numbers_set = {1,1,2,3,2,3,4,5,6,4,6,7}
print(numbers_set) 
#The concept of indxing does not exist with sets 
print(numbers_set[0]) # Type Error will come as there is no order or index

#To Create a empty set 
sample_empty_DS = {}
print(type(sample_empty_DS)) # if notice here py recognizes sample_empty_DS as a Dict , so in order to declare an empty set you should do this :

sample_empty_set = set()
print(type(sample_empty_set))

# Arithmaic Op's 
sample_set_1 = {1,2,3,7,9}
sample_set_2 = {4,5,6,7,8,9}

#Union - Everything combined 
print(sample_set_1 | sample_set_2)
# or you can write 
print(sample_set_1.union(sample_set_2))

#Intersection - only common Elements 
print(sample_set_1 & sample_set_2)
# or you can say 
print(sample_set_1.intersection(sample_set_2))

# Diff - unique elements in the first var 
print(sample_set_1 - sample_set_2)

# Symmetric diff - unique element from both obj or mul obj 
print(sample_set_1 ^ sample_set_2)

# Note : sets can contains tulpes 

# Mini Challenge 
languages = {"Python", "Java", "C++"}

#Q1 
languages.add("SQL")
print(languages)

#Q2 
languages.update(["R","JavaScript"])
print(languages)

#Q3
languages.discard("Java")
print(languages)

#Q4 - got a keyerror  
languages.remove("Go")

#Q5
languages.discard("Go")
print(languages)

#Q6
A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))
print(A.intersection(B))
print(A-B)
print(A^B)