
import requests
from bs4 import BeautifulSoup

def scrape_apple_stock():
    
    # Try different URL formats
    url = "https://finance.yahoo.com/quote/AAPL/history/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status code: {response.status_code}")
    print(f"Final URL: {response.url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check all tables
    tables = soup.find_all('table')
    print(f"Number of tables found: {len(tables)}")
    
    # Check page title to confirm we're on right page
    title = soup.find('title')
    print(f"Page title: {title.text if title else 'No title found'}")
    
    data = []
    if tables:
        for row in tables[0].find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) >= 5:
                date  = cells[0].text.strip()
                close = cells[4].text.strip()
                data.append({
                    'date':  date,
                    'close': close
                })
                print(f"Date: {date}, Close: {close}")
    else:
        print("No tables found — page is JavaScript rendered")
        print("Recommendation: switch to yfinance library")
    
    return data

if __name__ == "__main__":
    print("Running Apple Stock scrapper...")
    data = scrape_apple_stock()
      
    print(f"\nTotal records scraped: {len(data)}")