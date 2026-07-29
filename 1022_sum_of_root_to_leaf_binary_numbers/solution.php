<?php
// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

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
    function sumRootToLeaf($root) {
        return $this->dfs($root, 0);
    }

    private function dfs($node, $value) {
        if ($node === null) {
            return 0;
        }
        $value = $value * 2 + $node->val;
        if ($node->left === null && $node->right === null) {
            return $value;
        }
        return $this->dfs($node->left, $value) + $this->dfs($node->right, $value);
    }
}
