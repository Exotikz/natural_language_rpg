from util.MongoDB import *
from util.Serialization import deserialize_character_from_bson
from character.Character import *

class World:
    
    def __init__(self, name, date, places=[], races=[], characters=[]):
        self.name = name
        self.date = date
        self.places = places
        self.races = races
        self.characters = characters

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_places(self):
        return self.places

    def set_places(self, places):
        self.places = places
    
    def get_races(self):
        return self.races

    def set_races(self, races):
        self.races = races

    def get_characters(self):
        return self.characters

    def set_characters(self, characters):
        self.characters = characters

    def add_race(self, race):
        if race not in self.races:
            self.races.append(race)
    
    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            update_to_collection("world", "worlds", { "_id": self.name+str(self.date) }, { "$set": {"places": self.places} })
            return True
        return False

    def add_character(self, character):
        if character.get_id() not in self.characters:
            self.characters.append(character.get_id())
            update_to_collection("world", "worlds", { "_id": self.name+str(self.date) }, { "$set" : {"characters": self.characters} })
            return True
        return False
        
    def find_same_birthplace(self, char):
        link_found = []
        all_characters = query_collection("world", "characters")
        for character in all_characters:
            if character['birthplace'] == char.get_birthplace():
                name, birthplace, age, race, gender, classe, bio, id = deserialize_character_from_bson(character)
                c = Character(name, birthplace, age, race, gender, classe, bio, id)
                link_found.append(c)
        return link_found