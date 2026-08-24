<?php
// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution {
    function maxSubarraySumCircular($nums) {
        $total = array_sum($nums);
        $maxSum = $nums[0];
        $minSum = $nums[0];
        $curMax = $nums[0];
        $curMin = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $curMax = max($nums[$i], $curMax + $nums[$i]);
            $curMin = min($nums[$i], $curMin + $nums[$i]);
            $maxSum = max($maxSum, $curMax);
            $minSum = min($minSum, $curMin);
        }
        if ($maxSum < 0) return $maxSum;
        return max($maxSum, $total - $minSum);
    }
}
