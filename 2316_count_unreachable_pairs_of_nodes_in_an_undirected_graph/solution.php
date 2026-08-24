<?php
// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution {
    private $g;
    private $vis;

    function countPairs($n, $edges) {
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->vis = array_fill(0, $n, false);
        $ans = 0;
        $seen = 0;
        for ($i = 0; $i < $n; ++$i) {
            if (!$this->vis[$i]) {
                $sz = $this->dfs($i);
                $ans += $sz * $seen;
                $seen += $sz;
            }
        }
        return $ans;
    }

    private function dfs($u) {
        $this->vis[$u] = true;
        $size = 1;
        foreach ($this->g[$u] as $v) if (!$this->vis[$v]) $size += $this->dfs($v);
        return $size;
    }
}
