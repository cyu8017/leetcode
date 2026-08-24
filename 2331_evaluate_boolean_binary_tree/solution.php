<?php
// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

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
    function evaluateTree($root) {
        if ($root->left === null && $root->right === null) return $root->val === 1;
        $l = $this->evaluateTree($root->left);
        $r = $this->evaluateTree($root->right);
        if ($root->val === 2) return $l || $r;
        return $l && $r;
    }
}
