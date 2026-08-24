<?php
// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
    function makeTheIntegerZero($num1, $num2) {
        $popcount = function($x) {
            $c = 0;
            while ($x > 0) {
                $c += $x & 1;
                $x = intdiv($x, 2);
            }
            return $c;
        };
        for ($k = 1; $k <= 60; $k++) {
            $rem = $num1 - $k * $num2;
            if ($rem < $k) continue;
            if ($popcount($rem) <= $k) return $k;
        }
        return -1;
    }
}
