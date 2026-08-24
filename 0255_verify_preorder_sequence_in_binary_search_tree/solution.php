<?php
// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

class Solution {
    /**
     * @param Integer[] $preorder
     * @return Boolean
     */
    function verifyPreorder($preorder) {
        $low = PHP_INT_MIN;
        $stack = [];

        foreach ($preorder as $value) {
            if ($value < $low) {
                return false;
            }
            while (!empty($stack) && $stack[count($stack) - 1] < $value) {
                $low = array_pop($stack);
            }
            $stack[] = $value;
        }

        return true;
    }
}
