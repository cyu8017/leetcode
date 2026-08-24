<?php
// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

class Solution {
    function minOperationsQueries($n, $edges, $queries) {
        $LOG = 15;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $up = [];
        for ($j = 0; $j < $LOG; $j++) $up[$j] = array_fill(0, $n, 0);
        $depth = array_fill(0, $n, 0);
        $cnt = [];
        for ($i = 0; $i < $n; $i++) $cnt[$i] = array_fill(0, 27, 0);
        $dfs = function($u, $p) use (&$dfs, &$g, &$up, &$depth, &$cnt) {
            $up[0][$u] = $p;
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $w = $ew[1];
                if ($v === $p) continue;
                $depth[$v] = $depth[$u] + 1;
                for ($i = 0; $i < 27; $i++) $cnt[$v][$i] = $cnt[$u][$i];
                $cnt[$v][$w]++;
                $dfs($v, $u);
            }
        };
        $dfs(0, 0);
        for ($j = 1; $j < $LOG; $j++)
            for ($i = 0; $i < $n; $i++) $up[$j][$i] = $up[$j - 1][$up[$j - 1][$i]];
        $lca = function($a, $b) use ($LOG, &$up, &$depth) {
            if ($depth[$a] < $depth[$b]) {
                $tmp = $a; $a = $b; $b = $tmp;
            }
            $diff = $depth[$a] - $depth[$b];
            for ($j = 0; $j < $LOG; $j++) if (($diff & (1 << $j)) !== 0) $a = $up[$j][$a];
            if ($a === $b) return $a;
            for ($j = $LOG - 1; $j >= 0; $j--) {
                if ($up[$j][$a] !== $up[$j][$b]) {
                    $a = $up[$j][$a];
                    $b = $up[$j][$b];
                }
            }
            return $up[0][$a];
        };
        $ans = [];
        foreach ($queries as $q) {
            $a = $q[0];
            $b = $q[1];
            $c = $lca($a, $b);
            $total = $depth[$a] + $depth[$b] - 2 * $depth[$c];
            $best = 0;
            for ($w = 1; $w <= 26; $w++) {
                $f = $cnt[$a][$w] + $cnt[$b][$w] - 2 * $cnt[$c][$w];
                if ($f > $best) $best = $f;
            }
            $ans[] = $total - $best;
        }
        return $ans;
    }
}
