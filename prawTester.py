import praw
import csv
import datetime
import os

# Initialize Reddit instance with your credentials
reddit = praw.Reddit(client_id='i8fHdKMv_Y09k4eHP140HQ',
                     client_secret='tQ_eb4ZmFHCUVWWXAh1_HFM-o0ncAw',
                     user_agent='passportbrospraw')

# Input subreddit and data file name
subreddit_name = input("Enter the subreddit name: ")
data_file_name = input("Enter data file name: ")

# Access the subreddit
subreddit = reddit.subreddit(subreddit_name)

# Function to scrape all available posts in the subreddit
def process_reddit_posts():
    try:
        # Open CSV file for writing
        with open(data_file_name + '.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(["Subreddit", "Title", "Date", "Comments", "Upvotes", "Author", "URL"])

            # Fetching historical posts
            for post in subreddit.new(limit=None):  # Fetch all available posts
                subreddit_name = post.subreddit.display_name
                title = post.title
                post_date = datetime.datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d')
                num_comments = post.num_comments
                upvotes = post.score  
                author = post.author.name if post.author else "Unknown"
                url = post.url

                # Append the data as a new row in the .csv file
                writer.writerow([subreddit_name, title, post_date, num_comments, upvotes, 
                                 author, url])

            # Print the title as progress feedback
            print(f"Scraped post: {title}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to process posts
process_reddit_posts()

# Save the Excel file
file_name = data_file_name + '.csv'

# Automatically open the file after saving
try:
    os.system(f"open {file_name}")  # For macOS
    # os.system(f"start {file_name}")  # For Windows
    # os.system(f"xdg-open {file_name}")  # For Linux
except Exception as e:
    print(f"Failed to open the file: {e}")
