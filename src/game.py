import random 
from enum import Enum


class Game:
    def __init__(self, number = 1, pot = 100, bet = [1]) :       
        self.pot = pot                              # pot amount
        self.bet = bet                              # List of bet amounts on diff. faces : [spade, heart, diamond, club, crown, flag]
        self.number = number                        # number of die to roll
        self.__faces = [0]*number                   # list of rolled faces in numeral form

    @property
    def pot(self):
        return self.__pot
    
    @pot.setter
    def pot(self, pot):
        '''
        forces pot to be >= 0
        '''
        self.__pot = pot
        if self.__pot < 0 : self.__pot = 0
    
    @property
    def bet(self):
        return self.__bet
    
    @bet.setter
    def bet(self, bet):
        '''
        sets bet if in [1, pot]
        '''
        print(type(sum))
        if sum(bet) >= 1 and sum(bet) <= self.pot :
            self.__bet = bet
        else :
            raise ValueError(f' Total bet has to be 1..pot')
   
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        '''
        sets number of dices if bigger than 0
        '''
        if number > 0:
            self.__number = number
            self.__faces = [0]*number
    
    def roll(self) : 
        '''
        fills faces list with new random numbers [1,6]
        '''
        for i in range(self.number) :
            self.__faces[i] = random.randint(1, 6)
    
    def check(self):
        '''
        * If none or one of the dices show the face/symbol on which bet is placed, then the bet is lost
        * If more than one dices show the symbol on which bet is placed, player wins number of dices times
             the bet amount. Also, the player keeps the bet.

        Winnings (updated bet) are added into pot and lost bet is subtracted from the pot. 
        '''
        text = ''
        for i in range(len(self.__faces)) :
            text += f'{Game.Dice(self.__faces[i]).name}   '
        text += '\n\n'
        for dice in Game.Dice :
           # print(dice.value + 1)
            if self.bet[dice.value - 1] != 0 :
                try :
                    if self.__faces.count(dice.value) > 1 : 
                        text += f'You won {self.bet[dice.value - 1]} x {self.__faces.count(dice.value)} ! on {dice.name}\n'
                        self.pot += self.bet[dice.value - 1] * self.__faces.count(dice.value) 
                    else : 
                        text += f'You lost {self.bet[dice.value - 1]} ! on {dice.name}\n'
                        self.pot -= self.bet[dice.value - 1]
                except :
                    pass
                
        text += f'\nYour pot is now {self.pot}'
        return text
        
    ## Map numeral dice's faces to symbols
    class Dice(Enum) :
        SPADE = 1
        HEART = 2
        DIAMOND = 3
        CLUB = 4
        CROWN = 5
        FLAG = 6
        