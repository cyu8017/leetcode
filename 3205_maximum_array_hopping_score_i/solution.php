<?php
// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

class Solution {
    private $nums;
    private $n;
    private $f;

    function maxScore($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = array_fill(0, $this->n, 0);
        return $this->dfs(0);
    }

    private function dfs($i) {
        if ($this->f[$i] > 0) return $this->f[$i];
        for ($j = $i + 1; $j < $this->n; $j++) $this->f[$i] = max($this->f[$i], ($j - $i) * $this->nums[$j] + $this->dfs($j));
        return $this->f[$i];
    }
}
