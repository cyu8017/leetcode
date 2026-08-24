<?php
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
    function hasPathSum($root, $targetSum) {
        if ($root === null) {
            return false;
        }
        if ($root->left === null && $root->right === null) {
            return $root->val === $targetSum;
        }
        return $this->hasPathSum($root->left, $targetSum - $root->val) ||
            $this->hasPathSum($root->right, $targetSum - $root->val);
    }
}
