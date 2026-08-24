<?php
// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

class Solution {
    function maxSubgraphScore($n, $edges, $good) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $parent = array_fill(0, $n, -2);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($g[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $order[] = $v;
                }
            }
        }
        $down = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $down[$u] = 2 * $good[$u] - 1;
            foreach ($g[$u] as $v) {
                if ($parent[$v] === $u && $down[$v] > 0) $down[$u] += $down[$v];
            }
        }
        $ans = $down;
        foreach ($order as $u) {
            foreach ($g[$u] as $v) {
                if ($parent[$v] === $u) {
                    $outside = $ans[$u];
                    if ($down[$v] > 0) $outside -= $down[$v];
                    $ans[$v] = $down[$v];
                    if ($outside > 0) $ans[$v] += $outside;
                }
            }
        }
        return $ans;
    }
}
