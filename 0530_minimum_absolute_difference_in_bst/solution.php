<?php
// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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
    function getMinimumDifference($root) {
        return $this->get_minimum_difference($root);
    }

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function get_minimum_difference($root) {
        $previous = null;
        $best = PHP_INT_MAX;
        $inorder = function ($node) use (&$inorder, &$previous, &$best) {
            if ($node === null) {
                return;
            }
            $inorder($node->left);
            if ($previous !== null) {
                $best = min($best, $node->val - $previous);
            }
            $previous = $node->val;
            $inorder($node->right);
        };
        $inorder($root);
        return $best;
    }
}
