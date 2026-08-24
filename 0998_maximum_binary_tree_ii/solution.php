<?php
// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

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
     * @param Integer $val
     * @return TreeNode
     */
    function insertIntoMaxTree($root, $val) {
        if ($root === null || $val > $root->val) {
            $node = new TreeNode($val);
            $node->left = $root;
            return $node;
        }
        $root->right = $this->insertIntoMaxTree($root->right, $val);
        return $root;
    }
}
