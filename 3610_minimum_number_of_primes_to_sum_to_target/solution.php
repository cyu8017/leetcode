<?php
// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

class Solution {
    private static $primes = [];

    private function ensurePrimes() {
        if (count(self::$primes) > 0) return;
        $x = 2;
        while (count(self::$primes) < 1000) {
            $isPrime = true;
            foreach (self::$primes as $p) {
                if ($p * $p > $x) break;
                if ($x % $p === 0) { $isPrime = false; break; }
            }
            if ($isPrime) self::$primes[] = $x;
            $x++;
        }
    }

    function minNumberOfPrimes($n, $m) {
        $this->ensurePrimes();
        $Inf = intdiv(2147483647, 2);
        $f = array_fill(0, $n + 1, $Inf);
        $f[0] = 0;
        for ($pi = 0; $pi < $m; $pi++) {
            $x = self::$primes[$pi];
            for ($i = $x; $i <= $n; $i++)
                if ($f[$i - $x] + 1 < $f[$i]) $f[$i] = $f[$i - $x] + 1;
        }
        return $f[$n] < $Inf ? $f[$n] : -1;
    }
}
