<?php
// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAbsoluteSum($nums) {
        $prefix = 0;
        $low = 0;
        $high = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            $low = min($low, $prefix);
            $high = max($high, $prefix);
        }
        return $high - $low;
    }
}
