import os
import sys
import math
from tkinter import *

from sklearn.feature_extraction.text import TfidfVectorizer
from character.Character import *

def personnage_creer():
    histoire = LabelFrame(fiche, text = "Information", padx = 20, pady = 20)
    histoire.pack(fill = "both", expand = "yes")
    char = Character(nom_entry.get(), where_entry.get())

    tfidf = TfidfVectorizer()
    raw_origine = bio_entry.get(1.0, END)
    origine_phrases = raw_origine.split(".")
    phrase = []
    for phrases in origine_phrases:
        phrase.append(phrases)
    response = tfidf.fit_transform(phrase)

    Label(histoire, text = "Nom : {}".format(char.get_name())).pack()
    Label(histoire, text = "Origine : {}".format(char.get_where())).pack()
    
    features_names = tfidf.get_feature_names()
    for col in response.nonzero()[1]:
        Label(histoire, text = "{} - {}".format(features_names[col], response[0, col])).pack()
    # return Character, tf_idf bio

def compute_TF(word_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_dict.items():
        tf_dict[word] = count / float(bow_count)
    return tf_dict

def compute_IDF(doc_list):
    idf_dict = {}
    n = len(doc_list)
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)
    for doc in doc_list:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1
    for word, val in idf_dict.items():
        idf_dict[word] = math.log10(n / float(val))
    return idf_dict

def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

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
    # La bio
    bio_label = Label(questionnaire, text = "Biographie")
    bio_entry = Text(questionnaire, width = 100)

    print(nom_entry.get())
    # Boutton créer
    create_button = Button(questionnaire, text = "Créer", command=personnage_creer)

    nom_label.pack()
    nom_entry.pack()
    where_label.pack()
    where_entry.pack()
    bio_label.pack()
    bio_entry.pack()
    create_button.pack()

    

    questionnaire.pack(side = LEFT)
    fiche.pack(side = RIGHT)

    # Execution
    main_window.mainloop()