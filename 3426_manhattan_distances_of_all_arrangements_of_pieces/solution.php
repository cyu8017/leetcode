<?php
// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    private $mod = 1000000007;

    private function modPow($a, $e) {
        $r = 1;
        $base = $a % $this->mod;
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

    function distanceSum($m, $n, $k) {
        $mod = $this->mod;
        if ($k < 2) return 0;
        $totalCells = $m * $n;
        $pairChoose = $this->comb($totalCells - 2, $k - 2);
        $sumDist = 0;
        for ($d = 1; $d < $m; $d++) $sumDist += $d * ($m - $d) * $n * $n;
        for ($d = 1; $d < $n; $d++) $sumDist += $d * ($n - $d) * $m * $m;
        return ($sumDist % $mod) * $pairChoose % $mod;
    }
}
