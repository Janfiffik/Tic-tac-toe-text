import field as f
import player as p

game_is_on = True
while game_is_on:

    game_field = f.playground()          # Creates game field.

    f.show_playground(game_field)        # Show game field

    players = p.start_first()            # Choose first player.

    p.gameplay(players, game_field)      # Game

    game_is_on = p.game_on()             # Ask for game to continue or quit.
