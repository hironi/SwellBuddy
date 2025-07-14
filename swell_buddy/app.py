from swell_buddy.config import SPOT
from swell_buddy.fetch_conditions import fetch

VERSION = "0.1"

def main():
    print(f"🌊 Welcome to SwellBuddy v{VERSION}")
    print()
    fetch(SPOT)

if __name__ == "__main__":
    main()
