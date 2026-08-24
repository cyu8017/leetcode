<?php
// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

class Solution {
    private function modPowP($a, $e, $p) {
        $r = 1;
        while ($e > 0) {
            if ($e % 2 === 1) $r = $r * $a % $p;
            $a = $a * $a % $p;
            $e = intdiv($e, 2);
        }
        return $r;
    }

    private function modInvPrime($a, $p) {
        return $this->modPowP($a, $p - 2, $p);
    }

    private function binomMod($n, $k, $p) {
        if ($k < 0 || $k > $n) return 0;
        $num = 1;
        $den = 1;
        for ($i = 0; $i < $k; $i++) {
            $num = $num * ($n - $i) % $p;
            $den = $den * ($i + 1) % $p;
        }
        return $num * $this->modInvPrime($den, $p) % $p;
    }

    private function crt($a1, $m1, $a2, $m2) {
        for ($x = 0; $x < $m1 * $m2; $x++) {
            if ($x % $m1 === $a1 && $x % $m2 === $a2) return $x;
        }
        return 0;
    }

    private function binomMod10($n, $k) {
        return $this->crt($this->binomMod($n, $k, 2), 2, $this->binomMod($n, $k, 5), 5);
    }

    private function combineDigit($s, $offset) {
        $n = strlen($s);
        $sum = 0;
        for ($i = 0; $i <= $n - 2; $i++) {
            $sum = ($sum + $this->binomMod10($n - 2, $i) * (ord($s[$i + $offset]) - 48)) % 10;
        }
        return $sum;
    }

    function hasSameDigits($s) {
        return $this->combineDigit($s, 0) === $this->combineDigit($s, 1);
    }
}
