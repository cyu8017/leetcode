<?php
// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minPairSum($nums) {
        sort($nums);
        $n = count($nums);
        $best = 0;
        for ($i = 0; $i < $n / 2; $i++) {
            $best = max($best, $nums[$i] + $nums[$n - 1 - $i]);
        }
        return $best;
    }
}
