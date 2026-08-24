<?php
// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution {
    public $nums;
    public $andValues;
    public $n;
    public $m;
    public $f = [];
    function minimumValueSum($nums, $andValues) {
        $this->nums = $nums;
        $this->andValues = $andValues;
        $this->n = count($nums);
        $this->m = count($andValues);
        $this->f = [];
        $ans = $this->dfs(0, 0, -1);
        return $ans < (1 << 29) ? $ans : -1;
    }
    function dfs($i, $j, $a) {
        $INF = 1 << 29;
        if ($this->n - $i < $this->m - $j) return $INF;
        if ($j === $this->m) return $i === $this->n ? 0 : $INF;
        $a &= $this->nums[$i];
        if ($a < $this->andValues[$j]) return $INF;
        $key = $i . "," . $j . "," . $a;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = $this->dfs($i + 1, $j, $a);
        if ($a === $this->andValues[$j]) {
            $ans = min($ans, $this->dfs($i + 1, $j + 1, -1) + $this->nums[$i]);
        }
        $this->f[$key] = $ans;
        return $ans;
    }
}
