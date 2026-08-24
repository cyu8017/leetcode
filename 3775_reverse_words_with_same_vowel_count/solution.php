<?php
// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution {
    function reverseWords($s) {
        $calc = function($w) {
            $cnt = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $c = $w[$i];
                if ($c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u') $cnt++;
            }
            return $cnt;
        };
        $words = preg_split('/\s+/', trim($s));
        $cnt = $calc($words[0]);
        $ans = $words[0];
        for ($i = 1; $i < count($words); $i++) {
            $w = $words[$i];
            if ($calc($w) === $cnt) $w = strrev($w);
            $ans .= ' ' . $w;
        }
        return $ans;
    }
}
