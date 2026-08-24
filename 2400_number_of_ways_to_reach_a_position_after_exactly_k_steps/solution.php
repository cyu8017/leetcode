<?php
// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution {
    function numberOfWays($startPos, $endPos, $k) {
        $mod = 1000000007;
        $diff = abs($endPos - $startPos);
        if ($diff > $k || ($k - $diff) % 2 !== 0) return 0;
        $r = intdiv($k + $diff, 2);
        return $this->comb($k, $r, $mod);
    }

    private function comb($n, $r, $mod) {
        if ($r < 0 || $r > $n) return 0;
        $num = 1;
        $den = 1;
        for ($i = 0; $i < $r; $i++) {
            $num = ($num * ($n - $i)) % $mod;
            $den = ($den * ($i + 1)) % $mod;
        }
        return ($num * $this->modPow($den, $mod - 2, $mod)) % $mod;
    }

    private function modPow($a, $e, $mod) {
        $res = 1;
        $base = $a % $mod;
        while ($e > 0) {
            if ($e & 1) $res = ($res * $base) % $mod;
            $base = ($base * $base) % $mod;
            $e >>= 1;
        }
        return $res;
    }
}
