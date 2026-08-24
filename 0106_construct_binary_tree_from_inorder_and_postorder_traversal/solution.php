<?php
// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    private $postIndex;
    private $postorder;
    private $index;

    /**
     * @param Integer[] $inorder
     * @param Integer[] $postorder
     * @return TreeNode
     */
    function buildTree($inorder, $postorder) {
        $this->postorder = $postorder;
        $this->postIndex = count($postorder) - 1;
        $this->index = [];
        foreach ($inorder as $i => $v) {
            $this->index[$v] = $i;
        }
        return $this->build(0, count($inorder) - 1);
    }

    private function build($left, $right) {
        if ($left > $right) {
            return null;
        }
        $rootVal = $this->postorder[$this->postIndex--];
        $mid = $this->index[$rootVal];
        $root = new TreeNode($rootVal);
        $root->right = $this->build($mid + 1, $right);
        $root->left = $this->build($left, $mid - 1);
        return $root;
    }
}
