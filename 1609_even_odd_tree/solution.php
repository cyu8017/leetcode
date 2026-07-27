<?php
// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

class Solution {
    /**
     * @param TreeNode $root
     * @return Boolean
     */
    function isEvenOddTree($root) {
        $q = [$root];
        $level = 0;
        while ($q) {
            $prev = $level % 2 === 0 ? PHP_INT_MIN : PHP_INT_MAX;
            $nxt = [];
            foreach ($q as $node) {
                if ($node->val % 2 === $level % 2) {
                    return false;
                }
                if ($level % 2 === 0 && $node->val <= $prev) {
                    return false;
                }
                if ($level % 2 === 1 && $node->val >= $prev) {
                    return false;
                }
                $prev = $node->val;
                if ($node->left) {
                    $nxt[] = $node->left;
                }
                if ($node->right) {
                    $nxt[] = $node->right;
                }
            }
            $q = $nxt;
            $level++;
        }
        return true;
    }
}
