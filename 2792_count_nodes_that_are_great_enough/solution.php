<?php
// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    public $ans;
    public $k;
    function countGreatEnoughNodes($root, $k) {
        $this->ans = 0;
        $this->k = $k;
        $this->dfs($root);
        return $this->ans;
    }
    function dfs($node) {
        if (!$node) return [];
        $vals = array_merge([$node->val], $this->dfs($node->left), $this->dfs($node->right));
        $smaller = 0;
        foreach ($vals as $v) if ($v < $node->val) $smaller++;
        if ($smaller >= $this->k) $this->ans++;
        return $vals;
    }
}
