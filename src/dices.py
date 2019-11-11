# -*- coding: utf-8 -*-

import tkinter as tk
from game import Game

class Dices(tk.Tk) :
    '''
     Interface for game, UI layer.
     Inherits class tkinter.Tk() and provides GUI 
    '''
    def __init__(self, *args, **kwargs ) :
        '''
        defines and initializes attributes 
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer
        self.__game = Game(6)
        
        
        self.title("Langur Burja")
        self.geometry('900x450')
        

        self.__v_bet_spade = tk.IntVar()
        self.__v_bet_heart = tk.IntVar() 
        self.__v_bet_diamond = tk.IntVar() 
        self.__v_bet_club = tk.IntVar() 
        self.__v_bet_crown = tk.IntVar() 
        self.__v_bet_flag = tk.IntVar() 

        
        # registering validation command
        vldt_bet_cmd = (self.register(self.__validate_bet_amt),'%s', '%S', '%W')
        
        # Tkinter Labels
        tk.Label( self, text = 'Place your bet').grid(row = 0, column = 1) 
        tk.Label( self, text = 'Spade').grid(row = 1, column = 0)
        tk.Label( self, text = 'Heart').grid(row = 1, column = 1)
        tk.Label( self, text = 'Diamond').grid(row = 1, column = 2)
        tk.Label( self, text = 'Club').grid(row = 3, column = 0)
        tk.Label( self, text = 'Crown').grid(row = 3, column = 1)
        tk.Label( self, text = 'Flag').grid(row = 3, column = 2)
        
        
        # Spinboxes for selecting bet amount
        self.s_spade = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_spade, 
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_spade.grid(row = 2, column = 0)
        
        self.s_heart = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_heart,
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_heart.grid(row = 2, column = 1)
        
        self.s_diamond = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_diamond,
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_diamond.grid(row = 2, column = 2)
        
        self.s_club = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_club, 
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_club.grid(row = 4, column = 0)
        
        self.s_crown = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_crown,
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_crown.grid(row = 4, column = 1)
        
        self.s_flag = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_flag,
                              bd = 5, width = 30,
                              validate='all', validatecommand=vldt_bet_cmd)               
        self.s_flag.grid(row = 4, column = 2)
        
        
        # Label that displays result after rolling and checking
        self.__result = tk.StringVar()
        tk.Label( self, textvariable=self.__result, justify = tk.LEFT ).grid(row = 7, column = 1)
        
        # Button that rolls dices
        self.b = tk.Button(self, text = 'Roll dices', command=self.__handle_game)
        self.b.grid(row = 6, column = 1)
        
      # self.grid_columnconfigure(0, weight=1)
      # self.grid_columnconfigure(2, weight=1)
        

    def __bet_available(self):
        '''
        returns valid bet amount that can be placed. 
        return value is the difference between total pot amount and existing bet amounts on other symbols
        ''' 
        bet = [self.__v_bet_spade.get(), self.__v_bet_heart.get(), self.__v_bet_diamond.get(),
               self.__v_bet_club.get(), self.__v_bet_crown.get(), self.__v_bet_flag.get()]
        return self.game.pot - sum(bet)

    
    
    def __validate_bet_amt(self, prev_value, user_input, widget_name):
        '''
        let user select bet such that total bet amount placed on different symbols is less than or equal to pot
        '''
        valid = user_input == '' or not user_input.isalnum()      # disable entry field, only spin values allowed
        if not valid:
           self.bell() 
        
        if valid :
            max_value = self.__bet_available()          
            if max_value <= 0 :
                widget = self.nametowidget(widget_name)
                widget.configure(to=prev_value)
                valid = False
       
        return valid
    
    def __handle_game(self): 
        '''
        called when button is pressed, calls roll and then check and shows result
        '''      
        self.__game.bet = [self.__v_bet_spade.get(), self.__v_bet_heart.get(), self.__v_bet_diamond.get(),
                         self.__v_bet_club.get(), self.__v_bet_crown.get(), self.__v_bet_flag.get()]
        self.__game.roll()
        self.__result.set(self.__game.check())
        if self.__game.pot == 0 :
            self.b.configure(state= tk.DISABLED)
            self.__result.set(self.__result.get() + "\n" + "Game Over")
            
   
if __name__ == '__main__' :
    Dices().mainloop()