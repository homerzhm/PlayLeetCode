"""
There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
"""

import math

# good explaination: https://discuss.leetcode.com/topic/67482/solution-with-detailed-explanation

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return self.solution1(buckets, minutesToDie, minutesToTest)

    def solution1(self, buckets, minutesToDie, minutesToTest):

        number_of_try = math.floor(minutesToTest / minutesToDie)

        #maximum = buckets/number_of_try + buckets%number_of_try

        print number_of_try

        number_of_pig = math.ceil(math.log(buckets, number_of_try + 1))

        return int(number_of_pig)

    #     number_of_try = minutesToTest / minutesToDie
    #
    #     spliteCount = 2
    #     currentMinimumTry = None
    #
    #     while 1:
    #         pigs = self.numberOfPigs(buckets, spliteCount, number_of_try)
    #         print "pigs:", pigs, " splite Count:", spliteCount
    #         if currentMinimumTry == None:
    #             currentMinimumTry = pigs
    #         else:
    #             if currentMinimumTry >= pigs:
    #                 currentMinimumTry = pigs
    #             else:
    #                 break
    #         spliteCount += 1
    #     print "minimum pigs:", currentMinimumTry, " splite Count:", spliteCount - 1
    #     return currentMinimumTry
    #
    # def numberOfPigs(self, buckets, spliteCount, numberOfTry):
    #
    #     remaining = buckets
    #     for i in range(0, numberOfTry - 1):
    #         remaining = remaining/spliteCount + remaining%spliteCount
    #
    #
    #     if remaining < spliteCount - 1:
    #         remaining = spliteCount - 1
    #     print "Remaining :", remaining, " number of try:", numberOfTry
    #     return remaining + numberOfTry - 1




def main():
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 30
    s = Solution()

    print "Result:", s.poorPigs(buckets, minutesToDie, minutesToTest)


if __name__ == '__main__':
    main()