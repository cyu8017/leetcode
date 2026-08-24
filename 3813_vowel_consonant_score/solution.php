<?php
// LeetCode 3813 - Vowel-Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

class Solution {
    function vowelConsonantScore($s) {
        $v = 0;
        $c = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (($ch >= 'a' && $ch <= 'z') || ($ch >= 'A' && $ch <= 'Z')) {
                $c++;
                if ($ch === 'a' || $ch === 'e' || $ch === 'i' || $ch === 'o' || $ch === 'u') $v++;
            }
        }
        $c -= $v;
        if ($c === 0) return 0;
        return intdiv($v, $c);
    }
}
