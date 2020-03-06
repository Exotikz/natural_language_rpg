import json

def serialize_character_into_json(char, f):
    """ Serialize the data in string for JSON format. """
    return json.dump({'name': char.get_name(), 'birthplace': char.get_birthplace(), 'age': char.get_age(), 'race': char.get_race(), 'bio': char.get_bio()}, f, indent=4)

def deserialize_character_from_json(f):
    return json.load(f)

def serialize_character_into_bson(char):
    return { "_id" : char.get_name()+str(char.get_age()), "name": char.get_name(), "birthplace": char.get_birthplace(), "age": str(char.get_age()), "race": char.get_race(), "gender": char.get_gender(), "class": char.get_classe(), "bio": char.get_bio() }