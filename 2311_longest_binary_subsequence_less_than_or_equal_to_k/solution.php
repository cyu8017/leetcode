<?php
// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution {
    function longestSubsequence($s, $k) {
        $zeros = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $zeros++;
        $val = 0;
        $ones = 0;
        $pow = 1;
        for ($i = $n - 1; $i >= 0; --$i) {
            if ($s[$i] === '1') {
                if (!($pow > $k || $val + $pow > $k)) {
                    $val += $pow;
                    $ones++;
                }
            }
            if ($pow <= $k) {
                if ($pow > intdiv(PHP_INT_MAX, 2)) $pow = $k + 1;
                else $pow *= 2;
            }
        }
        return $zeros + $ones;
    }
}
