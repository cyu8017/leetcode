<?php
// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
    function smallestValue($n) {
        $sumPrimeFactors = function ($x) {
            $s = 0;
            for ($i = 2; $i * $i <= $x; $i++) {
                while ($x % $i === 0) {
                    $s += $i;
                    $x = intdiv($x, $i);
                }
            }
            if ($x > 1) $s += $x;
            return $s;
        };
        while (true) {
            $s = $sumPrimeFactors($n);
            if ($s === $n) return $n;
            $n = $s;
        }
    }
}
