import requests
import webbrowser

# Use NASA demo key or your own key
API_KEY = "eLGbNtz08MjlO4ILvAeHFNrccaK4IOW21ecoBQrp"  # You can replace this with your own if needed
API_URL = "https://api.nasa.gov/planetary/apod"

def fetch_apod():
    params = {
        "api_key": API_KEY
    }

    try:
        print("Fetching NASA's Astronomy Picture of the Day...")
        response = requests.get(API_URL, params=params)
        data = response.json()

        if "url" in data:
            return {
                "title": data.get("title"),
                "explanation": data.get("explanation"),
                "url": data.get("url")
            }
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    print("=== NASA APOD Viewer ===")
    apod = fetch_apod()

    if apod:
        print(f"\nTitle: {apod['title']}\n")
        print(f"Explanation:\n{apod['explanation']}\n")
        print(f"Image URL: {apod['url']}")

        open_now = input("\nOpen this image in your browser? (y/n): ").strip().lower()
        if open_now == 'y':
            webbrowser.open(apod["url"])
    else:
        print("Could not fetch APOD data.")
