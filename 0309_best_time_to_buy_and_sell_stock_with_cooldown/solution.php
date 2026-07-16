// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        if (empty($prices)) {
            return 0;
        }
        $free = 0;
        $hold = -$prices[0];
        $cooldown = 0;
        $count = count($prices);
        for ($index = 1; $index < $count; $index++) {
            $price = $prices[$index];
            $nextFree = max($free, $cooldown);
            $nextHold = max($hold, $free - $price);
            $nextCooldown = $hold + $price;
            $free = $nextFree;
            $hold = $nextHold;
            $cooldown = $nextCooldown;
        }
        return max($free, $cooldown);
    }
}
