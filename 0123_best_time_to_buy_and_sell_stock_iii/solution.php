// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $buyOne = PHP_INT_MAX;
        $buyTwo = PHP_INT_MAX;
        $sellOne = 0;
        $sellTwo = 0;
        foreach ($prices as $price) {
            $buyOne = min($buyOne, $price);
            $sellOne = max($sellOne, $price - $buyOne);
            $buyTwo = min($buyTwo, $price - $sellOne);
            $sellTwo = max($sellTwo, $price - $buyTwo);
        }
        return $sellTwo;
    }
}