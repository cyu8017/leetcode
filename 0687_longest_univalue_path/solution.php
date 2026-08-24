<?php
// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

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
    function longestUnivaluePath($root) {
        $best = 0;
        $dfs = function ($node) use (&$dfs, &$best) {
            if ($node === null) return 0;
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            $leftPath = $node->left !== null && $node->left->val === $node->val ? $left + 1 : 0;
            $rightPath = $node->right !== null && $node->right->val === $node->val ? $right + 1 : 0;
            $best = max($best, $leftPath + $rightPath);
            return max($leftPath, $rightPath);
        };
        $dfs($root);
        return $best;
    }
}
