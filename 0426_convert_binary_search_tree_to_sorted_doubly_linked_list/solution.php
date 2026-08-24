<?php
// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

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
    /** @var TreeNode|null */
    private $first = null;
    /** @var TreeNode|null */
    private $last = null;

    /**
     * @param TreeNode|null $root
     * @return TreeNode|null
     */
    function treeToDoublyList($root) {
        return $this->tree_to_doubly_list($root);
    }

    /**
     * @param TreeNode|null $root
     * @return TreeNode|null
     */
    function tree_to_doubly_list($root) {
        if ($root === null) {
            return null;
        }

        $this->first = null;
        $this->last = null;
        $this->inorder($root);
        if ($this->first !== null && $this->last !== null) {
            $this->first->left = $this->last;
            $this->last->right = $this->first;
        }
        return $this->first;
    }

    /**
     * @param TreeNode|null $node
     */
    private function inorder($node) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left);
        if ($this->last !== null) {
            $this->last->right = $node;
            $node->left = $this->last;
        } else {
            $this->first = $node;
        }
        $this->last = $node;
        $this->inorder($node->right);
    }
}
