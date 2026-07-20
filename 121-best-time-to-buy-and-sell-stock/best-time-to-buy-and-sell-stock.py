class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):

            current_price = prices[i]

            if current_price < min_price:
                min_price = current_price

            else:
                profit = current_price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit
        