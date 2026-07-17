<?php
// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution {
    function minOperations($nums) {
        $ops = 0;
        $prev = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $value = $nums[$i];
            if ($value <= $prev) {
                $needed = $prev + 1;
                $ops += $needed - $value;
                $prev = $needed;
            } else {
                $prev = $value;
            }
        }
        return $ops;
    }
}
