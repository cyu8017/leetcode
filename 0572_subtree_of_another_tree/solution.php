<?php
// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function isSubtree($root, $subRoot) {
        $same = function($a, $b) use (&$same) {
            if ($a == null || $b == null) return $a === $b;
            return $a->val === $b->val && $same($a->left, $b->left) && $same($a->right, $b->right);
        };
        if ($root == null) return false;
        return $same($root, $subRoot) || $this->isSubtree($root->left, $subRoot) || $this->isSubtree($root->right, $subRoot);
    }
}
