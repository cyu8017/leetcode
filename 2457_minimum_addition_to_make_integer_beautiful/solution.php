<?php
// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution {
    function makeIntegerBeautiful($n, $target) {
        $digitSum = function ($x) {
            $s = 0;
            while ($x > 0) {
                $s += $x % 10;
                $x = intdiv($x, 10);
            }
            return $s;
        };
        $orig = $n;
        $pow10 = 1;
        while ($digitSum($n) > $target) {
            $n = intdiv($n, 10) + 1;
            $pow10 *= 10;
        }
        return $n * $pow10 - $orig;
    }
}
