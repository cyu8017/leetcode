<?php
// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
    function heightOfTree($root) {
        if (!$root) return -1;
        return $this->dfs($root);
    }
    function dfs($node) {
        if (!$node) return -1;
        if ($node->left && $node->left->right === $node) return $this->dfs($node->right) + 1;
        if ($node->right && $node->right->left === $node) return $this->dfs($node->left) + 1;
        return max($this->dfs($node->left), $this->dfs($node->right)) + 1;
    }
}
