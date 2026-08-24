<?php
// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    function insertIntoBST($root, $val) {
        if ($root === null) return new TreeNode($val);
        $node = $root;
        while (true) {
            if ($val < $node->val) {
                if ($node->left === null) { $node->left = new TreeNode($val); break; }
                $node = $node->left;
            } else {
                if ($node->right === null) { $node->right = new TreeNode($val); break; }
                $node = $node->right;
            }
        }
        return $root;
    }
}
