<?php
// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution {
    public $k;
    public $f = [];
    function waysToReachStair($k) {
        $this->k = $k;
        $this->f = [];
        return $this->dfs(1, 0, 0);
    }
    function dfs($i, $j, $jump) {
        if ($i > $this->k + 1) return 0;
        $key = $i . "," . $j . "," . $jump;
        if (isset($this->f[$key])) return $this->f[$key];
        $ans = 0;
        if ($i === $this->k) $ans++;
        if ($i > 0 && $j === 0) $ans += $this->dfs($i - 1, 1, $jump);
        $ans += $this->dfs($i + (1 << $jump), 0, $jump + 1);
        $this->f[$key] = $ans;
        return $ans;
    }
}
