<?php
// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumAfterOperation($nums) {
        $noSquare = 0;
        $oneSquare = 0;
        $best = PHP_INT_MIN;
        foreach ($nums as $value) {
            $oneSquare = max($oneSquare + $value, $noSquare + $value * $value, $value * $value);
            $noSquare = max($noSquare + $value, $value);
            $best = max($best, $oneSquare);
        }
        return $best;
    }
}
