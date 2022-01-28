from http import client
import pymongo
from pymongo import MongoClient
coll1=[]
coll2=[]
a=[]
b=[]

firstUrl = input("Paste and edit your first url = ")
secondUrl = input("Paste and edit your second url = ")

i = firstUrl.index("/", 20, len(firstUrl)-1)+1
for x in firstUrl:
    if x == "?":
        c = firstUrl.index(x)
firstDbName = firstUrl[i:c]

j = secondUrl.index("/", 20, len(secondUrl)-1)+1
for y in secondUrl:
    if y == "?":
        c = secondUrl.index(y)
secondDbName = secondUrl[j:c]

def database():
    client1 = MongoClient(firstUrl)
    client2 = MongoClient(secondUrl)
    return client1[firstDbName], client2[secondDbName]

client1, client2 = database()

if __name__ == "__main__":
    for coll in client1.list_collection_names():
        coll1.append(coll)
    for coll in client2.list_collection_names():
        coll2.append(coll)
    if coll1 == coll2:
        print("The databases match")
        for x in range(len(coll1)):
            first_collection_name = client1[str(coll1[x])]
            second_collection_name = client2[str(coll2[x])]
            first_item_details = first_collection_name.find()
            second_item_details = second_collection_name.find()
            for first_item in first_item_details:
                a.append(first_item)
            for second_item in second_item_details:
                b.append(second_item)
            print(True) if a == b else print(False)
            print(x+1 , "collections matchs too")
            
    else:
        print("The database does not match")