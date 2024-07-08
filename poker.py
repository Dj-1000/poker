# 1. Decide number of players
# 2. initialise players properties like money, is_folded=false, name, hand=None
# 3. Define cads and round
# 3. distribute the card to players using random.
from enum import IntEnum
from random import randint

OPTIONS = [
    ('FOLD',0),
    ('CHECK',1),
    ('CALL',2),
    ('RAISE',3)
]

class Player:
    
    def __init__(self,name=None,money=None):
        if name is not None:
            self.name = name
        if money is not None:
            self.money = money
        
        self.is_folded = False
        self.card_count = 0

    
    def __repr__(self):
        return f"Player({self.name}, {self.money})"



class Card:
    card_count = 0
    existing_cards = set()
    # Class variables to map indices to names
    RANK_NAMES = {
       1: "ACE" , 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
        6: "SIX", 7: "SEVEN", 7: "EIGHT", 9: "NINE",
        10: "TEN", 11: "JACK", 12: "QUEEN", 13: "KING"
    }
    SUIT_NAMES = {
        0: "SPADE", 1: "CLUB", 2: "DIAMOND", 3: "HEART"
    }

    def __init__(self, rank_index, suit_index):
        self.rank_index = rank_index
        self.suit_index = suit_index
        Card.card_count+=1
        Card.existing_cards.add(self)

    def __repr__(self):
        rank_name = self.RANK_NAMES.get(self.rank_index, "Unknown Rank")
        suit_name = self.SUIT_NAMES.get(self.suit_index, "Unknown Suit")
        return f"Card(rank={rank_name}, suit={suit_name})"
    
    
def generate_unique_card():
    if Card.card_count<=52:
        while True:
            rank = randint(1,13)
            print(rank)  # Random rank between 0 and 13
            suit = randint(0,3)
            print(suit)  # Random suit between 0 and 3
            new_card = Card(rank, suit)
            if new_card in Card.existing_cards:
                return new_card
    else:
        print("Sorry card limit reached.")
    

class Table:
    def __init__(self, players=None, cards=None):
        self.players = players if players is not None else []
        self.cards = cards if cards is not None else []
        self.prize_money = 0

    def add_player(self, player):
        self.players.append(player)

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return f"Table(players={self.players}, cards={self.cards})"


no_of_players = int(input("Enter the number of players : "))
table = Table()
for i in range(no_of_players):
    name = input(f"Enter player {i+1}'s name : ")
    money = int(input(f"Enter player {i+1}'s money : "))
    player = Player(name, money)
    table.players.append(player)
    table.prize_money += player.money
    






