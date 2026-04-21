# Import libraries for API request and opening browser
import requests
import webbrowser

# NASA API key and endpoint URL
API_KEY = "eLGbNtz08MjlO4ILvAeHFNrccaK4IOW21ecoBQrp"  # You can replace this with your own if needed
API_URL = "https://api.nasa.gov/planetary/apod"

# Function to fetch Astronomy Picture of the Day (APOD)
def fetch_apod():
    params = {
        "api_key": API_KEY
    }

    try:
        print("Fetching NASA's Astronomy Picture of the Day...")

        # Send GET request to NASA API
        response = requests.get(API_URL, params=params)
        
        # Convert response to JSON
        data = response.json()

        # Check if response contains image URL
        if "url" in data:
            return {
                "title": data.get("title"),
                "explanation": data.get("explanation"),
                "url": data.get("url")
            }
        else:
            return None

    # Handle errors (network issues, API errors, etc.)
    except Exception as e:
        print("Error:", e)
        return None

# Main program execution
if __name__ == "__main__":
    print("=== NASA APOD Viewer ===")

    # Call function to fetch data
    apod = fetch_apod()

    if apod:
        # Display APOD information
        print(f"\nTitle: {apod['title']}\n")
        print(f"Explanation:\n{apod['explanation']}\n")
        print(f"Image URL: {apod['url']}")

        # Ask user if they want to open image
        open_now = input("\nOpen this image in your browser? (y/n): ").strip().lower()
        
        # Open image in default browser if user says yes
        if open_now == 'y':
            webbrowser.open(apod["url"])
    else:
        # Handle case where data could not be retrieved
        print("Could not fetch APOD data.")
