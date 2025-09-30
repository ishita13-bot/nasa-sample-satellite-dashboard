import folium
import json

def plot_iss_position(json_file="data/iss_position.json", output_file="docs/screenshots/iss_map.html"):
    # Load latest ISS position from JSON
    with open(json_file, "r") as f:
        data = json.load(f)
        lat = float(data["iss_position"]["latitude"])
        lon = float(data["iss_position"]["longitude"])

    # Create a map centered on ISS position
    m = folium.Map(location=[lat, lon], zoom_start=3)

    # Add a marker
    folium.Marker(
        [lat, lon],
        popup="🛰 ISS",
        icon=folium.Icon(color="red", icon="rocket")
    ).add_to(m)

    # Save to HTML file
    m.save(output_file)
    print(f"ISS map saved to {output_file}")

if __name__ == "__main__":
    plot_iss_position()
