<?php
// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

class Solution {
    private $g;
    private $cost;
    private $ans;

    private function dfs($u, $p) {
        $vals = [$this->cost[$u]];
        foreach ($this->g[$u] as $v) {
            if ($v === $p) continue;
            $vals = array_merge($vals, $this->dfs($v, $u));
        }
        sort($vals);
        if (count($vals) < 3) {
            $this->ans[$u] = 1;
        } else {
            $m = count($vals);
            $cand1 = $vals[$m - 1] * $vals[$m - 2] * $vals[$m - 3];
            $cand2 = $vals[0] * $vals[1] * $vals[$m - 1];
            $best = max($cand1, $cand2);
            if ($best < 0) $best = 0;
            $this->ans[$u] = $best;
        }
        if (count($vals) <= 5) return $vals;
        return [$vals[0], $vals[1], $vals[count($vals) - 3], $vals[count($vals) - 2], $vals[count($vals) - 1]];
    }

    function placedCoins($edges, $cost) {
        $n = count($cost);
        $this->cost = $cost;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->ans = array_fill(0, $n, 0);
        $this->dfs(0, -1);
        return $this->ans;
    }
}
