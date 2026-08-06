<?php
// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution {
    /**
     * @param Integer $p
     * @return Integer
     */
    function minNonZeroProduct($p) {
        $mod = 1000000007;
        $mx = (1 << $p) - 1;
        return (int)(($mx % $mod) * $this->modPow(($mx - 1) % $mod, (1 << ($p - 1)) - 1, $mod) % $mod);
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
