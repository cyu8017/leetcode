<?php
// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

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
     * @param Integer[][] $descriptions
     * @return TreeNode
     */
    function createBinaryTree($descriptions) {
        $nodes = [];
        $child = [];
        foreach ($descriptions as $d) {
            $p = $d[0];
            $c = $d[1];
            $isLeft = $d[2];
            if (!isset($nodes[$p])) $nodes[$p] = new TreeNode($p);
            if (!isset($nodes[$c])) $nodes[$c] = new TreeNode($c);
            if ($isLeft === 1) $nodes[$p]->left = $nodes[$c];
            else $nodes[$p]->right = $nodes[$c];
            $child[$c] = true;
        }
        foreach ($nodes as $k => $v)
            if (!isset($child[$k])) return $v;
        return null;
    }
}
