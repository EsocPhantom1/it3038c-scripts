import requests
from bs4 import BeautifulSoup

# URL where Node.js API is running
node_api_url = "http://localhost:3000/"

try:
    # Make a GET request to the Node.js API for HTML
    response_html = requests.get(f"{node_api_url}")

    # Check if the request was successful (status code 200)
    if response_html.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response_html.text, 'html.parser')

        # Extract widget information
        widgets = soup.find('p').get_text()

        # Print the widget information
        print(widgets)

    else:
        print(f"Error: {response_html.status_code} - {response_html.text}")

except requests.RequestException as e:
    print(f"Request failed: {e}")
