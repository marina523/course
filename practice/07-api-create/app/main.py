#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # zone apex
def read_root():
    return {"Welcome to my DS3002 project!"}

@app.get("/count/{word1}/{word2}")  #tells you how many letters are in two words combined
def add_me(word1: str, word2: str):
    if word1.isalpha() and word2.isalpha():
        len1=len(word1)
        len2=len(word2)
        sum = len1+len2
        return {"letter count": sum}
    else:
        return {"error": "Only letters are allowed. For example, make sure you did not insert a space, hyphen, number, etc."}
        

@app.get("/descriptiveword/{adj_num}/{noun_num}")  #outputs an adjective and noun
def describing_words(adj_num: str, noun_num: str):
    if adj_num.isdecimal():
        adj_num=int(adj_num)
        if noun_num.isdecimal():
            noun_num=int(noun_num)
            noun_r=open('nouns.txt')
            noun=noun_r.readlines()
            if noun_num > 135 or adj_num<1 or adj_num > 135 or noun_num<1:
                return {"error": "You're two values should be integers between 1 and 135"}
            noun_v=noun[noun_num-1]
            adj_r=open('adjectives.txt')
            adj=adj_r.readlines()
            adj_v=adj[adj_num-1]
            return {"adjective": adj_v.rstrip('\n').lower(), "noun":noun_v.rstrip('\n').lower()}
        else: 
            return {"error": "Only numbers allowed, specifically between 0 and 135"}
    else: 
        return {"error": "Only numbers allowed, specifically between 0 and 135"}
        
@app.get("/madlibs/{topic}/{adjective}/{noun}")  #choice of 3 madlibs using an adjective and noun
def reading_words(topic: str, adjective: str, noun: str):
    topic=topic.lower()
    if (topic=="zoo"):
        string="Today I went to the zoo. I saw a(n) __adjective__ __noun__ jumping up and down in its tree."
        choice1=string.replace("adjective",adjective)
        choice=choice1.replace("noun",noun)
        return {"Filled in Mad Libs": choice}
    elif (topic=="park"):
        string="Today, my fabulous camp group went to a (an) __adjective__ amusement park. It was a fun park with a cool __noun__."
        choice1=string.replace("adjective",adjective)
        choice=choice1.replace("noun",noun)
        return {"Filled in Mad Libs": choice}
    elif (topic=="clothing"):
        string="I wore a blue and white striped, long sleeve __noun__ with a collar on it, a red tie, dark gray pants, white socks, black shoes, and a(n) __adjective__ hat."
        choice1=string.replace("adjective",adjective)
        choice=choice1.replace("noun",noun)
        return {"Filled in Mad Libs": choice}
    else:
        return {"The first item you're entering should be one of three options: zoo, park, clothing. Do not put anything extra (for example, do not add any quotation marks or commas)."}

@app.get("/scrabble/{enter}")  #returns the total points dedicated to a word from Scrabble
def scrabble_words(enter: str):
    if enter.isalpha():
        one_letter_point = ['e', 'a', 'o', 't', 'i', 'n', 'r', 's', 'l', 'u']
        two_letter_point = ['d', 'g']
        three_letter_point = ['c', 'm', 'b', 'p']
        four_letter_point = ['h', 'f', 'w', 'y', 'v']
        five_letter_point = ['k']
        eight_letter_point = ['j', 'x']
        ten_letter_point = ['q', 'z']

        def scrabble_word_count(userword):
            total = 0
            for letter in userword:
                if letter in one_letter_point:
                    total += 1
                elif letter in two_letter_point:
                    total += 2
                elif letter in three_letter_point:
                    total += 3
                elif letter in four_letter_point:
                    total += 4
                elif letter in five_letter_point:
                    total += 5
                elif letter in eight_letter_point:
                    total += 8
                elif letter in ten_letter_point:
                    total += 10
            return total
        ans=scrabble_word_count(enter)
        return {"Points": ans}
    else:    
        return {"You should only input characters that are possible in Scrabble. For example, no spaces or numbers, etc."}

@app.get("/list/{typer}")  #returns a string link address to find a list of either verbs, nouns, adjectives or adverbs
def read_root(typer: str):
    typer=typer.lower()
    if (typer=="verb"):
        return {"check out this page: http://esl180.com/files/VERBS_REGULAR_Numbered_with_instuctions_Yelllow_background_636_2.0.pdf"}
    elif (typer=="noun"):
        return {"check out this page: https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx"}
    elif (typer=='adjective'):
        return {"check out this page: https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html"}
    elif (typer=='adverb'):
        return {"check out this page: https://grammar.yourdictionary.com/parts-of-speech/adverbs/list-of-100-adverbs.html"}
    else:
        return {"Please enter one of four options: verb, noun, adjective, adverb. Do not put anything extra (for example, do not add any quotation marks or commas)."}

    