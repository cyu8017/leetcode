<?php
// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution {
    private $g;

    private function dfs($i, $fa) {
        $res = 0;
        foreach ($this->g[$i] as $j) if ($j !== $fa) $res = max($res, $this->dfs($j, $i) + 1);
        return $res;
    }

    private function pow2($exp) {
        $a = 2;
        $res = 1;
        $m = 1000000007;
        while ($exp > 0) {
            if ($exp & 1) $res = (int)(($res * $a) % $m);
            $a = (int)(($a * $a) % $m);
            $exp >>= 1;
        }
        return $res;
    }

    function assignEdgeWeights($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        return $this->pow2($this->dfs(1, 0) - 1);
    }
}
