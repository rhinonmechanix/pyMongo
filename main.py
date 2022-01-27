import pymongo
from pymongo import MongoClient
coll1=[]
coll2=[]
a=[]
b=[]

firstUrl = input("Paste and edit your first url = ")
firstDbName = input("First DB Name = ")
secondUrl = input("Paste and edit your second url = ")
secondDbName = input("Second DB Name = ") 

def get_first_database():

    client = MongoClient(firstUrl)
    return client[firstDbName]

def get_second_database():

    client = MongoClient(secondUrl)
    return client[secondDbName]

if __name__ == "__main__":
    firstdb = get_first_database()
    seconddb = get_second_database()
    for coll in firstdb.list_collection_names():
        coll1.append(coll)
    for coll in seconddb.list_collection_names():
        coll2.append(coll)
    if coll1 == coll2:
        print("The databases match")
        for x in range(len(coll1)):
            first_collection_name = firstdb[str(coll1[x])]
            second_collection_name = seconddb[str(coll2[x])]
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