# Pokedex using Python

This is a simple GUI-based Pokedex application built using Python and Tkinter. It allows users to search for Pokemon by name, retrieve their details using the PokeAPI, display their images, play their cries, and even open a YouTube search for related videos.

## Features
- **Search Pokemon:** Enter a Pokemon's name and retrieve details instantly.
- **Detailed Information:** Get height, weight, types, abilities, and base experience.
- **Image Display:** Fetch and display official artwork from PokeAPI.
- **Sound Playback:** Play the Pokemon's cry sound using pygame.
- **YouTube Search:** Open a browser window with related Pokemon videos.
- **Error Handling:** Displays appropriate messages when an invalid search is performed.

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Cloning the Repository
To get started, clone the repository using the following command:

```bash
git clone https://github.com/upangshu1234/Pokedex-with-python.git
cd Pokedex-with-python
```

### Installing Dependencies
To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Alternatively, you can install them manually:

```bash
pip install requests pillow pygame
```

## Usage
Run the script using the following command:

```bash
python pokedex.py
```

### How to Use:
1. Open the application.
2. Enter the name of the Pokemon you want to search for.
3. Press `Enter` or click the `Search` button.
4. View the Pokemon's details, including its image and sound.
5. Click on `Watch Video` to explore related content on YouTube.

## Libraries Used
- `tkinter` - for GUI development.
- `requests` - to fetch data from PokeAPI.
- `Pillow` (PIL) - for image processing.
- `pygame` - for playing Pokemon cries.
- `webbrowser` - to open YouTube search results.
- `threading` - to prevent UI freezing during API requests.

## API Used
[PokeAPI](https://pokeapi.co/) is used to fetch real-time Pokemon data.

## Screenshots


## License
This project is open-source and available under the MIT License.

## Author
Upangshu Basak

---
Feel free to contribute to this project by submitting pull requests!

