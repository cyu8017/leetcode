<?php
// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

class Solution {
    function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = $r * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $r;
    }

    function key($a, $b) {
        return $a . ',' . $b;
    }

    function countBalancedPermutations($num) {
        $mod = 1000000007;
        $cnt = array_fill(0, 10, 0);
        $sum = 0;
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            $d = ord($num[$i]) - 48;
            $cnt[$d]++;
            $sum += $d;
        }
        if ($sum % 2 === 1) return 0;
        $halfN = intdiv($n, 2);
        $halfS = intdiv($sum, 2);
        $fact = [1];
        $invF = [];
        for ($i = 1; $i <= $n; $i++) $fact[$i] = $fact[$i - 1] * $i % $mod;
        $invF[$n] = $this->modPow($fact[$n], $mod - 2, $mod);
        for ($i = $n; $i > 0; $i--) $invF[$i - 1] = $invF[$i] * $i % $mod;
        $dp = [];
        $dp[$this->key(0, 0)] = 1;
        for ($d = 0; $d <= 9; $d++) {
            $ndp = [];
            foreach ($dp as $st => $ways) {
                $parts = explode(',', $st);
                $used = intval($parts[0]);
                $s = intval($parts[1]);
                for ($take = 0; $take <= $cnt[$d]; $take++) {
                    $nu = $used + $take;
                    $ns = $s + $take * $d;
                    if ($nu > $halfN || $ns > $halfS) continue;
                    $w = $ways * $invF[$take] % $mod * $invF[$cnt[$d] - $take] % $mod;
                    $nk = $this->key($nu, $ns);
                    $ndp[$nk] = (($ndp[$nk] ?? 0) + $w) % $mod;
                }
            }
            $dp = $ndp;
        }
        $ans = $dp[$this->key($halfN, $halfS)] ?? 0;
        $ans = $ans * $fact[$halfN] % $mod * $fact[$n - $halfN] % $mod;
        for ($d = 0; $d <= 9; $d++) $ans = $ans * $fact[$cnt[$d]] % $mod;
        return $ans;
    }
}
