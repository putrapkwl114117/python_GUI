import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

game_list = [
    { 
        "ps4": [
            {"name": "God of War", "price": 49.99, "stock": 10},
            {"name": "The Last of Us Remastered", "price": 39.99, "stock": 15},
            {"name": "Bloodborne", "price": 44.99, "stock": 20}
        ]
    },
    {
        "ps5": [
            {"name": "Demon's Souls", "price": 69.99, "stock": 12},
            {"name": "Spider-Man: Miles Morales", "price": 59.99, "stock": 8},
            {"name": "Astro's Playroom", "price": 19.99, "stock": 25}
        ]
    },
    {
        "nintendo_switch": [
            {"name": "The Legend of Zelda: Breath of the Wild", "price": 59.99, "stock": 18},
            {"name": "Animal Crossing: New Horizons", "price": 49.99, "stock": 20},
            {"name": "Mario Kart 8 Deluxe", "price": 59.99, "stock": 15}
        ]
    },
    {
        "pc": [
            {"name": "The Witcher 3: Wild Hunt", "price": 29.99, "stock": 30},
            {"name": "Cyberpunk 2077", "price": 59.99, "stock": 25},
            {"name": "Half-Life: Alyx", "price": 39.99, "stock": 20}
        ]
    },
    {
        "xbox_one": [
            {"name": "Halo: The Master Chief Collection", "price": 39.99, "stock": 10},
            {"name": "Forza Horizon 4", "price": 49.99, "stock": 15},
            {"name": "Gears 5", "price": 59.99, "stock": 20}
        ]
    },
    {
        "xbox_x": [
            {"name": "Assassin's Creed Valhalla", "price": 59.99, "stock": 12},
            {"name": "Watch Dogs: Legion", "price": 49.99, "stock": 18},
            {"name": "Call of Duty: Black Ops Cold War", "price": 69.99, "stock": 15}
        ]
    },
    {
        "xbox_s": [
            {"name": "Yakuza: Like a Dragon", "price": 49.99, "stock": 20},
            {"name": "Dirt 5", "price": 39.99, "stock": 25},
            {"name": "Minecraft Dungeons", "price": 29.99, "stock": 30}
        ]
    }
]


# Fungsi-fungsi CRUD
def display_console_list():
    consoles = set()
    for console in game_list:
        consoles.update(console.keys())

    console_list.delete(0, tk.END)
    for console in consoles:
        console_list.insert(tk.END, console)

def display_game_by_console(event=None):
    selected_indices = console_list.curselection()
    
    if not selected_indices:
        # game_frame dan menu_frame tidak akan disembunyikan jika tidak ada konsol yang dipilih
        return
    
    selected_console = console_list.get(selected_indices[0])
    games = []

    for console in game_list:
        for key, value in console.items():
            if key.lower() == selected_console.lower():
                games.extend(value)

    game_tree.delete(*game_tree.get_children())
    for game in games:
        game_tree.insert("", tk.END, values=(game["name"], game["price"], game["stock"]))

    if games:
        game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
    else:
        game_frame.grid_forget()
        menu_frame.grid_forget()

    

def on_game_select(event=None):
    selected_item = game_tree.selection()
    
    if selected_item:
        buy_frame.grid(row=0, column=1, padx=2, pady=2, sticky=tk.SW)
        add_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        edit_frame.grid(row=2, column=0, padx=2, pady=5, sticky=tk.W+tk.E)
        remove_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
        update_stock_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
 
    else:
        buy_frame.grid_forget()
        add_frame.grid_forget()
        edit_frame.grid_forget()
        remove_frame.grid_forget()
        pay_button.grid_forget()
        update_stock_frame.grid_forget()
        bought_game_frame.grid_forget()
        
def add_game():
    console_name = console_entry.get().lower()
    game_name = game_name_entry.get().strip()
    game_price = game_price_entry.get().strip()

    if not console_name or not game_name or not game_price:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    try:
        game_price = float(game_price)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid price.")
        return

    for console in game_list:
        if console_name in console.keys():
            for game in console[console_name]:
                if game_name.lower() == game["name"].lower():
                    messagebox.showwarning("Warning", "Game already exists.")
                    return
            console[console_name].append({"name": game_name.title(), "price": game_price, "stock": 0})
            
            # Tampilkan kembali frame game
            game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Tampilkan kembali menu frame
            menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Hapus pemanggilan display_game_by_console() di sini
            
            messagebox.showinfo("Success", "Game added successfully!")
            return
    messagebox.showwarning("Error", "Console not found. Game not added.")


def edit_game():
    selected_item = game_tree.selection()[0]
    game_name = game_tree.item(selected_item)["values"][0]
    
    for console in game_list:
        for key in console:
            for game in console[key]:
                if game_name == game["name"]:
                    try:
                        new_name = new_game_name_entry.get().title()
                        new_price = float(new_game_price_entry.get())
                        
                        game["name"] = new_name
                        game["price"] = new_price
                        
                        display_game_by_console()
                        messagebox.showinfo("Success", "Game updated successfully!")
                    except ValueError:
                        messagebox.showwarning("Warning", "Please enter a valid price.")
                    return

def remove_game():
    selected_item = game_tree.selection()[0]
    game_name = game_tree.item(selected_item)["values"][0]

    for console in game_list:
        for key in console:
            for game in console[key]:
                if game_name == game["name"]:
                    console[key].remove(game)
                    display_game_by_console()
                    messagebox.showinfo("Success", "Game removed successfully!")
                    return

def update_stock():
    selected_item = game_tree.selection()[0]
    game_name = game_tree.item(selected_item)["values"][0]
    
    for console in game_list:
        for key in console:
            for game in console[key]:
                if game_name == game["name"]:
                    try:
                        new_stock = int(new_stock_entry.get())
                        game["stock"] = new_stock
                        display_game_by_console()
                        messagebox.showinfo("Success", "Stock updated successfully!")
                    except ValueError:
                        messagebox.showwarning("Warning", "Please enter a valid stock number.")
                    return

bought_games = {}

# Fungsi untuk menampilkan daftar game yang dibeli
def display_bought_games():
    # Kosongkan Treeview
    bought_game_tree.delete(*bought_game_tree.get_children())
    
    total_payment = 0
    for game_name, info in bought_games.items():
        bought_game_tree.insert("", tk.END, values=(game_name, info['quantity'], info['price'], info['total_price']))
        total_payment += info['total_price']
    
    # Tampilkan tombol pembayaran
    pay_button.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W+tk.E)

def buy_game():
    selected_item = game_tree.selection()[0]
    game_name = game_tree.item(selected_item)["values"][0]
    
    for console in game_list:
        for key in console:
            for game in console[key]:
                if game_name == game["name"]:
                    try:
                        quantity = int(buy_quantity_entry.get())
                        if quantity > game["stock"]:
                            messagebox.showwarning("Peringatan", "Stok tidak mencukupi.")
                            return
                        
                        total_price = game["price"] * quantity
                        
                        # Mengurangi stok game yang dibeli dari stok yang tersedia
                        game["stock"] -= quantity
                        
                        if game_name in bought_games:
                            bought_games[game_name]["quantity"] += quantity
                            bought_games[game_name]["total_price"] += total_price
                        else:
                            bought_games[game_name] = {
                                "quantity": quantity,
                                "total_price": total_price,
                                "price": game["price"]
                            }
                        
                        bought_game_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
                        display_bought_games()
                        
                        # Kosongkan entry quantity
                        buy_quantity_entry.delete(0, tk.END)
                        
                    except ValueError:
                        messagebox.showwarning("Peringatan", "Silakan masukkan jumlah yang valid.")
                    return


# Fungsi untuk tombol bayar
def pay():
    total_payment = sum(info['total_price'] for info in bought_games.values())
    
    # Buat pop up untuk memasukkan jumlah pembayaran
    payment_input = simpledialog.askfloat("Pembayaran", f"Total Pembayaran: ${total_payment:.2f}\nMasukkan Jumlah Pembayaran:")
    
    if payment_input is not None:
        if payment_input < total_payment:
            messagebox.showwarning("Peringatan", "Pembayaran tidak mencukupi.")
        else:
            change = payment_input - total_payment
            messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran Berhasil!\nUang Kembalian: ${change:.2f}")
    
    # Kosongkan daftar pembelian
    bought_games.clear()
    display_bought_games()

def show_frame(frame):
    frame.tkraise()
    
# Membuat GUI
root = tk.Tk()
root.title("Game Store")

# Konfigurasi bobot grid
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

# Frame untuk list konsol
console_frame = ttk.LabelFrame(root, text="Consoles")
console_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

console_scroll = ttk.Scrollbar(console_frame, orient=tk.VERTICAL)
console_list = tk.Listbox(console_frame, yscrollcommand=console_scroll.set)
console_scroll.config(command=console_list.yview)
console_scroll.pack(side=tk.RIGHT, fill=tk.Y)
console_list.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
display_console_list()

# Frame untuk list game
game_frame = ttk.LabelFrame(root, text="Games")
game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
game_frame.grid_forget()
columns = ("Name", "Price", "Stock")
game_scroll = ttk.Scrollbar(game_frame, orient=tk.VERTICAL)
game_tree = ttk.Treeview(game_frame, columns=columns, show="headings", yscrollcommand=game_scroll.set)

for col in columns:
    game_tree.heading(col, text=col)

game_scroll.config(command=game_tree.yview)
game_scroll.pack(side=tk.RIGHT, fill=tk.Y)
game_tree.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

console_list.bind("<<ListboxSelect>>", display_game_by_console)
game_tree.bind("<<TreeviewSelect>>", on_game_select)

# Frame untuk menu aksi
menu_frame = ttk.LabelFrame(root, text="Actions")
menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Frame untuk menambah game
add_frame = ttk.LabelFrame(root, text="Add Game")
add_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
add_frame.grid_forget()

tk.Label(add_frame, text="Console Name:").grid(row=0, column=0, padx=5, pady=5)
console_entry = ttk.Combobox(add_frame, values=[console.capitalize() for game in game_list for console in game.keys()], state="readonly")
console_entry.grid(row=0, column=1, padx=5, pady=5)
console_entry.set("Select Console")

tk.Label(add_frame, text="Game Name:").grid(row=1, column=0, padx=5, pady=5)
game_name_entry = tk.Entry(add_frame)
game_name_entry.grid(row=1, column=1, padx=5, pady=5)
game_name_entry.insert(0, "Enter Game Name")

tk.Label(add_frame, text="Game Price:").grid(row=2, column=0, padx=5, pady=5)
game_price_entry = tk.Entry(add_frame)
game_price_entry.grid(row=2, column=1, padx=5, pady=5)
game_price_entry.insert(0, "0.00")

add_button = ttk.Button(add_frame, text="Add Game", command=add_game)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

# Frame untuk mengedit game
edit_frame = ttk.LabelFrame(root, text="Edit Game")
edit_frame.grid(row=2, column=0, padx=2, pady=5, sticky=tk.W+tk.E)
edit_frame.grid_forget()
tk.Label(edit_frame, text="New Game Name:").grid(row=0, column=0, padx=5, pady=5)
new_game_name_entry = tk.Entry(edit_frame)
new_game_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(edit_frame, text="New Game Price:").grid(row=1, column=0, padx=5, pady=5)
new_game_price_entry = tk.Entry(edit_frame)
new_game_price_entry.grid(row=1, column=1, padx=5, pady=5)

edit_button = ttk.Button(edit_frame, text="Edit Game", command=edit_game)
edit_button.grid(row=2, column=0, columnspan=2, pady=5)


# Frame untuk menampilkan daftar game yang dibeli
bought_game_frame = ttk.LabelFrame(root, text="Daftar Game yang Dibeli")
bought_game_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W+tk.E)
bought_game_frame.grid_forget()
columns = ("Name", "Quantity", "Price", "Total Price")
bought_game_tree = ttk.Treeview(bought_game_frame, columns=columns, show="headings")

# Menambahkan judul kolom
for col in columns:
    bought_game_tree.heading(col, text=col)

bought_game_tree.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


buy_frame = ttk.LabelFrame(root, text="Buy Game")
buy_frame.grid(row=0, column=1, padx=2, pady=2, sticky=tk.SW)
buy_frame.grid_forget()
tk.Label(buy_frame, text="Quantity:").grid(row=0, column=0, padx=2, pady=2)
buy_quantity_entry = tk.Entry(buy_frame)
buy_quantity_entry.grid(row=0, column=1, padx=2, pady=2)

buy_button = ttk.Button(buy_frame, text="Next..", command=buy_game)
buy_button.grid(row=0, column=2, padx=2, pady=2)


# Frame untuk tombol bayar
pay_button = tk.Button(root, text="Bayar", command=pay, width=2)
pay_button.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W+tk.E)
pay_button.grid_forget()

# Sembunyikan frame daftar game yang dibeli saat awal
bought_game_frame.grid_forget()

# Frame untuk menghapus game
remove_frame = ttk.LabelFrame(root, text="Remove Game")
remove_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
remove_frame.grid_forget()
remove_button = ttk.Button(remove_frame, text="Remove Game", command=remove_game)
remove_button.grid(row=0, column=0, columnspan=2, pady=5)

# Frame untuk update stok game
update_stock_frame = ttk.LabelFrame(root, text="Update Stock")
update_stock_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
update_stock_frame.grid_forget()
tk.Label(update_stock_frame, text="New Stock:").grid(row=0, column=0, padx=2, pady=1)
new_stock_entry = tk.Entry(update_stock_frame)
new_stock_entry.grid(row=0, column=1, padx=2, pady=1)

update_stock_button = ttk.Button(update_stock_frame, text="Update Stock", command=update_stock)
update_stock_button.grid(row=1, column=0, columnspan=2, padx=2, pady=5)




root.mainloop()