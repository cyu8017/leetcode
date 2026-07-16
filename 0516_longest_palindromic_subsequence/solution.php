<?php
// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestPalindromeSubseq($s) {
        return $this->longest_palindrome_subseq($s);
    }

    /**
     * @param String $s
     * @return Integer
     */
    function longest_palindrome_subseq($s) {
        $length = strlen($s);
        $dp = array_fill(0, $length, array_fill(0, $length, 0));

        for ($index = $length - 1; $index >= 0; $index--) {
            $dp[$index][$index] = 1;
            for ($end = $index + 1; $end < $length; $end++) {
                if ($s[$index] === $s[$end]) {
                    $dp[$index][$end] = $dp[$index + 1][$end - 1] + 2;
                } else {
                    $dp[$index][$end] = max($dp[$index + 1][$end], $dp[$index][$end - 1]);
                }
            }
        }

        return $dp[0][$length - 1];
    }
}
