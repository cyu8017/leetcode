<?php
// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numPrimeArrangements($n) {
        $mod = 1000000007;
        $isPrime = function ($x) {
            if ($x < 2) return false;
            for ($d = 2; $d * $d <= $x; $d++) {
                if ($x % $d === 0) return false;
            }
            return true;
        };
        $primes = 0;
        for ($i = 1; $i <= $n; $i++) if ($isPrime($i)) $primes++;
        $fact = function ($x) use ($mod) {
            $ans = 1;
            for ($i = 2; $i <= $x; $i++) $ans = $ans * $i % $mod;
            return $ans;
        };
        return $fact($primes) * $fact($n - $primes) % $mod;
    }
}
