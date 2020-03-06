import re
from typing import List
from util.NLTK_lib import term_frequency, term_frequency_without_stop_words, split_sentences, split_words
from util.MongoDB import query_specific_element

class Character:
    """ Character creation class """

    def __init__(self, name: str, birthplace: str, age: int, race: str, gender: str, classe: str, bio: str):
        self.name = name
        self.birthplace = birthplace
        self.age = age
        self.race = race
        self.gender = gender
        self.classe = classe
        self.bio = bio

    def get_name(self) -> str:
        """ Get the name of the character """
        return self.name

    def set_name(self, name: str):
        """ Set the name of the character """
        self.name = name

    def get_birthplace(self) -> str:
        """ Get the origin of the character """
        return self.birthplace

    def set_birthplace(self, birthplace: str):
        """ Set the origin of the character """
        self.birthplace = birthplace

    def get_age(self) -> int:
        """ Get the age of the character """
        return self.age

    def set_age(self, age: int):
        """ Set the age of the character """
        self.age = age

    def get_race(self) -> str:
        """ Get the race of the character """
        return self.race

    def set_race(self, race: str):
        """ Set the race of the character """
        self.race = race
    
    def get_gender(self) -> str:
        """ Get the gender of the character """
        return self.gender

    def set_gender(self, gender: str):
        """ Set the gender of the character """
        self.gender = gender

    def get_classe(self) -> str:
        """ Get the classe of the character """
        return self.classe

    def set_classe(self, classe: str):
        """ Set the classe of the character """
        self.classe = classe

    def get_bio(self) -> str:
        """ Get the bio of the character """
        return self.bio

    def set_bio(self, bio: str):
        """ Set the bio of the character """
        self.bio = bio

    def __str__(self) -> str:
        """ Represent a brief description of the character """
        return self.name + "\n" + self.birthplace + "\n" + str(self.age) + "\n" + self.race + "\n" + self.gender + "\n" + self.classe + "\n" + self.bio

    def guess_the_age(self) -> int:
        # split into phrases
        phrases: List[str] = split_sentences(self.bio)
        # isolating phrases including keywords related to age
        phrases = list(filter(lambda x: x.find("ans") != -1 or x.find("années") != -1, phrases))
        phrase_with_age: str = ""
        if (len(phrases) == 1):
            phrase_with_age = phrases[0]
        else:
            for phrase in phrases:
                #? On imagine impossible que l'age soit inférieur à 0 ou
                #? supérieur à 150
                temp_int: int = re.search(r'\d+', phrase)
                if temp_int:
                    if (int(temp_int) >= 0 and int(temp_int) < 151):
                        phrase_with_age = phrase
            
        if re.search(r'\d+', phrase_with_age):
            return int(re.search(r'\d+', phrase_with_age).group())
        else:
            return -1

    def guess_the_gender(self) -> str:
        # * Splitting the bio
        bio_split = split_words(self.bio)
        # * Frequency from nltk
        freq = term_frequency(bio_split)

        # * Data
        # Get warrior's keyword from db
        male: List[str] = ["Il", "il", "à lui"]
        female: List[str] = ["Elle", "elle", "à elle"]

        # * Counting
        freq_male: float = 0
        freq_female: float = 0
        for word, frequency in freq.most_common(30):
            if (word in male): freq_male += frequency
            elif (word in female): freq_female += frequency

        if (freq_male > freq_female):
            return "masculin"
        elif (freq_female > freq_male):
            return "féminin"
        else:
            return "non détérminé"

    def guess_the_class(self) -> str:
        # * frequency from nltk
        freq = term_frequency_without_stop_words(self.bio)
        
        # * Data
        # Get warrior's keyword from db
        warrior: List[str] = query_specific_element("rules", "classes", "name", "warrior")
        for key in warrior:
            warrior = key["keyword"]
        # Get mage's keyword from db
        mage: List[str] = query_specific_element("rules", "classes", "name", "mage")
        for key in mage:    
            mage = key["keyword"] 
        # Get ranger's keyword from db
        ranger: List[str] = query_specific_element("rules", "classes", "name", "ranger")
        for key in ranger:
            ranger = key["keyword"] 

        # * counting
        freq_warrior: float = 0
        freq_mage: float = 0
        freq_ranger: float = 0
        for word, frequency in freq.most_common(30):
            if (word in warrior): freq_warrior += frequency
            elif (word in mage): freq_mage += frequency
            elif (word in ranger): freq_ranger += frequency

        if (freq_warrior > freq_mage and freq_warrior > freq_ranger):
            if self.gender == "masculin":
                return "guerrier"
            else:
                return "guerrière"
        elif (freq_mage > freq_warrior and freq_mage > freq_ranger):
            return "mage"
        elif (freq_ranger > freq_warrior and freq_ranger > freq_mage):
            if self.gender == "masculin":
                return "rôdeur"
            else:
                return "rôdeuse"
        else:
            return "non détérminée"
