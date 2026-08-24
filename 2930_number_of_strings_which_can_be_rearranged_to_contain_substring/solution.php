<?php
// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

class Solution {
    private $MOD = 1000000007;

    function stringCount($n) {
        if ($n < 4) return 0;
        $ans = $this->modPow(26, $n);
        $ans = ($ans - 3 * $this->modPow(25, $n) % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + 3 * $this->modPow(24, $n) % $this->MOD) % $this->MOD;
        $ans = ($ans - $this->modPow(23, $n) + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * $this->modPow(25, $n - 1) % $this->MOD) % $this->MOD;
        $ans = ($ans - 2 * ($n % $this->MOD) % $this->MOD * $this->modPow(24, $n - 1) % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * $this->modPow(23, $n - 1) % $this->MOD) % $this->MOD;
        $ans = ($ans - $n % $this->MOD * (($n - 1 + $this->MOD) % $this->MOD) % $this->MOD * $this->modPow(24, $n - 2) % $this->MOD % $this->MOD + $this->MOD) % $this->MOD;
        $ans = ($ans + $n % $this->MOD * (($n - 1 + $this->MOD) % $this->MOD) % $this->MOD * $this->modPow(23, $n - 2) % $this->MOD) % $this->MOD;
        return (int)$ans;
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= $this->MOD;
        while ($b > 0) {
            if ($b % 2 === 1) $res = ($res * $a) % $this->MOD;
            $a = ($a * $a) % $this->MOD;
            $b = intdiv($b, 2);
        }
        return $res;
    }
}
