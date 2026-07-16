<?php
// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

class Solution {
    /**
     * @param Integer $amount
     * @param Integer[] $coins
     * @return Integer
     */
    function change($amount, $coins) {
        $dp = array_fill(0, $amount + 1, 0);
        $dp[0] = 1;

        foreach ($coins as $coin) {
            for ($value = $coin; $value <= $amount; $value++) {
                $dp[$value] += $dp[$value - $coin];
            }
        }

        return $dp[$amount];
    }
}
