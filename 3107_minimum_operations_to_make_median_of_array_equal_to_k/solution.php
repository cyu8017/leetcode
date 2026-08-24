<?php
// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution {
    function minOperationsToMakeMedianK($nums, $k) {
        sort($nums);
        $n = count($nums);
        $m = $n >> 1;
        $ans = abs($nums[$m] - $k);
        if ($nums[$m] > $k) {
            for ($i = $m - 1; $i >= 0 && $nums[$i] > $k; $i--) $ans += $nums[$i] - $k;
        } else {
            for ($i = $m + 1; $i < $n && $nums[$i] < $k; $i++) $ans += $k - $nums[$i];
        }
        return $ans;
    }
}
