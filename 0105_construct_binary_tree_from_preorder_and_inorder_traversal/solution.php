<?php
// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    private $preIndex;
    private $preorder;
    private $index;

    /**
     * @param Integer[] $preorder
     * @param Integer[] $inorder
     * @return TreeNode
     */
    function buildTree($preorder, $inorder) {
        $this->preorder = $preorder;
        $this->preIndex = 0;
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
        $rootVal = $this->preorder[$this->preIndex++];
        $mid = $this->index[$rootVal];
        $root = new TreeNode($rootVal);
        $root->left = $this->build($left, $mid - 1);
        $root->right = $this->build($mid + 1, $right);
        return $root;
    }
}
