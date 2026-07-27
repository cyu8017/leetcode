<?php
// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution {
    function minOperations($nums, $x) {
        $target = array_sum($nums) - $x;
        if ($target < 0) return -1;
        $best = -1;
        $left = 0;
        $cur = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $cur += $nums[$right];
            while ($cur > $target) {
                $cur -= $nums[$left];
                $left++;
            }
            if ($cur === $target) $best = max($best, $right - $left + 1);
        }
        return $best < 0 ? -1 : $n - $best;
    }
}
