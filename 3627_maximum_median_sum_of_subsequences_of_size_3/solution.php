<?php
// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

class Solution {
    function maximumMedianSum($nums) {
        sort($nums);
        $n = count($nums);
        $ans = 0;
        for ($i = intdiv($n, 3); $i < $n; $i += 2) $ans += $nums[$i];
        return $ans;
    }
}
