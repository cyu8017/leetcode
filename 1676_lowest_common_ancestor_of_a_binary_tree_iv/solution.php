<?php
// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

class Solution {
    function lowestCommonAncestor($root, $nodes) {
        $targets = new SplObjectStorage();
        foreach ($nodes as $node) {
            $targets->attach($node);
        }
        $dfs = function($node) use (&$dfs, $targets) {
            if ($node === null) return null;
            $l = $dfs($node->left);
            $r = $dfs($node->right);
            if ($targets->contains($node) || ($l && $r)) return $node;
            return $l ?: $r;
        };
        return $dfs($root);
    }
}
