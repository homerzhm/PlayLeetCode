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

"""
    Using List Node
"""

class ListNode(object):
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

    def connectToNext(self, nextNode):
        #print "Connecting :", self.key, " to :", nextNode.key
        self.next = nextNode
        nextNode.prev = self

    def printItSelf(self):
        print "Key: " + self.key + " value:"+self.val

class LFUCache(object):

    def __init__(self, capacity):

        if capacity < 0:
            capacity = 0

        self.capcity = capacity

        #dic for store the head node for this frequency
        self.fdNodes = {}

        #place holder for list node structure
        self.header = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.header.connectToNext(self.tail)

        #dic for key to Node and frequency
        self.cachedDic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cachedDic:
            node, fre = self.cachedDic[key]
            self.cachedDic[key] = [node, fre + 1]
            #print "connecting tmp:", node.key
            tmpNode = ListNode(node.val, "tmp")
            self.cachedDic["tmp"] = [tmpNode, fre]
            node.prev.connectToNext(tmpNode)
            tmpNode.connectToNext(node.next)
            if self.fdNodes[fre].key == node.key:
                #print "update curret fre to tmp:",fre
                self.fdNodes[fre] = tmpNode

            self.moveNodeForward(node, fre + 1)
            #print "in get tmp prev:", tmpNode.prev.key, " tmp next:", tmpNode.next.key
            tmpNode.prev.connectToNext(tmpNode.next)
            self.removeKey("tmp")
            #need to update fdNodes Dic and the whole list node
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if self.capcity == 0:
            return

        if key in self.cachedDic:
            node, fre = self.cachedDic[key]
            node.val = value
            self.cachedDic[key] = [node, fre + 1]

            #print "connecting tmp:", node.key
            tmpNode = ListNode(node.val, "tmp")
            self.cachedDic["tmp"] = [tmpNode, fre]
            node.prev.connectToNext(tmpNode)
            tmpNode.connectToNext(node.next)
            if self.fdNodes[fre].key == node.key:
                self.fdNodes[fre] = tmpNode

            self.moveNodeForward(node, fre + 1)
            #print "tmp prev:", tmpNode.prev.key, " tmp next:", tmpNode.next.key
            tmpNode.prev.connectToNext(tmpNode.next)
            self.removeKey("tmp")
        else:
            if len(self.cachedDic.keys()) >= self.capcity:
                #need to evite LFU Key
                eviteNode = self.tail.prev
                # print "eviting:", self.cachedDic
                #print "evit Node:" , eviteNode.key, " count:", self.cachedDic[eviteNode.key]
                # print "hell,,,,,",self.header.next
                eviteNode.prev.connectToNext(self.tail)
                self.removeKey(eviteNode.key)

            newNode = ListNode(value, key)
            fre = 1
            self.cachedDic[key] = [newNode, fre]

            if fre in self.fdNodes:
                #print "creating new??", fre
                #print self.fdNodes[fre].key
                firstInFre = self.fdNodes[fre]

                preNode = firstInFre.prev

                preNode.connectToNext(newNode)
                newNode.connectToNext(firstInFre)
                self.fdNodes[fre] = newNode
            else:
                self.fdNodes[fre] = newNode
                prevNode = self.tail.prev
                prevNode.connectToNext(newNode)
                newNode.connectToNext(self.tail)
            pass

    def removeKey(self, key):
        #print "removing key:", key, " and fre:", self.cachedDic[key][1]
        fre = self.cachedDic[key][1]
        if fre in self.fdNodes and self.fdNodes[fre].key == key:
            #print "hit:", key, "fre :", fre
            firstNode = self.fdNodes[fre]
            if firstNode.next.key in self.cachedDic and self.cachedDic[firstNode.next.key][1] == fre:
                self.fdNodes[fre] = firstNode.next
            else:
                del self.fdNodes[fre]
        del self.cachedDic[key]

        pass

    def moveNodeForward(self, node, fre):
        #print "moving forward:", fre, " node:", node.key
        if fre in self.fdNodes:
            currentFirstNode = self.fdNodes[fre]
            #print "fre in the node:", currentFirstNode.key , " fre:", fre
            prevFN = currentFirstNode.prev
            prevFN.connectToNext(node)
            node.connectToNext(currentFirstNode)
            #print currentFirstNode.prev.key, " key:", currentFirstNode.key
            self.fdNodes[fre] = node
        else:
            #print  "new fre"
            self.fdNodes[fre] = node
            currentNextNode = self.fdNodes[fre - 1]
            prevCNN = currentNextNode.prev
            prevCNN.connectToNext(node)
            node.connectToNext(currentNextNode)
        pass

"""
    My Solution
"""

valueKey = "valueKey"
countKey = "countKey"
historyKey = "historyKey"

class LFUCache_Mine(object):

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
    operations = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    inputs = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    # operations = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
    # inputs = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

    cache = LFUCache(inputs[0][0])

    for opIndex in range(1, len(operations)):
        op = operations[opIndex]
        data = inputs[opIndex]
        if op == "put":
            cache.put(data[0], data[1])
            print None
            #print str(cache.cachedDic)

        elif op == "get":

            print cache.get(data[0])
            #print str(cache.cachedDic)

    print str(cache.cachedDic)

if __name__ == '__main__':
    main()