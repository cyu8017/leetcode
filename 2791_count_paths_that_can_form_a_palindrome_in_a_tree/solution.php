<?php
// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
    public $g;
    public $s;
    public $freq;
    public $ans;
    function countPalindromePaths($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->s = $s;
        $this->freq = [0 => 1];
        $this->ans = 0;
        $this->dfs(0, 0);
        return $this->ans;
    }
    function dfs($u, $mask) {
        foreach ($this->g[$u] as $v) {
            $nm = $mask ^ (1 << (ord($this->s[$v]) - 97));
            $this->ans += $this->freq[$nm] ?? 0;
            for ($b = 0; $b < 26; $b++) $this->ans += $this->freq[$nm ^ (1 << $b)] ?? 0;
            $this->freq[$nm] = ($this->freq[$nm] ?? 0) + 1;
            $this->dfs($v, $nm);
        }
    }
}
