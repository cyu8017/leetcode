<?php
// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function addOneRow($root, $val, $depth) {
        if ($depth === 1) return new TreeNode($val, $root, null);
        $dfs = function($node, $current) use (&$dfs, $val, $depth) {
            if ($node == null) return;
            if ($current === $depth - 1) {
                $node->left = new TreeNode($val, $node->left, null);
                $node->right = new TreeNode($val, null, $node->right);
                return;
            }
            $dfs($node->left, $current + 1);
            $dfs($node->right, $current + 1);
        };
        $dfs($root, 1);
        return $root;
    }
}
