<?php
// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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
    private $i = 0;
    private $preorder;

    /**
     * @param Integer[] $preorder
     * @return TreeNode
     */
    function bstFromPreorder($preorder) {
        $this->i = 0;
        $this->preorder = $preorder;
        return $this->build(PHP_INT_MAX);
    }

    private function build($bound) {
        if ($this->i === count($this->preorder) || $this->preorder[$this->i] > $bound) {
            return null;
        }
        $root = new TreeNode($this->preorder[$this->i]);
        $this->i++;
        $root->left = $this->build($root->val);
        $root->right = $this->build($bound);
        return $root;
    }
}
