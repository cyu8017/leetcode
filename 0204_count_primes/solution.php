<?php
// LeetCode 0204 - Count Primes
// https://leetcode.com/problems/count-primes/

class Solution {
    function countPrimes($n) {
        if ($n <= 2) {
            return 0;
        }
        $isPrime = array_fill(0, $n, true);
        $isPrime[0] = false;
        $isPrime[1] = false;
        for ($p = 2; $p * $p < $n; $p++) {
            if ($isPrime[$p]) {
                for ($multiple = $p * $p; $multiple < $n; $multiple += $p) {
                    $isPrime[$multiple] = false;
                }
            }
        }
        return count(array_filter($isPrime));
    }
}
