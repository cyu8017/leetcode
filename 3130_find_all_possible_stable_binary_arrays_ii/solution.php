<?php
// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

class Solution {
    public $limit;
    public $f;
    function numberOfStableArrays($zero, $one, $limit) {
        $MOD = 1000000007;
        $this->limit = $limit;
        $this->f = [];
        for ($i = 0; $i <= $zero; $i++) {
            $this->f[$i] = [];
            for ($j = 0; $j <= $one; $j++) $this->f[$i][$j] = [-1, -1];
        }
        return ($this->dfs($zero, $one, 0) + $this->dfs($zero, $one, 1)) % $MOD;
    }
    function dfs($i, $j, $k) {
        $MOD = 1000000007;
        $limit = $this->limit;
        if ($i < 0 || $j < 0) return 0;
        if ($i === 0) return ($k === 1 && $j <= $limit) ? 1 : 0;
        if ($j === 0) return ($k === 0 && $i <= $limit) ? 1 : 0;
        if ($this->f[$i][$j][$k] !== -1) return $this->f[$i][$j][$k];
        if ($k === 0)
            $res = ($this->dfs($i - 1, $j, 0) + $this->dfs($i - 1, $j, 1) - $this->dfs($i - $limit - 1, $j, 1) + $MOD) % $MOD;
        else
            $res = ($this->dfs($i, $j - 1, 0) + $this->dfs($i, $j - 1, 1) - $this->dfs($i, $j - $limit - 1, 0) + $MOD) % $MOD;
        return $this->f[$i][$j][$k] = $res;
    }
}
