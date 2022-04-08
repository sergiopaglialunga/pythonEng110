me = {
    "name":"David",
    "job":"Trainer",
    "age": 31
}

print(me, type(me))

print(me["job"]) # diccionary name [ Key ]
me["job"] = "Zoo Keeper"
print(me)
me["hobbies"] = ["Video Games", "Board Games"]
print(me)

print(me.get("name")) # if get doesn't find anything returns None
me.update({"name": "D. Harvey"})
print(me)

# film

film = {
    "title": "Saving Private Ryan",
    "director": "Spielberg",
    "budget": 2550000,
    "genre": "action",
    "ratings": {
        'IMDF': 0.79,
        'Rotten Tomatoes': 0.88,
        'Metacritic': 0.84
    }
}

print(film.keys())
print(film["ratings"]["IMDF"])
print(film.items()) # give you a list of tuples: key and value

