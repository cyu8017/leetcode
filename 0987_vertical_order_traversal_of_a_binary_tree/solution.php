<?php
// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

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
     * @return Integer[][]
     */
    function verticalTraversal($root) {
        $nodes = [];
        $dfs = null;
        $dfs = function ($node, $row, $col) use (&$dfs, &$nodes) {
            if ($node === null) return;
            $nodes[] = [$col, $row, $node->val];
            $dfs($node->left, $row + 1, $col - 1);
            $dfs($node->right, $row + 1, $col + 1);
        };
        $dfs($root, 0, 0);
        usort($nodes, function ($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            if ($a[1] !== $b[1]) return $a[1] <=> $b[1];
            return $a[2] <=> $b[2];
        });
        $byCol = [];
        foreach ($nodes as $t) {
            $byCol[$t[0]][] = $t[2];
        }
        ksort($byCol);
        return array_values($byCol);
    }
}
