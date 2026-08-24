<?php
// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

class Solution {
    private $ans;
    private $val;

    private function dfs($x, $y, $k) {
        if ($k === 1) {
            $this->ans[$x][$y] = $this->val++;
            return;
        }
        $h = $k >> 1;
        $this->dfs($x, $y, $h);
        $this->dfs($x + $h, $y, $h);
        $this->dfs($x + $h, $y - $h, $h);
        $this->dfs($x, $y - $h, $h);
    }

    function specialGrid($n) {
        $m = 1 << $n;
        $this->ans = [];
        for ($i = 0; $i < $m; $i++) $this->ans[$i] = array_fill(0, $m, 0);
        $this->val = 0;
        $this->dfs(0, $m - 1, $m);
        return $this->ans;
    }
}
