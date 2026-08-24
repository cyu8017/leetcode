<?php
// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode {
    public $val;
    public $left;
    public $right;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    public $sizes;

    function dfs($node) {
        if (!$node) return [0, 0, 1];
        $L = $this->dfs($node->left);
        $R = $this->dfs($node->right);
        $sz = $L[1] + $R[1] + 1;
        $perf = $L[2] === 1 && $R[2] === 1 && $L[0] === $R[0];
        if ($perf) $this->sizes[] = $sz;
        return [max($L[0], $R[0]) + 1, $sz, $perf ? 1 : 0];
    }

    function kthLargestPerfectSubtree($root, $k) {
        $this->sizes = [];
        $this->dfs($root);
        rsort($this->sizes);
        if ($k > count($this->sizes)) return -1;
        return $this->sizes[$k - 1];
    }
}
