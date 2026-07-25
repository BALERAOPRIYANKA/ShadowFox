
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string
    print("Page Title:", title)

    with open("page_title.txt", "w") as file:
        file.write(title)

    print("Title saved successfully in page_title.txt")
else:
    print("Failed to fetch the webpage.")
