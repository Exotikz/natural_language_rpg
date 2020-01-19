from util.Compute_Frequency import term_frequency

class Character(object):
    ''' Character creation class
    '''
    def __init__(self, name, birthplace, birthdate, race, bio):
        self.name = name
        self.birthplace = birthplace
        self.birthdate = birthdate
        self.race = race
        self.bio = bio

    ''' Get the name of the character
    '''
    def get_name(self):
        return self.name

    ''' Set the name of the character
    '''
    def set_name(self, name):
        self.name = name

    ''' Get the origin of the character
    '''
    def get_birthplace(self):
        return self.birthplace

    ''' Set the origin of the character
    '''
    def set_birthplace(self, birthplace):
        self.birthplace = birthplace

    ''' Get the birthdate of the character
    '''
    def get_birthdate(self):
        return self.birthdate

    ''' Set the birthdate of the character
    '''
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    ''' Get the race of the character
    '''
    def get_race(self):
        return self.race

    ''' Set the race of the character
    '''
    def set_race(self, race):
        self.race = race

    ''' Get the bio of the character
    '''
    def get_bio(self):
        return self.bio

    ''' Set the bio of the character
    '''
    def set_bio(self, bio):
        self.bio = bio

    ''' Represent a brief description of the character
    '''
    def __str__(self):
        return self.name + "\n" + self.birthplace + "\n" + str(self.birthdate) + "\n" + self.race + "\n" + self.bio

    def guess_the_class(self):
        # frequency from nltk
        freq = term_frequency(self.bio)
        
        # Data
        warrior = [
            "guerrier", "soldat", "gladiateur", "solide", "force", "fort", "forte", "grand", "grande", "herculéen", "hérculéenne",
            "sabre", "épée", "bouclier", "lance", "hache", "masse", "massue",
            "corps à corps", "mélée", "front", "première ligne"
        ]
        mage = [
            "mage", "esprit", "intelligence", "intelligent", "intelligente", "sorcier", "sorcière", "magicien", "magicienne"
            "bâton", "baguette", "livre d'incantation", 
            "magie", "éléments", "mana", "énérgie", "sorcellerie", "sort", "incantation"
        ]
        ranger = [
            "chasseur", "chasseresse", "rôdeur", "rôdeuse", "gardien", "sauvage", "agile", "dompteur", "animal", "imprévisible",
            "arc", "flèche", "carquois", "arbalète", "carreau", "dague", "couteau", "animaux", "piège",
            "camouflage", "dissimulation", "forêt", "bois"
        ]

        # counting
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