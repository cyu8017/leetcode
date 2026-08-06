<?php
class Solution {
    function numOfArrays($n, $m, $k) {
        $mod = 1000000007;
        $dp = array_fill(0, $k + 1, array_fill(0, $m + 1, 0));
        for ($maximum = 1; $maximum <= $m; $maximum++) $dp[1][$maximum] = 1;
        for ($len = 1; $len < $n; $len++) {
            $nxt = array_fill(0, $k + 1, array_fill(0, $m + 1, 0));
            for ($cost = 1; $cost <= $k; $cost++) {
                $prefix = 0;
                for ($maximum = 1; $maximum <= $m; $maximum++) {
                    $prefix = ($prefix + $dp[$cost - 1][$maximum - 1]) % $mod;
                    $nxt[$cost][$maximum] = ($maximum * $dp[$cost][$maximum] + $prefix) % $mod;
                }
            }
            $dp = $nxt;
        }
        return array_sum($dp[$k]) % $mod;
    }
}
