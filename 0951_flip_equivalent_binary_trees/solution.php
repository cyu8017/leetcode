<?php
// LeetCode 0951 - Flip Equivalent Binary Trees
// https://leetcode.com/problems/flip-equivalent-binary-trees/

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
    function flipEquiv($root1, $root2) {
        if ($root1 === null && $root2 === null) return true;
        if ($root1 === null || $root2 === null || $root1->val !== $root2->val) return false;
        return ($this->flipEquiv($root1->left, $root2->left) && $this->flipEquiv($root1->right, $root2->right)) ||
               ($this->flipEquiv($root1->left, $root2->right) && $this->flipEquiv($root1->right, $root2->left));
    }
}
