from pymongo import MongoClient

def init():
    client = MongoClient('localhost', 27017)
    db = client.sqw
    collectios = db.corp_info
    return db

def insert_detail(db, detail):
    db.my_collection.insert(detail)

def main():
    db = init()
    print(db.my_collection)
    print(db.name)
    db.my_collection.insert({'das': 212, 'dasdasda': 'sasasa'})
    for item in db.my_collection.find():
        print(item['das'])

if __name__ == '__main__':
    main()