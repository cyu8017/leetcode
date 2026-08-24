<?php
// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

class Solution {
    function minimumCoins($prices) {
        $n = count($prices);
        $dp = array_fill(0, $n + 1, 1 << 30);
        $dp[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = $i; $j <= $n && $j <= $i + $i; $j++) {
                $cand = $dp[$i - 1] + $prices[$i - 1];
                if ($cand < $dp[$j]) $dp[$j] = $cand;
            }
        }
        return $dp[$n];
    }
}
