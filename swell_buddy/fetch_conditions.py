import requests
import json

def fetch(spot):
    print(f"[*] Fetching surf conditions for {spot}...")

    # Simulate param-based URL
    url = f"https://jsonplaceholder.typicode.com/posts/1"
    print(f"[i] Using URL: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("[✓] Example data fetched:")
        print(json.dumps(data, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching data: {e}")
