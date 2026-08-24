<?php
// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

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
     * @param Integer $x
     * @param Integer $y
     * @return Boolean
     */
    function isCousins($root, $x, $y) {
        $depth = [];
        $parent = [];
        $dfs = null;
        $dfs = function ($node, $p, $d) use (&$dfs, &$depth, &$parent) {
            if ($node === null) return;
            $depth[$node->val] = $d;
            $parent[$node->val] = $p;
            $dfs($node->left, $node, $d + 1);
            $dfs($node->right, $node, $d + 1);
        };
        $dfs($root, null, 0);
        return ($depth[$x] ?? null) === ($depth[$y] ?? null) && ($parent[$x] ?? null) !== ($parent[$y] ?? null);
    }
}
