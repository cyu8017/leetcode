<?php
// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function lengthOfLIS($nums) {
        $piles = [];
        foreach ($nums as $num) {
            $left = 0;
            $right = count($piles);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($piles[$mid] < $num) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            if ($left === count($piles)) {
                $piles[] = $num;
            } else {
                $piles[$left] = $num;
            }
        }
        return count($piles);
    }
}
