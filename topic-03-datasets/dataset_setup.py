import dataset

db = dataset.connect('sqlite:////home/Jaswanth434/mysite/Advanced-database-management/topic-03-datasets/shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'apples','quantity':'' },
        { "description": 'broccoli','quantity':''},
        { "description": 'pizza','quantity':'' },
        { "description": 'tangerine','quantity':''},
        { "description": 'potatoes','quantity':'' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()
