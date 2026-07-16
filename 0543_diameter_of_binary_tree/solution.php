<?php
// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

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
     * @param TreeNode|null $root
     * @return Integer
     */
    function diameterOfBinaryTree($root) {
        return $this->diameter_of_binary_tree($root);
    }

    /**
     * @param TreeNode|null $root
     * @return Integer
     */
    function diameter_of_binary_tree($root) {
        $best = 0;
        $depth = function ($node) use (&$depth, &$best) {
            if ($node === null) {
                return 0;
            }
            $left = $depth($node->left);
            $right = $depth($node->right);
            $best = max($best, $left + $right);
            return 1 + max($left, $right);
        };
        $depth($root);
        return $best;
    }
}
