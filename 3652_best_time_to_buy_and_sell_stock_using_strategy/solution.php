<?php
// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution {
    function maxProfit($prices, $strategy, $k) {
        $n = count($prices);
        $s = array_fill(0, $n + 1, 0);
        $t = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $s[$i] = $s[$i - 1] + $prices[$i - 1] * $strategy[$i - 1];
            $t[$i] = $t[$i - 1] + $prices[$i - 1];
        }
        $ans = $s[$n];
        for ($i = $k; $i <= $n; $i++)
            $ans = max($ans, $s[$n] - ($s[$i] - $s[$i - $k]) + ($t[$i] - $t[$i - intdiv($k, 2)]));
        return $ans;
    }
}
