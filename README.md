# Langur Burja
## Description
Langur Burja is a Nepalese dice game traditionally played for gambling
between Dashain and Tihar (two major festivals that usually fall at the 
beginning and towards the end of October respectively). The game uses six
identical dice, each with six different symbols on it (Heart, Spade, Diamond,
Club, Crown and Flag printed on six faces of each dice). The game is usually
played on the street where a mat/carpet/canvas with the symbols printed is
placed and players place their bet on the symbols. The host/banker is usually
called ”The House” and there can be multiple betters on each roll.
Furthermore, each player can place their bet on multiple symbols.

After the bet/s are placed, the House rolls the dices and results are
calculated as follows : 
 * If none or one of the dices show the symbol on which bet is placed, then
 the bet is lost and the house takes the money.
 *	If more than one dices show the symbol on which bet is placed, the house
 pays the the player the number of dices times the bet amount. Also, the
 player keeps the bet.
 

## Implementation 
Langur Burja  is a dice game where user can input upto six different bets and
the total bet/s  amount is between 1 - pot. Pot is 100 in the beginning, and
after the roll user's bet/s  is first checked, win or lose is calculated, and
added to the pot. The result, pot, and faces are displayed and if the pot is
bigger than 0 the game continues and user can enter new bet. 
The game ends when the pot is gone. User cannot be in debt. (pot is always
bigger or equal to 0), if user ends game before the pot is gone the pot is
saved to next game. When the program starts, if there is an existing pot,
user is asked if he wants to continue previous game. If there is no previous
game or it ended in 0 pot then the game is started from the beginning. User
can see the net win or loss incurred since the first playing session.
