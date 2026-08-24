<?php
// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution {
    function findLHS($nums) {
        $counts = [];
        foreach ($nums as $num) $counts[$num] = ($counts[$num] ?? 0) + 1;
        $best = 0;
        foreach ($counts as $key => $value) {
            if (isset($counts[$key + 1])) $best = max($best, $value + $counts[$key + 1]);
        }
        return $best;
    }
}
