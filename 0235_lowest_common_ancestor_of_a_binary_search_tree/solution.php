<?php

// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
    function lowestCommonAncestor($root, $p, $q) {
        while ($root !== null) {
            if ($p->val < $root->val && $q->val < $root->val) {
                $root = $root->left;
            } elseif ($p->val > $root->val && $q->val > $root->val) {
                $root = $root->right;
            } else {
                return $root;
            }
        }
        return $root;
    }
}
