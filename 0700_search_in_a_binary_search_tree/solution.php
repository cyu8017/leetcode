<?php
// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

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
    function searchBST($root, $val) {
        while ($root !== null && $root->val !== $val) {
            $root = $val < $root->val ? $root->left : $root->right;
        }
        return $root;
    }
}
