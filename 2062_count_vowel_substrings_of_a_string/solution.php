<?php
// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function countVowelSubstrings($word) {
        $isVowel = function ($c) { return strpos("aeiou", $c) !== false; };
        $ans = 0;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n && $isVowel($word[$j]); $j++) {
                $seen[$word[$j]] = true;
                if (count($seen) === 5) $ans++;
            }
        }
        return $ans;
    }
}
