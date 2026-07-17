<?php
// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumScore($nums, $k) {
        $n = count($nums);
        $stack = [];
        $ans = 0;
        for ($i = 0; $i <= $n; $i++) {
            while (!empty($stack) && ($i === $n || $nums[$i] < $nums[end($stack)])) {
                $mid = array_pop($stack);
                $left = !empty($stack) ? end($stack) + 1 : 0;
                $right = $i - 1;
                if ($left <= $k && $k <= $right) {
                    $ans = max($ans, $nums[$mid] * ($right - $left + 1));
                }
            }
            $stack[] = $i;
        }
        return $ans;
    }
}
