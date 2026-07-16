<?php
// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    /** @var int */
    private $running = 0;

    /**
     * @param TreeNode|null $root
     * @return void
     */
    function convertBST($root) {
        $this->convert_bst($root);
    }

    /**
     * @param TreeNode|null $root
     * @return void
     */
    function convert_bst($root) {
        $this->running = 0;
        $reverseInorder = function ($node) use (&$reverseInorder) {
            if ($node === null) {
                return;
            }
            $reverseInorder($node->right);
            $this->running += $node->val;
            $node->val = $this->running;
            $reverseInorder($node->left);
        };
        $reverseInorder($root);
    }
}
