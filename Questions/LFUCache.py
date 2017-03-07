"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Test Case:
["LFUCache","put","put","get","put","get","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

"""

valueKey = "valueKey"
countKey = "countKey"
historyKey = "historyKey"

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity < 0:
            capacity = 0
        self.capacity = capacity
        self.cachedDic = {}
        self.operationCount = 0
        self.evitKeys = []

    def updateEvitKeys(self, key, isNew = False):
        if isNew:
            shouldReCreate = False
            for index in self.evitKeys:
                if self.cachedDic[index][countKey] != 1:
                    shouldReCreate = True
                    break
            if shouldReCreate:
                self.evitKeys = []
            self.evitKeys.append(key)
        else:
            for eKey in self.evitKeys:
                if eKey == key:
                    self.evitKeys.remove(eKey)
                    break
            if len(self.evitKeys) == 0:
                lowestKeyCount = None
                keysForLowestKeyCount = []
                for key in self.cachedDic.keys():
                    c = self.cachedDic[key]
                    if lowestKeyCount == None:
                        lowestKeyCount = c[countKey]
                        keysForLowestKeyCount.append(key)
                        continue
                    if c[countKey] < lowestKeyCount:
                        lowestKeyCount = c[countKey]
                        keysForLowestKeyCount = []
                        keysForLowestKeyCount.append(key)
                    elif c[countKey] == lowestKeyCount:
                        keysForLowestKeyCount.append(key)
                self.evitKeys = keysForLowestKeyCount

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cachedDic.has_key(key):
            self.operationCount += 1
            c = self.cachedDic[key]
            c[countKey] += 1
            c[historyKey] = self.operationCount
            self.updateEvitKeys(key)
            return c[valueKey]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        self.operationCount += 1
        if self.cachedDic.has_key(key):
            c = self.cachedDic[key]
            c[valueKey] = value
            c[countKey] += 1
            c[historyKey] = self.operationCount
            self.updateEvitKeys(key)
        else:
            if len(self.cachedDic.keys()) == self.capacity:
                theEvitKey = self.getKeyToEvicts()
                del self.cachedDic[theEvitKey]
                self.evitKeys.remove(theEvitKey)
            c = {}
            c[valueKey] = value
            c[countKey] = 1
            c[historyKey] = self.operationCount
            self.cachedDic[key] = c
            self.updateEvitKeys(key, isNew=True)

    def getKeyToEvicts(self):
        """
        :rtype: int
        """
        if len(self.evitKeys) > 1:
            theLeastRecentKey = None
            thePositionOfKey = None
            for key in self.evitKeys:
                c = self.cachedDic[key]
                if thePositionOfKey == None:
                    thePositionOfKey = c[historyKey]
                    theLeastRecentKey = key
                    continue
                if thePositionOfKey > c[historyKey]:
                    thePositionOfKey = c[historyKey]
                    theLeastRecentKey = key

            return theLeastRecentKey
        else:
            return self.evitKeys[0]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    operations = ["LFUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    inputs = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

    cache = LFUCache(inputs[0][0])

    for opIndex in range(1, len(operations)):
        op = operations[opIndex]
        data = inputs[opIndex]
        if op == "put":
            cache.put(data[0], data[1])
            print None
        elif op == "get":
            print cache.get(data[0])

    print cache.cachedDic

if __name__ == '__main__':
    main()