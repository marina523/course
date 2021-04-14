#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import boto3

app = FastAPI()

# Model data you are expecting.
# Set defaults, data types, etc.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")  # zone apex
def read_root():
    return {"Welcome to my DS3002 project!"}

# Adds two integers as PATH parameters
@app.get("/count/{word1}/{word2}")
def add_me(word1: str, word2: str):
    try:
        for character in word1:
            if character.isdigit():
                return {"error": "Do not put a number in your word"}
        for characters in word2:
            if characters.isdigit():
                return {"error": "Do not put a number in your word"}
        len1=len(word1)
        len2=len(word2)
        sum = len1+len2
        return {"letter count": sum}
    except:
        return {"You should enter two words"}


# Introduce data types and defaults from the Optional library
@app.get("/descriptiveword/{adj_num}/{noun_num}")
def get_words(adj_num: int, noun_num: int):
    if adj_num > 135:
        return {"error": "Select an integer between 1 and 135"}
    else:
        noun_r=open('nouns.txt')
        noun=noun_r.readlines()
        noun_v=noun[noun_num-1]
        adj_r=open('adjectives.txt')
        adj=adj_r.readlines()
        adj_v=adj[adj_num-1]
        return {"adjective": adj_v.rstrip('\n'), "noun":noun_v.rstrip('\n')}



# Start using the "Item" BaseModel
# Post / Delete / Patch methods
@app.post("/items/{item_id}")
def add_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}

@app.delete("/items/{item_id}")
def delete_item(item_id: int, item: Item):
    return {"action": "deleted", "item_id": item_id}

@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: Item):
    return {"action": "patch", "item_id": item_id}

@app.get("/aws/s3")
def fetch_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response['Buckets']
    return {"buckets": buckets}
