# Westminster Scrapper
# Scrapping url https://en.wikipedia.org/wiki/List_of_Best_in_Show_winners_of_the_Westminster_Kennel_Club_Dog_Show
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Best_in_Show_winners_of_the_Westminster_Kennel_Club_Dog_Show"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the winners
table = soup.find('table', {'class': 'wikitable'})

# Extract the data from the table
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    if cells:
        year = cells[0].text.strip()
        dog_name = cells[1].text.strip()
        breed = cells[2].text.strip()
        owner = cells[3].text.strip()
        print(f"Year: {year}, Dog Name: {dog_name}, Breed: {breed}, Owner: {owner}")

if __name__ == "__main__":
    print("Running scrapper one...")
