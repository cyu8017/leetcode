<?php
// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

class Solution {
    function countTrapezoids($points) {
        $MOD = 1000000007;
        $cnt = [];
        foreach ($points as $p) {
            $y = $p[1];
            if (!isset($cnt[$y])) $cnt[$y] = 0;
            $cnt[$y]++;
        }
        $ans = 0;
        $pre = 0;
        foreach ($cnt as $c) {
            $lines = intdiv($c * ($c - 1), 2);
            $ans = ($ans + $pre * $lines) % $MOD;
            $pre = ($pre + $lines) % $MOD;
        }
        return $ans;
    }
}
