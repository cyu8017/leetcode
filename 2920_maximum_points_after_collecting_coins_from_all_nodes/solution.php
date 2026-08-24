<?php
// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution {
    function maximumPoints($edges, $coins, $k) {
        $n = count($coins);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $memo = [];
        $dfs = function($u, $p, $shifts) use (&$dfs, &$g, &$coins, $k, &$memo) {
            if ($shifts > 14) $shifts = 14;
            $key = ($u << 5) | $shifts;
            if (isset($memo[$key])) return $memo[$key];
            $c = $coins[$u] >> $shifts;
            $opt1 = $c - $k;
            $opt2 = intdiv($c, 2);
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $opt1 += $dfs($v, $u, $shifts);
                $opt2 += $dfs($v, $u, $shifts + 1);
            }
            $best = max($opt1, $opt2);
            $memo[$key] = $best;
            return $best;
        };
        return $dfs(0, -1, 0);
    }
}
