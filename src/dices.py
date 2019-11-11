# -*- coding: utf-8 -*-
import tkinter as tk
from game import Game

class Dices(tk.Tk) :
    '''
     Inherits class tkinter.Tk() and provides GUI 
    '''
    def __init__(self, *args, **kwargs ) :
        '''
        defines and initializes attributes 
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer
        
        self.game = Game(6)
        self.title("Langur Burja")
        self.geometry('900x450')
        
        # 
        self.__v_bet_spade = tk.IntVar()
        self.__v_bet_heart = tk.IntVar() 
        self.__v_bet_diamond = tk.IntVar() 
        self.__v_bet_club = tk.IntVar() 
        self.__v_bet_crown = tk.IntVar() 
        self.__v_bet_flag = tk.IntVar() 
        
        # Tkinter Labels
        tk.Label( self, text = 'Place your bet').grid(row = 0, column = 1) 
        tk.Label( self, text = 'Spade').grid(row = 1, column = 0)
        tk.Label( self, text = 'Heart').grid(row = 1, column = 1)
        tk.Label( self, text = 'Diamond').grid(row = 1, column = 2)
        tk.Label( self, text = 'Club').grid(row = 3, column = 0)
        tk.Label( self, text = 'Crown').grid(row = 3, column = 1)
        tk.Label( self, text = 'Flag').grid(row = 3, column = 2)
        
        
        # Spinboxes for selecting bet amount
        self.s_1 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_spade, bd = 5, width = 30)               
        self.s_1.grid(row = 2, column = 0)
        self.s_2 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_heart, bd = 5, width = 30)               
        self.s_2.grid(row = 2, column = 1)
        self.s_3 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_diamond, bd = 5, width = 30)               
        self.s_3.grid(row = 2, column = 2)
        self.s_4 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_club, bd = 5, width = 30)               
        self.s_4.grid(row = 4, column = 0)
        self.s_5 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_crown, bd = 5, width = 30)               
        self.s_5.grid(row = 4, column = 1)
        self.s_6 = tk.Spinbox(self, from_ = 0, to = self.game.pot,  textvariable = self.__v_bet_flag, bd = 5, width = 30)               
        self.s_6.grid(row = 4, column = 2)
        
        
        # Display result after rolling and checking
        self.__result = tk.StringVar()
        tk.Label( self, textvariable=self.__result, justify = tk.LEFT ).grid(row = 7, column = 1)
        
        # Button that rolls dices
        self.b = tk.Button(self, text = 'Roll dices', command=self.__handle_game)
        self.b.grid(row = 6, column = 1)
        
      # self.grid_columnconfigure(0, weight=1)
      # self.grid_columnconfigure(2, weight=1)
        
        
    def __handle_game(self): 
        '''
        called when button is pressed, calls roll and then check and shows result
        '''      
        self.game.bet = [self.__v_bet_spade.get(), self.__v_bet_heart.get(), self.__v_bet_diamond.get(),
                         self.__v_bet_club.get(), self.__v_bet_crown.get(), self.__v_bet_flag.get()]
        print(self.game.bet)
        self.game.roll()
        self.__result.set(self.game.check())
        if self.game.pot == 0 :
            self.b.configure(state= tk.DISABLED)
            self.__result.set(self.__result.get() + "\n" + self.game.end_text)
            
   
if __name__ == '__main__' :
    Dices().mainloop()