<?php
// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution {
    private $mapping = [
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
    ];

    /**
     * @param String $digits
     * @return String[]
     */
    function letterCombinations($digits) {
        if ($digits === "") {
            return [];
        }

        $result = [];
        $path = "";

        $backtrack = function($index) use (&$backtrack, $digits, &$result, &$path) {
            if ($index === strlen($digits)) {
                $result[] = $path;
                return;
            }
            $letters = $this->mapping[(int)$digits[$index]];
            $len = strlen($letters);
            for ($i = 0; $i < $len; $i++) {
                $path .= $letters[$i];
                $backtrack($index + 1);
                $path = substr($path, 0, -1);
            }
        };

        $backtrack(0);
        return $result;
    }
}
