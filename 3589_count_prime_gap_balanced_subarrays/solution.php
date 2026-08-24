<?php
// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

class Solution {
    function primeSubarray($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $isPrime = array_fill(0, $mx + 1, false);
        for ($i = 2; $i <= $mx; $i++) $isPrime[$i] = true;
        for ($i = 2; $i * $i <= $mx; $i++)
            if ($isPrime[$i])
                for ($j = $i * $i; $j <= $mx; $j += $i) $isPrime[$j] = false;
        $n = count($nums);
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $primes = [];
            for ($r = $l; $r < $n; $r++) {
                if ($isPrime[$nums[$r]]) $primes[] = $nums[$r];
                if (count($primes) >= 2) {
                    $mn = $primes[0];
                    $mxp = $primes[0];
                    foreach ($primes as $p) {
                        $mn = min($mn, $p);
                        $mxp = max($mxp, $p);
                    }
                    if ($mxp - $mn <= $k) $ans++;
                }
            }
        }
        return $ans;
    }
}
