<?php
// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution {
    function vowelStrings($words, $queries) {
        $isV = function($c) {
            return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
        };
        $n = count($words);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i];
            $w = $words[$i];
            $len = strlen($w);
            if ($len > 0 && $isV($w[0]) && $isV($w[$len - 1])) $pref[$i + 1]++;
        }
        $ans = [];
        foreach ($queries as $q) {
            $ans[] = $pref[$q[1] + 1] - $pref[$q[0]];
        }
        return $ans;
    }
}
