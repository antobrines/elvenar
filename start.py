import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from PIL import Image, ImageTk
import time
import os


# Dictionnaire contenant les bots disponibles
bot_files = {
    "Farm elvenar": {"file": "elvenar/help.py", "command": "python", "description": "Permet de farmer les amis rapidement"},
    "Code sw": {"file": "sw/code summoners/index.js", "command": "node", "description": "Permet de récupérer les coupons de code SWC et de les utiliser directement POG"}
}

# Création de la fenêtre principale
window = tk.Tk()
window.title("Summoners War Chronicle")

# Définition de la taille de la fenêtre
window.geometry("400x300")

description_frame = tk.Frame(window)
description_frame.pack(pady=10)

# Ajout d'une image
image = Image.open("summoners_war.png")
width, height = image.size
if width > 200:
    ratio = 200 / width
    width = 200
    height = int(height * ratio)
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
image_label = tk.Label(description_frame, image=image)
image_label.pack()

# Ajout d'une description
description = tk.Label(text="Bienvenue dans Summoners War Chronicler !")
description.pack(pady=10)


bot_desc_label = tk.Label(window, wraplength=400)
bot_desc_label.pack(side=tk.TOP)

current_process = None
# Fonction pour démarrer ou arrêter le bot


def start_stop_bot():
    global current_process
    if start_stop_button["text"] == "Démarrer":
        bot_label.pack_forget()
        bot_list.pack_forget()
        bot_selected_label.pack(side=tk.LEFT, before=start_stop_button)
        bot_selected_label.config(
            text="Bot sélectionné : '{}'".format(bot_selected.get()))

        start_stop_button["text"] = "Arrêter"

        bot_file = bot_files[bot_selected.get()]["file"]
        command = bot_files[bot_selected.get()]["command"]
        try:
            current_process = subprocess.Popen([command, bot_file])
        except:
            print("Impossible de démarrer le bot {}.".format(bot_selected.get()))
        print("Le bot {} a été démarré.".format(bot_selected.get()))
    else:
        bot_label.pack(side=tk.LEFT, before=start_stop_button)
        bot_list.pack(side=tk.LEFT, before=start_stop_button)
        bot_selected_label.pack_forget()
        bot_file = bot_files[bot_selected.get()]["file"]
        current_process.terminate()
        start_stop_button["text"] = "Démarrer"
        print("Le bot {} a été arrêté.".format(bot_selected.get()))


# Ajout d'un bouton pour démarrer ou arrêter le bot
start_stop_button = tk.Button(text="Démarrer", command=start_stop_bot)
start_stop_button.pack(side=tk.LEFT, padx=10)

# Ajout de la liste de bots
bots = list(bot_files.keys())
bot_selected = tk.StringVar(window)
bot_selected.set(bots[0])
bot_label = tk.Label(text="Sélectionnez un bot :")
bot_label.pack(side=tk.LEFT, before=start_stop_button)
# bot_list = tk.ttk.Combobox(window, textvariable=bot_selected)
# bot_list["values"] = list(bot_files.keys())
bot_list = tk.OptionMenu(window, bot_selected, *bot_files.keys())
bot_list.pack(side=tk.LEFT, before=start_stop_button)
bot_selected_label = tk.Label(window, text="")
bot_selected_label.pack(side=tk.LEFT, before=start_stop_button)


def on_bot_selected(*args):
    selected_bot = bot_selected.get()
    bot_desc = bot_files[selected_bot]["description"]
    bot_desc_label.config(text=bot_desc)


on_bot_selected()

# ajout event listener on change to bot list
bot_selected.trace("w", on_bot_selected)
# Fonction appelée lorsque la fenêtre est fermée


def on_closing():
    if current_process is not None and current_process.poll() is None:
        current_process.terminate()
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

# Boucle principale de la fenêtre
window.mainloop()
