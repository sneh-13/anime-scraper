import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver

def details(soup):
    # Get the anime description
    info = soup.find('div', {'class': 'pure-1 md-3-5'})
    if info:
        p = info.find('p')
        if p:
            print("\nAbout the Anime:\n\t", p.getText(), "\n")
        else:
            print("Anime description not found.")
    else:
        print("Anime description container not found.")

    # Get total number of episodes
    total_episodes = soup.find('div', {'class': 'pure-1 md-1-5'})
    if total_episodes:
        span_ep = total_episodes.find('span')
        if span_ep:
            episodes = re.sub("[^0-9]", "", span_ep.getText())
            print("\nTotal number of episodes:\t", episodes)
        else:
            print("Episodes count not found.")
    else:
        print("Episodes container not found.")

    # Get active years
    active_years = soup.find('span', {'class': 'iconYear'})
    if active_years:
        print("\nYears Active (From-To):\t", active_years.getText(), "-")
    else:
        print("Active years not found.")

    # Get rating
    rating = soup.find('div', {'class': 'avgRating'})
    if rating:
        span_rating = rating.find('span')
        if span_rating:
            print("\nRating:\t", span_rating.getText())
        else:
            print("Rating details not found.")
    else:
        print("Rating container not found.")

    # Get tags and remove extra spaces
    tags = soup.find('div', {'class': 'tags'})
    if tags:
        tags_list = tags.find('ul')
        if tags_list:
            tags_text = tags_list.getText().replace("\n", " ").strip()
            tags_text = " ".join(tags_text.split())  # Removes extra spaces
            print("\nTags:\n", tags_text)
        else:
            print("Tags list not found.")
    else:
        print("Tags container not found.")

def entry():
    print("\nType complete name>>\n")
    anime_name = input("Enter the name of the anime: ")
    # Format the anime name appropriately for the URL
    anime_name = " ".join(anime_name.split()).title().replace(" ", "-")
    print("\nFormatted Anime Name:", anime_name)

    search_url = "https://www.anime-planet.com/anime/" + anime_name

    try:
        driver = webdriver.Safari()
    except Exception as e:
        print("Error initializing Safari WebDriver. Make sure Remote Automation is enabled in Safari's Develop menu.", e)
        sys.exit(1)

    try:
        driver.get(search_url)
    except Exception as e:
        print("Error fetching the page with Safari:", e)
        driver.quit()
        sys.exit(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        details(soup)
    except AttributeError:
        print("Anime info not found.")
    
    driver.quit()

if __name__ == "__main__":
    entry()
