<?php
// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

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
    function treeQueries($root, $queries) {
        $height = [];
        $level = [];
        $levelMax = [];
        $dfs = function ($node, $d) use (&$dfs, &$height, &$level, &$levelMax) {
            if ($node === null) return -1;
            $level[$node->val] = $d;
            $h = 1 + max($dfs($node->left, $d + 1), $dfs($node->right, $d + 1));
            $height[$node->val] = $h;
            if (!isset($levelMax[$d])) $levelMax[$d] = [];
            $arr =& $levelMax[$d];
            if (count($arr) === 0) $arr[] = $h;
            elseif ($h >= $arr[0]) {
                if (count($arr) === 1) $arr[] = $arr[0];
                else $arr[1] = $arr[0];
                $arr[0] = $h;
            } elseif (count($arr) === 1 || $h > $arr[1]) {
                if (count($arr) === 1) $arr[] = $h;
                else $arr[1] = $h;
            }
            unset($arr);
            return $h;
        };
        $dfs($root, 0);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $q = $queries[$i];
            $d = $level[$q];
            $h = $height[$q];
            $top = $levelMax[$d];
            if ($top[0] === $h) {
                if (count($top) > 1) $ans[$i] = $d + $top[1];
                else $ans[$i] = $d - 1;
            } else {
                $ans[$i] = $d + $top[0];
            }
        }
        return $ans;
    }
}
