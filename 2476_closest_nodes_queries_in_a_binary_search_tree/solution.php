<?php
// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

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
    function closestNodes($root, $queries) {
        $vals = [];
        $inorder = function ($node) use (&$inorder, &$vals) {
            if ($node === null) return;
            $inorder($node->left);
            $vals[] = $node->val;
            $inorder($node->right);
        };
        $inorder($root);
        $lowerBound = function ($q) use ($vals) {
            $lo = 0;
            $hi = count($vals);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($vals[$mid] < $q) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = [];
        foreach ($queries as $q) {
            $j = $lowerBound($q);
            $mx = $j < count($vals) ? $vals[$j] : -1;
            $mn = -1;
            if ($j < count($vals) && $vals[$j] === $q) $mn = $q;
            elseif ($j > 0) $mn = $vals[$j - 1];
            $ans[] = [$mn, $mx];
        }
        return $ans;
    }
}
