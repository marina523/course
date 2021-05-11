
#!/usr/bin/env python
import tweepy
import time
import random
# Authenticate to Twitter
FILE_NAME = 'last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = str(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id( last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
CONSUMER_KEY = 'yXI09sPx3CSr0omvH7oT6yavU'
CONSUMER_SECRET = 'lm9nrA5pL2Xf9n2NoOJlid2fXA9vt0uCDX12trCZvlheSywr1I'
ACCESS_TOKEN = '1390884054317342721-ifWzBdqZiMsCoeTuSTlIcbcNoxo9NA'
ACCESS_TOKEN_SECRET = 'VHKoL1Nu6b1RWh6WWH4z3XCkHEFn97sQ5STxLfoardjYn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)

#mentions=api.mentions_timeline()
#for mention in mentions:
    #print(str(mention.id) + '-' + mention.text)
    #if 'support' in mention.text.lower():
        #print('found')
        #print('respondin')


def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    tweets = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for tweet in reversed(tweets):
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'support' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            api.update_status('@' + tweet.user.screen_name +
                    'Some things you can say: last post? a vegan? a vegetarian? if you want a recommendation of veetarian food from a continent, just tweet it (except Antarctica)', tweet.id)

            
        elif 'last' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            timeline = api.home_timeline()
            for tweetf in timeline:
                api.update_status(f"{tweetf.user.name} said {tweetf.text}", tweet.id)
                
                
        elif 'australia' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['Vegetarian sausage rolls',
            'Mushroom sliders with pickled fennel and harissa creme fraiche',
            'Eggplant parmigiana "meatball" subs',
            'Harissa haloumi burgers with mint mayonnaise',
            'Vegetable skewers with parsley and cashew pesto',
            'Roasted sticky tofu buns',
            'Eggplant and mushroom pasta pot pies',
            'Smoked tofu salad with peanut dressing',
            'Roasted capsicum and labne salad',
            'Broccoli steaks with quinoa and ricotta']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)
        elif 'europe' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['French Lentils and Kale',
            'Avocat Tartine',
            'Vegan Spaghetti Bolognese',
            'Classic Minestrone',
            'Vegan Paella',
            'Patatas Bravas',
            'Spanish Potato Tortilla',
            'Spanish Croquettes',
            'Gazpacho',
            'Vegan Tzatziki']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)
        elif 'define vegan' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            api.update_status('a person who does not eat any food derived from animals and who typically does not use other animal products.', tweet.id)
        elif 'define vegetarian' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            api.update_status('a person who does not eat meat, and sometimes other animal products, especially for moral, religious, or health reasons.', tweet.id)
        elif 'south america' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['Black Bean Chili',
            'Quinoa Pesto Salad',
            'Strawberry Salsa',
            'Fava Bean Cookies',
            'Tomatillo Salsa',
            'Quinoa Coconut and Coriander Salad',
            'Roasted Red Pepper Soup',
            'Sweet Potatoe Bread',
            'Chia Pudding',
            'Grilled Avocado with Black Bean Salsa']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)
        elif 'north america' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['Maque choux', 
            'Fried green tomatoe',
            'Avocado toast',
            'Caesar salad',
            'Tostones',
            'Platillo Moros y Cristiano',
            'Arroz verde',
            'Festival dumpling',
            'Arroz Rojo',
            'Arroz con huevo']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)
        elif 'asia' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['Rice Paper Rolls with Mango and Mint',
            'Vegan Thai Green Curry Soup',
            'Pineapple-Fried Rice',
            'Sesame Tofu Dumplings',
            'Vegan Bun Chay Vietnamese Noodle Salad',
            'Vegan Bibimbap',
            'Vegan Pad Thai',
            'Chickpea Curry with Potatoes',
            'Tofu Teriyaki Skewers',
            'Asian Salad with Ginger Sesame Dressing']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)
        elif 'africa' in tweet.full_text.lower():
            print(str(tweet.id) + '-' +  tweet.full_text)
            food=['West African Mango Overnight Oats',
            'Vegan Cornbread',
            'Nutmeg Plantain Pancakes',
            'East African Breakfast Wraps',
            'Ethiopian Spiced Red Lentils',
            'Ethiopian Collard Greens',
            'Chermoula-Spiced Karantita & Pomegranate Salad',
            'Curried Chickpea Stuffed Sweet Potatoes',
            'Atakilt Wat (Ethiopian Spiced Cabbage, Carrot & Potatoes)',
            'Spiced Cauliflower and Almond Soup']
            num=random.randint(1,10)
            index=food[num-1]
            ans=str(index)
            api.update_status(ans, tweet.id)     
        else:
            print(str(tweet.id) + '-' +  tweet.full_text)
            api.update_status('Some things you can say: last post? a vegan? a vegetarian? if you want a recommendation of veetarian food from a continent, just tweet it (except Antarctica)', tweet.id)  
while True:
    reply_to_tweets()
    time.sleep(14)