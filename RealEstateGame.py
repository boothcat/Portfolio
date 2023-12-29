# Author: Katie Booth
# GitHub username: boothcat
# Date: 06/03/2022
# Description: Defines class RealEstateGame which represents the Real Estate Game with game players and game spaces.
#              Defines methods for creating spaces, creating players, moving players around the circular board, buying
#              properties, paying rent, and checking if the game has a winner.

class RealEstateGame:
    """
    A class to represent the Real Estate Game with players and game spaces arranged around a circular game board.
    """
    def __init__(self):
        """
        Creates a RealEstateGame object.  Initializes private data members spaces and players to empty dictionaries.
        """
        self._spaces = {}
        self._players = {}

    def create_spaces(self, go_amount, rent_list):
        """
        Given parameter go_amount, the amount of money earned when a player passes or lands on GO space, and parameter
        rent_list, a list of rents for the other twenty-four spaces, create_spaces sets up the dictionary spaces which
        represents 25 games spaces including the GO space.
        """
        # Add GO amount to beginning of rent_list
        rent_list.insert(0, go_amount)

        # Set unique names for all spaces
        name_list = ["GO", "Dothraki Sea", "Meereen", "Quarth", "Volantis", "Braavos", "Iron Islands", "Dreadfort",
                     "Craster's Keep", "The Twins", "Eyrie", "Harrenhal", "Storm's End", "Oldtown", "Dragonstone",
                     "Sandstone", "Sunspear", "Castle Black", "Eastwatch", "Castamere", "Riverrun", "Highgarden",
                     "Casterly Rock", "Winterfell", "King's Landing"]

        # Set up spaces dictionary. Keywords are space positions 0-24 and values are dictionaries of space information.
        for index in range(len(rent_list)):
            if index == 0:
                # GO space cannot be purchased and does not have an owner.  GO bonus is set to go_amount.
                self._spaces[index] = {"Name": name_list[index], "Purchase": False, "Bonus": go_amount, "Owner": False}
            else:
                # Spaces 1-24 have names, purchase prices, and rents from corresponding name_list and rent_list.
                # Owner is initialized to None.
                self._spaces[index] = {"Name": name_list[index], "Purchase": 5 * rent_list[index],
                                       "Rent": rent_list[index], "Owner": None}
        return

    def create_player(self, name, starting_balance):
        """
        Given parameter name, the unique player name, and parameter starting_balance, the initial starting amount of
        money, create_player sets up the dictionary players which represents game players. Returns "Name already taken"
        if name is not unique. Otherwise, returns "Player Successfully Created"
        """
        # Check that player name is unique
        if name in self._players:
            return "Name already taken."

        # Set up player dictionary. Keyword is player's name. Value is dictionary of player game information.
        # Player starts game at GO with starting_balance and an empty list of properties.
        self._players[name] = {"Position": 0, "Balance": starting_balance, "Properties": []}
        return "Player successfully created."

    def get_player_account_balance(self, name):
        """
        Returns the given player's account balance. Returns 'Invalid player' if player's name does not exist.
        """
        if name not in self._players:                            # Check that player name exists.
            return "Invalid player."
        return self._players[name]["Balance"]

    def get_player_current_position(self, name):
        """
        Returns the given player's current position as an integer [0-24] where O represents the GO space.
        Returns 'Invalid player' if player's name does not exist.
        """
        if name not in self._players:                           # Check that player name exists.
            return "Invalid player."
        return self._players[name]["Position"]

    def get_players(self):
        """
        Returns the player dictionary which contains all player information: name, account balance, position, and
        properties owned.
        """
        return self._players

    def get_spaces(self):
        """
        Returns the spaces dictionary which contains all space information: name, purchase amount, rent, and owner.
        """
        return self._spaces

    def buy_space(self, name):
        """
        Given the player's name, buy_space returns True if the player purchases the space and False if the player cannot
        make the purchase. If the player's name does not exist, buy_space returns 'invalid player.' If the space is
        purchased, the space is added to the player's list of properties. The player is set as the owner of the space.
        The price is deducted from the player's account.
        """
        # Check that player name exists.
        if name not in self._players:
            return "Invalid player."

        # Get player's current position.
        space = self.get_player_current_position(name)

        # Check that the space is not owned by another player or GO space.
        if self._spaces[space]["Owner"] is None:

            # Check that the player's balance is greater than the purchase price
            if self._players[name]["Balance"] > self._spaces[space]["Purchase"]:

                # Update the space's owner in the spaces dictionary
                self._spaces[space]["Owner"] = name
                # Deduct the purchase price from the player's account balance.
                self._players[name]["Balance"] -= self._spaces[space]["Purchase"]
                # Add the space to the list of the player's properties
                self._players[name]["Properties"].append(space)
                return True
            return False
        return False

    def pay_rent(self, name, position, owner):
        """
        Helper method for move_player.  Given  the player's name, current position, and owner of the space, pay_rent
        deducts the rent price from the player's balance and pays the amount to the space owner. If the player's balance
        is less than or equal to the rent payment, pay_rent calls declare_bankruptcy method.
        """
        # Check if the player's balance is less than or equal to the rent.
        if self._players[name]["Balance"] <= self._spaces[position]["Rent"]:
            # Call declare_bankruptcy method
            self.declare_bankruptcy(name, owner)
            return

        # Player pays rent to the space owner
        payment = self._spaces[position]["Rent"]
        self._players[name]["Balance"] -= payment
        self._players[owner]["Balance"] += payment
        return

    def declare_bankruptcy(self, name, owner):
        """
        Helper method for pay_rent.  Given the player's name and the owner of the space, declare_bankruptcy
        pays the owner the entirety of the player's balance, sets the player's balance to zero, and
        removes all properties from the player's property list.  Player has lost the game.
        """
        payment = self._players[name]["Balance"]
        self._players[owner]["Balance"] += payment              # Pay owner player's balance.
        self._players[name]["Balance"] = 0                      # Set player balance to zero.

        property_list = self._players[name]["Properties"]
        # Remove all properties from player's property list
        for item in list(property_list):
            property_list.remove(item)
            self._spaces[item]["Owner"] = None                  # Set space's owner back to None
        return

    def move_player(self, name, number):
        """
        Given the player's name and the number of spaces to move [1-6], move_player moves active players the specified
        amount around the game board. The player's current position is updated and if the space is owned by another
        player, the helper method pay_rent is called. If number is not, move_player returns 'Invalid move.'  If player
        name does not exist, move_player returns 'Invalid player.'
        """
        # Check that number is 1-6
        if number < 1 or number > 6:
            return "Invalid move."

        # Check that player name exists.
        if name not in self._players:
            return "Invalid player."

        # If the player has zero balance, the player has lost the game and cannot move.
        if self._players[name]["Balance"] == 0:
            return

        past_position = self._players[name]["Position"]         # Player's previous position on the board before moving
        # Check if the player will land on or pass "GO."
        if past_position + number > 24:
            # Player earns GO bonus
            self._players[name]["Balance"] += self._spaces[0]["Bonus"]
            # Reset position numbering at 0 for GO space and set player's current position
            self._players[name]["Position"] = (past_position - 24) + (number - 1)
        else:
            # Set player's current position
            self._players[name]["Position"] += number

        current_position = self._players[name]["Position"]      # Player's current position on the board after moving
        owner = self._spaces[current_position]["Owner"]

        # If space is owned by another player, player pays rent
        if owner is not None and owner is not False and owner != name:
            self.pay_rent(name, current_position, owner)
        return

    def check_game_over(self):
        """
        Returns the winning player's name if all but one player have zero balances.  Otherwise, returns an empty string.
        """
        zero_counter = 0                                        # Initialize count of players with zero balances to 0.
        for player in self._players:
            # Check if player has zero balance
            if self._players[player]["Balance"] == 0:
                zero_counter += 1                               # Increment zero counter
            else:
                name = player                                   # Keep track of name of nonzero balance player
        # If all but one player have zero balance, game is over.
        if zero_counter == len(self._players) - 1:
            return name
        else:
            return ""
