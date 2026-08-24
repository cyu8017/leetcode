<?php
// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function findSecondMinimumValue($root) {
        if ($root == null) return -1;
        $ans = -1;
        $rootVal = $root->val;
        $dfs = function($node) use (&$dfs, &$ans, $rootVal) {
            if ($node == null) return;
            if ($node->val > $rootVal) {
                if ($ans === -1 || $node->val < $ans) $ans = $node->val;
                return;
            }
            $dfs($node->left);
            $dfs($node->right);
        };
        $dfs($root);
        return $ans;
    }
}
