<?php
// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution {
    /**
     * @param int[] $nums
     * @return int
     */
    function findMaxConsecutiveOnes($nums) {
        return $this->find_max_consecutive_ones($nums);
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function find_max_consecutive_ones($nums) {
        $left = 0;
        $best = 0;
        $zeros = 0;
        $count = count($nums);
        for ($right = 0; $right < $count; $right++) {
            if ($nums[$right] === 0) {
                $zeros++;
            }
            while ($zeros > 1) {
                if ($nums[$left] === 0) {
                    $zeros--;
                }
                $left++;
            }
            $best = max($best, $right - $left + 1);
        }
        return $best;
    }
}
