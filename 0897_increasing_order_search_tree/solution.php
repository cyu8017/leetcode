<?php
// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

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
    function increasingBST($root) {
        $dummy = new TreeNode(0);
        $cur = $dummy;
        $inorder = function ($node) use (&$inorder, &$cur) {
            if ($node === null) return;
            $inorder($node->left);
            $node->left = null;
            $cur->right = $node;
            $cur = $node;
            $inorder($node->right);
        };
        $inorder($root);
        return $dummy->right;
    }
}
