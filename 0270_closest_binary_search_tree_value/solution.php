<?php
// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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
     * @param Float $target
     * @return Integer
     */
    function closestValue($root, $target) {
        $closest = $root->val;
        $current = $root;
        while ($current !== null) {
            if (abs($closest - $target) > abs($current->val - $target)) {
                $closest = $current->val;
            }
            if ($current->val == $target) {
                return $current->val;
            }
            $current = $target < $current->val ? $current->left : $current->right;
        }
        return $closest;
    }
}
