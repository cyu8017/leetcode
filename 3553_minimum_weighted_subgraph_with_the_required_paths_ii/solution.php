<?php
// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

class Solution {
    private $LOG = 17;
    private $g;
    private $parent;
    private $depth;
    private $dist;

    private function dfs($u, $p) {
        $this->parent[0][$u] = $p;
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $this->depth[$to] = $this->depth[$u] + 1;
            $this->dist[$to] = $this->dist[$u] + $w;
            $this->dfs($to, $u);
        }
    }

    private function lca($u, $v) {
        if ($this->depth[$u] < $this->depth[$v]) { $t = $u; $u = $v; $v = $t; }
        for ($k = $this->LOG - 1; $k >= 0; $k--)
            if ($this->parent[$k][$u] !== -1 && $this->depth[$this->parent[$k][$u]] >= $this->depth[$v]) $u = $this->parent[$k][$u];
        if ($u === $v) return $u;
        for ($k = $this->LOG - 1; $k >= 0; $k--)
            if ($this->parent[$k][$u] !== -1 && $this->parent[$k][$u] !== $this->parent[$k][$v]) {
                $u = $this->parent[$k][$u];
                $v = $this->parent[$k][$v];
            }
        return $this->parent[0][$u];
    }

    private function path($u, $v) {
        $a = $this->lca($u, $v);
        return $this->dist[$u] + $this->dist[$v] - 2 * $this->dist[$a];
    }

    function minimumWeight($edges, $queries) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        $this->parent = [];
        for ($k = 0; $k < $this->LOG; $k++) $this->parent[$k] = array_fill(0, $n, -1);
        $this->depth = array_fill(0, $n, 0);
        $this->dist = array_fill(0, $n, 0);
        $this->dfs(0, -1);
        for ($k = 1; $k < $this->LOG; $k++)
            for ($v = 0; $v < $n; $v++)
                if ($this->parent[$k - 1][$v] !== -1) $this->parent[$k][$v] = $this->parent[$k - 1][$this->parent[$k - 1][$v]];
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $a = $queries[$i][0];
            $b = $queries[$i][1];
            $c = $queries[$i][2];
            $ans[$i] = intdiv($this->path($a, $b) + $this->path($b, $c) + $this->path($a, $c), 2);
        }
        return $ans;
    }
}
