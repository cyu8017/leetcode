<?php
// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

class Solution {
    function waysToDistribute($n, $k) {
        $mod = 1000000007;
        $dp = array_fill(0, $k + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = min($i, $k); $j >= 1; $j--) {
                $dp[$j] = ($dp[$j - 1] + $j * $dp[$j]) % $mod;
            }
            $dp[0] = 0;
        }
        return $dp[$k];
    }
}
