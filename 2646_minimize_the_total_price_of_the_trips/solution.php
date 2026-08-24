<?php
// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
    function minimumTotalPrice($n, $edges, $price, $trips) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $cnt = array_fill(0, $n, 0);
        $path = function($u, $p, $target) use (&$path, &$g, &$cnt) {
            if ($u === $target) { $cnt[$u]++; return true; }
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if ($path($v, $u, $target)) { $cnt[$u]++; return true; }
            }
            return false;
        };
        foreach ($trips as $t) $path($t[0], -1, $t[1]);
        $dfs = function($u, $p) use (&$dfs, &$g, &$price, &$cnt) {
            $full = $price[$u] * $cnt[$u];
            $half = intdiv($full, 2);
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $child = $dfs($v, $u);
                $full += min($child[0], $child[1]);
                $half += $child[0];
            }
            return [$full, $half];
        };
        $res = $dfs(0, -1);
        return min($res[0], $res[1]);
    }
}
