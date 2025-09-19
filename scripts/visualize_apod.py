# visualize_apod.py
# Read data/apod.json, download the APOD image, save to docs/screenshots/apod.jpg
# Requires: requests, pillow

import json
import os
import requests
from PIL import Image
from io import BytesIO

def visualize_apod(apod_json="data/apod.json", save_to="docs/screenshots/apod.jpg"):
    # Make sure apod json exists
    if not os.path.exists(apod_json):
        raise FileNotFoundError(f"{apod_json} not found. Run fetch_sample_data.py first.")

    # Load APOD JSON
    with open(apod_json, "r") as f:
        data = json.load(f)

    # Choose the best image URL
    url = data.get("hdurl") or data.get("url")
    media_type = data.get("media_type", "image")

    if media_type != "image":
        print("APOD is not an image (media_type =", media_type, "). Script will not download a video.")
        return

    if not url:
        raise ValueError("No image URL found in apod.json")

    # Download image
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    # Save image into docs/screenshots/
    os.makedirs(os.path.dirname(save_to), exist_ok=True)
    img = Image.open(BytesIO(resp.content))
    # Optional: convert to RGB to avoid mode issues (e.g., "P" or "RGBA")
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    img.save(save_to, quality=85)
    print(f"APOD image saved to {save_to}")

if __name__ == "__main__":
    visualize_apod()
