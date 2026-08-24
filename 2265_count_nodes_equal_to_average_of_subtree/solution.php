<?php
// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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
    function averageOfSubtree($root) {
        $ans = 0;
        $dfs = function($node) use (&$dfs, &$ans) {
            if ($node === null) return [0, 0];
            $L = $dfs($node->left);
            $R = $dfs($node->right);
            $sum = $L[0] + $R[0] + $node->val;
            $cnt = $L[1] + $R[1] + 1;
            if (intdiv($sum, $cnt) === $node->val) $ans++;
            return [$sum, $cnt];
        };
        $dfs($root);
        return $ans;
    }
}
