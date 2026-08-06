<?php
// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $target
     * @return Integer
     */
    function numRollsToTarget($n, $k, $target) {
        $mod = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;
        for ($dice = 0; $dice < $n; $dice++) {
            $new = array_fill(0, $target + 1, 0);
            for ($s = 0; $s <= $target; $s++) {
                if ($dp[$s] === 0) continue;
                for ($face = 1; $face <= $k; $face++) {
                    if ($s + $face <= $target) {
                        $new[$s + $face] = ($new[$s + $face] + $dp[$s]) % $mod;
                    }
                }
            }
            $dp = $new;
        }
        return $dp[$target];
    }
}
