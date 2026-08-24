<?php
// LeetCode 0226 - Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

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
    /**
     * @param TreeNode $root
     * @return TreeNode
     */
    function invertTree($root) {
        if ($root === null) {
            return null;
        }
        $left = $this->invertTree($root->left);
        $right = $this->invertTree($root->right);
        $root->left = $right;
        $root->right = $left;
        return $root;
    }
}
