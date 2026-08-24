<?php
// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

class Solution {
    private $g;
    private $path;

    private function dfs($u) {
        if (!isset($this->g[$u])) $this->g[$u] = [];
        while (count($this->g[$u])) {
            $v = array_pop($this->g[$u]);
            $this->dfs($v);
        }
        $this->path[] = $u;
    }

    /**
     * @param Integer[][] $pairs
     * @return Integer[][]
     */
    function validArrangement($pairs) {
        $this->g = [];
        $indeg = [];
        $outdeg = [];
        foreach ($pairs as $e) {
            $u = $e[0];
            $v = $e[1];
            if (!isset($this->g[$u])) $this->g[$u] = [];
            $this->g[$u][] = $v;
            $outdeg[$u] = ($outdeg[$u] ?? 0) + 1;
            $indeg[$v] = ($indeg[$v] ?? 0) + 1;
        }
        $start = $pairs[0][0];
        foreach ($outdeg as $u => $o) {
            if ($o - ($indeg[$u] ?? 0) === 1) {
                $start = $u;
                break;
            }
        }
        $this->path = [];
        $this->dfs($start);
        $this->path = array_reverse($this->path);
        $ans = [];
        for ($i = 0; $i + 1 < count($this->path); $i++) {
            $ans[] = [$this->path[$i], $this->path[$i + 1]];
        }
        return $ans;
    }
}
