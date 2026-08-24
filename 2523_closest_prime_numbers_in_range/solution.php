<?php
// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution {
    function closestPrimes($left, $right) {
        $isPrime = array_fill(0, $right + 1, true);
        if ($right >= 0) $isPrime[0] = false;
        if ($right >= 1) $isPrime[1] = false;
        for ($i = 2; $i * $i <= $right; $i++) {
            if (!$isPrime[$i]) continue;
            for ($j = $i * $i; $j <= $right; $j += $i) $isPrime[$j] = false;
        }
        $primes = [];
        for ($i = $left; $i <= $right; $i++) if ($isPrime[$i]) $primes[] = $i;
        if (count($primes) < 2) return [-1, -1];
        $bestDiff = PHP_INT_MAX;
        $best = [-1, -1];
        $m = count($primes);
        for ($i = 0; $i + 1 < $m; $i++) {
            $d = $primes[$i + 1] - $primes[$i];
            if ($d < $bestDiff) {
                $bestDiff = $d;
                $best = [$primes[$i], $primes[$i + 1]];
            }
        }
        return $best;
    }
}
