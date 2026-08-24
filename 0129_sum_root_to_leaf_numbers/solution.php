<?php
// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
    function sumNumbers($root) {
        $dfs = function ($node, $value) use (&$dfs) {
            if ($node === null) {
                return 0;
            }
            $current = $value * 10 + $node->val;
            if ($node->left === null && $node->right === null) {
                return $current;
            }
            return $dfs($node->left, $current) + $dfs($node->right, $current);
        };
        return $dfs($root, 0);
    }
}
