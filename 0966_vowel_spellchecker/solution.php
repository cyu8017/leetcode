<?php
// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

class Solution {
    function spellchecker($wordlist, $queries) {
        $exact = array_fill_keys($wordlist, true);
        $lowerMap = [];
        $vowelMap = [];
        $devowel = function ($w) {
            return preg_replace('/[aeiou]/', '*', strtolower($w));
        };
        foreach ($wordlist as $w) {
            $low = strtolower($w);
            if (!array_key_exists($low, $lowerMap)) $lowerMap[$low] = $w;
            $dv = $devowel($w);
            if (!array_key_exists($dv, $vowelMap)) $vowelMap[$dv] = $w;
        }
        $ans = [];
        foreach ($queries as $q) {
            if (isset($exact[$q])) { $ans[] = $q; continue; }
            $low = strtolower($q);
            if (array_key_exists($low, $lowerMap)) { $ans[] = $lowerMap[$low]; continue; }
            $dv = $devowel($q);
            if (array_key_exists($dv, $vowelMap)) { $ans[] = $vowelMap[$dv]; continue; }
            $ans[] = "";
        }
        return $ans;
    }
}
