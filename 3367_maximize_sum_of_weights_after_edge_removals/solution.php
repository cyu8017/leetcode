<?php
// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

class Solution {
    public $g;
    public $k;

    function dfs($u, $p) {
        $base = 0;
        $gains = [];
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $child = $this->dfs($to, $u);
            $base += $child[1];
            $gain = $child[0] + $w - $child[1];
            if ($gain > 0) $gains[] = $gain;
        }
        rsort($gains);
        $withP = $base;
        $without = $base;
        for ($i = 0; $i < count($gains) && $i < $this->k - 1; $i++) $withP += $gains[$i];
        for ($i = 0; $i < count($gains) && $i < $this->k; $i++) $without += $gains[$i];
        return [$withP, $without];
    }

    function maximizeSumOfWeights($edges, $k) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        $this->k = $k;
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        return $this->dfs(0, -1)[1];
    }
}
