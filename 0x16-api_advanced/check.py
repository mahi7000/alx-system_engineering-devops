import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("Subreddit not found or no posts available.")
    else:
        print("Error accessing subreddit. Please check the subreddit name.")

# Fetch top posts from the "programming" subreddit with user-agent header
top_ten("programming")  # Display titles of the top 10 hot posts from the "programming" subreddit
