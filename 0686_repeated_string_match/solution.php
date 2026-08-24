<?php
// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

class Solution {
    function repeatedStringMatch($a, $b) {
        $repeats = intdiv(strlen($b) + strlen($a) - 1, strlen($a));
        $built = '';
        for ($i = 0; $i < $repeats; $i++) $built .= $a;
        if (strpos($built, $b) !== false) return $repeats;
        $built .= $a;
        if (strpos($built, $b) !== false) return $repeats + 1;
        return -1;
    }
}
