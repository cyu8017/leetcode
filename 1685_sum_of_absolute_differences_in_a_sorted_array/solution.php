<?php
// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution {
    function getSumAbsoluteDifferences($nums) {
        $total = array_sum($nums);
        $left = 0;
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $ans[] = $x * $i - $left + ($total - $left - $x) - $x * ($n - $i - 1);
            $left += $x;
        }
        return $ans;
    }
}
