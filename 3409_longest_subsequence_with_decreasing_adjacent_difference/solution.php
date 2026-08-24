<?php
// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

class Solution {
    function longestSubsequence($nums) {
        $n = count($nums);
        $ans = 1;
        $dp = [];
        for ($i = 0; $i < $n; $i++) $dp[$i] = array_fill(0, 301, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $d = abs($nums[$i] - $nums[$j]);
                $best = 1;
                for ($pd = $d; $pd <= 300; $pd++) {
                    if ($dp[$j][$pd] > $best) $best = $dp[$j][$pd];
                }
                if ($best + 1 > $dp[$i][$d]) $dp[$i][$d] = $best + 1;
                if ($dp[$i][$d] > $ans) $ans = $dp[$i][$d];
            }
            if ($dp[$i][0] < 1) $dp[$i][0] = 1;
        }
        return $ans;
    }
}
