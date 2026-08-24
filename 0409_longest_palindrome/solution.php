<?php
// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestPalindrome($s) {
        return $this->longest_palindrome($s);
    }

    /**
     * @param String $s
     * @return Integer
     */
    function longest_palindrome($s) {
        $counts = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if (!isset($counts[$char])) {
                $counts[$char] = 0;
            }
            $counts[$char]++;
        }

        $result = 0;
        $odd = false;
        foreach ($counts as $count) {
            $result += intdiv($count, 2) * 2;
            if ($count % 2 === 1) {
                $odd = true;
            }
        }

        return $result + ($odd ? 1 : 0);
    }
}
