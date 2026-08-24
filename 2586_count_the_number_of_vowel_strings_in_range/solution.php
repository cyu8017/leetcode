<?php
// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
    function vowelStrings($words, $left, $right) {
        $isV = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $ans = 0;
        for ($i = $left; $i <= $right; $i++) {
            $w = $words[$i];
            if ($isV($w[0]) && $isV($w[strlen($w) - 1])) $ans++;
        }
        return $ans;
    }
}
