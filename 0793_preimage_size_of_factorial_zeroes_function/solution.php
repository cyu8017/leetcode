<?php
// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
    /**
     * @param Integer $k
     * @return Integer
     */
    function preimageSizeFZF($k) {
        $zeros = function($n) {
            $z = 0;
            while ($n > 0) {
                $n = intdiv($n, 5);
                $z += $n;
            }
            return $z;
        };
        $firstGe = function($target) use ($zeros) {
            $lo = 0;
            $hi = 5 * $target + 5;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($zeros($mid) >= $target) $hi = $mid;
                else $lo = $mid + 1;
            }
            return $lo;
        };
        return $firstGe($k + 1) - $firstGe($k);
    }
}
