<?php
// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestArithSeqLength($nums) {
        $n = count($nums);
        $dp = array_fill(0, $n, []);
        $ans = 1;
        for ($j = 1; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                $d = $nums[$j] - $nums[$i];
                $dp[$j][$d] = ($dp[$i][$d] ?? 1) + 1;
                $ans = max($ans, $dp[$j][$d]);
            }
        }
        return $ans;
    }
}
