import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends a GET request to the URL and returns the response body as bytes
        response = requests.get(self.url)
        return response.content  # returns the raw response body as a byte string

    def load_json(self):
        # Uses get_response_body to send a request and converts the response to JSON
        response_body = self.get_response_body()
        return json.loads(response_body)  # converts the byte string to Python dict/list
