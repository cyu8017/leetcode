<?php
// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

class Solution {
    function solve($n, $edges, $query) {
        $LOG = 17;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $up = [];
        for ($k = 0; $k < $LOG; $k++) $up[$k] = array_fill(0, $n, 0);
        $depth = array_fill(0, $n, 0);
        $dfs = function($u, $p) use (&$dfs, &$up, &$depth, $g) {
            $up[0][$u] = $p;
            foreach ($g[$u] as $v) if ($v !== $p) {
                $depth[$v] = $depth[$u] + 1;
                $dfs($v, $u);
            }
        };
        $dfs(0, 0);
        for ($k = 1; $k < $LOG; $k++)
            for ($v = 0; $v < $n; $v++)
                $up[$k][$v] = $up[$k - 1][$up[$k - 1][$v]];
        $lift = function($v, $d) use ($LOG, $up) {
            for ($k = 0; $k < $LOG; $k++)
                if ((($d >> $k) & 1) !== 0) $v = $up[$k][$v];
            return $v;
        };
        $lca = function($a, $b) use ($depth, $lift, $LOG, $up) {
            if ($depth[$a] < $depth[$b]) { $tmp = $a; $a = $b; $b = $tmp; }
            $a = $lift($a, $depth[$a] - $depth[$b]);
            if ($a === $b) return $a;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                if ($up[$k][$a] !== $up[$k][$b]) {
                    $a = $up[$k][$a];
                    $b = $up[$k][$b];
                }
            }
            return $up[0][$a];
        };
        $dist = function($a, $b) use ($lca, $depth) {
            $c = $lca($a, $b);
            return $depth[$a] + $depth[$b] - 2 * $depth[$c];
        };
        $ans = array_fill(0, count($query), 0);
        for ($i = 0; $i < count($query); $i++) {
            $a = $query[$i][0];
            $b = $query[$i][1];
            $x = $query[$i][2];
            $cands = [$lca($a, $b), $lca($a, $x), $lca($b, $x)];
            $best = $cands[0];
            $bestD = $dist($cands[0], $x);
            for ($t = 1; $t < 3; $t++) {
                $d = $dist($cands[$t], $x);
                if ($d < $bestD) { $bestD = $d; $best = $cands[$t]; }
            }
            $ans[$i] = $best;
        }
        return $ans;
    }
}
