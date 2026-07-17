<?php
// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minMoves($nums, $k) {
        $adjusted = [];
        foreach ($nums as $i => $v) {
            if ($v === 1) {
                $adjusted[] = $i - count($adjusted);
            }
        }
        $m = count($adjusted);
        $prefix = [0];
        foreach ($adjusted as $value) {
            $prefix[] = $prefix[count($prefix) - 1] + $value;
        }
        $best = PHP_INT_MAX;
        for ($left = 0; $left + $k <= $m; $left++) {
            $right = $left + $k;
            $mid = $left + intdiv($k, 2);
            $median = $adjusted[$mid];
            $cost = $median * ($mid - $left) - ($prefix[$mid] - $prefix[$left]);
            $cost += ($prefix[$right] - $prefix[$mid + 1]) - $median * ($right - $mid - 1);
            $best = min($best, $cost);
        }
        return $best;
    }
}
