<?php
// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function findTilt($root) {
        $total = 0;
        $subtreeSum = function($node) use (&$subtreeSum, &$total) {
            if ($node == null) return 0;
            $left = $subtreeSum($node->left);
            $right = $subtreeSum($node->right);
            $total += abs($left - $right);
            return $node->val + $left + $right;
        };
        $subtreeSum($root);
        return $total;
    }
}
