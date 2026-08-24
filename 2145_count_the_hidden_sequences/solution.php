<?php
// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

class Solution {
    /**
     * @param Integer[] $differences
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function numberOfArrays($differences, $lower, $upper) {
        $cur = 0;
        $mn = 0;
        $mx = 0;
        foreach ($differences as $d) {
            $cur += $d;
            $mn = min($mn, $cur);
            $mx = max($mx, $cur);
        }
        $res = ($upper - $lower) - ($mx - $mn) + 1;
        return $res < 0 ? 0 : $res;
    }
}
