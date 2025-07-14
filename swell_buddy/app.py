VERSION = "0.1"

def main():
    print(f"🌊 Welcome to SwellBuddy v{VERSION}")
    spot = "Costa da Caparica"
    print()

    from swell_buddy.fetch_conditions import fetch
    fetch(spot)

if __name__ == "__main__":
    main()
