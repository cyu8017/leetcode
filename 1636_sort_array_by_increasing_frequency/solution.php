<?php
// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function frequencySort($nums) {
        $count = array_count_values($nums);
        usort($nums, function ($a, $b) use ($count) {
            if ($count[$a] === $count[$b]) {
                return $b <=> $a;
            }
            return $count[$a] <=> $count[$b];
        });
        return $nums;
    }
}
