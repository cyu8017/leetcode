// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $minimum = PHP_INT_MAX;
        $profit = 0;
        foreach ($prices as $price) {
            $minimum = min($minimum, $price);
            $profit = max($profit, $price - $minimum);
        }
        return $profit;
    }
}