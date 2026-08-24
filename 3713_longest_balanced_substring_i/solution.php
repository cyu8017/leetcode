<?php
// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

class Solution {
    function longestBalanced($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 26, 0);
            $mx = 0;
            $v = 0;
            for ($j = $i; $j < $n; $j++) {
                $c = ord($s[$j]) - 97;
                $cnt[$c]++;
                if ($cnt[$c] === 1) $v++;
                $mx = max($mx, $cnt[$c]);
                if ($mx * $v === $j - $i + 1) $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
