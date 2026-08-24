<?php
// LeetCode 3891 - Minimum Increase to Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    public $nums;
    public $n;
    public $f;
    function dfs($i, $j) {
        if ($i >= $this->n - 1) return 0;
        if ($this->f[$i][$j] !== -1) return $this->f[$i][$j];
        $cost = max(0, max($this->nums[$i - 1], $this->nums[$i + 1]) + 1 - $this->nums[$i]);
        $ans = $cost + $this->dfs($i + 2, $j);
        if ($j > 0) $ans = min($ans, $this->dfs($i + 1, 0));
        return $this->f[$i][$j] = $ans;
    }
    function minIncrease($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = [];
        for ($i = 0; $i < $this->n; $i++) $this->f[$i] = [-1, -1];
        return $this->dfs(1, ($this->n & 1) ^ 1);
    }
}
