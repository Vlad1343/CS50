import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        btc = float(sys.argv[1])
        if btc <= 0:
            raise ValueError("Number must be positive")
    except ValueError as e:
        print(f"Command-line argument is not a number: {e}")
        sys.exit(1)

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()
        usd = float(data['data']['priceUsd'])
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

    total_cost = btc * usd
    print(f"${total_cost:,.4f}")


main()
