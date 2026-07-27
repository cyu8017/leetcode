<?php
// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

class Solution {
    function maximumUniqueSubarray($nums) {
        $seen = [];
        $left = 0;
        $cur = 0;
        $best = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $x = $nums[$right];
            if (isset($seen[$x]) && $seen[$x] >= $left) {
                $stop = $seen[$x];
                while ($left <= $stop) {
                    $cur -= $nums[$left];
                    $left++;
                }
            }
            $seen[$x] = $right;
            $cur += $x;
            $best = max($best, $cur);
        }
        return $best;
    }
}
