<?php
// LeetCode 0617 - Merge Two Binary Trees
// https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function mergeTrees($root1, $root2) {
        if ($root1 == null) return $root2;
        if ($root2 == null) return $root1;
        $root1->val += $root2->val;
        $root1->left = $this->mergeTrees($root1->left, $root2->left);
        $root1->right = $this->mergeTrees($root1->right, $root2->right);
        return $root1;
    }
}
