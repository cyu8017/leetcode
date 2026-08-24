<?php
// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution {
    /**
     * @param String[] $words
     * @return String
     */
    function firstPalindrome($words) {
        foreach ($words as $w) {
            $ok = true;
            for ($l = 0, $r = strlen($w) - 1; $l < $r; $l++, $r--) {
                if ($w[$l] !== $w[$r]) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) return $w;
        }
        return "";
    }
}
