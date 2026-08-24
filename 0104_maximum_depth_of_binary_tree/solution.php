<?php
// LeetCode 0104 - Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    function maxDepth($root) {
        if ($root === null) {
            return 0;
        }
        return 1 + max($this->maxDepth($root->left), $this->maxDepth($root->right));
    }
}
