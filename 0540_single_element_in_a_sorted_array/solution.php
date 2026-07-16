<?php
// LeetCode 0540 - Single Element in a Sorted Array
// https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNonDuplicate($nums) {
        return $this->single_non_duplicate($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function single_non_duplicate($nums) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($mid % 2 === 1) {
                $mid--;
            }
            if ($nums[$mid] === $nums[$mid + 1]) {
                $left = $mid + 2;
            } else {
                $right = $mid;
            }
        }
        return $nums[$left];
    }
}
