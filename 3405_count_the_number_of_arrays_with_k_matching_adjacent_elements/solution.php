<?php
// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

class Solution {
    private $mod = 1000000007;

    private function modPow($a, $e) {
        $r = 1;
        $base = (($a % $this->mod) + $this->mod) % $this->mod;
        $mod = $this->mod;
        while ($e > 0) {
            if ($e & 1) $r = ($r * $base) % $mod;
            $base = ($base * $base) % $mod;
            $e >>= 1;
        }
        return $r;
    }

    private function comb($nn, $kk) {
        if ($kk < 0 || $kk > $nn) return 0;
        $num = 1;
        $den = 1;
        $mod = $this->mod;
        for ($i = 0; $i < $kk; $i++) {
            $num = ($num * ($nn - $i)) % $mod;
            $den = ($den * ($i + 1)) % $mod;
        }
        return ($num * $this->modPow($den, $mod - 2)) % $mod;
    }

    function countGoodArrays($n, $m, $k) {
        $mod = $this->mod;
        return ($this->comb($n - 1, $k) * $m % $mod * $this->modPow($m - 1, $n - 1 - $k) % $mod);
    }
}
