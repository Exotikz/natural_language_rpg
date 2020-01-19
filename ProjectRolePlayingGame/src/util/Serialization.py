import json

''' Serialize the data in string for JSON format.
'''
def serialize_character(char, f):
    return json.dump({'name': char.get_name(), 'birthplace': char.get_birthplace(), 'birthdate': char.get_birthdate(), 'race': char.get_race(), 'bio': char.get_bio()}, f, indent=4)

def deserialize_character(f):
    return json.load(f)