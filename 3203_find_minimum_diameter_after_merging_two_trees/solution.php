<?php
// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution {
    private $ans;
    private $a;
    private $g;

    function minimumDiameterAfterMerge($edges1, $edges2) {
        $d1 = $this->treeDiameter($edges1);
        $d2 = $this->treeDiameter($edges2);
        return max($d1, $d2, intdiv($d1 + 1, 2) + intdiv($d2 + 1, 2) + 1);
    }

    private function dfs($i, $fa, $t) {
        foreach ($this->g[$i] as $j) if ($j !== $fa) $this->dfs($j, $i, $t + 1);
        if ($this->ans < $t) { $this->ans = $t; $this->a = $i; }
    }

    private function treeDiameter($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->ans = 0;
        $this->a = 0;
        $this->dfs(0, -1, 0);
        $this->dfs($this->a, -1, 0);
        return $this->ans;
    }
}
