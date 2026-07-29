<?php
// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    function maxAncestorDiff($root) {
        return $this->dfs($root, $root->val, $root->val);
    }

    private function dfs($node, $lo, $hi) {
        if ($node === null) {
            return $hi - $lo;
        }
        $lo = min($lo, $node->val);
        $hi = max($hi, $node->val);
        return max($this->dfs($node->left, $lo, $hi), $this->dfs($node->right, $lo, $hi));
    }
}
