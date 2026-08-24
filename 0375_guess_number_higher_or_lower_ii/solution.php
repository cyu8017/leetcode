<?php
// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function getMoneyAmount($n) {
        return $this->get_money_amount($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function get_money_amount($n) {
        $dp = array_fill(0, $n + 2, array_fill(0, $n + 2, 0));

        for ($length = 2; $length <= $n; $length++) {
            for ($left = 1; $left <= $n - $length + 1; $left++) {
                $right = $left + $length - 1;
                $dp[$left][$right] = PHP_INT_MAX;
                for ($guess = $left; $guess < $right; $guess++) {
                    $cost = $guess + max($dp[$left][$guess - 1], $dp[$guess + 1][$right]);
                    $dp[$left][$right] = min($dp[$left][$right], $cost);
                }
            }
        }

        return $dp[1][$n];
    }
}
