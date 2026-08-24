<?php
// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

class Solution {
    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPattern($pattern, $s) {
        $words = explode(" ", $s);
        if (strlen($pattern) !== count($words)) {
            return false;
        }
        $charToWord = [];
        $wordToChar = [];
        for ($index = 0; $index < strlen($pattern); $index++) {
            $char = $pattern[$index];
            $word = $words[$index];
            if (isset($charToWord[$char])) {
                if ($charToWord[$char] !== $word) {
                    return false;
                }
            } elseif (isset($wordToChar[$word])) {
                return false;
            } else {
                $charToWord[$char] = $word;
                $wordToChar[$word] = $char;
            }
        }
        return true;
    }
}
