<?php
// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function findTarget($root, $k) {
        $seen = [];
        $dfs = function($node) use (&$dfs, &$seen, $k) {
            if ($node == null) return false;
            if (isset($seen[$k - $node->val])) return true;
            $seen[$node->val] = true;
            return $dfs($node->left) || $dfs($node->right);
        };
        return $dfs($root);
    }
}
