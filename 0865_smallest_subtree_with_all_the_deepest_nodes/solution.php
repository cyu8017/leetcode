<?php
// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

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
     * @return TreeNode
     */
    function subtreeWithAllDeepest($root) {
        $dfs = function($node) use (&$dfs) {
            if ($node === null) return [0, null];
            $left = $dfs($node->left);
            $right = $dfs($node->right);
            if ($left[0] > $right[0]) return [$left[0] + 1, $left[1]];
            if ($right[0] > $left[0]) return [$right[0] + 1, $right[1]];
            return [$left[0] + 1, $node];
        };
        return $dfs($root)[1];
    }
}
