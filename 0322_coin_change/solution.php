<?php
// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

class Solution {
    /**
     * @param Integer[] $coins
     * @param Integer $amount
     * @return Integer
     */
    function coinChange($coins, $amount) {
        $maxValue = $amount + 1;
        $dp = array_fill(0, $amount + 1, $maxValue);
        $dp[0] = 0;
        foreach ($coins as $coin) {
            for ($value = $coin; $value <= $amount; $value++) {
                $dp[$value] = min($dp[$value], $dp[$value - $coin] + 1);
            }
        }
        return $dp[$amount] === $maxValue ? -1 : $dp[$amount];
    }
}
