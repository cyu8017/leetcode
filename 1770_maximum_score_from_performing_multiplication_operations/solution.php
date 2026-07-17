<?php
// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[] $multipliers
     * @return Integer
     */
    function maximumScore($nums, $multipliers) {
        $n = count($nums);
        $m = count($multipliers);
        $next = array_fill(0, $m + 1, 0);
        for ($i = $m - 1; $i >= 0; $i--) {
            $cur = array_fill(0, $m + 1, 0);
            for ($left = $i; $left >= 0; $left--) {
                $right = $n - 1 - ($i - $left);
                $takeLeft = $nums[$left] * $multipliers[$i] + $next[$left + 1];
                $takeRight = $nums[$right] * $multipliers[$i] + $next[$left];
                $cur[$left] = max($takeLeft, $takeRight);
            }
            $next = $cur;
        }
        return $next[0];
    }
}
