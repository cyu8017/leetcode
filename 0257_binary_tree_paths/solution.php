<?php
// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

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
     * @return String[]
     */
    function binaryTreePaths($root) {
        $result = [];
        $this->dfs($root, [], $result);
        return $result;
    }

    private function dfs($node, $path, &$result) {
        if ($node === null) {
            return;
        }
        $path[] = (string)$node->val;
        if ($node->left === null && $node->right === null) {
            $result[] = implode('->', $path);
            return;
        }
        $this->dfs($node->left, $path, $result);
        $this->dfs($node->right, $path, $result);
    }
}
