class Solution1:
    def max_profit(self, prices):
        max = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max:
                    max = profit
        return max


# Best Solution
class Solution2:
    def max_profit(self, prices):
        buy_price = prices[0]
        best_profit = 0
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > best_profit:
                best_profit = price - buy_price
        return best_profit