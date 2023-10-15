person={
    'nile': 'egypt',
    'ravi': 'pakistan',
    'papya': 'thailalnd',
    'bosphorus': 'turkey',
    'Thames':   'london'

        }

#print(person['age'])
favourite_city= person['nile'].title()
print(f"\nEhsun's favourite city is {favourite_city}")
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(person)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for mydata in person.values():
    print(mydata)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
for river in person.keys():
    print(river)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
favourite_places={
                  'Ehsun':['egypt','turkey','amsterdam'],
                    'Mahnoor':['dubai','paris','toronto'],
                    'Saira':['lahore','islamabad','london'],
}
for people,places in favourite_places.items():
        print(f"{people}'s favourite place is:")
        for place in places:
             print(f"\t {place.title()}")

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
cities={
        'London':{
            'country':'UK',
            'population':'10 million',
            'fact':'Most visited city in the world'},

        'Lahore':{
            'country':'Pakistan',
            'population':'14 million',
            'fact':'Most polluted city in the world'},

        'New York':{
            'country':'USA',
            'population':'12 million',
            'fact':'capital of USA'}
    }
for cityname,cityfact in cities.items():
    print(f"\n city:{cityname}")
    country=cityfact['country']
    population=cityfact['population']
    fact=cityfact['fact']
    print(f"country:{country}")
    print(f"population:{population}")
    print(f"fact:{fact}")
