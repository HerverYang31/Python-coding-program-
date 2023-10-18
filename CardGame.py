from array import*
class CardGame:
    def __init__(self,c_values,c_suits,c_faceup):
        self.value = c_values
        self.suit = c_suits
        self.faceup = c_faceup

    def get_faceup(self):
        return f"Face up: {self.faceup}"
    
    def flip(self):
        return f"Face up: {not self.faceup}"
    
    def __repr__(self):
        return f"Card value: {self.value}, Card suit: {self.suit}, FaceUp: {self.faceup}"



class Deck:
    deckArr = []
    def __init__(self,*card):
        if len(card) == 1:
            self.deckArr.append(card[0])   
        else:
            for i in range(len(card)):
                self.deckArr.append(card[i])
                 
    def printDeck(self):
        for i in range(len(self.deckArr)):
            print(self.deckArr[i])

    def deal(self):
        self.deckArr.pop(-1)
    
    def add(self,c):
        self.deckArr.append(c)




p1 = CardGame(8,"Spade",False)
p2 = CardGame(2,"Heart",True)
p3 = CardGame(10,"Diamond",False)
p4 = CardGame("k","Club",True)
print(p1)


d2 = Deck(p1,p2,p3,p4)
print()
d2.printDeck()
print()
print("Remove the last card")
d2.deal()
d2.printDeck()

print()
print("Add a new card")
d2.add(p1)
d2.printDeck()

