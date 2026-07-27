<?php
// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

class Solution {
    function correctBinaryTree($root) {
        $seen = new SplObjectStorage();
        $dfs = function($node) use (&$dfs, $seen) {
            if ($node === null) return null;
            if ($node->right !== null && $seen->contains($node->right)) return null;
            $seen->attach($node);
            $node->right = $dfs($node->right);
            $node->left = $dfs($node->left);
            return $node;
        };
        return $dfs($root);
    }
}
