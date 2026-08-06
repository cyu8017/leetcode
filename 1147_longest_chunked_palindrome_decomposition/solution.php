<?php
// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function longestDecomposition($text) {
        $n = strlen($text);
        $ans = 0;
        $i = 0;
        while ($i < $n - $i) {
            $found = false;
            $maxLen = intdiv($n - 2 * $i, 2);
            for ($length = 1; $length <= $maxLen; $length++) {
                if (substr($text, $i, $length) === substr($text, $n - $i - $length, $length)) {
                    $ans += 2;
                    $i += $length;
                    $found = true;
                    break;
                }
            }
            if (!$found) {
                $ans++;
                break;
            }
        }
        return $ans;
    }
}
