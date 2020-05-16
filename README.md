# Installation  

- Clone this repo to a directory
- Install Python 3
- Install required python dependencies
  - PRAW

# Usage
- Run script using `py main.py`
- Current available arguments
  - `--count` An integer value for number of posts to make
  - `--images` Directory containing images to choose from
  - `--words` A .txt file containing word list to pick words from (1 per line)
  - `--subreddit` The subreddit to post to
- Example usage: `py main.py --subreddit mxethaephfouer --count 10 --images images --words words.txt`
  - Submits 10 posts to the subreddit "mxethaephfouer" choosing images from the "images" directory and words from the
   file "words.txt"