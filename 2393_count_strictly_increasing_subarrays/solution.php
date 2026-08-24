<?php
// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

class Solution {
    function countSubarrays($nums) {
        $ans = 0;
        $len = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $nums[$i] > $nums[$i - 1]) $len++;
            else $len = 1;
            $ans += $len;
        }
        return $ans;
    }
}
