<?php
// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
    private $count = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function countUnivalSubtrees($root) {
        $this->count = 0;
        $this->dfs($root);
        return $this->count;
    }

    private function dfs($node) {
        if ($node === null) {
            return true;
        }
        $leftOk = $this->dfs($node->left);
        $rightOk = $this->dfs($node->right);
        if (!$leftOk || !$rightOk) {
            return false;
        }
        if ($node->left !== null && $node->left->val !== $node->val) {
            return false;
        }
        if ($node->right !== null && $node->right->val !== $node->val) {
            return false;
        }
        $this->count++;
        return true;
    }
}
