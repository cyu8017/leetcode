<?php
// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function countVowels($word) {
        $n = strlen($word);
        $ans = 0;
        for ($i = 0; $i < $n; $i++)
            if (strpos("aeiou", $word[$i]) !== false) $ans += ($i + 1) * ($n - $i);
        return $ans;
    }
}
