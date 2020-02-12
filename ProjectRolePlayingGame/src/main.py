import os
import sys
import codecs
import math
import pprint

from util.Serialization import *
from character.Character import *
from util.MongoDB import query_collection
from util.InputVerification import *

def create_character():
    print("Veuillez entrer un nom : ")
    name = correct_str_input()
    print("Saisissez maintenant une description de votre personnage : ")
    desc = correct_str_input()
    character = Character(name, "None", "None", "None", "None", desc)
    print("Il semblerait que votre personne soit ", character.guess_the_class())
    is_right_class = yes_no_question("Est-ce correcte ?")
    if is_right_class :
        character.set_classe(character.guess_the_class())
    else:
        print("Quelle est sa classe ? :")
        character.set_classe(correct_str_input())

    print("Il semblerait que votre personne soit agé de : ", character.guess_the_age())
    is_right_age = yes_no_question("Est-ce correcte ?")
    if is_right_age :
        character.set_birthdate(character.guess_the_age())
    else:
        print("Quelle est son age ? :")
        character.set_classe(correct_int_input())

    return character

if __name__ == "__main__":
    print("Bienvenue sur NLRPG !")
    char = create_character()
    print(char)

    























    # # Test char & serialize
    # warrior = ""
    # with codecs.open("ProjectRolePlayingGame/src/util/warrior.txt", 'r', encoding='utf8') as f:
    #     warrior = f.read()
    # mage = ""
    # with codecs.open("ProjectRolePlayingGame/src/util/mage.txt", 'r', encoding='utf8') as f:
    #     mage = f.read()
    # ranger = ""
    # with codecs.open("ProjectRolePlayingGame/src/util/ranger.txt", 'r', encoding='utf8') as f:
    #     ranger = f.read()
    
    # char = Character("Test", "TEST", 1082, "humain", warrior)
    # print("Il semblerait que la classe de votre personnage soit {}.".format(char.guess_the_class()))

    # print(warrior)
    # # for word in warrior:
    # #     print(word)
