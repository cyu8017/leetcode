<?php
// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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
    function minDiffInBST($root) {
        $hasPrev = false;
        $prev = 0;
        $best = PHP_INT_MAX;
        $inorder = function($node) use (&$inorder, &$hasPrev, &$prev, &$best) {
            if ($node === null) return;
            $inorder($node->left);
            if ($hasPrev) $best = min($best, $node->val - $prev);
            $prev = $node->val;
            $hasPrev = true;
            $inorder($node->right);
        };
        $inorder($root);
        return $best;
    }
}
