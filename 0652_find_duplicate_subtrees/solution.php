<?php
// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val; $this->left = $left; $this->right = $right;
    }
}

class Solution {
    function findDuplicateSubtrees($root) {
        $counts = [];
        $result = [];
        $serialize = function($node) use (&$serialize, &$counts, &$result) {
            if ($node == null) return "#";
            $key = $node->val . "," . $serialize($node->left) . "," . $serialize($node->right);
            $count = ($counts[$key] ?? 0) + 1;
            $counts[$key] = $count;
            if ($count === 2) $result[] = $node;
            return $key;
        };
        $serialize($root);
        return $result;
    }
}
