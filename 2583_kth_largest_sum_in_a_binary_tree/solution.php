<?php
// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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
    function kthLargestLevelSum($root, $k) {
        if (!$root) return -1;
        $sums = [];
        $q = [$root];
        while ($q) {
            $sz = count($q);
            $s = 0;
            for ($i = 0; $i < $sz; $i++) {
                $node = array_shift($q);
                $s += $node->val;
                if ($node->left) $q[] = $node->left;
                if ($node->right) $q[] = $node->right;
            }
            $sums[] = $s;
        }
        rsort($sums);
        if ($k > count($sums)) return -1;
        return $sums[$k - 1];
    }
}
