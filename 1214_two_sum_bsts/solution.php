<?php
// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class Solution {
    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @param Integer $target
     * @return Boolean
     */
    function twoSumBSTs($root1, $root2, $target) {
        $values = [];
        $stack = $root1 !== null ? [$root1] : [];
        while (!empty($stack)) {
            $node = array_pop($stack);
            $values[$node->val] = true;
            if ($node->left !== null) $stack[] = $node->left;
            if ($node->right !== null) $stack[] = $node->right;
        }
        $stack = $root2 !== null ? [$root2] : [];
        while (!empty($stack)) {
            $node = array_pop($stack);
            if (isset($values[$target - $node->val])) return true;
            if ($node->left !== null) $stack[] = $node->left;
            if ($node->right !== null) $stack[] = $node->right;
        }
        return false;
    }
}
