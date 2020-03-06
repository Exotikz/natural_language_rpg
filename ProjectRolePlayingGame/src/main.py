import os
import sys
import codecs
import math
import pprint

from util.Serialization import *
from util.MongoDB import query_specific_element, query_collection, insert_to_collection
from util.InputVerification import *
from character.Character import *

def create_character():
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
    
    

    return character


if __name__ == "__main__":
    print("Bienvenue sur NLRPG !")
    while True:
        print("Que souhaitez-vous faire ?")
        print("\t(1) Créer un personnage")
        print("\t(2) Voir les personnages")
        print("\t(3) Quitter")
        usr_input = correct_int_input()
        if usr_input == 1:
            char = create_character()
            insert_to_collection("world", "characters", serialize_character_into_bson(char))
        elif usr_input == 2:
            print("Voici l'id (il s'agit de NomAge) des personnages crées : ")
            all_char = query_collection("world", "characters")
            for item in all_char:
                print("\t", item['_id'])
            print("Entrez l'(id) du personnage pour voir ses informations, ou (q) pour revenir en arrière : ")
            usr_input = correct_str_input()
            if usr_input != 'q':
                selected = query_specific_element("world", "characters", "_id", usr_input)
                for key in selected:
                    print(key)
            elif usr_input == "q":
                continue
        else:
            exit()
