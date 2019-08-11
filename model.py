from pymongo import MongoClient

client = MongoClient()
db = client['amazon_valley']


def check_user(username):
	query = {'username':username}
	result = db['users'].find_one(query)
	return result

def add_user_to_db(user_info):
	db['users'].insert_one(user_info)
