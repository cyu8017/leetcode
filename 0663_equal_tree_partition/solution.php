<?php
// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function checkEqualTree($root) {
        $subtreeSums = [];
        $dfs = function($node) use (&$dfs, &$subtreeSums) {
            if ($node == null) return 0;
            $total = $node->val + $dfs($node->left) + $dfs($node->right);
            $subtreeSums[] = $total;
            return $total;
        };
        $total = $dfs($root);
        if ($subtreeSums) array_pop($subtreeSums);
        if ($total % 2 !== 0) return false;
        $half = intdiv($total, 2);
        return in_array($half, $subtreeSums, true);
    }
}
