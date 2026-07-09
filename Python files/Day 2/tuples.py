# Here we are going to learn about tuples (Used in Cases whre data is static i.e does not change no matter what like DOB,Name, Latitude)

# Ordered Collection of items - Tuples but they are immutable (Read  Only ). They are faster in speed in terms of traversal 

players =("Messi","Neymar","Suarez")
print(players)

# indexing - Same as List ( -ve indexing is also the same here )
print(players[0])
print(players[1])
print(players[2])


# Slcing is also the same as list 
mls_players = players[0:3:2] # Start index : End Index : Step Value (Default == 1)
print(mls_players)

fruits = ("banana","Strawberry","Pineapple","Apple","Orange")
print(fruits[0:5:2])


# Tuple Packing - Process of grouping multiple values together into a single tuple object
print(fruits)

#Tuple Unpacking - The reverse of tuple packing - extract individual values from a packed variable and assign them to separate variables.
Player_Info=("Messi",39,"Inter Miami","Forward/CAM") # Packed tuple 
player_name,player_age,current_club,position = Player_Info # Unpacking the tuple 
print("The details of the player are as follows: ")
print(player_name)
print(player_age)
print(current_club)
print(position)


# Tuple Methods (worth using) - .count(), .index()
numbers = (1,2,2,3,2)
print(numbers.count(2))

players = ("Messi","Neymar","Pedri")
print(players.index("Pedri"))

# Mini Challenge 
movie = ("Interstellar",2014,"Sci-Fi",8.7)

# Q1 
print("The name of the movie is :- ",movie[0])

#Q2 
print("The movie was released in: - ",movie[-3])

#Q3
print(movie[1:3])


#Q4
movie_name,movie_release_year,movie_genre,movie_rating = movie
print(movie_rating)

#Q5
movie[0] =  "Cars"