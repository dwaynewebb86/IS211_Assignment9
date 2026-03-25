# Westminster Scrapper
# Scrapping url https://en.wikipedia.org/wiki/List_of_Best_in_Show_winners_of_the_Westminster_Kennel_Club_Dog_Show
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_westminster():
    url = "https://en.wikipedia.org/wiki/List_of_Best_in_Show_winners_of_the_Westminster_Kennel_Club_Dog_Show"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the winners table
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    # extract data from the first table (which contains the winners)
    data = []
    for row in tables[0].find_all('tr')[1:]:
        th_cells = row.find_all('th')
        td_cells = row.find_all('td')
        
        if len(td_cells) >= 5:
            year =   th_cells[0].text.strip() if th_cells else ''
            winner = td_cells[0].text.strip()
            breed =  td_cells[2].text.strip()
            group =  td_cells[3].text.strip()
            owner =  td_cells[4].text.strip()
            
            data.append({
                'year':   year,
                'winner': winner,
                'breed':  breed,
                'group':  group,
                'owner':  owner
            })
            
            print(f"Year: {year}, Winner: {winner}, Breed: {breed}, Group: {group}, Owner: {owner}")
    
    return data

if __name__ == "__main__":
    print("Running scrapper...")
    data = scrape_westminster()
    
    print("\n10 Recent Winners:")
    for row in data[-10:]:  
        print(f"Year: {row['year']}, Winner: {row['winner']}, Breed: {row['breed']}, Group: {row['group']}, Owner: {row['owner']}")
    
    print(f"\nTotal records scraped: {len(data)}")