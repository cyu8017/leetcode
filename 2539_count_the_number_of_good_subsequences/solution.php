<?php
// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

class Solution {
    function countGoodSubsequences($s) {
        $MOD = 1000000007;
        $cnt = array_fill(0, 26, 0);
        $maxf = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
            if ($cnt[$idx] > $maxf) $maxf = $cnt[$idx];
        }
        $fact = array_fill(0, $maxf + 1, 0);
        $invFact = array_fill(0, $maxf + 1, 0);
        $modPow = function($a, $e) use ($MOD) {
            $res = 1;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        $fact[0] = 1;
        for ($i = 1; $i <= $maxf; $i++) $fact[$i] = $fact[$i - 1] * $i % $MOD;
        $invFact[$maxf] = $modPow($fact[$maxf], $MOD - 2);
        for ($i = $maxf; $i > 0; $i--) $invFact[$i - 1] = $invFact[$i] * $i % $MOD;
        $comb = function($n, $k) use ($fact, $invFact, $MOD) {
            if ($k < 0 || $k > $n) return 0;
            return $fact[$n] * $invFact[$k] % $MOD * $invFact[$n - $k] % $MOD;
        };
        $ans = 0;
        for ($k = 1; $k <= $maxf; $k++) {
            $ways = 1;
            for ($i = 0; $i < 26; $i++) {
                if ($cnt[$i] >= $k) $ways = $ways * (1 + $comb($cnt[$i], $k)) % $MOD;
            }
            $ans = ($ans + $ways - 1 + $MOD) % $MOD;
        }
        return $ans;
    }
}
