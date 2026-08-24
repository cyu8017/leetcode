<?php
// LeetCode 3327 - Check if DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

class Solution {
    public $g;
    public $s;
    public $ans;

    function isPal($t) {
        for ($i = 0, $j = strlen($t) - 1; $i < $j; $i++, $j--) {
            if ($t[$i] !== $t[$j]) return false;
        }
        return true;
    }

    function dfsStr($u) {
        $out = '';
        foreach ($this->g[$u] as $v) $out .= $this->dfsStr($v);
        $out .= $this->s[$u];
        $this->ans[$u] = $this->isPal($out);
        return $out;
    }

    function findAnswer($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->s = $s;
        $this->ans = array_fill(0, $n, false);
        $this->dfsStr(0);
        return $this->ans;
    }
}
