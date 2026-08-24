<?php
// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution {
    function longestSubarray($nums) {
        $f = 2;
        $ans = $f;
        $n = count($nums);
        for ($i = 2; $i < $n; $i++) {
            if ($nums[$i] === $nums[$i - 1] + $nums[$i - 2]) {
                $f++;
                $ans = max($ans, $f);
            } else $f = 2;
        }
        return $ans;
    }
}
