<?php
// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
     * @return String
     */
    function smallestFromLeaf($root) {
        $best = "~";
        $dfs = null;
        $dfs = function ($node, $path) use (&$dfs, &$best) {
            if ($node === null) return;
            $path = chr(97 + $node->val) . $path;
            if ($node->left === null && $node->right === null) {
                if ($path < $best) $best = $path;
                return;
            }
            $dfs($node->left, $path);
            $dfs($node->right, $path);
        };
        $dfs($root, "");
        return $best;
    }
}
