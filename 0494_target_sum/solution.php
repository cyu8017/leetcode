<?php
// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function findTargetSumWays($nums, $target) {
        return $this->find_target_sum_ways($nums, $target);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function find_target_sum_ways($nums, $target) {
        $total = array_sum($nums);
        if (($total + $target) % 2 !== 0 || abs($target) > $total) {
            return 0;
        }
        $need = intdiv($total + $target, 2);
        $dp = array_fill(0, $need + 1, 0);
        $dp[0] = 1;
        foreach ($nums as $num) {
            for ($amount = $need; $amount >= $num; $amount--) {
                $dp[$amount] += $dp[$amount - $num];
            }
        }
        return $dp[$need];
    }
}
