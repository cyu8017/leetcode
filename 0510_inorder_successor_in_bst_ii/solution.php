<?php
// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node {
    public $val = 0;
    public $left = null;
    public $right = null;
    public $parent = null;

    function __construct($val = 0, $left = null, $right = null, $parent = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
        $this->parent = $parent;
    }
}

class Solution {
    /**
     * @param Node $node
     * @return Node|null
     */
    function inorderSuccessor($node) {
        return $this->inorder_successor($node);
    }

    /**
     * @param Node $node
     * @return Node|null
     */
    function inorder_successor($node) {
        if ($node->right !== null) {
            $current = $node->right;
            while ($current->left !== null) {
                $current = $current->left;
            }
            return $current;
        }
        $current = $node;
        while ($current->parent !== null && $current === $current->parent->right) {
            $current = $current->parent;
        }
        return $current->parent;
    }
}
