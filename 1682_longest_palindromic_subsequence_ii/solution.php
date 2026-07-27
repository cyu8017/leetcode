<?php
// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

class Solution {
    function longestPalindromeSubseq($s) {
        $n = strlen($s);
        $dp = [];
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) {
                $dp[$i][$j] = array_fill(0, 26, 0);
            }
        }
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                for ($c = 0; $c < 26; $c++) {
                    $dp[$i][$j][$c] = max($dp[$i + 1][$j][$c], $dp[$i][$j - 1][$c]);
                }
                if ($s[$i] === $s[$j]) {
                    $c = ord($s[$i]) - 97;
                    $inner = 0;
                    if ($length > 2) {
                        for ($x = 0; $x < 26; $x++) {
                            if ($x !== $c) $inner = max($inner, $dp[$i + 1][$j - 1][$x]);
                        }
                    }
                    $dp[$i][$j][$c] = max($dp[$i][$j][$c], $inner + 2);
                }
            }
        }
        return max($dp[0][$n - 1]);
    }
}
