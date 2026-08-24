<?php
// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    function isCompleteTree($root) {
        $q = [$root];
        $end = false;
        while ($q) {
            $node = array_shift($q);
            if ($node === null) $end = true;
            else {
                if ($end) return false;
                $q[] = $node->left;
                $q[] = $node->right;
            }
        }
        return true;
    }
}
