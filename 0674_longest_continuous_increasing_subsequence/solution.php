<?php
// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution {
    function findLengthOfLCIS($nums) {
        $best = 1;
        $cur = 1;
        for ($i = 1; $i < count($nums); ++$i) {
            if ($nums[$i] > $nums[$i - 1]) {
                ++$cur;
                $best = max($best, $cur);
            } else {
                $cur = 1;
            }
        }
        return $best;
    }
}
