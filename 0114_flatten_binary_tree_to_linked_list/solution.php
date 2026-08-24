<?php
class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function flatten($root) {
        if ($root === null) return;
        $this->flatten($root->left);
        $this->flatten($root->right);
        if ($root->left === null) return;
        $tail = $root->left;
        while ($tail->right !== null) $tail = $tail->right;
        $tail->right = $root->right;
        $root->right = $root->left;
        $root->left = null;
    }
}
