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
        self.endValue = None

    def solution1(self, start, end, bank):

        if len(bank) == 0 or end not in bank:
            return -1

        topList = bank[:]
        self.endValue = end
        startNode = TreeNote(start, None)

        self.composeTree(startNode, topList)

        if self.checkWhetherIsOnMutation(start, end):
            return 1
        elif len(startNode.childNodes) == 0 and len(endNode.childNodes) == 0:
            return -1

        if self.endValue in self.topValueCache:
            return self.topValueCache[self.endValue]
        else:
            return -1

    def composeTree(self, rootNode, data_set):

        needToRemove = []

        for i in range(0, len(data_set)):
            value = data_set[i]

            if self.checkWhetherIsOnMutation(value, rootNode.val):
                needToRemove.append(value)
                newNode = TreeNote(value, rootNode)
                rootNode.addChildTreeNode(newNode)
                #print "tree node :", value, " level :", newNode.level, " rootNode:", rootNode.val, " level:", rootNode.level
                if self.endValue == value:
                    if value in self.topValueCache:
                        #print "current Cache:", self.topValueCache[value]
                        if self.topValueCache[value] > newNode.level:
                            self.topValueCache[value] = newNode.level
                    else:
                        #print "current Cache:", newNode.level
                        self.topValueCache[value] = newNode.level

        for item in needToRemove:
            data_set.remove(item)

        new_data_set = data_set[:]
        for childNode in rootNode.childNodes:
            #print "composing childNode:", childNode.val, " level:", childNode.level
            self.composeTree(childNode, new_data_set)



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

    start = "AAAACCCC"
    end = "CCCCCCCC"
    bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]

    s = Solution()
    print s.minMutation(start, end, bank)

if __name__ == '__main__':
    main()