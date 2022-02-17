class GotCharacter:
    '''Game Of Thrones Character'''
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    '''A class representing the Stark family.\
 Or when bad things happen to good people.'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter Is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        if self.is_alive:
            self.is_alive = False
        else:
            print("I'm already dead")


class Lannister(Stark):
    '''A coat of gold a coat of red a lion still has claws
And mine are long and sharp my lord
As long and sharp as yours
And so he spoke, and so he spoke
That Lord of Castamere
But now the rains weep o'er his hall
With no one there to hear
Yes now the rains weep o'er his hall
And not a soul to hear'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear me roar!"
