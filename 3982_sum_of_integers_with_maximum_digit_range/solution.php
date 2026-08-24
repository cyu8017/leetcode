<?php
// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

class Solution {
    function maxDigitRange($nums) {
        $mx = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $a = 10;
            $b = 0;
            for ($y = $x; $y > 0; $y = intdiv($y, 10)) {
                $v = $y % 10;
                $a = min($a, $v);
                $b = max($b, $v);
            }
            $r = $b - $a;
            if ($mx < $r) {
                $mx = $r;
                $ans = $x;
            } else if ($mx == $r) {
                $ans += $x;
            }
        }
        return $ans;
    }
}
