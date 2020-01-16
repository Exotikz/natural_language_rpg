class Character(object):
    ''' Character creation class
    
    '''
    def __init__(self, name=None, where=None):
        self.name = name
        self.where = where

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
    def get_where(self):
        return self.where

    ''' Set the origin of the character
    '''
    def set_where(self, where):
        self.where = where

    ''' Represent a brief description of the character
    '''
    def __str__(self):
        return self.name + " from " + self.where
