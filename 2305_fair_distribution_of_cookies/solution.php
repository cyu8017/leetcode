<?php
// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution {
    private $bags;
    private $cookies;
    private $ans;

    function distributeCookies($cookies, $k) {
        $this->cookies = $cookies;
        $this->bags = array_fill(0, $k, 0);
        $this->ans = PHP_INT_MAX;
        $this->dfs(0);
        return $this->ans;
    }

    private function dfs($i) {
        if ($i === count($this->cookies)) {
            $mx = 0;
            foreach ($this->bags as $b) $mx = max($mx, $b);
            $this->ans = min($this->ans, $mx);
            return;
        }
        $seen = [];
        $n = count($this->bags);
        for ($j = 0; $j < $n; ++$j) {
            if (isset($seen[$this->bags[$j]])) continue;
            $seen[$this->bags[$j]] = true;
            $this->bags[$j] += $this->cookies[$i];
            if ($this->bags[$j] < $this->ans) $this->dfs($i + 1);
            $this->bags[$j] -= $this->cookies[$i];
            if ($this->bags[$j] === 0) break;
        }
    }
}
