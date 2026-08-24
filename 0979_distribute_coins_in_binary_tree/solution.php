<?php
// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

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
    function distributeCoins($root) {
        $ans = 0;
        $dfs = function ($node) use (&$dfs, &$ans) {
            if ($node === null) return 0;
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            $ans += abs($left) + abs($right);
            return $node->val + $left + $right - 1;
        };
        $dfs($root);
        return $ans;
    }
}
