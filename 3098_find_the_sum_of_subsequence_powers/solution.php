<?php
// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution {
    public $nums;
    public $n;
    public $f = [];
    function sumOfPowers($nums, $k) {
        sort($nums);
        $this->nums = $nums;
        $this->n = count($nums);
        $this->f = [];
        return $this->dfs(0, $this->n, $k, PHP_INT_MAX);
    }
    function dfs($i, $j, $kk, $mi) {
        $MOD = 1000000007;
        if ($i >= $this->n) return $kk === 0 ? $mi : 0;
        if ($this->n - $i < $kk) return 0;
        $key = $mi . "," . $i . "," . $j . "," . $kk;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = $this->dfs($i + 1, $j, $kk, $mi);
        if ($j === $this->n) $ans = ($ans + $this->dfs($i + 1, $i, $kk - 1, $mi)) % $MOD;
        else $ans = ($ans + $this->dfs($i + 1, $i, $kk - 1, min($mi, $this->nums[$i] - $this->nums[$j]))) % $MOD;
        $this->f[$key] = $ans;
        return $ans;
    }
}
