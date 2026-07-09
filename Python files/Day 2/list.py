# Here we are going to learn about data structures in py 
# List 
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Indexing in List 
print(fruits[0])
print(fruits[1])

# Lists are mutable that means we can change the value of list
fruits[0]= "kiwi"
print(fruits)

# .append is a method that is used to add an element at the end of the list
fruits.append("orange")
print(fruits)

# .remove is a method that is used to remove an element from the list
fruits.remove("banana")
print(fruits)

# len  is a function that we use to find the length of the string 
len(fruits)


 # list slicing is used to access a range of elements in a list. It takes two indexes, the start index and the end index, and returns a new list containing the elements from the start index to the end index (excluding the end index).
print(fruits[0:3:2]) # here 0 is the start index, 3 is the end index and 2 is the step size(Basically tells how many elements to skip). 
# Mini challenge 
favorite_players = ["Messi", "Neymar Jr", "Mbappe", "Lamine Yamal", "Pedri"]

#Q1 
print(favorite_players)

#Q2 
print(favorite_players[0])

#Q3 
print(favorite_players[-1])

#Q4
favorite_players[3] = "Dani Olmo"
#Q5
favorite_players.append("Jordi Alba")

#Q6
favorite_players.remove("Neymar Jr")

#Q7
print(len(favorite_players))

#Nested list - a list inside another list. follows the same indexing as the normal list but we have to use two indexes to access the elements of the nested list.
employees = [
    ["John", "Data Scientist", 8],
    ["Sarah", "Data Analyst", 5],
    ["Mike", "ML Engineer", 6]
]




numbers_sort=[1,2,3,4,5,6,7,8]
numbers_sort.sort() # sort method is used to sort the list in ascending order
sorted(numbers_sort) # sorted function is used to sort the list in ascending order and returns a new list