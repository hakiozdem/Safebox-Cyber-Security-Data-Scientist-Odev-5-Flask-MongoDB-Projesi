from faker import Faker
import random
import pymongo

myclient = pymongo.MongoClient("Connection String Here")
db = myclient["flaskmongodb"]
#print(db.list_collection_names()) bir test ettim nolur nolmaz.
collection = db["Users"]
faker = Faker(["it_IT","en_US","es_ES"]) #maksat eğlence olsun, İspanyol, İtalyan Amerikan isimleri karışık :)
users = []
for i in range(50):
    name = faker.name()
    job = faker.job()
    age = random.randint(22,60) 
    user = {
        "_id":i,
        "name":name,
        "job":job,
        "age":age,
        "description":"1"
        }
    users.append(user)
    print("******************")
    print(name+"\n"+job+"\n"+str(age)+"\nDescription : 1 \n***************\nhas added to db")

collection.insert_many(users)
    