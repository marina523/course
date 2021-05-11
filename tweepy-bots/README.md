# Data Project 2: Twitter Bot
###### Marina Awad
I created an interactive Twitter based bot (@datasci25159468) that can help users with what vegetarian and vegan dishes to get at different continents (except for Antarctica). It can also define what a vegan is versus vegetarian, and it can tell the user who and what was the last tweet in the home timeline. When running  the cj.py file, it is important to run it in the bots folder directory.
## Summary:

- Prints the author and text of the last tweet in your home timeline: 
make sure to include the word "last" in the tweet.

- Prints the definition of vegan or vegetarian
include the phrase 'define vegan' or 'define  vegetarian' respectively.

- Recommends a vegetarian dish from a user's stated continent: 
in the cj.py, I have lists of vegetarian foods from different continents. The user must include the name of the continent (ex: "North America") to which a random vegetarian dish that is present in that area will be tweeted. I did this by importing the random module to get a random index of the list. 

- Need Help 
tweet the bot something with the word 'help' and it will give you options for things to ask the bot.

The key way that the not decided on how to ansswer is by looking for certain words in the user's input tweet, and then returning a data-driven reply. An example of a problem I had to solve is I originally wrote a code that returned the last 20 tweets and authors, but I only wanted the most recent one, so I had to go through some parsing and indexing to only get the last one. 
