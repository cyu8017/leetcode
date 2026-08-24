<?php
// LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

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
    public $g;
    public $vis;
    function dfs($node, $p) {
        if (!$node) return;
        $this->g[spl_object_id($node)] = [$p, $node->left, $node->right];
        $this->dfs($node->left, $node);
        $this->dfs($node->right, $node);
    }
    function dfs2($node) {
        if (!$node || ($this->vis[$node->val] ?? false) === true) return 0;
        $this->vis[$node->val] = true;
        $res = $node->val;
        $best = 0;
        foreach ($this->g[spl_object_id($node)] as $nxt) $best = max($best, $this->dfs2($nxt));
        $this->vis[$node->val] = false;
        return $res + $best;
    }
    function collect($node, &$nodes) {
        if (!$node) return;
        $nodes[] = $node;
        $this->collect($node->left, $nodes);
        $this->collect($node->right, $nodes);
    }
    function maxSum($root) {
        $this->g = [];
        $this->vis = [];
        $this->dfs($root, null);
        $nodes = [];
        $this->collect($root, $nodes);
        $ans = PHP_INT_MIN;
        foreach ($nodes as $node) {
            $ans = max($ans, $this->dfs2($node));
            $this->vis = [];
        }
        return $ans;
    }
}
