<?php
// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function tree2str($root) {
        if ($root == null) return "";
        $result = strval($root->val);
        if ($root->left != null || $root->right != null) $result .= "(" . $this->tree2str($root->left) . ")";
        if ($root->right != null) $result .= "(" . $this->tree2str($root->right) . ")";
        return $result;
    }
}
