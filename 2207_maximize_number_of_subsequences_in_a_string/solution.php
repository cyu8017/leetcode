<?php
// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution {
    function maximumSubsequenceCount($text, $pattern) {
        $a = $pattern[0];
        $b = $pattern[1];
        $count = function($s) use ($a, $b) {
            $ca = 0;
            $ans = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $ch = $s[$i];
                if ($ch === $b) $ans += $ca;
                if ($ch === $a) $ca++;
            }
            return $ans;
        };
        return max($count($a . $text), $count($text . $b));
    }
}
