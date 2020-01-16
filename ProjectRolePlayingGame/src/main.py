import os
import sys
import math
from tkinter import *

from sklearn.feature_extraction.text import TfidfVectorizer
from character.Character import *

def personnage_creer():
    histoire = LabelFrame(fiche, text = "Information", padx = 20, pady = 20)
    histoire.pack(fill = "both", expand = "yes")
    char = Character(nom_entry.get(), where_entry.get(), age_entry.get(), race_entry.get(), bio_entry.get(1.0, END))

    tfidf = TfidfVectorizer()
    raw_origine = bio_entry.get(1.0, END)
    origine_phrases = raw_origine.split(".")
    phrase = []
    for phrases in origine_phrases:
        phrase.append(phrases)
    response = tfidf.fit_transform(phrase)

    Label(histoire, text = "Nom : {}".format(char.get_name())).pack()
    Label(histoire, text = "Origine : {}".format(char.get_birthplace())).pack()
    Label(histoire, text = "Age : {}".format(char.get_age())).pack()
    Label(histoire, text = "Race : {}".format(char.get_race())).pack()
    
    features_names = tfidf.get_feature_names()
    for col in response.nonzero()[1]:
        Label(histoire, text = "{} - {}".format(features_names[col], response[0, col])).pack()
    # return Character, tf_idf bio


if __name__ == "__main__":
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
    create_button = Button(questionnaire, text = "Créer", command=personnage_creer)

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
    char = Character("Jason", "MURICA", 1776, "humanoid", "Fuck yeah")
    print(char)
    print(char.serialize())

    questionnaire.pack(side = LEFT)
    fiche.pack(side = RIGHT)

    # Execution
    main_window.mainloop()