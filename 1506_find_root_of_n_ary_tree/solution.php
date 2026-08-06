<?php
// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

class Node {
    public $val = null;
    /** @var Node[] */
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    /**
     * @param Node[] $tree
     * @return Node
     */
    function findRoot($tree) {
        $value = 0;
        $nodes = [];
        foreach ($tree as $node) {
            $nodes[$node->val] = $node;
            $value ^= $node->val;
            foreach ($node->children as $child) {
                $value ^= $child->val;
            }
        }
        return $nodes[$value];
    }
}
