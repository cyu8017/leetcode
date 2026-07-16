<?php
// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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
    /**
     * @param TreeNode|null $root
     * @return Integer
     */
    function longestConsecutive($root) {
        $best = 0;
        $dfs = function ($node) use (&$dfs, &$best) {
            if ($node === null) {
                return [0, 0];
            }

            [$leftInc, $leftDec] = $dfs($node->left);
            [$rightInc, $rightDec] = $dfs($node->right);

            $inc = 1;
            $dec = 1;
            if ($node->left !== null) {
                if ($node->left->val === $node->val + 1) {
                    $inc = max($inc, $leftInc + 1);
                } elseif ($node->left->val === $node->val - 1) {
                    $dec = max($dec, $leftDec + 1);
                }
            }
            if ($node->right !== null) {
                if ($node->right->val === $node->val + 1) {
                    $inc = max($inc, $rightInc + 1);
                } elseif ($node->right->val === $node->val - 1) {
                    $dec = max($dec, $rightDec + 1);
                }
            }

            if ($node->left !== null && $node->right !== null) {
                if ($node->left->val + 1 === $node->val && $node->val === $node->right->val - 1) {
                    $best = max($best, $leftDec + 1 + $rightInc);
                }
                if ($node->left->val - 1 === $node->val && $node->val === $node->right->val + 1) {
                    $best = max($best, $leftInc + 1 + $rightDec);
                }
            }

            $best = max($best, $inc, $dec);
            return [$inc, $dec];
        };

        $dfs($root);
        return $best;
    }
}
