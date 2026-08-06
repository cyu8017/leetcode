<?php
// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class Solution {
    /**
     * @param TreeNode $root
     * @return TreeNode
     */
    function lcaDeepestLeaves($root) {
        return $this->dfs($root)[0];
    }

    private function dfs($node) {
        if ($node === null) return [null, 0];
        [$lNode, $lDepth] = $this->dfs($node->left);
        [$rNode, $rDepth] = $this->dfs($node->right);
        if ($lDepth > $rDepth) return [$lNode, $lDepth + 1];
        if ($rDepth > $lDepth) return [$rNode, $rDepth + 1];
        return [$node, $lDepth + 1];
    }
}
