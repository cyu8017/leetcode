<?php
// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node {
    public $val = null;
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    function preorder($root) {
        $result = [];
        $dfs = function($node) use (&$dfs, &$result) {
            if ($node == null) return;
            $result[] = $node->val;
            if ($node->children) foreach ($node->children as $child) $dfs($child);
        };
        $dfs($root);
        return $result;
    }
}
