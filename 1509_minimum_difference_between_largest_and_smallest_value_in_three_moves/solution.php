<?php
// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDifference($nums) {
        if (count($nums) <= 4) {
            return 0;
        }
        sort($nums);
        $ans = PHP_INT_MAX;
        for ($i = 0; $i < 4; $i++) {
            $ans = min($ans, $nums[count($nums) - 4 + $i] - $nums[$i]);
        }
        return $ans;
    }
}
