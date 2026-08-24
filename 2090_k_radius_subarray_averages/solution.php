<?php
// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function getAverages($nums, $k) {
        $n = count($nums);
        $ans = array_fill(0, $n, -1);
        if (2 * $k + 1 > $n) return $ans;
        $sum = 0;
        for ($i = 0; $i < 2 * $k + 1; $i++) $sum += $nums[$i];
        $ans[$k] = intdiv($sum, 2 * $k + 1);
        for ($i = $k + 1; $i + $k < $n; $i++) {
            $sum += $nums[$i + $k] - $nums[$i - $k - 1];
            $ans[$i] = intdiv($sum, 2 * $k + 1);
        }
        return $ans;
    }
}
