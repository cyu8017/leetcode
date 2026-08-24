<?php
// LeetCode 0938 - Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

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
    function rangeSumBST($root, $low, $high) {
        if ($root === null) return 0;
        if ($root->val < $low) return $this->rangeSumBST($root->right, $low, $high);
        if ($root->val > $high) return $this->rangeSumBST($root->left, $low, $high);
        return $root->val + $this->rangeSumBST($root->left, $low, $high) + $this->rangeSumBST($root->right, $low, $high);
    }
}
