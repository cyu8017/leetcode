<?php
// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node {
    public $val = null;
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    function postorder($root) {
        $result = [];
        $dfs = function($node) use (&$dfs, &$result) {
            if ($node == null) return;
            if ($node->children) foreach ($node->children as $child) $dfs($child);
            $result[] = $node->val;
        };
        $dfs($root);
        return $result;
    }
}
