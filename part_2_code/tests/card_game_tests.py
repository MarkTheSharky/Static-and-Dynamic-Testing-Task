import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card = Card("spade", 5)
        self.card1 = Card("heart", 9)
        self.card2 = Card("diamond", 2)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame(self.card)

    def test_check_for_ace(self):
        result = self.cardgame.check_for_ace(self.card)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(9, result.value)

    def test_cards_total(self):
        result = self.cardgame.cards_total(self.cards)
        self.assertEqual("You have a total of11", result)