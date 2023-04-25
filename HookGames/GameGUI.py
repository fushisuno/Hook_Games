from tkinter import*
from tkinter import ttk
import tkinter.messagebox as messagebox
from GameStore import GameStore
from Games import *

class GameStoreGUI:
    def __init__(self, store: GameStore):
        self.store = store
        self.store.get_games()
        self.store.games
        self.root = Tk()
        self.root.title("Game Store")

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.games_menu = Menu(self.menu, tearoff=0)
        self.games_menu.add_command(label="Todos os jogos", command=self.show_all_games)
        self.games_menu.add_command(label="Ação", command=lambda: self.show_games_by_category("Ação"))
        self.games_menu.add_command(label="Terror", command=lambda: self.show_games_by_category("Terror"))
        self.games_menu.add_command(label="Esporte", command=lambda: self.show_games_by_category("Esporte"))
        self.games_menu.add_command(label="RPG", command=lambda: self.show_games_by_category("RPG"))
        self.menu.add_cascade(label="Jogos", menu=self.games_menu)

        self.cart_menu = Menu(self.menu, tearoff=0)
        self.cart_menu.add_command(label="Comprar jogos", command=self.show_cart)
        self.menu.add_cascade(label="Carrinho", menu=self.cart_menu)

        self.menu.add_command(label="Sair", command=self.root.quit)

        self.listbox = Listbox(self.root, width=50)
        self.listbox.pack(padx=10, pady=10)

        self.cart = []

        self.buy_button = Button(self.root, text="Comprar", command=self.buy_game)
        self.buy_button.pack(side="left", pady=10, padx=10)

        self.add_game_button = Button(self.root, text="Adicionar jogo", command=self.add_game)
        self.add_game_button.pack(side="right", pady=10, padx=10)

        self.root.mainloop()

    def show_all_games(self):
        self.listbox.delete(0, END)
        for game in self.store.games:
            self.listbox.insert(END, f"{game.title} - {game.category} - R$ {game.price:.2f}")

    def show_games_by_category(self, category):
        self.listbox.delete(0, END)
        for game in self.store.games:
            if game.category == category:
                self.listbox.insert(END, f"{game.title} - {game.category} - R$ {game.price:.2f}")

    def buy_game(self):
        selection = self.listbox.curselection()
        if selection:
            game = self.listbox.get(selection[0])
            self.cart.append(game)
            messagebox.showinfo("Compra", f"Jogo {game} adicionado ao carrinho.")
        else:
            messagebox.showwarning("Seleção inválida", "Nenhum jogo selecionado.")

    def show_cart(self):
        messagebox.showinfo("Carrinho", "\n".join(self.cart))

    def add_game(self):
        add_game_window = Toplevel(self.root)
        add_game_window.title("Adicionar jogo")

        game_name_label = Label(add_game_window, text="Nome do jogo:")
        game_name_label.grid(row=0, column=0, padx=5, pady=5)
        game_name_entry = Entry(add_game_window, width=30)
        game_name_entry.grid(row=0, column=1, padx=5, pady=5)

        category_label = Label(add_game_window, text="Categoria:")
        category_label.grid(row=1, column=0, padx=5, pady=5)
        category_combobox = ttk.Combobox(add_game_window, values=["Ação", "Terror", "RPG", "Esporte"])
        category_combobox.grid(row=1, column=1, padx=5, pady=5)

        price_label = Label(add_game_window, text="Preço:")
        price_label.grid(row=2, column=0, padx=5, pady=5)
        price_entry = Entry(add_game_window, width=10)
        price_entry.grid(row=2, column=1, padx=5, pady=5)

        def confirm():
            game_name = game_name_entry.get()
            category = category_combobox.get()
            price = float(price_entry.get())
            if (game_name == None or len(game_name)<5) or (category == None or len(category) < 3) or (price < 0):
                add_game_window.destroy()
                messagebox.showerror("Error", "Valor Inválido")
            else:
                if category == "Ação":
                    self.store.add_game(ActionGame(game_name, price))
                elif category == "Terror":
                    self.store.add_game(HorrorGame(game_name, price))
                elif category == "RPG":
                    self.store.add_game(RPGGame(game_name, price))
                elif category == "Esporte":
                    self.store.add_game(SportsGame(game_name, price)) 

                self.store = GameStore()
                self.store.get_games()
                add_game_window.destroy()

        confirm_button = Button(add_game_window, text="Confirmar", command=confirm)
        confirm_button.grid(row=3, column=1, padx=5, pady=5)


