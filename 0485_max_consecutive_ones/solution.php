<?php
// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

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
        $best = 0;
        $current = 0;
        foreach ($nums as $num) {
            if ($num === 1) {
                $current++;
                $best = max($best, $current);
            } else {
                $current = 0;
            }
        }
        return $best;
    }
}
