<?php
// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

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
     * @param TreeNode|null $root
     * @return Integer[]
     */
    function boundaryOfBinaryTree($root) {
        return $this->boundary_of_binary_tree($root);
    }

    /**
     * @param TreeNode|null $root
     * @return Integer[]
     */
    function boundary_of_binary_tree($root) {
        if ($root === null) {
            return [];
        }

        $isLeaf = function ($node) {
            return $node !== null && $node->left === null && $node->right === null;
        };

        $leftBoundary = function ($node) use (&$leftBoundary, $isLeaf) {
            if ($node === null || $isLeaf($node)) {
                return [];
            }
            if ($node->left !== null) {
                return array_merge([$node->val], $leftBoundary($node->left));
            }
            return array_merge([$node->val], $leftBoundary($node->right));
        };

        $rightBoundary = function ($node) use (&$rightBoundary, $isLeaf) {
            if ($node === null || $isLeaf($node)) {
                return [];
            }
            if ($node->right !== null) {
                return array_merge($rightBoundary($node->right), [$node->val]);
            }
            return array_merge($rightBoundary($node->left), [$node->val]);
        };

        $leaves = function ($node) use (&$leaves, $isLeaf) {
            if ($node === null) {
                return [];
            }
            if ($isLeaf($node)) {
                return [$node->val];
            }
            return array_merge($leaves($node->left), $leaves($node->right));
        };

        if ($isLeaf($root)) {
            return [$root->val];
        }

        return array_merge(
            [$root->val],
            $leftBoundary($root->left),
            $leaves($root),
            $rightBoundary($root->right)
        );
    }
}
