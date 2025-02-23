Pokedex using Python

This is a simple GUI-based Pokedex application built using Python and Tkinter. It allows users to search for Pokemon by name, retrieve their details using the PokeAPI, display their images, play their cries, and even open a YouTube search for related videos.

Features

Search Pokemon: Enter a Pokemon's name and retrieve details instantly.

Detailed Information: Get height, weight, types, abilities, and base experience.

Image Display: Fetch and display official artwork from PokeAPI.

Sound Playback: Play the Pokemon's cry sound using pygame.

YouTube Search: Open a browser window with related Pokemon videos.

Error Handling: Displays appropriate messages when an invalid search is performed.

Installation

Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Cloning the Repository

To get started, clone the repository using the following command:

git clone https://github.com/yourusername/pokedex-python.git
cd pokedex-python

Installing Dependencies

To install the required dependencies, run the following command:

pip install -r requirements.txt

Alternatively, you can install them manually:

pip install requests pillow pygame

Usage

Run the script using the following command:

python pokedex.py

How to Use:

Open the application.

Enter the name of the Pokemon you want to search for.

Press Enter or click the Search button.

View the Pokemon's details, including its image and sound.

Click on Watch Video to explore related content on YouTube.

Libraries Used

tkinter - for GUI development.

requests - to fetch data from PokeAPI.

Pillow (PIL) - for image processing.

pygame - for playing Pokemon cries.

webbrowser - to open YouTube search results.

threading - to prevent UI freezing during API requests.

API Used

PokeAPI is used to fetch real-time Pokemon data.

Screenshots



License

This project is open-source and available under the MIT License.

Author

Upangshu Basak

