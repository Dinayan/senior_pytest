from _senior_test_1.initdata import bob, sue,tom
import pickle
for key, value in [('bob', bob), ('sue', sue), ('tom', tom)]:
    recfile = open(key+'.pkl', 'wb')
    pickle.dump(value,recfile)
    recfile.close()
