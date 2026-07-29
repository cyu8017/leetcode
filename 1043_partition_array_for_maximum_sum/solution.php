<?php
// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function maxSumAfterPartitioning($arr, $k) {
        $n = count($arr);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $best = 0;
            for ($size = 1; $size <= min($k, $i); $size++) {
                $best = max($best, $arr[$i - $size]);
                $dp[$i] = max($dp[$i], $dp[$i - $size] + $best * $size);
            }
        }
        return $dp[$n];
    }
}
