<?php
// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution {
    function longestBalanced($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $vis = [];
            $cnt = [0, 0];
            for ($j = $i; $j < $n; $j++) {
                if (!isset($vis[$nums[$j]])) {
                    $vis[$nums[$j]] = true;
                    $cnt[$nums[$j] & 1]++;
                }
                if ($cnt[0] === $cnt[1]) $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
