"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""


class Solution(object):
    def lengthLongestPath(self, input):
        return self.solution2(input)

    # not sure whether it is a good solution, it is short, but time complexity is not O(n), because all the operation of strings
    def solution2(self, input):
        maxlen = 0
        cache = {0:0}
        inputLines = input.split('\n')
        for line in inputLines:
            l = line.lstrip("\t")
            depth = len(line) - len(l)
            if "." in line:
                maxlen = max(maxlen, cache[depth] + len(l))
            else:
                cache[depth + 1] = cache[depth] + len(l) + 1

        return maxlen

    # holly.... how I write this hug solution......
    def solution1(self, input):
        lengthOfInput = len(input)
        i = 0
        tempSum = 0
        formerTreeLevel = ''
        currentTreeLevel = 'r'
        cache = {}
        resetTreeStart = 0
        currentMax = 0
        formerMax = 0

        isFile = 0

        while i < lengthOfInput:
            currentS = input[i]
            if currentS == '\n':
                if currentTreeLevel != 'r':
                    tempSum += 1 ## for \ in file path
                currentMax = tempSum
                cache[currentTreeLevel] = tempSum
                formerTreeLevel = currentTreeLevel
                currentTreeLevel = 'r'
                resetTreeStart = 1

            elif currentS == '\t':
               currentTreeLevel += 't'
            else:

                if currentS == '.':## it has to be file, then it counts
                    isFile = 1

                if len(formerTreeLevel) > 0 and len(formerTreeLevel) >= len(currentTreeLevel) and resetTreeStart:## means the level goes back'
                    if isFile == 1:
                        formerMax = max(formerMax, currentMax)
                    if currentTreeLevel == 'r':
                        tempSum = 0
                    else:
                        print 'user former:', cache[currentTreeLevel[:-1]], " current:", currentTreeLevel
                        tempSum = cache[currentTreeLevel[:-1]]
                    resetTreeStart = 0
                    isFile = 0

                tempSum += 1

            i += 1
            if i == lengthOfInput:
                if currentTreeLevel != 'r':
                    tempSum += 1
                cache[currentTreeLevel] = tempSum
                currentMax = tempSum
                if isFile == 1:
                    formerMax = max(formerMax, currentMax)

        return formerMax


def main():
    testCase = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    s = Solution()
    print s.lengthLongestPath(testCase)
    pass

if __name__ == '__main__':
    print len("dir/subdir2/file.ext")
    main()