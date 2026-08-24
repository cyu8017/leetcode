<?php
// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode {
    public $len = 0;
    public $val = "";
    public $left = null;
    public $right = null;
    function __construct($len = 0, $val = "", $left = null, $right = null) {
        $this->len = $len;
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function getKthCharacter($root, $k) {
        $dfs = function($node, $kk) use (&$dfs) {
            if ($node->left === null && $node->right === null) return $node->val;
            $leftLen = 0;
            if ($node->left) $leftLen = $node->left->len > 0 ? $node->left->len : 1;
            if ($kk <= $leftLen) return $dfs($node->left, $kk);
            return $dfs($node->right, $kk - $leftLen);
        };
        return $dfs($root, $k);
    }
}
