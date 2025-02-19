favorite_places = {
    'michael': ['california', 'florida', 'spain'],
    'dad': ['ovid', 'charlotte'],
    'mom': ['manhattan']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
    print()
