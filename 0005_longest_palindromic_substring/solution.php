<?php
// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $bestStart = 0;
        $bestLen = 0;
        $n = strlen($s);

        $expand = function ($left, $right) use ($s, $n, &$bestStart, &$bestLen) {
            while ($left >= 0 && $right < $n && $s[$left] === $s[$right]) {
                $left--;
                $right++;
            }
            $len = $right - $left - 1;
            if ($len > $bestLen) {
                $bestLen = $len;
                $bestStart = $left + 1;
            }
        };

        for ($i = 0; $i < $n; $i++) {
            $expand($i, $i);
            $expand($i, $i + 1);
        }

        return substr($s, $bestStart, $bestLen);
    }
}
