class Game:
    def __init__(self, title, category, price):
        self.title = title
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.title} ({self.category}) - ${self.price:.2f}"
    
class ActionGame(Game):
    def __init__(self, title, price):
        super().__init__(title, "Ação", price)


class HorrorGame(Game):
    def __init__(self, title, price):
        super().__init__(title, "Terror", price)


class SportsGame(Game):
    def __init__(self, title, price):
        super().__init__(title, "Esporte", price)


class RPGGame(Game):
    def __init__(self, title, price):
        super().__init__(title, "RPG", price)