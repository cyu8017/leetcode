<?php
// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $difference
     * @return Integer
     */
    function longestSubsequence($arr, $difference) {
        $dp = [];
        $best = 0;
        foreach ($arr as $x) {
            $dp[$x] = ($dp[$x - $difference] ?? 0) + 1;
            $best = max($best, $dp[$x]);
        }
        return $best;
    }
}
