<?php
// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function houseOfCards($n) {
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($k = 1; 3 * $k - 1 <= $n; $k++) {
            $cost = 3 * $k - 1;
            for ($j = $n; $j >= $cost; $j--) $dp[$j] += $dp[$j - $cost];
        }
        return $dp[$n];
    }
}
