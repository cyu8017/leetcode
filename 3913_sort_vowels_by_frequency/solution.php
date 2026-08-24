<?php
// LeetCode 3913 - Sort Vowels by Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

class Solution {
    function sortVowels($s) {
        $st = ['a' => true, 'e' => true, 'i' => true, 'o' => true, 'u' => true];
        $vowels = [];
        $cnt = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!isset($st[$c])) continue;
            if (!isset($cnt[$c])) { $vowels[] = $c; $cnt[$c] = 0; }
            $cnt[$c]++;
        }
        usort($vowels, function($a, $b) use (&$cnt) {
            return $cnt[$b] <=> $cnt[$a];
        });
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[] = $s[$i];
        $i = 0;
        for ($k = 0; $k < $n; $k++) {
            if (!isset($st[$s[$k]])) continue;
            $ch = $vowels[$i];
            $ans[$k] = $ch;
            $cnt[$ch]--;
            if ($cnt[$ch] === 0) $i++;
        }
        return implode('', $ans);
    }
}
