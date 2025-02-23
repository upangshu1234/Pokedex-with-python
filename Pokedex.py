import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import ImageTk, Image
import io
import threading
import pygame
from pygame.locals import *
import webbrowser
class PokemonSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Search Ultimate")
        self.root.geometry("800x700")
        self.setup_ui()
        pygame.init()
        # Initialize variables
        self.current_image = None
        self.current_sound = None
    def setup_ui(self):
        # Search Frame
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=20)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<Return>", lambda event: self.search_pokemon())
        search_btn = ttk.Button(search_frame, text="Search", command=self.search_pokemon)
        search_btn.pack(side=tk.LEFT, padx=5)
        # Display Frame
        self.display_frame = ttk.Frame(self.root)
        self.display_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        # Image Label
        self.img_label = ttk.Label(self.display_frame)
        self.img_label.pack(pady=10)
        # Details Text
        self.details_text = tk.Text(self.display_frame, height=15, width=50)
        self.details_text.pack(pady=10, fill=tk.BOTH, expand=True)
        # Video Button
        self.video_btn = ttk.Button(self.display_frame, text="Watch Video", command=self.open_video)
        self.video_btn.pack(pady=5)
        self.video_btn.pack_forget()
    def search_pokemon(self):
        query = self.search_var.get().strip().lower()
        if not query:
            messagebox.showwarning("Warning", "Please enter a Pokemon name!")
            return
        # Use threading to prevent GUI freeze
        threading.Thread(target=self.fetch_pokemon_data, args=(query,), daemon=True).start()
    def fetch_pokemon_data(self, query):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query}")
            response.raise_for_status()
            data = response.json()
            # Get species data for more details
            species_response = requests.get(data['species']['url'])
            species_data = species_response.json()
            # Process data in main thread
            self.root.after(0, self.update_display, data, species_data)
            # Load and play sound
            self.root.after(0, self.play_sound, data['cries']['latest'])
        except requests.exceptions.RequestException:
            self.root.after(0, self.show_error, "Pokemon not found!")
    def update_display(self, data, species_data):
        self.clear_display() 
        # Load image
        img_url = data['sprites']['other']['official-artwork']['front_default']
        img_data = requests.get(img_url).content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        self.current_image = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.current_image)
        # Display details
        details = f"""Name: {data['name'].capitalize()}
Height: {data['height'] / 10} m
Weight: {data['weight'] / 10} kg
Types: {', '.join([t['type']['name'].capitalize() for t in data['types']])}
Abilities: {', '.join([a['ability']['name'].capitalize() for a in data['abilities']])}
Base Experience: {data['base_experience']}
Species: {species_data['generation']['name'].capitalize()}
Description: {species_data['flavor_text_entries'][0]['flavor_text']}
"""
        self.details_text.insert(tk.END, details)
        # Show video button if available
        self.video_btn.pack()
    def play_sound(self, sound_url):
        try:
            if self.current_sound:
                pygame.mixer.music.stop()
            sound_data = requests.get(sound_url).content
            with open("temp_sound.mp3", "wb") as f:
                f.write(sound_data)
            pygame.mixer.music.load("temp_sound.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print("Error playing sound:", e)
    def open_video(self):
        pokemon_name = self.search_var.get().strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={pokemon_name}+pokemon")
    def clear_display(self):
        self.details_text.delete(1.0, tk.END)
        self.img_label.config(image='')
        self.video_btn.pack_forget()
    def show_error(self, message):
        messagebox.showerror("Error", message)
        self.clear_display()
    def on_closing(self):
        if self.current_sound:
            pygame.mixer.music.stop()
        self.root.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonSearchApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()