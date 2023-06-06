import pymongo
myclient = pymongo.MongoClient("Connection String Here")
db = myclient["flaskmongodb"]
#print(db.list_collection_names())
collection = db["Users"]
#counter = 0
#for document in collection.find({}): # İlk Sorgu
#     print(document)
#     counter+=1
#print(counter)

# myquery={"name":{"$regex":"Valeria ?"}} # Araştırıp bu şekilde yapıldığını öğrendim, sadece isminde Mary olan birini aratmak istedim.
# doc = collection.find(myquery)       # 2. Sorgu
# for i in doc:
#     print(i)

# myquery={"age":{"$gt":30}}            #3. Sorgu
# doc = collection.find(myquery)
# counter = 0
# liste = []
# for i in doc:
#     liste.append(i)
#     counter+=1
# print(liste[2]["age"])
 
# myquery = {"age":{"$gt":40}}         
# new_val = {"$set":{"description":"0"}}
# collection.update_many(myquery,new_val)  # 4. Sorgu
# cursor = collection.find({"description":"0"})
# counter = 0
# for i in cursor:
#      print(i)
#      counter+=1
# print(counter)

myquery={"age":{"$gte":42,"$lte":48}}            #5. Sorgu
collection.delete_many(myquery) # bundan önce sadece 9 adet veri vardı
doc = collection.find()
counter = 0
for i in doc:
     print(i)
     counter+=1
print(counter)

