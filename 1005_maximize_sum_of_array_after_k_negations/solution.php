<?php
// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function largestSumAfterKNegations($nums, $k) {
        sort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($k > 0 && $nums[$i] < 0) {
                $nums[$i] = -$nums[$i];
                $k--;
            }
        }
        if ($k % 2 === 1) {
            sort($nums);
            $nums[0] = -$nums[0];
        }
        return array_sum($nums);
    }
}
