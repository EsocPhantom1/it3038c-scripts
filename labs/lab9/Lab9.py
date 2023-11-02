import requests

# url where Node.js is running
node_api_url = "http://localhost:3000/"

try:
    # Make a GET request to the Node.js API for all widgets
    response_all_widgets = requests.get(f"{node_api_url}")

    # Check if the request was successful (status code 200)
    if response_all_widgets.status_code == 200:
        # Parse JSON response
        widgets_all = response_all_widgets.json()

        # Print all widget names and colors 
        print("All widgets:")
        for widget in widgets_all:
            print(f"{widget['name']} is {widget['color']}.")

    else:
        print(f"Error: {response_all_widgets.status_code} - {response_all_widgets.text}")

except requests.RequestException as e:
    print(f"Request failed: {e}")
