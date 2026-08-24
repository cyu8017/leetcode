<?php
// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution {
    function answerQueries($nums, $queries) {
        sort($nums);
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) $nums[$i] += $nums[$i - 1];
        $qn = count($queries);
        $ans = array_fill(0, $qn, 0);
        for ($i = 0; $i < $qn; $i++) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($nums[$mid] <= $queries[$i]) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ans[$i] = $lo;
        }
        return $ans;
    }
}
