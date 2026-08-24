<?php
// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

class Solution {
    function solve($n, $highways, $k) {
        if ($k + 1 > $n) return -1;
        $g = array_fill(0, $n, []);
        foreach ($highways as $h) {
            $g[$h[0]][] = [$h[1], $h[2]];
            $g[$h[1]][] = [$h[0], $h[2]];
        }
        $dp = [];
        for ($mask = 0; $mask < (1 << $n); $mask++) $dp[$mask] = array_fill(0, $n, -1);
        for ($i = 0; $i < $n; $i++) $dp[1 << $i][$i] = 0;
        $ans = -1;
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            $cities = 0;
            $tmp = $mask;
            while ($tmp) { $cities += $tmp & 1; $tmp >>= 1; }
            for ($u = 0; $u < $n; $u++) {
                if ($dp[$mask][$u] < 0) continue;
                if ($cities - 1 === $k) $ans = max($ans, $dp[$mask][$u]);
                foreach ($g[$u] as $vw) {
                    $v = $vw[0];
                    $w = $vw[1];
                    if (($mask & (1 << $v)) !== 0) continue;
                    $nm = $mask | (1 << $v);
                    $dp[$nm][$v] = max($dp[$nm][$v], $dp[$mask][$u] + $w);
                }
            }
        }
        return $ans;
    }
}
