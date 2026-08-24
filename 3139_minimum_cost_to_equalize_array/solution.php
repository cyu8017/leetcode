<?php
// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution {
    function minCostToEqualizeArray($nums, $cost1, $cost2) {
        $MOD = 1000000007;
        $n = count($nums);
        $minNum = min($nums);
        $maxNum = max($nums);
        $sum = array_sum($nums);
        if ($cost1 * 2 <= $cost2 || $n < 3) {
            $totalGap = $maxNum * $n - $sum;
            return ($cost1 * $totalGap) % $MOD;
        }
        $ans = PHP_INT_MAX;
        for ($target = $maxNum; $target < 2 * $maxNum; $target++) {
            $maxGap = $target - $minNum;
            $totalGap = $target * $n - $sum;
            $pairs = intdiv($totalGap, 2);
            $alt = $totalGap - $maxGap;
            if ($alt < $pairs) $pairs = $alt;
            $cost = $cost1 * ($totalGap - 2 * $pairs) + $cost2 * $pairs;
            $ans = min($ans, $cost);
        }
        return $ans % $MOD;
    }
}
