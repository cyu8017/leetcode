<?php
// LeetCode 3770 - Largest Prime from Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

class Solution {
    function largestPrime($n) {
        $MX = 500000;
        $isPrime = array_fill(0, $MX + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        $primes = [];
        for ($i = 2; $i <= $MX; $i++) {
            if ($isPrime[$i]) {
                $primes[] = $i;
                if ($i * $i <= $MX) {
                    for ($j = $i * $i; $j <= $MX; $j += $i) $isPrime[$j] = false;
                }
            }
        }
        $S = [0];
        $t = 0;
        foreach ($primes as $x) {
            $t += $x;
            if ($t > $MX) break;
            if ($isPrime[$t]) $S[] = $t;
        }
        $lo = 0;
        $hi = count($S);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($S[$mid] <= $n) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $S[$lo - 1];
    }
}
