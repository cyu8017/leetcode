<?php
// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function check($nums) {
        $n = count($nums);
        $drops = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $nums[($i + 1) % $n]) {
                $drops++;
            }
        }
        return $drops <= 1;
    }
}
