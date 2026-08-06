<?php
// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countGoodNumbers($n) {
        $mod = 1000000007;
        $even = intdiv($n + 1, 2);
        $odd = intdiv($n, 2);
        return ($this->modPow(5, $even, $mod) * $this->modPow(4, $odd, $mod)) % $mod;
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
