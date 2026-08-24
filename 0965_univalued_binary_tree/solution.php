<?php
// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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
    function isUnivalTree($root) {
        if ($root === null) return true;
        $dfs = function ($node, $v) use (&$dfs) {
            if ($node === null) return true;
            if ($node->val !== $v) return false;
            return $dfs($node->left, $v) && $dfs($node->right, $v);
        };
        return $dfs($root, $root->val);
    }
}
