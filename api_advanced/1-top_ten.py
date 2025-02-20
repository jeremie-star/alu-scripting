#!/usr/bin/python3
"""Script to fetch the top 10 hot posts for a given subreddit."""

import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}

def top_ten(subreddit):
    """Fetch the first 10 hot posts from a given subreddit."""
    
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'limit': 10}
    
    response = requests.get(subreddit_url, headers=headers, params=parameters, allow_redirects=False)
    
    # If the subreddit is invalid (status code != 200), return None
    if response.status_code != 200:
        print(None)
        return
    
    # Parse the response JSON to get post titles
    json_data = response.json()
    
    # Get the title of the first 10 posts
    for post in json_data['data']['children']:
        print(post['data']['title'])

