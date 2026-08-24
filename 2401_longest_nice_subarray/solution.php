<?php
// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

class Solution {
    function longestNiceSubarray($nums) {
        $used = 0;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            while (($used & $nums[$right]) !== 0) {
                $used ^= $nums[$left];
                $left++;
            }
            $used |= $nums[$right];
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
