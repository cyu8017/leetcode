<?php
// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

class Solution {
    function beautifulSubstrings($s, $k) {
        $isVowel = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $v = 0;
            $c = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($isVowel($s[$j])) $v++;
                else $c++;
                if ($v === $c && ($v * $c) % $k === 0) $ans++;
            }
        }
        return $ans;
    }
}
