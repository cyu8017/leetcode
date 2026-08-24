<?php
// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

class Solution {
    private $MOD = 1000000007;
    private $LOG = 17;
    private $depth;
    private $graph;
    private $parent;

    private function dfs($u, $p) {
        $this->parent[0][$u] = $p;
        foreach ($this->graph[$u] as $v) {
            if ($v !== $p) {
                $this->depth[$v] = $this->depth[$u] + 1;
                $this->dfs($v, $u);
            }
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

    private function modPow($exp) {
        $base = 2;
        $res = 1;
        $m = $this->MOD;
        while ($exp > 0) {
            if ($exp & 1) $res = (int)(($res * $base) % $m);
            $base = (int)(($base * $base) % $m);
            $exp >>= 1;
        }
        return $res;
    }

    function assignEdgeWeights($edges, $queries) {
        $n = count($edges) + 1;
        $this->depth = array_fill(0, $n + 1, 0);
        $this->graph = array_fill(0, $n + 1, []);
        $this->parent = [];
        for ($k = 0; $k < $this->LOG; $k++) $this->parent[$k] = array_fill(0, $n + 1, -1);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->dfs(1, -1);
        for ($k = 1; $k < $this->LOG; $k++)
            for ($v = 1; $v <= $n; $v++)
                if ($this->parent[$k - 1][$v] !== -1) $this->parent[$k][$v] = $this->parent[$k - 1][$this->parent[$k - 1][$v]];
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $u = $queries[$i][0];
            $v = $queries[$i][1];
            if ($u === $v) { $ans[$i] = 0; continue; }
            $a = $this->lca($u, $v);
            $d = $this->depth[$u] + $this->depth[$v] - 2 * $this->depth[$a];
            $ans[$i] = $this->modPow($d - 1);
        }
        return $ans;
    }
}
