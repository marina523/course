# Data Project 1: API-based Chatbot
###### Marina Awad

I have written an API with at least 5 endpoints. It is all about words,
and can be useful for games such as Scribble and Mad Libs. 
## The endpoints:
/
###### description: 
this is the zone apex, with an introductory welcome to the user.

/count/{word1}/{word2}
###### description: 
the bracketed words word1 and word2 represent two words 
that the user will enter. The output is an integer, the number of letters
in those two words combined. These items should only be composed of letters.

/descriptiveword/{adj_num}/{noun_num}
###### description: 
both items to be entered (variables adj_num and noun_num) should be 
integers. It returns two generated words, an adjective and noun. These come from 
the files adjectives.txt and nouns.txt respectively. The numbers entered by the 
user indicates an index for a row in the text file (each row has a word).

/madlibs/{topic}/{adjective}/{noun}
###### description: 
the user has three options for the topic item. They can either enter
zoo, park, or clothing. This represents the topic of the Mad Lib. Then the users enters 
an adjective and then a noun. Any characters can be accepted since English grammar allows for it.
For example, integer numbers are at times a noun. The endpoint returns the user's selected Mad Lib 
according to the topic typed, with filled in blanks for an adjective and noun.

/scrabble/{enter}
###### description: 
the user enters a single word that can be created in a Scrabble game. For example,
characters such as spaces, hyphens and numbers will yield an error message. The endpoint returns
the points earned for playing that entered word in a game of Scrabble.

/list/{typer}
###### description: 
the user enters one of the following for the {typer} item: noun, verb, adjective,
adverb. Hence, only letters should be entered. It returns a string telling the user to check out 
a specific website that can give them a list of words depending on what the user entered.
