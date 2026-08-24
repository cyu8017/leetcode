<?php
// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function largestSumOfAverages($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dp = array_fill(0, $n, 0.0);
        for ($i = 0; $i < $n; $i++) $dp[$i] = ($prefix[$i + 1] - $prefix[0]) / ($i + 1);
        for ($groups = 2; $groups <= $k; $groups++) {
            $nxt = array_fill(0, $n, 0.0);
            for ($i = $groups - 1; $i < $n; $i++) {
                $best = 0.0;
                for ($j = $groups - 2; $j < $i; $j++) {
                    $best = max($best, $dp[$j] + ($prefix[$i + 1] - $prefix[$j + 1]) / ($i - $j));
                }
                $nxt[$i] = $best;
            }
            $dp = $nxt;
        }
        return $dp[$n - 1];
    }
}
