import requests

def example_get_request():
    # Example 1: Making a GET request to a public API
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Example 1 - GET Request:")
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
        print("\n")
    else:
        print("Example 1 - GET Request failed. Status Code:", response.status_code)

def example_post_request():
    # Example 2: Making a POST request with data
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    
    # Check if the request was successful (status code 201 for created)
    if response.status_code == 201:
        print("Example 2 - POST Request:")
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
        print("\n")
    else:
        print("Example 2 - POST Request failed. Status Code:", response.status_code)

def example_json_parsing():
    # Example 3: Handling response content (JSON parsing)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Example 3 - JSON Parsing:")
        post_data = response.json()
        print("Post Title:", post_data['title'])
        print("Post Body:", post_data['body'])
        print("\n")
    else:
        print("Example 3 - GET Request failed. Status Code:", response.status_code)

if __name__ == "__main__":
    example_get_request()
    example_post_request()
    example_json_parsing()
