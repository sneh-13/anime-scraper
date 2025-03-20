import tkinter as tk
from tkinter import messagebox
import anime_scraper  # This is your existing module
import io
import contextlib
from selenium import webdriver
from bs4 import BeautifulSoup

def get_anime_details(anime_name):
    """
    Mimics the functionality of anime_scraper.entry() but uses the provided
    anime_name parameter. It formats the name, fetches the page using Safari,
    parses it with BeautifulSoup, and captures the output of anime_scraper.details().
    """
    # Format the anime name (e.g., "Naruto Shippuden" becomes "Naruto-Shippuden")
    formatted_name = " ".join(anime_name.split()).title().replace(" ", "-")
    search_url = "https://www.anime-planet.com/anime/" + formatted_name

    try:
        # Initialize Safari WebDriver (ensure Remote Automation is enabled in Safari)
        driver = webdriver.Safari()
    except Exception as e:
        return f"Error initializing Safari WebDriver. Make sure Remote Automation is enabled in Safari's Develop menu.\n{e}"
    
    try:
        driver.get(search_url)
    except Exception as e:
        driver.quit()
        return f"Error fetching the page with Safari:\n{e}"

    # Get the page source and parse it with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Capture the output from anime_scraper.details(soup) which prints details
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        try:
            anime_scraper.details(soup)
        except AttributeError:
            print("Anime info not found.")
    
    driver.quit()
    return output_buffer.getvalue()

def search_anime():
    anime_name = entry.get().strip()
    if not anime_name:
        messagebox.showerror("Error", "Please enter an anime name.")
        return
    # Clear previous output
    text_output.delete("1.0", tk.END)
    
    # Get the anime details from our wrapper function
    result = get_anime_details(anime_name)
    text_output.insert(tk.END, result)

# Set up the main application window
root = tk.Tk()
root.title("Anime Scraper GUI")

# Frame for the search input and button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter Anime Name:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=(5, 5))

button = tk.Button(frame, text="Search", command=search_anime)
button.pack(side=tk.LEFT)

# Text widget to display the output details
text_output = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_output.pack(padx=10, pady=10)

root.mainloop()
