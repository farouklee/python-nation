class  hashmap:
    def __init__(self):
        self.size =6
        self.map = [None] * self.size

    def _get_hash_(self, key):
        hash=0
        for char in str(key):
            hash+=ord(char)
        return hash%self.size

    def add(self, key, value):
        key_hash= self._get_hash_(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash]= list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair [0] == key:
                    pair[1]=value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash= self._get_hash_(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash =self._get_hash_(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0]==key:
                self.map[key_hash].pop(i)
                return True

    def printable(self):
        print ("contact")
        for item in self.map:
            if item is not None:
                print(str(item))


h= hashmap()
h.add('bolu', '08025250421')
h.add('lara', '08028504332')
h.add('lara','123456745')
h.add('olaolu', '08084484241')
h.add('waiz', '07080377094')
h.add('mum', '08035022141')
h.add('dad', '08023215637')
h.add('olaolu', '08011223347')
h.add('cool' , '07055663213')
#h.print()
temp= vars(h)
for items in temp:
    print(items)
#print(h)
h.delete('bolu')
print(hashmap)
#print(h)
#h.print()
print ('lara : ' + h.get('lara'))