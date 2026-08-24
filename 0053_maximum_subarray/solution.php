<?php
// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubArray($nums) {
        $best = $nums[0];
        $current = $nums[0];

        for ($i = 1; $i < count($nums); $i++) {
            $current = max($nums[$i], $current + $nums[$i]);
            $best = max($best, $current);
        }

        return $best;
    }
}
