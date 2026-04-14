import praw

# Replace with your own credentials
client_id = 'Jfur91sOuW_w8WrVzLZmqQ'
client_secret = 'J8LaeM6gUd-b6SNU4gxrCUGxXpkj3A'
user_agent = 'MyRedditScraper/1.0 by MyRedditUsername'
username = 'Single_Anything_1848'
password = 'bajajworld15'

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)

# Define the subreddit you want to scrape
subreddit_name = 'python'

# Define the number of posts to retrieve
num_posts = 10

# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Loop through the top posts in the subreddit
for submission in subreddit.top(limit=num_posts):
    print(f'Title: {submission.title}')
    print(f'Score: {submission.score}')
    print(f'URL: {submission.url}')
    print(f'Author: {submission.author}')
    print(f'Number of comments: {submission.num_comments}')
    print(f'Upvote ratio: {submission.upvote_ratio}')
    print(f'Post ID: {submission.id}')
    print(f'Submission time: {submission.created_utc}')
    print(f'Submission text: {submission.selftext}')
    print(f'Link to comments: {submission.permalink}')
    print(f'Subreddit: {submission.subreddit.display_name}')
    print(f'Link flair text: {submission.link_flair_text}')
    print(f'Locked: {submission.locked}')
    print(f'Sticky: {submission.stickied}')
    print(f'Is NSFW: {submission.over_18}')
    print(f'Spoiler: {submission.spoiler}')
    print(f'Is Video: {submission.is_video}')
    print(f'Archived: {submission.archived}')
    print(f'Gilded: {submission.gilded}')
    print(f'URL domain: {submission.domain}')
    print(f'Upvoted: {submission.likes}')
    # print(f'Downvoted: {submission.dislikes}')
    print(f'Original content: {submission.is_original_content}')
    print(f'Upvotes: {submission.ups}')
    print(f'Downvotes: {submission.downs}')
    print(f'Content categories: {submission.link_flair_richtext}')
    print(f'Reddit awards: {submission.all_awardings}')
    print(f'Is a crosspost: {submission.is_crosspostable}')
    # print(f'Crosspost parent: {submission.crosspost_parent}')
    # print(f'Crosspost parent list: {submission.crosspost_parent_list}')
    print(f'Saved by: {submission.saved}')
    print(f'User upvote: {submission.user_reports}')
    print(f'Media: {submission.media}')
    print(f'Is edited: {submission.edited}')
    print(f'Number of reports: {submission.num_reports}')
    # print(f'Flair: {submission.link_flair_template_id}')
    print(f'Post awards: {submission.total_awards_received}')
    print(f'Post upvote ratio: {submission.upvote_ratio}')
    # print(f'Stickied comment: {submission.stickied_comment}')
    print(f'Quarantined: {submission.quarantine}')
    print(f'User flair: {submission.author_flair_text}')
    print(f'Reddit gold: {submission.gilded}')
    print(f'Subreddit icon: {submission.subreddit.icon_img}')
    # print(f'Post preview: {submission.preview}')
    # print(f'Link to crosspost: {submission.url}')
    print('------------------')