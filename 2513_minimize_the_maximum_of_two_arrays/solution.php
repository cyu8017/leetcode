<?php
// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
    function minimizeSet($divisor1, $divisor2, $uniqueCnt1, $uniqueCnt2) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $lcm = intdiv($divisor1, $gcd($divisor1, $divisor2)) * $divisor2;
        $ok = function ($x) use ($divisor1, $divisor2, $lcm, $uniqueCnt1, $uniqueCnt2) {
            $a = $x - intdiv($x, $divisor1);
            $b = $x - intdiv($x, $divisor2);
            $both = $x - intdiv($x, $lcm);
            return $a >= $uniqueCnt1 && $b >= $uniqueCnt2 && $both >= $uniqueCnt1 + $uniqueCnt2;
        };
        $lo = 1;
        $hi = 1 << 62;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
