<?php
// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

class Solution {
    function beautifulSubstrings($s, $k) {
        $isVowel = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $x = 1;
        while (($x * $x) % $k !== 0) $x++;
        $freq = [];
        $freq["0|0"] = 1;
        $bal = 0;
        $vowels = 0;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($isVowel($ch)) { $bal++; $vowels++; }
            else $bal--;
            $key = $bal . '|' . ($vowels % $x);
            $f = $freq[$key] ?? 0;
            $ans += $f;
            $freq[$key] = $f + 1;
        }
        return $ans;
    }
}
