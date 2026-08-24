<?php
// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

class Solution {
    function maxWeight($n, $edges, $k, $t) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) $graph[$e[0]][] = [$e[1], $e[2]];
        $dp = [];
        for ($u = 0; $u < $n; $u++) {
            $dp[$u] = [];
            for ($i = 0; $i <= $k; $i++) $dp[$u][$i] = [];
            $dp[$u][0][0] = true;
        }
        for ($i = 0; $i < $k; $i++) {
            for ($u = 0; $u < $n; $u++) {
                foreach ($dp[$u][$i] as $sum => $_) {
                    foreach ($graph[$u] as $e) {
                        $ns = $sum + $e[1];
                        if ($ns < $t) $dp[$e[0]][$i + 1][$ns] = true;
                    }
                }
            }
        }
        $ans = -1;
        for ($u = 0; $u < $n; $u++)
            foreach ($dp[$u][$k] as $sum => $_) if ($sum > $ans) $ans = $sum;
        return $ans;
    }
}
