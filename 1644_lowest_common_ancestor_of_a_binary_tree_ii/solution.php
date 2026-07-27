<?php
// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

class Solution {
    private $found = 0;

    /**
     * @param TreeNode $root
     * @param TreeNode $p
     * @param TreeNode $q
     * @return TreeNode
     */
    function lowestCommonAncestor($root, $p, $q) {
        $this->found = 0;
        $ans = $this->dfs($root, $p, $q);
        return $this->found === 2 ? $ans : null;
    }

    private function dfs($node, $p, $q) {
        if ($node === null) {
            return null;
        }
        $left = $this->dfs($node->left, $p, $q);
        $right = $this->dfs($node->right, $p, $q);
        if ($node === $p || $node === $q) {
            $this->found++;
            return $node;
        }
        return ($left && $right) ? $node : ($left ?: $right);
    }
}
