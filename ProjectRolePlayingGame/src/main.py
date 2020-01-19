import os
import sys
import codecs
import math
from tkinter import *

from character.Character import *
from util.Serialization import *

def create_character():
    # @TO_DO: check if the input is correct.
    print("Character created.")
    return Character(nom_entry.get(), where_entry.get(), age_entry.get(), race_entry.get(), bio_entry.get(1.0, END))


if __name__ == "__main__":
    #@TO_DO: Ménagerie

    # Programme principale
    main_window = Tk()
    # Titre de la fenetre
    main_window.title("Projet Annuel")

    # Partie gauche
    questionnaire = Frame(main_window)
    # Partie droite
    fiche = Frame(main_window)
    # Le nom
    nom_label = Label(questionnaire, text="Nom")
    nom = StringVar()
    nom.set("Grom")
    nom_entry = Entry(questionnaire, textvariable = nom, width = 50)
    # La provenance
    where_label = Label(questionnaire, text="Origine")
    where = StringVar()
    where.set("Bricquebec")
    where_entry = Entry(questionnaire, textvariable = where, width = 50)
    # L'age
    age_label = Label(questionnaire, text="Age")
    age = StringVar()
    age.set("29")
    age_entry = Entry(questionnaire, textvariable = age, width = 50)
    # La race
    race_label = Label(questionnaire, text="Race")
    race = StringVar()
    race.set("Human")
    race_entry = Entry(questionnaire, textvariable = race, width = 50)
    # La bio
    bio_label = Label(questionnaire, text = "Biographie")
    bio_entry = Text(questionnaire, width = 100)

    # Boutton créer
    create_button = Button(questionnaire, text = "Créer", command=create_character)

    nom_label.pack()
    nom_entry.pack()

    where_label.pack()
    where_entry.pack()
    
    age_label.pack()
    age_entry.pack()
    
    race_label.pack()
    race_entry.pack()

    bio_label.pack()
    bio_entry.pack()
    create_button.pack()

    # Test char & serialize
    warrior = ""
    with codecs.open("natural_language_rpg/ProjectRolePlayingGame/src/util/warrior.txt", 'r', encoding='utf8') as f:
        warrior = f.read()
    mage = ""
    with codecs.open("natural_language_rpg/ProjectRolePlayingGame/src/util/mage.txt", 'r', encoding='utf8') as f:
        mage = f.read()
    ranger = ""
    with codecs.open("natural_language_rpg/ProjectRolePlayingGame/src/util/ranger.txt", 'r', encoding='utf8') as f:
        ranger = f.read()
    
    char = Character("Test", "TEST", 1082, "humain", warrior)
    print("Il semblerait que la classe de votre personnage soit {}.".format(char.guess_the_class()))

    with codecs.open("natural_language_rpg/ProjectRolePlayingGame/src/character/warrior.txt", 'w', encoding='utf8') as f:
        serialize_character(char, f)

    with codecs.open("natural_language_rpg/ProjectRolePlayingGame/src/character/warrior.txt", 'r', encoding='utf8') as f:
        warrior_character = deserialize_character(f)
        print(warrior_character)

    questionnaire.pack(side = LEFT)
    fiche.pack(side = RIGHT)

    # Execution
    # main_window.mainloop()