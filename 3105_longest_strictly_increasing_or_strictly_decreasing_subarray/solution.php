<?php
// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution {
    function longestMonotonicSubarray($nums) {
        $ans = 1;
        $t = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] < $nums[$i]) {
                $t++;
                $ans = max($ans, $t);
            } else $t = 1;
        }
        $t = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] > $nums[$i]) {
                $t++;
                $ans = max($ans, $t);
            } else $t = 1;
        }
        return $ans;
    }
}
