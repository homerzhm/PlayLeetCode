"""

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3

"""

class TreeNote(object):
    def __init__(self, nodeValue, parentTreeNode):
        self.val = nodeValue
        self.prev = parentTreeNode
        if parentTreeNode != None:
            self.level = parentTreeNode.level + 1
        else:
            self.level = 0
        self.childNodes = []

    def addChildTreeNode(self, node):
        self.childNodes.append(node)

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        return self.solution1(start, end, bank)

    def __init__(self):
        self.topValueCache = {}
        self.bottomValueCache = {}
        self.currentCache = None

    def solution1(self, start, end, bank):

        if len(bank) == 0 or end not in bank:
            return -1

        topList = bank[:]
        botList = bank[:]

        startNode = TreeNote(start, None)
        endNode = TreeNote(end, None)

        topList.remove(end)
        botList.remove(end)

        self.currentCache = self.topValueCache
        self.composeTree(startNode, topList)

        self.currentCache = self.bottomValueCache
        self.composeTree(endNode, botList)

        if self.checkWhetherIsOnMutation(start, end):
            return 1
        elif len(startNode.childNodes) == 0 and len(endNode.childNodes) == 0:
            return -1

        smallestMuta = None
        for key in self.topValueCache:
            if key in self.bottomValueCache:
                if smallestMuta == None:
                    smallestMuta = self.topValueCache[key] + self.bottomValueCache[key]
                else:
                    if smallestMuta > self.topValueCache[key] + self.bottomValueCache[key]:
                        smallestMuta = self.topValueCache[key] + self.bottomValueCache[key]

        print self.topValueCache
        print self.bottomValueCache


        if smallestMuta == None:
            return -1
        else:
            return smallestMuta

    def composeTree(self, rootNode, data_set):

        needToRemove = []

        for i in range(0, len(data_set)):
            value = data_set[i]
            print "checking :", rootNode.val, " value:", value
            if self.checkWhetherIsOnMutation(value, rootNode.val):
                needToRemove.append(value)
                newNode = TreeNote(value, rootNode)
                if value in self.currentCache:
                    if self.currentCache[value] > newNode.level:
                        self.currentCache[value] = newNode.level
                else:
                    self.currentCache[value] = newNode.level

                rootNode.addChildTreeNode(newNode)

        for item in needToRemove:
            data_set.remove(item)

        for childNode in rootNode.childNodes:
            self.composeTree(childNode, data_set)



    def checkWhetherIsOnMutation(self, value1, value2):
        result = False
        count = 0
        for i in range(0, len(value1)):
            if value1[i] != value2[i]:
                count += 1
            if count > 1:
                break

        if count == 1:
            result = True
        return result

def main():

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]

    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    s = Solution()
    print s.minMutation(start, end, bank)

if __name__ == '__main__':
    main()