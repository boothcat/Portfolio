import unittest
from RealEstateGame import RealEstateGame


class TestGame(unittest.TestCase):
    """Contains units tests for RealEstateGame class methods."""

    def test1(self):
        """Tests that create_spaces creates "GO" space and 24 more game spaces."""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        self.assertEqual(len(game.get_spaces()), 25)

    def test2(self):
        """Tests that go space is set up correctly"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        self.assertEqual(game.get_spaces()[0]["Name"], "GO")

    def test3(self):
        """Tests that space 24 is set up correctly"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        self.assertEqual(game.get_spaces()[24], {"Name": "King's Landing", "Purchase": 1750, "Rent": 350,
                                                 "Owner": None})

    def test4(self):
        """Tests that a player can be added"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        self.assertEqual(game.get_players()["Player 1"], {"Position": 0, "Balance": 1000, "Properties": []})

    def test5(self):
        """Test get_player_balance for initial balance"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        self.assertEqual(game.get_player_account_balance("Player 1"), 1000)

    def test6(self):
        """Test get_player_position for initial position"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        self.assertEqual(game.get_player_current_position("Player 1"), 0)

    def test7(self):
        """Player cannot buy "GO" space.  buy_space returns False"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        self.assertEqual(game.buy_space("Player 1"), False)

    def test8(self):
        """Player can move forward 6 spaces """
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        self.assertEqual(game.get_players()["Player 1"]["Position"], 6)

    def test9(self):
        """Player can move completely around the board, land on "GO" space and position is 0"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 1)
        self.assertEqual(game.get_players()["Player 1"]["Position"], 0)

    def test10(self):
        """Player can move completely around the board, land on "GO" space and receive GO bonus"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 1)
        self.assertEqual(game.get_player_account_balance("Player 1"), 1050)

    def test11(self):
        """Player currently at position 23, rolls a 4.  Player's position is correctly moved to 2"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 5)
        game.move_player("Player 1", 4)
        self.assertEqual(game.get_player_current_position("Player 1"), 2)

    def test12(self):
        """Player currently at position 23, rolls a 4.  Player's receive "GO" bonus"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 5)
        game.move_player("Player 1", 4)
        self.assertEqual(game.get_player_account_balance("Player 1"), 1050)

    def test13(self):
        """Player currently at position 22, rolls a 4.  Player's position is correctly moved to 2"""
        game = RealEstateGame()
        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 6)
        game.move_player("Player 1", 4)
        game.move_player("Player 1", 4)
        self.assertEqual(game.get_player_current_position("Player 1"), 1)

    def test14(self):
        """Player buys a space.  Buy space returns true."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        self.assertEqual(game.buy_space("Player 1"), True)

    def test15(self):
        """Player buys a space.  Purchase price is deducted from player's account balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.get_player_account_balance("Player 1"), 625)

    def test16(self):
        """Player buys a space.  Space's owner is updated to player's name."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.get_spaces()[6]["Owner"], "Player 1")

    def test17(self):
        """Player buys a space.  Property is added to player's list of properties."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.get_players()["Player 1"]["Properties"], [6])

    def test18(self):
        """Player buys space 6, moves three more spaces, and buys space 9.  Properties are added to player's list of
        properties."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 1", 3)
        game.buy_space("Player 1")
        self.assertEqual(game.get_players()["Player 1"]["Properties"], [6, 9])

    def test19(self):
        """Player cannot buy a property owned by another player.  buy_space returns false"""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.buy_space("Player 2"), False)

    def test20(self):
        """Player cannot buy a property if their balance is equal to the purchase price. Buy_space returns false."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 625)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.buy_space("Player 1"), False)

    def test21(self):
        """Player cannot buy a property if their balance is less than the purchase price. Buy_space returns false."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 620)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.buy_space("Player 1"), False)

    def test22(self):
        """Player cannot buy a property they already own.  buy_space returns false"""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        self.assertEqual(game.buy_space("Player 1"), False)

    def test23(self):
        """Player moves to a space owned by another player.  Player pays rent."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.get_player_account_balance("Player 2"), 925)

    def test24(self):
        """Player moves to a space owned by another player.  Owner receives rent."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.get_player_account_balance("Player 1"), 700)

    def test25(self):
        """Player moves to a space they already own.  Player does not pay rent."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 1000)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 1", 6)
        self.assertEqual(game.get_player_account_balance("Player 1"), 625)

    def test26(self):
        """Player has exactly the amount of rent.  Player has zero balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 75)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.get_player_account_balance("Player 2"), 0)

    def test27(self):
        """Player has exactly the amount of rent.  Owner gets player's remaining balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 75)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.get_player_account_balance("Player 1"), 700)

    def test28(self):
        """Player has does not have the rent money.  Owner gets player's remaining balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 70)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 6)
        self.assertEqual(game.get_player_account_balance("Player 1"), 695)

    def test29(self):
        """Player cannot pay rent - properties are removed."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 300)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 3)
        self.assertEqual(game.get_players()["Player 2"]["Properties"], [])

    def test30(self):
        """Player 2 goes around the board buys property 3 and property 1."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300,
                 350, 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        self.assertEqual(game.get_players()["Player 2"]["Properties"], [3, 1])

    def test31(self):
        """Player's Balance is 0.  They will not be able to move position."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 300)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 3)
        game.move_player("Player 2", 5)
        self.assertEqual(game.get_player_current_position("Player 2"), 6)

    def test32(self):
        """Player 2 goes around the board buys property 3 and property 1 and then loses the game with zero balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        game.move_player("Player 2", 5)
        self.assertEqual(game.get_player_account_balance("Player 2"), 0)

    def test33(self):
        """Player 2 goes around the board buys property 3 and property 1 and properties are removed."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        game.move_player("Player 2", 5)
        self.assertEqual(game.get_players()["Player 2"]["Properties"], [])

    def test34(self):
        """Player 2 goes around the board buys property 3 and property 1, Owner of Property 3 is returned to None."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        game.move_player("Player 2", 5)
        self.assertEqual(game.get_spaces()[1]["Owner"], None)

    def test35(self):
        """check_game_over returns winner's name."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
                 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        game.move_player("Player 2", 5)
        self.assertEqual(game.check_game_over(), "Player 1")

    def test36(self):
        """check_game_over returns an empty string if more than one player has nonzero balance."""
        game = RealEstateGame()

        rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300,
                 350, 350, 350]
        game.create_spaces(50, rents)
        game.create_player("Player 1", 1000)
        game.create_player("Player 2", 525)
        game.move_player("Player 1", 6)
        game.buy_space("Player 1")
        game.move_player("Player 2", 3)
        game.buy_space("Player 2")
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 6)
        game.move_player("Player 2", 5)
        game.buy_space("Player 2")
        self.assertEqual(game.check_game_over(), "")
