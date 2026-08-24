<?php
// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

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
    function reverseOddLevels($root) {
        if ($root !== null) $this->dfs($root->left, $root->right, 1);
        return $root;
    }

    private function dfs($a, $b, $level) {
        if ($a === null || $b === null) return;
        if ($level % 2 === 1) {
            $tmp = $a->val;
            $a->val = $b->val;
            $b->val = $tmp;
        }
        $this->dfs($a->left, $b->right, $level + 1);
        $this->dfs($a->right, $b->left, $level + 1);
    }
}
