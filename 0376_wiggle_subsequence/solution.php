<?php
// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function wiggleMaxLength($nums) {
        return $this->wiggle_max_length($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function wiggle_max_length($nums) {
        $length = count($nums);
        if ($length < 2) {
            return $length;
        }

        $up = 1;
        $down = 1;
        for ($index = 1; $index < $length; $index++) {
            if ($nums[$index] > $nums[$index - 1]) {
                $up = $down + 1;
            } elseif ($nums[$index] < $nums[$index - 1]) {
                $down = $up + 1;
            }
        }

        return max($up, $down);
    }
}
