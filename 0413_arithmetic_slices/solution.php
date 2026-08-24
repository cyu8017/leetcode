<?php
// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfArithmeticSlices($nums) {
        return $this->number_of_arithmetic_slices($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function number_of_arithmetic_slices($nums) {
        if (count($nums) < 3) {
            return 0;
        }

        $total = 0;
        $current = 0;
        for ($index = 2; $index < count($nums); $index++) {
            if ($nums[$index] - $nums[$index - 1] === $nums[$index - 1] - $nums[$index - 2]) {
                $current++;
                $total += $current;
            } else {
                $current = 0;
            }
        }
        return $total;
    }
}
