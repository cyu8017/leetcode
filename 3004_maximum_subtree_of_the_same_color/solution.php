<?php
// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

class Solution {
    private $g;
    private $colors;
    private $size;
    private $ans;

    private function dfs($a, $fa) {
        $this->size[$a] = 1;
        $ok = true;
        foreach ($this->g[$a] as $b) {
            if ($b !== $fa) {
                $t = $this->dfs($b, $a);
                $ok = $ok && $t && $this->colors[$a] === $this->colors[$b];
                $this->size[$a] += $this->size[$b];
            }
        }
        if ($ok) $this->ans = max($this->ans, $this->size[$a]);
        return $ok;
    }

    function maximumSubtreeSize($edges, $colors) {
        $n = count($edges) + 1;
        $this->colors = $colors;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->size = array_fill(0, $n, 0);
        $this->ans = 0;
        $this->dfs(0, -1);
        return $this->ans;
    }
}
