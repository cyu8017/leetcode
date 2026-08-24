<?php
// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution {
    private $nums;
    private $n;
    private $f;
    private $s;

    private function dfs($i, $j) {
        if ($j - $i < 1) return 0;
        if ($this->f[$i][$j] !== -1) return $this->f[$i][$j];
        $ans = 0;
        if ($this->nums[$i] + $this->nums[$i + 1] === $this->s) $ans = max($ans, 1 + $this->dfs($i + 2, $j));
        if ($this->nums[$i] + $this->nums[$j] === $this->s) $ans = max($ans, 1 + $this->dfs($i + 1, $j - 1));
        if ($this->nums[$j - 1] + $this->nums[$j] === $this->s) $ans = max($ans, 1 + $this->dfs($i, $j - 2));
        return $this->f[$i][$j] = $ans;
    }

    private function g($i0, $j0, $score) {
        $this->f = [];
        for ($i = 0; $i < $this->n; $i++) $this->f[$i] = array_fill(0, $this->n, -1);
        $this->s = $score;
        return $this->dfs($i0, $j0);
    }

    function maxOperations($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $n = $this->n;
        $a = $this->g(2, $n - 1, $nums[0] + $nums[1]);
        $b = $this->g(0, $n - 3, $nums[$n - 1] + $nums[$n - 2]);
        $c = $this->g(1, $n - 2, $nums[0] + $nums[$n - 1]);
        return 1 + max($a, max($b, $c));
    }
}
