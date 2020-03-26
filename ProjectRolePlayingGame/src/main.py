import os
import sys
import codecs
import math
import pprint
import pymongo

from util.Serialization import *
from util.MongoDB import *
from util.InputVerification import *
from world.World import *
from character.Character import *

def create_the_world():
    print("Vous voici dans la création de votre monde.")
    print("Quel est le nom de votre monde ?")
    name = correct_str_input()
    print("Quelle sera la date à laquel votre monde commencera ? : ")
    date = correct_int_input()

    return World(name, date)

def create_character(world):
    # * -- Character's name --
    print("Veuillez entrer le nom de votre personnage : ")
    name = correct_str_input()

    # * -- Character's description --
    print("Saisissez maintenant une description de votre personnage : ")
    desc = correct_str_input()

    # Character's creation without much details
    # ? for now needed to call the guessing functions
    character = Character(name, "None", "None", "None", "None", "None", desc)

    # * -- Trying to guess the gender of the character...
    char_gender = character.guess_the_gender()
    print("Il semblerait que votre personnage soit de sexe", char_gender)
    is_right_gender = yes_no_question("Est-ce correcte ? : ")
    # ... if it is not correct then asks for the gender ...
    if not is_right_gender :
        char_gender = ask_str("Quelle est le sexe de votre personnage ?", m="asculin", f="éminin")
    # ... add the class to the character
        if char_gender == "m":
            character.set_gender("masculin")
        elif char_gender == "f":
            character.set_gender("féminin")
    character.set_gender(char_gender)

    # * -- Trying to guess the class of the character by its description...
    char_class = character.guess_the_class()
    print("Il semblerait que votre personnage soit", char_class)
    is_right_class = yes_no_question("Est-ce correcte ?")
    # ... if it is not correct then asks for the class ...
    if not is_right_class :
        print("Quelle est sa classe ? :")
        char_class = correct_str_input()
    # ... add the class to the character
    character.set_classe(char_class)

    # * -- Trying to guess the race of the character by its description...
    char_race = character.guess_the_race()
    print("Il semblerait que votre personnage soit", char_race)
    is_right_race = yes_no_question("Est-ce correcte ?")
    # ... if it is not correct then asks for the race ...
    if not is_right_race :
        print("Quelle est sa racee ? :")
        char_race = correct_str_input()
    # ... add the race to the character
    character.set_race(char_race)
    world.add_race(char_race)

    # * -- Trying to guess the age of the character as well...
    char_age = character.guess_the_age()
    print("Il semblerait que votre personnage soit agé(e) de :", char_age)
    is_right_age = yes_no_question("Est-ce correcte ?")
    # ... if it is not correct then asks for the age ...
    if not is_right_age :
        print("Quelle est son age ? (0 à 150) :")
        char_age = correct_int_input()
    # ... add the class to the character
    character.set_age(char_age)
    
    # * -- Trying to guess the birthplace of the character by its description...
    char_birthplace = character.guess_the_birthplace()
    print("Il semblerait que votre personnage vient de ", char_birthplace)
    is_right_birthplace = yes_no_question("Est-ce correcte ?")
    # ... if it is not correct then asks for the class ...
    if not is_right_birthplace :
        print("D'où vient votre personnage ? :")
        char_birthplace = correct_str_input()
    # ... add the class to the character
    character.set_birthplace(char_birthplace)
    # make sure the place didn't exists before adding to the world
    world.add_place(char_birthplace)
    try:
        insert_to_collection("world", "places", serialize_place_into_bson(world, char_birthplace))
    except pymongo.errors.DuplicateKeyError:
        pass

    try_to_link_birthplace = world.find_same_birthplace(character)
    if (len(try_to_link_birthplace) != 0) and (character not in try_to_link_birthplace):
        print("Vous avez grandi à " + char_birthplace + ". Connaissez-vous un des personnages suivant qui y ont également grandi ? :")
        for c in try_to_link_birthplace:
            print(c.get_name(), sep=", ")
        print("Lequel ?")
        knowing = correct_str_input()
        for c in try_to_link_birthplace:
            if knowing == c.get_name():
                print("Votre personnage connaît", c.get_name())
                try:
                    insert_to_collection("links", "grew_up_in", serialize_birth_link_into_bson(character, c, "grew_up_in"))
                except:
                    print("Une erreur est survenue lors de la création de lien")
                else:
                    print("Lien crée")

    world.add_character(character)
    return character


if __name__ == "__main__":
    a_world_has_been_selected = False
    world_chosen = None

    print("Bienvenue sur NLRPG !")
    while True:
        if not a_world_has_been_selected:
            print("Que souhaitez-vous faire ?")
            print("\t(1) Créer un monde")
            print("\t(2) Choisir un monde existant")
            print("\t(3) Quitter")
            user_input = correct_int_input()
            if user_input == 1:
                new_world = create_the_world()
                try:
                    insert_to_collection("world", "worlds", serialize_world_into_bson(new_world))
                except pymongo.errors.DuplicateKeyError:
                    print("Le monde existe déjà.")
                else:
                    world_chosen = new_world
                    a_world_has_been_selected = True
            elif user_input == 2:
                print("Voici l'id (il s'agit de NomDate) des mondes existants : ")
                all_worlds = query_collection("world", "worlds")
                for world in all_worlds:
                    print("\t", world['_id'])
                print("Entrez l'(id) du monde pour le sélectionner, ou (q) pour retourner en arrière : ")
                user_input = correct_str_input()
                if user_input != 'q':
                    selected = query_specific_element("world", "worlds", "_id", user_input)
                    print(selected)
                    name, date, places, races, characters = deserialize_world_from_bson(selected)
                    world_chosen = World(name, date, places, races, characters)
                    a_world_has_been_selected = True
                    print(world_chosen, world_chosen.get_name(), world_chosen.get_places())
                    for key in selected:
                        print(key)
                elif user_input == 'q':
                    continue
            elif user_input == 3:
                exit()
            
        if a_world_has_been_selected:
            print("Que souhaitez-vous faire ?")
            print("\t(1) Créer un personnage")
            print("\t(2) Voir les personnages")
            print("\t(3) Quitter")
            user_input = correct_int_input()
            if user_input == 1:
                new_character = create_character(world_chosen)
                try:
                    insert_to_collection("world", "characters", serialize_character_into_bson(new_character))
                except pymongo.errors.DuplicateKeyError:
                    print("Le personnage existe déjà.")
                else:
                    print("Personnage crée.")
            elif user_input == 2:
                print("Voici l'id (il s'agit de NomAge) des personnages crées : ")
                all_characters = query_collection("world", "characters")
                for character in all_characters:
                    print("\t", character['_id'])
                print("Entrez l'(id) du personnage pour voir ses informations, ou (q) pour revenir en arrière : ")
                user_input = correct_str_input()
                if user_input != 'q':
                    selected = query_specific_element("world", "characters", "_id", user_input)
                    for key in selected:
                        print("Key :", key)
                elif user_input == "q":
                    continue
            elif user_input == 3:
                exit()
