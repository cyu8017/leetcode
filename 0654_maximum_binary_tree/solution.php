<?php
// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function constructMaximumBinaryTree($nums) {
        $build = function($left, $right) use (&$build, $nums) {
            if ($left > $right) return null;
            $mid = $left;
            for ($i = $left; $i <= $right; ++$i) if ($nums[$i] > $nums[$mid]) $mid = $i;
            return new TreeNode($nums[$mid], $build($left, $mid - 1), $build($mid + 1, $right));
        };
        return $build(0, count($nums) - 1);
    }
}
