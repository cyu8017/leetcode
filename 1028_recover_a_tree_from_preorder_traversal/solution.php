<?php
// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

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
     * @param String $traversal
     * @return TreeNode
     */
    function recoverFromPreorder($traversal) {
        $stack = [];
        $i = 0;
        $n = strlen($traversal);
        while ($i < $n) {
            $depth = 0;
            while ($i < $n && $traversal[$i] === '-') {
                $depth++;
                $i++;
            }
            $start = $i;
            while ($i < $n && ctype_digit($traversal[$i])) {
                $i++;
            }
            $node = new TreeNode(intval(substr($traversal, $start, $i - $start)));
            while (count($stack) > $depth) {
                array_pop($stack);
            }
            if (!empty($stack)) {
                $parent = $stack[count($stack) - 1];
                if ($parent->left === null) {
                    $parent->left = $node;
                } else {
                    $parent->right = $node;
                }
            }
            $stack[] = $node;
        }
        return $stack[0];
    }
}
