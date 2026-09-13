movies = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Avengers:"]

movies.append("Lucy")  # Adds "Lucy" to the end of the list
print(movies)  # Prints the updated list of movies

print(movies[1:3])  # Prints a slice of the list: ['Inception', 'Interstellar']
print(movies[:2])   # Prints the first two movies: ['The Matrix', 'Inception']
print(movies[-1])   # Prints the last movie in the list: 'Lucy'