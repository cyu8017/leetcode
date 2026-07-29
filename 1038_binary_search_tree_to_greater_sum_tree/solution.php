<?php
// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    private $total = 0;

    /**
     * @param TreeNode $root
     * @return TreeNode
     */
    function bstToGst($root) {
        $this->total = 0;
        $this->reverseInorder($root);
        return $root;
    }

    private function reverseInorder($node) {
        if ($node === null) {
            return;
        }
        $this->reverseInorder($node->right);
        $this->total += $node->val;
        $node->val = $this->total;
        $this->reverseInorder($node->left);
    }
}
