<?php
// LeetCode 3902 - Zigzag Level Sum of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

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
    function zigzagLevelSum($root) {
        $ans = [];
        $q = [$root];
        $left = true;
        while (count($q)) {
            $nq = [];
            foreach ($q as $node) {
                if ($node->left) $nq[] = $node->left;
                if ($node->right) $nq[] = $node->right;
            }
            $m = count($q);
            $s = 0;
            for ($i = 0; $i < $m; $i++) {
                $node = $left ? $q[$i] : $q[$m - $i - 1];
                $child = $left ? $node->left : $node->right;
                if (!$child) break;
                $s += $node->val;
            }
            $ans[] = $s;
            $left = !$left;
            $q = $nq;
        }
        return $ans;
    }
}
