<?php
// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

class Solution {
    private static $MX = 500001;
    private static $MOD = 1000000007;
    private static $f = null;
    private static $g = null;
    private static $inited = false;

    function countValidSequences($n, $k) {
        $this->ensureInit();
        $ans = $this->comb($n - 1, $k - 1);
        if (($n + $k) % 2 == 0) {
            $ans = ($ans - $this->comb(intdiv($n + $k, 2) - 1, $k - 1) + self::$MOD) % self::$MOD;
        }
        return $ans;
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= self::$MOD;
        while ($b > 0) {
            if (($b & 1) != 0) $res = $res * $a % self::$MOD;
            $a = $a * $a % self::$MOD;
            $b >>= 1;
        }
        return $res;
    }

    private function ensureInit() {
        if (self::$inited) return;
        self::$inited = true;
        self::$f = array_fill(0, self::$MX, 0);
        self::$g = array_fill(0, self::$MX, 0);
        self::$f[0] = 1;
        self::$g[0] = 1;
        for ($i = 1; $i < self::$MX; $i++) {
            self::$f[$i] = self::$f[$i - 1] * $i % self::$MOD;
            self::$g[$i] = $this->modPow(self::$f[$i], self::$MOD - 2);
        }
    }

    private function comb($n, $k) {
        if ($k < 0 || $k > $n) return 0;
        return self::$f[$n] * self::$g[$k] % self::$MOD * self::$g[$n - $k] % self::$MOD;
    }
}
