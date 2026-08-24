<?php
// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution {
    function sumSubseqWidths($nums) {
        $MOD = 1000000007;
        sort($nums);
        $n = count($nums);
        $pow2 = array_fill(0, $n, 0);
        $pow2[0] = 1;
        for ($i = 1; $i < $n; $i++) $pow2[$i] = ($pow2[$i - 1] * 2) % $MOD;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = ($ans + $nums[$i] * ($pow2[$i] - $pow2[$n - 1 - $i])) % $MOD;
        }
        return ($ans + $MOD) % $MOD;
    }
}
