<?php
// LeetCode 0209 - Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution {
    function minSubArrayLen($target, $nums) {
        $left = 0;
        $sum = 0;
        $best = PHP_INT_MAX;
        foreach ($nums as $right => $num) {
            $sum += $num;
            while ($sum >= $target) {
                $best = min($best, $right - $left + 1);
                $sum -= $nums[$left];
                $left++;
            }
        }
        return $best === PHP_INT_MAX ? 0 : $best;
    }
}
