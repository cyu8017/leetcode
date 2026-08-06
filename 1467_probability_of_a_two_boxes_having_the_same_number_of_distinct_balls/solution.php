<?php
class Solution {
    function getProbability($balls) {
        $half = intdiv(array_sum($balls), 2);
        $good = 0;
        $total = 0;
        $comb = function($n, $k) {
            if ($k < 0 || $k > $n) return 0;
            $r = 1;
            for ($i = 0; $i < $k; $i++) $r = $r * ($n - $i) / ($i + 1);
            return $r;
        };
        $dfs = function($i, $left, $dl, $ways) use (&$dfs, &$good, &$total, $balls, $half, $comb) {
            if ($i === count($balls)) {
                if ($left === $half) {
                    $total += $ways;
                    if ($dl === 0) $good += $ways;
                }
                return;
            }
            for ($x = 0; $x <= $balls[$i]; $x++) {
                if ($left + $x <= $half) {
                    $dfs($i + 1, $left + $x, $dl + ($x > 0 ? 1 : 0) - ($x < $balls[$i] ? 1 : 0), $ways * $comb($balls[$i], $x));
                }
            }
        };
        $dfs(0, 0, 0, 1);
        return $good / $total;
    }
}
