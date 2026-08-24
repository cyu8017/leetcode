<?php
// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function nthMagicalNumber($n, $a, $b) {
        $MOD = 1000000007;
        $gcd = function($x, $y) {
            while ($y !== 0) {
                $t = $x % $y;
                $x = $y;
                $y = $t;
            }
            return $x;
        };
        $lcm = intdiv($a, $gcd($a, $b)) * $b;
        $lo = 1;
        $hi = $n * min($a, $b);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if (intdiv($mid, $a) + intdiv($mid, $b) - intdiv($mid, $lcm) >= $n) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo % $MOD;
    }
}
