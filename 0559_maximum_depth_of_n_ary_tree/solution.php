<?php
// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node {
    public $val = null;
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    function maxDepth($root) {
        if ($root == null) return 0;
        if (!$root->children || count($root->children) === 0) return 1;
        $best = 0;
        foreach ($root->children as $child) $best = max($best, $this->maxDepth($child));
        return $best + 1;
    }
}
