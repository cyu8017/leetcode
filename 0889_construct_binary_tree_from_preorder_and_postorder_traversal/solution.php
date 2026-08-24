<?php
// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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
    function constructFromPrePost($preorder, $postorder) {
        $postIndex = [];
        foreach ($postorder as $i => $v) $postIndex[$v] = $i;
        $build = function ($preLo, $preHi, $postLo, $postHi) use (&$build, $preorder, $postIndex) {
            if ($preLo > $preHi) return null;
            $root = new TreeNode($preorder[$preLo]);
            if ($preLo === $preHi) return $root;
            $leftVal = $preorder[$preLo + 1];
            $leftPost = $postIndex[$leftVal];
            $leftSize = $leftPost - $postLo + 1;
            $root->left = $build($preLo + 1, $preLo + $leftSize, $postLo, $leftPost);
            $root->right = $build($preLo + $leftSize + 1, $preHi, $leftPost + 1, $postHi - 1);
            return $root;
        };
        $n = count($preorder);
        return $build(0, $n - 1, 0, $n - 1);
    }
}
