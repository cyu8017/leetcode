<?php
// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

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
    function findClosestLeaf($root, $k) {
        $graph = [];
        $leaves = [];
        $build = function ($node, $parent) use (&$build, &$graph, &$leaves) {
            if ($node === null) return;
            if (!isset($graph[$node->val])) $graph[$node->val] = [];
            if ($parent !== null) {
                if (!isset($graph[$parent->val])) $graph[$parent->val] = [];
                $graph[$node->val][] = $parent->val;
                $graph[$parent->val][] = $node->val;
            }
            if ($node->left === null && $node->right === null) $leaves[$node->val] = true;
            $build($node->right, $node);
            $build($node->left, $node);
        };
        $build($root, null);
        $q = [$k];
        $seen = [$k => true];
        while (count($q) > 0) {
            $value = array_shift($q);
            if (isset($leaves[$value])) return $value;
            if (!isset($graph[$value])) continue;
            foreach ($graph[$value] as $neighbor) {
                if (!isset($seen[$neighbor])) {
                    $seen[$neighbor] = true;
                    $q[] = $neighbor;
                }
            }
        }
        return -1;
    }
}
