import pymongo
from pymongo import MongoClient
coll1=[]
coll2=[]
a=[]
b=[]

def get_first_database():

    URL = "mongodb+srv://test:testaccess@cluster0.eu2qw.mongodb.net/sample_geospatial?retryWrites=true&w=majority"
    client = MongoClient(URL)
    return client['sample_geospatial']

def get_second_database():

    URL = "mongodb+srv://test:testaccess@cluster0.eu2qw.mongodb.net/sample_geospatial1?retryWrites=true&w=majority"
    client = MongoClient(URL)
    return client['sample_geospatial1']

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