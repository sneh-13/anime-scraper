# Anime Scraper

A Python-based project that scrapes anime details from [Anime-Planet](https://www.anime-planet.com) using Selenium and BeautifulSoup. The project provides both a command-line interface (CLI) and a graphical user interface (GUI) to display information such as the anime description, number of episodes, active years, rating, and tags.

## Features

- **Web Scraping:** Extracts anime details by parsing the HTML content of Anime-Planet pages.
- **CLI and GUI Support:** Run as a command-line tool or use the Tkinter-based graphical interface.
- **Selenium Integration:** Automates the web browser (Safari) to fetch live data.
- **Error Handling:** Provides user-friendly error messages for issues such as missing data or browser configuration problems.

## Prerequisites

- **Python 3.x**
- **Libraries:**
  - [Selenium](https://selenium-python.readthedocs.io/)
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- **Safari Browser:** Ensure Safari is installed.
  - **Note:** Remote Automation must be enabled in Safari. To do this, open Safari, go to **Develop > Allow Remote Automation** and enable it.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the Required Python Packages:**

    ```bash
    pip3 install selenium beautifulsoup4
    ```

## Project Structure

- **anime_scraper.py:** Contains the core logic for scraping anime details.
- **gui.py:** Implements a graphical user interface using Tkinter to interact with the scraper.

## Gui Interface

```bash
python gui.py
```

### Command-Line Interface

Run the CLI version by executing:

```bash
python anime_scraper.py
