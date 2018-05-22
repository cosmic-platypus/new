def dominance(s1, s2):
    if (s1 == "goose" or s2 == "goose"):
        return "goose"
    elif (s1 == "Max" and s2 != "Max"):
        return s2
    elif (s2 == "Max" and s1 != "Max"):
        return s1
    elif (s1 == "Max" and s2 == "Max"):
        return "Cuck."
    else:
        return "The goose rules all."

competitors = [
    ("Max", "Kat"), 
    ("goose", "Max"),
    ("Evan", "Max"),
    ("Max", "Max"),
    ("poop", "pee")
]

for couple in competitors:
    print(dominance(*couple))