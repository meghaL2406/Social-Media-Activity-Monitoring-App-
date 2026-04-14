import praw
import os
import requests
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Pydantic model for incoming login requests
class LoginRequest(BaseModel):
    subreddit_name : str



app = FastAPI()

lst = []
# Initialize the Reddit API wrapper
reddit = praw.Reddit(
    client_id = 'Jfur91sOuW_w8WrVzLZmqQ',
    client_secret = 'J8LaeM6gUd-b6SNU4gxrCUGxXpkj3A',
    user_agent = 'MyRedditScraper/1.0 by My Scraper',
)

@app.post("/reddit-login")
async def login(login_request: LoginRequest):
    subreddit_name = login_request.subreddit_name

    # Get the subreddit instance
    subreddit = reddit.subreddit(subreddit_name)

    # Specify the number of posts to download
    num_posts = 20 # Adjust as needed

    # Directory where you want to save downloaded media
    download_directory = r'./images'

    # Create the download directory if it doesn't exist
    os.makedirs(download_directory, exist_ok=True)
    num = 1
    for submission in subreddit.top(limit=num_posts):
        print("Post No. - ", num)
        print("title -- ",submission.title)
        print("url -- ",submission.url)
        if submission.url.endswith(('.jpg', '.png', '.gif', '.jpeg', '.webp')):
            media_url = submission.url
            file_extension = media_url.split('.')[-1]
            filename = f"{num}.{file_extension}"
            file_path = os.path.join(download_directory, filename)

            with open(file_path, 'wb') as file:
                file.write(requests.get(media_url).content)
            print(f"Downloaded: {filename}")
        num+=1

    print("Downloads completed.")
    return {"message": "Login successful"}




@app.get("/reddit-images")
async def get_images():
    lst = os.listdir('./images')
    print(lst)

    dict1 =  {"urls": [
        "https://i.redd.it/p1i8awsivji51.jpg",
        "https://i.redd.it/47qqwabpvqv41.png",
        "https://i.redd.it/cbz37hmdx9751.jpg",
    ]
    }

    return dict1

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)