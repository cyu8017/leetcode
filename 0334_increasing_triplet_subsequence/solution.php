<?php
// LeetCode 0334 - Increasing Triplet Subsequence
// https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function increasingTriplet($nums) {
        return $this->increasing_triplet($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function increasing_triplet($nums) {
        $first = PHP_INT_MAX;
        $second = PHP_INT_MAX;
        foreach ($nums as $num) {
            if ($num <= $first) {
                $first = $num;
            } elseif ($num <= $second) {
                $second = $num;
            } else {
                return true;
            }
        }
        return false;
    }
}
