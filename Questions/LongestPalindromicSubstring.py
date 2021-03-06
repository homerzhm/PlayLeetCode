"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

"""

import math

class Solution(object):
    def longestPalindrome(self, s):

        return self.solution2_manacher_algorithm(s)

    def preprocessForString(self, string): # put prefix and postfix for abvoid dealing bonce
        result = "^#"
        for c in string:
            result += (c + "#")
        result += "$"
        return result

    def solution2_manacher_algorithm(self, s):
        processed = self.preprocessForString(s)
        centerIndex = 0
        rightBound = 0
        i = 1
        cached = {}
        print processed
        while i < len(processed) - 1:
            i_mirror = 2 * centerIndex - i
            cached[i] = min(rightBound - i, cached[i_mirror]) if rightBound > i else 0

            while (processed[i + 1 + cached[i]] == processed[i - 1 - cached[i]]):
                cached[i] += 1

            if i + cached[i] > rightBound:
                centerIndex = i
                rightBound = centerIndex + cached[i]
            i += 1
            print cached , " centerIndex:", centerIndex, " length:", cached[centerIndex]
        print cached
        theMaxLength = 0
        theMaxCenterIndex = 0
        for index in range(1, len(processed) - 1):
            if theMaxLength < cached[index]:
                theMaxLength = cached [index]
                theMaxCenterIndex = index

        print theMaxCenterIndex , '   center: ', processed[theMaxCenterIndex]
        return s[(theMaxCenterIndex - 1 - theMaxLength)/2: (theMaxCenterIndex - 1 - theMaxLength)/2 + theMaxLength]


    def checkIsPStringWithCenterString(self, mainString, centerIndex, offset):
        if offset + centerIndex >= len(mainString) or centerIndex - offset < 0:
            return False
        return mainString[offset + centerIndex] == mainString[centerIndex - offset]

    def checkIsPStingWithTwoCenterString(self, mainString, centerIndex, offset):# will always acent check
        if offset + centerIndex + 1 >= len(mainString) or centerIndex - offset < 0:
            return False
        return mainString[centerIndex - offset] == mainString[centerIndex + 1 + offset]

    def solution1(self, s):
        result = s[0]
        length = len(s)
        i = 0
        maxLengthOfHPString = math.floor(len(s) / 2)
        #print maxLengthOfHPString
        if maxLengthOfHPString == 0:
            return s
        while i < length:
            character = s[i]
            j = 1
            theOffset = 0
            if i + 1 < length and character == s[i + 1]:# two center
                if len(result) < 2:
                    result = s[i : i + 2]
                while j <= maxLengthOfHPString:
                    isP = self.checkIsPStingWithTwoCenterString(s, i, j)
                    if isP == False:
                        j -= 1
                        theOffset = j
                        break
                    theOffset = j
                    j += 1
                if theOffset > 0 and 2 + theOffset * 2 > len(result):
                    result = s[i - theOffset: i + 2 + theOffset]
                # if theOffset > 0:
                #     print "Found (2)center Index : ", i, " offset:", theOffset, ' foundresult:', s[i - theOffset: i + 2 + theOffset]
            #always check whether it is center string
            theOffset = 0
            j = 1
            while j <= maxLengthOfHPString:
                isP = self.checkIsPStringWithCenterString(s, i, j)
                if isP == False:
                    j -= 1
                    theOffset = j
                    break
                theOffset = j
                j += 1
            if theOffset > 0 and 1 + theOffset * 2 > len(result):
                result = s[i - theOffset: i + 1 + theOffset]
            # if theOffset > 0:
            #     print "Found (1)center Index : " , i , " offset:" , theOffset, ' foundresult:', s[i - theOffset: i + 1 + theOffset]
            # if len(result) > 0:
            #     print "maxResult:", result
            i += 1
        return result

def main():
    testCase = "babcbabcbaccba"#wabcbabcbabzba
    s = Solution()
    print "solution 2: " + s.solution2_manacher_algorithm(testCase)
    print "solution 1: " + s.solution1(testCase)
if __name__ == '__main__':
    main()