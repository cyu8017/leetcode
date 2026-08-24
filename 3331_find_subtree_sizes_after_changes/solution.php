<?php
// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution {
    public $g;
    public $s;
    public $newParent;
    public $last;
    public $ng;
    public $ans;

    function dfs1($u) {
        $c = ord($this->s[$u]) - 97;
        $prev = $this->last[$c];
        if ($prev !== -1) $this->newParent[$u] = $prev;
        $this->last[$c] = $u;
        foreach ($this->g[$u] as $v) $this->dfs1($v);
        $this->last[$c] = $prev;
    }

    function dfs2($u) {
        $sz = 1;
        foreach ($this->ng[$u] as $v) $sz += $this->dfs2($v);
        return $this->ans[$u] = $sz;
    }

    function findSubtreeSizes($parent, $s) {
        $n = count($parent);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$parent[$i]][] = $i;
        $this->newParent = $parent;
        $this->s = $s;
        $this->last = array_fill(0, 26, -1);
        $this->dfs1(0);
        $this->ng = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->ng[$this->newParent[$i]][] = $i;
        $this->ans = array_fill(0, $n, 0);
        $this->dfs2(0);
        return $this->ans;
    }
}
