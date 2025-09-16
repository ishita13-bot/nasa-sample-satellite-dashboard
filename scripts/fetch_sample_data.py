# fetch_sample_data.py
# Script to fetch NASA Astronomy Picture of the Day (APOD) data
# Uses NASA's public API with DEMO_KEY

import requests
import os
import json

def fetch_apod(api_key="DEMO_KEY", save_to="data/apod.json"):
    """Fetch APOD data from NASA API and save to a local file."""
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    os.makedirs(os.path.dirname(save_to), exist_ok=True)
    with open(save_to, "w") as f:
        json.dump(resp.json(), f, indent=2)
    print(f"NASA APOD data saved to {save_to}")

if __name__ == "__main__":
    fetch_apod()
