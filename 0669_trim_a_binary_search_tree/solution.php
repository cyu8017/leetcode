<?php
// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function trimBST($root, $low, $high) {
        if ($root == null) return null;
        if ($root->val < $low) return $this->trimBST($root->right, $low, $high);
        if ($root->val > $high) return $this->trimBST($root->left, $low, $high);
        $root->left = $this->trimBST($root->left, $low, $high);
        $root->right = $this->trimBST($root->right, $low, $high);
        return $root;
    }
}
