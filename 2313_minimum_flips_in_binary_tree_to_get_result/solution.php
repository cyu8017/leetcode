<?php
// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

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
    function minimumFlips($root, $result) {
        $res = $this->dfs($root);
        return $result ? $res[1] : $res[0];
    }

    private function dfs($node) {
        if ($node->left === null && $node->right === null) {
            return $node->val === 0 ? [0, 1] : [1, 0];
        }
        if ($node->val === 5) {
            $x = $this->dfs($node->left);
            return [$x[1], $x[0]];
        }
        $L = $this->dfs($node->left);
        $R = $this->dfs($node->right);
        $lf = $L[0]; $lt = $L[1]; $rf = $R[0]; $rt = $R[1];
        if ($node->val === 2) {
            return [$lf + $rf, min($lt + $rt, min($lt + $rf, $lf + $rt))];
        }
        if ($node->val === 3) {
            return [min($lf + $rf, min($lf + $rt, $lt + $rf)), $lt + $rt];
        }
        if ($node->val === 4) {
            return [min($lf + $rf, $lt + $rt), min($lf + $rt, $lt + $rf)];
        }
        return [0, 0];
    }
}
