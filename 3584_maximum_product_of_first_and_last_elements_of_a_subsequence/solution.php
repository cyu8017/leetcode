<?php
// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

class Solution {
    function maximumProduct($nums, $m) {
        $ans = PHP_INT_MIN;
        $mx = PHP_INT_MIN;
        $mi = PHP_INT_MAX;
        $n = count($nums);
        for ($i = $m - 1; $i < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$i - $m + 1];
            $mi = min($mi, $y);
            $mx = max($mx, $y);
            $ans = max($ans, max($x * $mi, $x * $mx));
        }
        return $ans;
    }
}
