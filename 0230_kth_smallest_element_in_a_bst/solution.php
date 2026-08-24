<?php
// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($root, $k) {
        $stack = [];
        $current = $root;

        while ($current !== null || !empty($stack)) {
            while ($current !== null) {
                $stack[] = $current;
                $current = $current->left;
            }
            $current = array_pop($stack);
            $k--;
            if ($k === 0) {
                return $current->val;
            }
            $current = $current->right;
        }

        return -1;
    }
}
