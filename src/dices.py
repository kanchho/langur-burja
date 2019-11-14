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
        before_new_bet = (self.register(self.__validate_bet_amt),'%S')
        # registering spinbox up/down click callback
        on_bet_change = (self.register(self.__spinbox_maxbet_setter), self.__bet_available(), '%W')
        
        
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
                              validate = 'all', validatecommand = before_new_bet,
                              command = on_bet_change)               
        self.s_spade.grid(row = 2, column = 0)
        
        self.s_heart = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_heart,
                              bd = 5, width = 30,
                              validate = 'all', validatecommand = before_new_bet,
                              command = on_bet_change)               
        self.s_heart.grid(row = 2, column = 1)
        
        self.s_diamond = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_diamond,
                              bd = 5, width = 30,
                              validate = 'all', validatecommand = before_new_bet,
                              command = on_bet_change)             
        self.s_diamond.grid(row = 2, column = 2)
        
        self.s_club = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_club, 
                              bd = 5, width = 30,
                              validate = 'all', validatecommand = before_new_bet,
                              command=on_bet_change)               
        self.s_club.grid(row = 4, column = 0)
        
        self.s_crown = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_crown,
                              bd = 5, width = 30,
                              validate = 'all', validatecommand = before_new_bet,
                              command = on_bet_change)               
        self.s_crown.grid(row = 4, column = 1)
        
        self.s_flag = tk.Spinbox(self, from_ = 0, to = self.__game.pot,  textvariable = self.__v_bet_flag,
                              bd = 5, width = 30,
                              validate = 'all', validatecommand = before_new_bet,
                              command = on_bet_change)               
        self.s_flag.grid(row = 4, column = 2)
        
        
        # Label that displays result after rolling and checking
        self.__result = tk.StringVar()
        tk.Label( self, textvariable=self.__result, justify = tk.LEFT ).grid(row = 7, column = 1)
        
        # Button that rolls dices
        self.b = tk.Button(self, text = 'Roll dices', command=self.__handle_game)
        self.b.grid(row = 6, column = 1)
        
      # self.grid_columnconfigure(0, weight=1)
      # self.grid_columnconfigure(2, weight=1)

        if not self.__game.read('pot.dat') :
            self.__result.set(f'The pot starts from {self.__game.pot}')
        else :
            if tk.messagebox.askyesno('Continue previous game?', f'The pot is {self.__game.pot}'):
                self.__result.set(f'The pot is {self.__game.pot}')
                self.__spinbox_maxbet_setter(self.__game.pot)
            else :
                self.__game.pot = 100
                self.__result.set(f'The pot starts from {self.__game.pot}')
        
     
    def __bet_available(self):
        '''
        returns valid bet amount that can be placed. 
        return value is the difference between total pot amount and existing bet amounts on other symbols
        ''' 
        bets = [self.__v_bet_spade.get(), self.__v_bet_heart.get(), self.__v_bet_diamond.get(),
               self.__v_bet_club.get(), self.__v_bet_crown.get(), self.__v_bet_flag.get()]
        return self.__game.pot - sum(bets)

    
    
    def __validate_bet_amt(self, user_input):
        '''
        Only allow bets in the numeric form within range of values
        specified in spinbox configuration.
        '''
        # valid = user_input == '' or user_input.isdigit() and int(user_input) not in range(self.__bet_available())
        valid = user_input == '' or not user_input.isalnum()  # disable entry field i.e. only set range values.
        if not valid:
           self.bell() 
        return valid
  
     
    def __spinbox_maxbet_setter(self, max_bet = 0, current_widget = None): 
        ''' 
        Sets each spinbox to allow selecting bet upto maximum available bet amount.
        Available bets = Pot - Other bets.
        Called after each write to spinbox.           
        '''
        spinboxes = [self.s_spade, self.s_heart, self.s_diamond,
                     self.s_club, self.s_crown, self.s_flag]
        
        widget_name = None
        if current_widget :
            max_bet = self.__bet_available()
            widget_name = self.nametowidget(current_widget)
        for spinbox in spinboxes : 
            if spinbox is widget_name :
                spinbox.config(to = int(spinbox.get()) + max_bet)       
            else :
                if int(spinbox.get()) > max_bet :
                    if max_bet == self.__game.pot : 
                        spinbox.config(to = max_bet)
                    else :
                        spinbox.config(to = int(spinbox.get()) + max_bet)
                else : 
                    spinbox.config(to = max_bet)
                
    
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
            
        self.__spinbox_maxbet_setter(self.__game.pot)
        self.__game.save('pot.dat')
                
   
if __name__ == '__main__' :
    Dices().mainloop()