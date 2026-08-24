<?php
// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

class Solution {
    function countSubstrings($s) {
        $expand = function($left, $right) use ($s) {
            $count = 0;
            $n = strlen($s);
            while ($left >= 0 && $right < $n && $s[$left] === $s[$right]) {
                ++$count;
                --$left;
                ++$right;
            }
            return $count;
        };
        $total = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ++$i) {
            $total += $expand($i, $i);
            $total += $expand($i, $i + 1);
        }
        return $total;
    }
}
