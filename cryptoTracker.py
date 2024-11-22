import requests
import time
from datetime import datetime

def fetch_data():
    # Include pi-network along with bitcoin and ethereum
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,pi-network&vs_currencies=usd"
    
    while True:
        try:
            # Make the API request
            response = requests.get(url)
            
            # Debugging: Print the response URL and status code for troubleshooting
            print(f"Request URL: {response.url}")
            print(f"HTTP Status Code: {response.status_code}")

            # Check if the response status code is 422 (Unprocessable Entity)
            if response.status_code == 422:
                print(f"Error 422: The request could not be processed.")
                print(f"Response Content: {response.json()}")  # Print the detailed error response
                break  # Exit the loop as we can't continue with this request
            
            # Handle 429 (Rate Limit Exceeded)
            if response.status_code == 429:
                print("Rate limit exceeded. Retrying in 60 seconds...")
                time.sleep(60)  # Wait for 60 seconds before retrying
                continue
            
            # If response status is successful (200 OK)
            if response.status_code == 200:
                data = response.json()
                
                # Fetch prices for bitcoin, ethereum, and pi-network
                bitcoin_price = data.get('bitcoin', {}).get('usd', 'N/A')
                ethereum_price = data.get('ethereum', {}).get('usd', 'N/A')
                pi_network_price = data.get('pi-network', {}).get('usd', 'N/A')
                
                # Display the fetched data
                print(f"Bitcoin Price: ${bitcoin_price}")
                print(f"Ethereum Price: ${ethereum_price}")
                print(f"PI Network Price: ${pi_network_price}")
                break  # Exit the loop if data is fetched successfully
            
            else:
                print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
                break  # Exit the loop if status code isn't 200, 422, or 429

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            break  # Exit the loop on any exception (e.g., network issues)

if __name__ == "__main__":
    print(f"Updating data at {datetime.now()}")
    fetch_data()
