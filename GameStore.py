import sqlite3
from Games import Game

class GameStore:
    def __init__(self):
        self.conn = sqlite3.connect("games.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS games
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            price REAL)"""
        )
        self.conn.commit()
        self.games = []
        self.categories = []

    def add_game(self, game):
        self.cursor.execute(
            "INSERT INTO games (title, category, price) VALUES (?, ?, ?)",
            (game.title, game.category, game.price)
        )
        self.conn.commit()

    def get_games(self, category=None):
        if category:
            self.cursor.execute(
                "SELECT * FROM games WHERE category=?", (category)
            )
        else:
            self.cursor.execute("SELECT * FROM games")
        rows = self.cursor.fetchall()

        for row in rows:
            game = Game(row[1], row[2], row[3])
            self.games.append(game)

            if row[2] not in self.categories:
                self.categories.append(row[2])

    def __del__(self):
        self.cursor.close()
        self.conn.close()