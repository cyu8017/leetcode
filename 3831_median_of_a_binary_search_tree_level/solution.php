<?php
// LeetCode 3831 - Median of a Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    public $nums;
    public $level;
    function dfs($node, $i) {
        if (!$node) return;
        $this->dfs($node->left, $i + 1);
        if ($i === $this->level) $this->nums[] = $node->val;
        $this->dfs($node->right, $i + 1);
    }
    function levelMedian($root, $level) {
        $this->nums = [];
        $this->level = $level;
        $this->dfs($root, 0);
        if (!count($this->nums)) return -1;
        return $this->nums[intdiv(count($this->nums), 2)];
    }
}
