import csv

movies = []

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movies.append(row)

print("MOVIE RECOMMENDATION SYSTEM")
print("----------------------------")

genre = input("Enter your favorite genre: ").strip().lower()

recommendations = []

for movie in movies:
    if genre in movie["genre"].lower():
        recommendations.append(movie["title"])

if recommendations:
    print("\nRecommended Movies:")

    for movie in recommendations:
        print("-", movie)
else:
    print("\nSorry, no movies found for this genre.")