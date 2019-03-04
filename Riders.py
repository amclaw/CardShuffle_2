from random import shuffle
from abc import ABCMeta

class team:
    #team stff
#new stuff?
class rider:
    """
    Riders in Flamme Rouge have the following attributes:
    1. A deck of cards
    2. A hand of cards, drawn from the deck
    3. A discard pile
    4. A recycle deck
    There is technically a 'card drawn' however ultimately this is the top card of the discard.
    """
    __metaclass__ = ABCMeta

    def __init__(self, type, deck, hand, recycle, discard):
        self.type = type
        self.deck = deck
        self.hand = hand
        self.recycle = recycle
        self.discard = discard

    def move(self):
        if len(self.deck)>4:
            handsize = 4
        elif len(self.recycle)>0:
            shuffle(self.recycle)
            self.deck.extend(self.recycle)
            del self.recycle[:]
            handsize = min(4,len(self.deck))
        elif len(self.deck)>0:
            print ("Didn't expect this scenario. Go check the Move method in Rider Class.")
            handsize = len(self.deck)
        else:
            self.deck.append("E")
            handsize = len(self.deck)

        self.hand = self.deck[:handsize]
        self.deck = self.deck[handsize:]

        played = str(input("Select a card from your {} hand to play: {} ".format(self.type, self.hand)))
        while played not in self.hand:
            played = str(input("Select a card from your {} hand to play: {} ".format(self.type, self.hand)))
        self.hand.remove(played)
        self.discard.append(played)
        self.recycle.extend(self.hand)

    def exhausted(self):
        self.recycle.append('E')

rider_list = {1:"Rouler", 2:"Sprinteur"}

deck_list = {"Rouler":['3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7'],\
             "Sprinteur":['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '9', '9', '9']}

#Start game
print ("Game is starting!")

#create riders
select_first_rider = int(input("Select a Rider: {} ".format(rider_list)))
select_second_rider = int(input("Select a Rider: {} ".format(rider_list)))

rider_1 = rider(rider_list[select_first_rider], deck_list[rider_list[select_first_rider]],\
                [], [], [])
rider_2 = rider(rider_list[select_second_rider], deck_list[rider_list[select_second_rider]],\
                [], [], [])

team = {1:rider_1, 2:rider_2}

for riders in team:
    print("Rider", riders, "is a ", team[riders].type, "and has the following deck:", team[riders].deck)
    shuffle(team[riders].deck)
    print(team[riders].deck)

print("Rider 1 is a", rider_1.type, "and has the following deck:", rider_1.deck)
print("Rider 2 is a", rider_2.type, "and has the following deck:", rider_2.deck)

playing = True

while playing == True:

    for riders in team:
        team[riders].move()

    for riders in team:
        print(team[riders].type, "moves", team[riders].discard[-1], "spaces.")
        print(team[riders].type, "recycled", team[riders].hand)
        print(team[riders].type, "full recycle list", team[riders].recycle)
        print(team[riders].type, "discard list", team[riders].discard)

    keep_playing = "string"
    while keep_playing not in "yn":
        keep_playing = str(input("Keep playing (y/n)?: ")).lower()
    if keep_playing != "y":
        playing = False
        for riders in team:
            print(team[riders].type, "has", team[riders].deck.count('E') + team[riders].recycle.count('E'),\
                  "exhaustion cards")
        print("Game Over")
        break
    for riders in team:
        is_exhausted = "string"
        while is_exhausted not in 'yn':
            is_exhausted = str(input("Is your {} leading a pack? (y/n): ".format(team[riders].type))).lower()
        if is_exhausted == "y":
            team[riders].exhausted()