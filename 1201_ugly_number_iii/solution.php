<?php
// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function nthUglyNumber($n, $a, $b, $c) {
        $gcd = function ($x, $y) use (&$gcd) {
            return $y === 0 ? $x : $gcd($y, $x % $y);
        };
        $lcm = fn($x, $y) => intdiv($x, $gcd($x, $y)) * $y;
        $ab = $lcm($a, $b); $ac = $lcm($a, $c); $bc = $lcm($b, $c);
        $abc = $lcm($ab, $c);
        $count = function ($x) use ($a, $b, $c, $ab, $ac, $bc, $abc) {
            return intdiv($x, $a) + intdiv($x, $b) + intdiv($x, $c)
                - intdiv($x, $ab) - intdiv($x, $ac) - intdiv($x, $bc) + intdiv($x, $abc);
        };
        $lo = 1; $hi = 2000000000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($count($mid) >= $n) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
