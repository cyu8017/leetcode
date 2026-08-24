<?php
// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxRotateFunction($nums) {
        return $this->max_rotate_function($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function max_rotate_function($nums) {
        $length = count($nums);
        $total = array_sum($nums);
        $current = 0;
        foreach ($nums as $index => $value) {
            $current += $index * $value;
        }
        $best = $current;

        for ($index = $length - 1; $index > 0; $index--) {
            $current += $total - $length * $nums[$index];
            $best = max($best, $current);
        }

        return $best;
    }
}
