import re

from util.Compute_Frequency import term_frequency
from util.MongoDB import query_collection

class Character(object):
    """ Character creation class """
    def __init__(self, name, birthplace, birthdate, race, classe, bio):
        self.name = name
        self.birthplace = birthplace
        self.birthdate = birthdate
        self.race = race
        self.classe = classe
        self.bio = bio

    """ Get the name of the character """
    def get_name(self):
        return self.name

    """ Set the name of the character """
    def set_name(self, name):
        self.name = name

    """ Get the origin of the character """
    def get_birthplace(self):
        return self.birthplace

    """ Set the origin of the character """
    def set_birthplace(self, birthplace):
        self.birthplace = birthplace

    """ Get the birthdate of the character """
    def get_birthdate(self):
        return self.birthdate

    """ Set the birthdate of the character """
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    """ Get the race of the character """
    def get_race(self):
        return self.race

    """ Set the race of the character """
    def set_race(self, race):
        self.race = race

    """ Get the classe of the character """
    def get_classe(self):
        return self.classe

    """ Set the classe of the character """
    def set_classe(self, classe):
        self.classe = classe

    """ Get the bio of the character """
    def get_bio(self):
        return self.bio

    """ Set the bio of the character """
    def set_bio(self, bio):
        self.bio = bio

    """ Represent a brief description of the character """
    def __str__(self):
        return self.name + "\n" + self.birthplace + "\n" + str(self.birthdate) + "\n" + self.race + "\n" + self.bio

    def guess_the_age(self):
        phrases = self.bio.split(".")
        phrases = list(filter(lambda x: x.find("ans") != -1 or x.find("années") != -1, phrases))
        phrase_with_age = ""
        if (len(phrases) == 1):
            phrase_with_age = phrases[0]
        else:
            for phrase in phrases:
                #? On imagine impossible que l'age soit inférieur à 0 ou
                #? supérieur à 150
                temp_int = int(re.search(r'\d+', phrase).group())
                if (temp_int >= 0 and temp_int < 151):
                    phrase_with_age = phrase
            
        return int(re.search(r'\d+', phrase_with_age).group())


    def guess_the_class(self):
        # * frequency from nltk
        freq = term_frequency(self.bio)
        
        # * Data
        # Get warrior's keyword from db
        warrior = query_collection("rules", "classes", "name", "warrior")
        for key in warrior:
            warrior = key["keyword"]
        # Get mage's keyword from db
        mage = query_collection("rules", "classes", "name", "mage")
        for key in mage:    
            mage = key["keyword"] 
        # Get ranger's keyword from db
        ranger = query_collection("rules", "classes", "name", "ranger")
        for key in ranger:
            ranger = key["keyword"] 

        # * counting
        freq_warrior = 0
        freq_mage = 0
        freq_ranger = 0
        for word, frequency in freq.most_common(30):
            if (word in warrior): freq_warrior += frequency
            elif (word in mage): freq_mage += frequency
            elif (word in ranger): freq_ranger += frequency

        if (freq_warrior > freq_mage and freq_warrior > freq_ranger):
            return "guerrier"
        elif (freq_mage > freq_warrior and freq_mage > freq_ranger):
            return "mage"
        elif (freq_ranger > freq_warrior and freq_ranger > freq_mage):
            return "rôdeur"
        else:
            return "non détérminé"
