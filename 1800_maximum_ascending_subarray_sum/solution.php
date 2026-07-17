<?php
// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAscendingSum($nums) {
        $best = $nums[0];
        $cur = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $cur += $nums[$i];
            } else {
                $cur = $nums[$i];
            }
            $best = max($best, $cur);
        }
        return $best;
    }
}
