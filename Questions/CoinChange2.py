"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self.fillMatrixSolution(amount, coins)

    def solution2(self, amount, coins):
        cache = [0] * (amount + 1)
        cache[0] = 1
        for i in coins:
            print "coin :", i
            for j in range(1, amount + 1):
                if j >= i:
                    cache[j] += cache[j - i]
                print "j:",j, " cache:", cache[j]
        return cache[amount]

    def fillMatrixSolution(self, amount, coins):

        # because there will be amout == 0 and no coin
        matrix = [[0 for x in  range(0, amount + 1)] for y in range(0, len(coins) + 1)]
        #if amount is 0, only 1 way
        for index in range(0, len(coins) + 1):
            matrix[index][0] = 1

        #if no coin, 0 ways
        for index in range(1, amount + 1):
            matrix[0][index] = 0


        for coinIndex in range(1, len(coins) + 1):
            for the_value in range(1, amount + 1):
                if coins[coinIndex - 1] <= the_value:
                    matrix[coinIndex][the_value] = matrix[coinIndex - 1][the_value] + matrix[coinIndex][the_value - coins[coinIndex - 1]]
                else:
                    matrix[coinIndex][the_value] = matrix[coinIndex - 1][the_value]

        for index in range(0, len(matrix)):
            print matrix[index]

        return matrix[len(coins)][amount]


    def solution1(self, amount, coins):
        coin_dic = {}
        itom_coin = {}
        sortedCoins = sorted(coins)
        result = 0
        processed = False
        for index in range(0, len(sortedCoins)):
            coinValue = sortedCoins[index]
            # first one, create Dic count for it
            if index == 0:
                coin_dic[coinValue] = 1
                itom_coin[coinValue] = 1
                continue
            # others, Do the coin Dic Initial.
            self.createDataByCoin(coin_dic, sortedCoins, index - 1, coinValue, True, itom_coin)
            if coinValue > amount:
                self.createDataByCoin(coin_dic, sortedCoins, index - 1, amount, False, itom_coin)
                result = coin_dic[amount]
                processed = True
                break
        print "coint Dic :", coin_dic
        if not processed:
            self.createDataByCoin(coin_dic, sortedCoins, len(sortedCoins) - 1, amount, False, itom_coin)
            result = coin_dic[amount]
        print "coint Dic finish :", coin_dic
        print "itom Dic finish :", itom_coin

        return result

    def createDataByCoin(self, coin_dic, sorted_coin, endIndex, the_value, is_value_belong, itom_coin):
        index = endIndex
        count = 0
        if is_value_belong == True:
            count = 1
        while index >= 0:
            coin_value = sorted_coin[index]

            number = the_value / coin_value
            modValue = the_value % coin_value

            cannotCombine = False
            print " the Value:",the_value, " Coin_value:", coin_value, " numbeR:", number, "  mod:", modValue
            if modValue > 0:
                if coin_dic.has_key(modValue):
                    if coin_dic[modValue] == 0:
                        cannotCombine = True
                else:
                    self.createDataByCoin(coin_dic, sorted_coin, endIndex - 1, modValue, False)
                    if coin_dic[modValue] == 0:
                        cannotCombine = True

            if not cannotCombine:
                if modValue > 0:
                    count += coin_dic[modValue]
                else:
                    count += 1

                if number > 0:
                    count += (number - 1) * (coin_dic[coin_value] - 1)
            index -= 1

        if count == 1 or (count == 2 and is_value_belong):
            itom_coin[the_value] = count
        coin_dic[the_value] = count


def main():
    testCaseParam1 = 15
    testCaseParam2 = [1, 2, 5]
    s = Solution()
    result = s.change(testCaseParam1, testCaseParam2)
    print "The Result : ", result
    pass


if __name__ == '__main__':
    main()
