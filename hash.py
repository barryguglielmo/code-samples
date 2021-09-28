class item:
    '''Simple Item That Will Be Stored In Our Hash Table'''
    def __init__(self, name, age, stuff):
        self.name = name
        self.age = age
        self.stuff = stuff
class hashtable:
    '''Simple Hash Table
        NOTE: No Defense for Collisions With This Example'''
    def __init__(self, length = 100):
        self.length = length
        self.table = [0]*length
    def hash_get(self, item):
        return self.table[hash(item.name)%self.length]
    def hash_get_loc(self, item):
        return hash(item.name)%self.length
    def hash_put(self, item):
        self.table[hash(item.name)%self.length] = item
# h = hashtable()
# i1 = item('Barry',30,{"dict":"stuff"})
# h.hash_put(i1)
# h.hash_get_loc(i1)
# h.table[45].name
