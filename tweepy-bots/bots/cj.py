import tweepy
import time
import random
#sensitive keys kidden
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt' #stores id

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'help' in mention.full_text.lower():    #if found "help", returns tweet with guidance
            print('found', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    " " 'Some things you can say: last post? a vegan? a vegetarian? if you want a recommendation of vegetarian food from a continent, just tweet it (except Antarctica)', mention.id)
        if 'last' in mention.full_text.lower():
            timeline = api.home_timeline()
            line=[]
            aut=[]
            for tweetf in timeline:
                line.append(tweetf.text)
                aut.append(tweetf.user.name)
                auto=aut[0]
                writ=line[0]   #split up to get tweet on the timeline
                try:
                    api.update_status('@' + mention.user.screen_name + " "
                        f"{auto} said {writ}", mention.id)
                except:
                    pass
        if 'australia' in mention.full_text.lower():  #if  found "australia" , returns random vegetarian dish in Australia
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name + ans, mention.id)
        if 'europe' in mention.full_text.lower():  #if  found "europe" , returns random vegetarian dish in Europe
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name + ans, mention.id)
        if 'define vegan' in mention.full_text.lower():  #defines vegan 
            print('found', flush=True)
            api.update_status('@' + mention.user.screen_name + " " 'a person who does not eat any food derived from animals and who typically does not use other animal products.', mention.id)
        if 'define vegetarian' in mention.full_text.lower():   #defines vegetarian
            print('found', flush=True)
            api.update_status('@' + mention.user.screen_name + " " 'a person who does not eat meat, and sometimes other animal products, especially for moral, religious, or health reasons.', mention.id)
        if 'south america' in mention.full_text.lower():   #if  found "south america" , returns random vegetarian dish in South America
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name +  ans, mention.id)
        if 'north america' in mention.full_text.lower():   #if  found "north america" , returns random vegetarian dish in North America
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name + ans, mention.id)
        if 'asia' in mention.full_text.lower():   #if  found "asia" , returns random vegetarian dish in Asia
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name + ans, mention.id)
        if 'africa' in mention.full_text.lower():      #if  found "africa" , returns random vegetarian dish in Africa
            print('found', flush=True)
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
            api.update_status('@' + mention.user.screen_name + ans, mention.id)
        
        

while True:     #continues to do the reply_to_tweets function
    reply_to_tweets()
    time.sleep(15)
