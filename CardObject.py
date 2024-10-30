from math import *

class Card:
    def __init__(self, attack, defense, rarity):
        self.attack = attack
        self.defense = defense
        self.rarity = rarity

    def setAttack(self, attack):
        self.attack = attack

    def setDefense(self, defense):
        self.defense = defense

    def setRarity(self, rarity):
        self.rarity = rarity


class ComboCard(Card):
    def __init__(self, attack, defense, rarity):
        super().__init__(attack, defense, rarity)
        self.combinations = dict()

    def setCombinations(self, combinations):
        self.combinations = combinations

    def addCombo(self, combo, result):
        self.combinations[combo] = result


class FinalFormCard(Card):
    def __init__(self, attack, defense, rarity):
        super().__init__(attack, defense, rarity)
        self.orbs = None

    def setOrbs(self, orbs):
        self.orbs = orbs


# Onyx Rarity == 5
def determineRarity(rarity):
    if rarity == 'Diamond':
        rarity = 4
    elif rarity == 'Rare':
        rarity = 3
    elif rarity == 'Uncommon':
        rarity = 2
    else:
        rarity = 1
    return rarity


def determine_stats(attack, defense, level, rarity):
    if rarity == 5:
        rarity = 4
    attack = attack + (level - 1)*rarity
    defense = defense + (level - 1)*rarity
    return attack, defense


def update_stats_based_on_ability(attack, defense, ability):
    health_score = 0
    if ability == "Block":
        defense = int(defense * 1.5)
    elif ability == "Protection":
        defense = int(defense * 2)
    elif ability == "Siphon":
        health_score = int(attack * 0.5)
    elif ability == "Absorb":
        health_score = attack
    elif ability == "Amplify":
        attack = int(attack * 1.5)
    elif ability == "Critical Strike":
        attack = int(attack * 2)
    return attack, defense, health_score
