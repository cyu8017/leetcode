<?php
// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

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
    function minCameraCover($root) {
        $cameras = 0;
        $dfs = function ($node) use (&$dfs, &$cameras) {
            if ($node === null) return 1;
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            if ($left === 0 || $right === 0) {
                $cameras++;
                return 2;
            }
            if ($left === 2 || $right === 2) return 1;
            return 0;
        };
        $rootState = $dfs($root);
        return $cameras + ($rootState === 0 ? 1 : 0);
    }
}
