class Character(object):
    ''' Character creation class
        nom, origine, age, race, bio
    '''
    def __init__(self, name, birthplace):
        self.name = name
        self.birthplace = birthplace

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

    ''' Represent a brief description of the character
    '''
    def __str__(self):
        return self.name + " from " + self.birthplace
