<?php
// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
     * @param Integer $limit
     * @return TreeNode
     */
    function sufficientSubset($root, $limit) {
        $dfs = null;
        $dfs = function ($node, $pathSum) use (&$dfs, $limit) {
            if ($node === null) {
                return null;
            }
            $pathSum += $node->val;
            if ($node->left === null && $node->right === null) {
                return $pathSum >= $limit ? $node : null;
            }
            $node->left = $dfs($node->left, $pathSum);
            $node->right = $dfs($node->right, $pathSum);
            if ($node->left === null && $node->right === null) {
                return null;
            }
            return $node;
        };
        return $dfs($root, 0);
    }
}
