<?php
class Solution {
    function minDistance($houses, $k) {
        sort($houses);
        $n = count($houses);
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                $mid = $houses[intdiv($i + $j, 2)];
                $s = 0;
                for ($t = $i; $t <= $j; $t++) $s += abs($houses[$t] - $mid);
                $cost[$i][$j] = $s;
            }
        }
        $dp = array_fill(0, $n + 1, 10 ** 15);
        $dp[0] = 0;
        for ($mb = 0; $mb < $k; $mb++) {
            $ndp = array_fill(0, $n + 1, 10 ** 15);
            $ndp[0] = 0;
            for ($j = 1; $j <= $n; $j++) {
                for ($i = 0; $i < $j; $i++) {
                    $ndp[$j] = min($ndp[$j], $dp[$i] + $cost[$i][$j - 1]);
                }
            }
            $dp = $ndp;
        }
        return $dp[$n];
    }
}
