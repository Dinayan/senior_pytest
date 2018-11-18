import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

dbfile = open('people-pickle', 'wb')
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
pickle.dump(db, dbfile)
dbfile.close()
