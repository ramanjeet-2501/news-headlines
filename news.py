import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url, output_file):
    """
    Scrapes news headlines from a given URL and saves them to a text file.
    
    Args:
        url (str): URL of the news website to scrape
        output_file (str): Path to the output text file
    """
    try:
        # Step 1: Fetch the HTML content
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Step 2: Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Step 3: Find all headline elements (adjust selector as needed)
        # Common selectors for headlines: h1, h2, h3, or specific class names
        headlines = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_=lambda x: x and 'headline' in x.lower())
        
        # If no headlines found with class, try without class filter
        if not headlines:
            headlines = soup.find_all(['h1', 'h2', 'h3'])
        
        # Step 4: Extract and clean the headline text
        cleaned_headlines = []
        for headline in headlines:
            text = headline.get_text().strip()
            if text:  # Only add non-empty headlines
                cleaned_headlines.append(text)
        
        # Step 5: Save to a text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Top Headlines from {url}\n")
            f.write("="*50 + "\n\n")
            for i, headline in enumerate(cleaned_headlines, 1):
                f.write(f"{i}. {headline}\n")
        
        print(f"Successfully scraped {len(cleaned_headlines)} headlines to {output_file}")
    
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Use BBC News as an example (always check a site's terms before scraping)
    news_url = "https://www.bbc.com/news"
    output_filename = "news_headlines.txt"
    
    scrape_news_headlines(news_url, output_filename)
