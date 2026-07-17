<?php
// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
    /**
     * @param Integer $primeFactors
     * @return Integer
     */
    function maxNiceDivisors($primeFactors) {
        $mod = 1000000007;
        if ($primeFactors <= 3) {
            return $primeFactors;
        }
        if ($primeFactors % 3 === 0) {
            return $this->modPow(3, intdiv($primeFactors, 3), $mod);
        }
        if ($primeFactors % 3 === 1) {
            return ($this->modPow(3, intdiv($primeFactors, 3) - 1, $mod) * 4) % $mod;
        }
        return ($this->modPow(3, intdiv($primeFactors, 3), $mod) * 2) % $mod;
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
