<?php
// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution {
    function lengthOfLongestSubsequence($nums, $target) {
        $dp = array_fill(0, $target + 1, -1);
        $dp[0] = 0;
        foreach ($nums as $v)
            for ($s = $target; $s >= $v; $s--)
                if ($dp[$s - $v] >= 0 && $dp[$s - $v] + 1 > $dp[$s]) $dp[$s] = $dp[$s - $v] + 1;
        return $dp[$target];
    }
}
