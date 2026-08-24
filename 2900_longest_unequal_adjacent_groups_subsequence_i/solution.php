<?php
// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution {
    function getLongestSubsequence($words, $groups) {
        $ans = [$words[0]];
        $last = $groups[0];
        $n = count($words);
        for ($i = 1; $i < $n; $i++) {
            if ($groups[$i] !== $last) {
                $ans[] = $words[$i];
                $last = $groups[$i];
            }
        }
        return $ans;
    }
}
