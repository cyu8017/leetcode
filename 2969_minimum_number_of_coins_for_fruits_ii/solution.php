<?php
// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

class Solution {
    function minimumCoins($prices) {
        $n = count($prices);
        $dp = array_fill(0, $n + 1, 1 << 30);
        $dp[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = $i; $j <= $n && $j <= 2 * $i; $j++) {
                $dp[$j] = min($dp[$j], $dp[$i - 1] + $prices[$i - 1]);
            }
        }
        return $dp[$n];
    }
}
