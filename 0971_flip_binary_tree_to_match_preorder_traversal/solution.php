<?php
// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

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
    function flipMatchVoyage($root, $voyage) {
        $i = 0;
        $ans = [];
        $dfs = function ($node) use (&$dfs, &$i, &$ans, $voyage) {
            if ($node === null) return true;
            if ($node->val !== $voyage[$i]) return false;
            $i++;
            if ($node->left !== null && $node->left->val !== $voyage[$i]) {
                $ans[] = $node->val;
                return $dfs($node->right) && $dfs($node->left);
            }
            return $dfs($node->left) && $dfs($node->right);
        };
        return $dfs($root) ? $ans : [-1];
    }
}
