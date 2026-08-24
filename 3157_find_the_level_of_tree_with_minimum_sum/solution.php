<?php
// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
    function minimumLevel($root) {
        $q = [$root];
        $s = PHP_INT_MAX;
        $ans = 0;
        for ($level = 1; $q; $level++) {
            $t = 0;
            $m = count($q);
            while ($m-- > 0) {
                $node = array_shift($q);
                $t += $node->val;
                if ($node->left !== null) $q[] = $node->left;
                if ($node->right !== null) $q[] = $node->right;
            }
            if ($s > $t) {
                $s = $t;
                $ans = $level;
            }
        }
        return $ans;
    }
}
