<?php
// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

class Solution {
    /**
     * @param int[] $nums
     * @return bool
     */
    function find132pattern($nums) {
        $stack = [];
        $third = PHP_INT_MIN;

        for ($index = count($nums) - 1; $index >= 0; $index--) {
            $value = $nums[$index];
            if ($value < $third) {
                return true;
            }
            while (!empty($stack) && $value > $stack[count($stack) - 1]) {
                $third = array_pop($stack);
            }
            $stack[] = $value;
        }

        return false;
    }
}
