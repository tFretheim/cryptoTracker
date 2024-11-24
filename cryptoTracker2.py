import requests
from datetime import datetime

def fetch_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,pi-network&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def recommend_crypto(data, budget=100):
    recommendations = []
    for coin, details in data.items():
        price = details.get("usd", 0)
        change_24hr = details.get("usd_24h_change", 0)
        market_cap = details.get("usd_market_cap", 0)

        # Recommendation logic:
        # - Price is within budget
        # - Positive growth over 24 hours
        if price <= budget and change_24hr > 0:
            recommendations.append({
                "name": coin.capitalize(),
                "price": price,
                "24hr_change": round(change_24hr, 2),
                "market_cap": round(market_cap, 2),
            })
    
    return recommendations

def display_recommendations(recommendations):
    if not recommendations:
        print("No recommendations found based on the current criteria.")
    else:
        print("\nRecommended Cryptocurrencies to Buy:")
        for rec in recommendations:
            print(
                f"- {rec['name']}: ${rec['price']} (24hr Change: {rec['24hr_change']}%, Market Cap: ${rec['market_cap']})"
            )

if __name__ == "__main__":
    print(f"Updating data at {datetime.now()}")
    data = fetch_data()
    
    if data:
        # Display fetched data
        print("\nCurrent Cryptocurrency Prices:")
        for coin, details in data.items():
            print(f"{coin.capitalize()}: ${details.get('usd', 'N/A')} (24hr Change: {details.get('usd_24h_change', 'N/A')}%)")
        
        # Generate and display recommendations
        recommendations = recommend_crypto(data, budget=100)  # Set a budget of $100
        display_recommendations(recommendations)
