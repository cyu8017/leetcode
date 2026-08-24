<?php
// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    private $ans;

    function countDominantNodes($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node == null) return -2147483648;
        $l = $this->dfs($node->left);
        $r = $this->dfs($node->right);
        $mx = max(max($l, $r), $node->val);
        if ($mx == $node->val) $this->ans++;
        return $mx;
    }
}
