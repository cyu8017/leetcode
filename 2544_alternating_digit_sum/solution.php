<?php
// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
    function alternateDigitSum($n) {
        $digits = [];
        $x = $n;
        while ($x > 0) {
            $digits[] = $x % 10;
            $x = intdiv($x, 10);
        }
        $ans = 0;
        $sign = 1;
        for ($i = count($digits) - 1; $i >= 0; $i--) {
            $ans += $sign * $digits[$i];
            $sign = -$sign;
        }
        return $ans;
    }
}
