Here is how you can run a Python script that I created, which uses a plugin called Requests.

First, let's create install requests to our machine. go to command prompt and go to the path to where your Lab7.py script is by using the "cd" command followed by the path
then you want to install requests by using the pip command "pip install requests"

This script demonstrates the usage of the `requests` library in Python to make HTTP requests. Below are three examples of different use cases:

Example 1: Makes a GET request to retrieve information about a specific post, in this case we have a post with ID 1 from the JSONPlaceholder API. It prints the status code and the response JSON if the request is successful.
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
sends a GET request to the specified URL, requesting information about the post with ID 1 from the JSONPlaceholder API.

if response.status_code == 200:
    print("Example 1 - GET Request:")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
Checks if the GET request was successful (status code 200). If successful, it prints the status code and the response JSON.

Example 2: Makes a POST request to create a new post on the JSONPlaceholder API. It includes some data (title, body, userId) in the request payload. It prints the status code and the response JSON if the request is successful.

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
sends a POST request to the specified URL, creating a new post with the provided data.

if response.status_code == 201:
    print("Example 2 - POST Request:")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
Checks if the POST request was successful (status code 201). If successful, it prints the status code and the response JSON

Example 3: Makes another GET request to retrieve information about a specific post (post with ID 1) from the JSONPlaceholder API. It then parses the JSON response and prints specific details like the post title and body.

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
This line sends another GET request to retrieve information about the post with ID 1.

if response.status_code == 200:
    print("Example 3 - JSON Parsing:")
    post_data = response.json()
    print("Post Title:", post_data['title'])
    print("Post Body:", post_data['body'])
Checks if the GET request was successful (status code 200). If successful, it parses the JSON response and prints specific details like the post title and body.

Finally all three functions are called sequentially when the script is executed in the "main" block.

if __name__ == "__main__":
    example_get_request()
    example_post_request()
    example_json_parsing()
