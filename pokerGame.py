import random
from enum import Enum
from unicodedata import name
from unittest import suite


class Suite(Enum):
    """花色（枚举）"""

    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌"""

    def __init__(self, suite, face) -> None:
        self.suite = suite
        self.face = face


    def __repr__(self) -> str:
        suite = '♠♥♣♦'
        face = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suite[self.suite.value]}{face[self.face]}'
    

    def __lt__(self, other):
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


class Poker:
    """扑克"""

    def __init__(self) -> None:
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0


    def shuffle(self):
        '''洗牌'''

        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)


    def deal(self):
        '''发牌'''

        card = self.cards[self.current]
        self.current += 1
        return card


    @property
    def has_next(self):
        """还有没有牌可以发"""

        return self.current < len(self.cards)


class Player:
    """玩家"""

    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    
    def get_one(self, card):
        """摸牌"""

        self.cards.append(card)

    
    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)  
