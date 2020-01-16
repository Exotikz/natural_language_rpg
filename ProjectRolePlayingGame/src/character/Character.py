class Character(object):
    ''' Character creation class
    '''
    def __init__(self, name, birthplace, age, race, bio):
        self.name = name
        self.birthplace = birthplace
        self.age = age
        self.race = race
        self.bio = bio

    ''' Serialize the data in string for JSON format.
    '''
    def serialize(self):
        return '{"name": "'+self.name+'", "birthplace": "'+self.birthplace+'", "age": "'+str(self.age)+'", "race": "'+self.race+'", "bio": "'+self.bio+'"}'

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

    ''' Get the age of the character
    '''
    def get_age(self):
        return self.age

    ''' Set the age of the character
    '''
    def set_age(self, age):
        self.age = age

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
        return self.name + "\n" + self.birthplace + "\n" + str(self.age) + "\n" + self.race + "\n" + self.bio
