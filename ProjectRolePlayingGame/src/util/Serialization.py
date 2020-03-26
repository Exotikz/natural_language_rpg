import json

def serialize_character_into_json(char, f):
    """ Serialize the data in string for JSON format. """
    return json.dump({'name': char.get_name(), 'birthplace': char.get_birthplace(), 'age': char.get_age(), 'race': char.get_race(), 'bio': char.get_bio()}, f, indent=4)

def deserialize_character_from_json(f):
    return json.load(f)

def serialize_place_into_bson(world, place):
    return { "_id" : world.get_name()+"_"+place, "world" : world.get_name(), "name": place }

def serialize_birth_link_into_bson(char1, char2, link):
    return { "_id" : char1.get_name()+link+char2.get_name(), "type": link, "birthplace": char1.get_birthplace(), "idchar1" : char1.get_name()+str(char1.get_age()), "idchar2" : char2.get_name()+str(char2.get_age()) }

def serialize_character_into_bson(char):
    return { "_id" : char.get_name()+str(char.get_age()), "name": char.get_name(), "birthplace": char.get_birthplace(), "age": str(char.get_age()), "id": char.get_id(), "race": char.get_race(), "gender": char.get_gender(), "class": char.get_classe(), "bio": char.get_bio() }

def deserialize_character_from_bson(bson):
    name = ""
    birthplace = ""
    age = 0
    id = ""
    race = ""
    gender = ""
    classe = ""
    bio = ""
    for key, value in bson.items():
        if key == "name":
            name = value
        elif key == "birthplace":
            birthplace = value
        elif key == "age":
            age = value
        elif key == "id":
            id = value
        elif key == "race":
            race = value
        elif key == "gender":
            gender = value
        elif key == "class":
            classe = value
        elif key == "bio":
            bio = value

    return name, birthplace, age, race, gender, classe, bio, id

def serialize_world_into_bson(world):
    return { "_id" : world.get_name()+str(world.get_date()), "name": world.get_name(), "date": world.get_date(), "places": world.get_places(), "races": world.get_races(), "characters": world.get_characters() }

def deserialize_world_from_bson(bson):
    name = ""
    date = 0
    places = []
    races = []
    characters = []
    for item in bson:
        for key, value in item.items():
            if key == "name":
                name = value
            elif key == "date":
                date = value
            elif key == "places":
                places = value
            elif key == "races":
                races = value
            elif key == "characters":
                characters = value

    return name, date, places, races, characters