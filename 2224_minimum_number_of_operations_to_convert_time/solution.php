<?php
// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution {
    function convertTime($current, $correct) {
        $toMin = function($t) {
            return (ord($t[0]) - 48) * 600 + (ord($t[1]) - 48) * 60
                + (ord($t[3]) - 48) * 10 + (ord($t[4]) - 48);
        };
        $diff = $toMin($correct) - $toMin($current);
        $ans = 0;
        foreach ([60, 15, 5, 1] as $step) {
            $ans += intdiv($diff, $step);
            $diff %= $step;
        }
        return $ans;
    }
}
