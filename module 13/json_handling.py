import json

movie= {
    "name": "bee movie",
    "year": 2024,
    "actors": ["Same Smith", "janedoe"]
}

with open("movie.json","r") as file:
    movie_data = json.load(file)
    
print(f"Name: {movie_data['name']}")
print(f"Year: {movie_data['year']}")
print(f"Actors: {movie_data['actors']}")


