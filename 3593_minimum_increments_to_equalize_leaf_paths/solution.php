<?php
// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

class Solution {
    private $graph;
    private $cost;
    private $ans;

    private function dfs($u, $p) {
        if (count($this->graph[$u]) === 1 && $p !== -1) return $this->cost[$u];
        $childVals = [];
        foreach ($this->graph[$u] as $v) {
            if ($v === $p) continue;
            $childVals[] = $this->dfs($v, $u);
        }
        if (count($childVals) === 0) return $this->cost[$u];
        $mx = 0;
        foreach ($childVals as $c) $mx = max($mx, $c);
        foreach ($childVals as $c) if ($c < $mx) $this->ans++;
        return $mx + $this->cost[$u];
    }

    function minIncrease($n, $edges, $cost) {
        $this->graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->cost = $cost;
        $this->ans = 0;
        $this->dfs(0, -1);
        return $this->ans;
    }
}
