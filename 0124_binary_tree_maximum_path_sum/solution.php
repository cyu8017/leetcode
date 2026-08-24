<?php
// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

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
     * @return Integer
     */
    function maxPathSum($root) {
        $best = PHP_INT_MIN;
        $gain = function ($node) use (&$gain, &$best) {
            if ($node === null) {
                return 0;
            }
            $left = max($gain($node->left), 0);
            $right = max($gain($node->right), 0);
            $best = max($best, $node->val + $left + $right);
            return $node->val + max($left, $right);
        };
        $gain($root);
        return $best;
    }
}
