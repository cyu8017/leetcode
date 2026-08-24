<?php
// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    function splitBST($root, $target) {
        if ($root === null) return [null, null];
        if ($root->val <= $target) {
            $parts = $this->splitBST($root->right, $target);
            $root->right = $parts[0];
            return [$root, $parts[1]];
        }
        $leftParts = $this->splitBST($root->left, $target);
        $root->left = $leftParts[1];
        return [$leftParts[0], $root];
    }
}
