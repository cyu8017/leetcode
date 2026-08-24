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
    function minDepth($root) {
        if ($root === null) {
            return 0;
        }
        if ($root->left === null) {
            return 1 + $this->minDepth($root->right);
        }
        if ($root->right === null) {
            return 1 + $this->minDepth($root->left);
        }
        return 1 + min($this->minDepth($root->left), $this->minDepth($root->right));
    }
}
