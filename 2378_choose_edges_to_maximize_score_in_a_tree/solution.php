<?php
// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

class Solution {
    private $g;

    function maxScore($edges) {
        $n = count($edges);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $edges[$i][0];
            $w = $edges[$i][1];
            $this->g[$p][] = [$i, $w];
        }
        return $this->dfs(0)[0];
    }

    private function dfs($u) {
        $base = 0;
        $bestGain = 0;
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            $child = $this->dfs($to);
            $base += $child[0];
            $gain = $child[1] + $w - $child[0];
            if ($gain > $bestGain) $bestGain = $gain;
        }
        return [$base + $bestGain, $base];
    }
}
