<?php
// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution {
    function maxSumOfThreeSubarrays($nums, $k) {
        $n = count($nums);
        $windows = $n - $k + 1;
        $sums = array_fill(0, $windows, 0);
        $total = 0;
        for ($i = 0; $i < $k; $i++) $total += $nums[$i];
        $sums[0] = $total;
        for ($i = 1; $i < $windows; $i++) {
            $total += $nums[$i + $k - 1] - $nums[$i - 1];
            $sums[$i] = $total;
        }
        $left = array_fill(0, $windows, 0);
        $best = 0;
        for ($i = 0; $i < $windows; $i++) {
            if ($sums[$i] > $sums[$best]) $best = $i;
            $left[$i] = $best;
        }
        $right = array_fill(0, $windows, 0);
        $best = $windows - 1;
        for ($i = $windows - 1; $i >= 0; $i--) {
            if ($sums[$i] >= $sums[$best]) $best = $i;
            $right[$i] = $best;
        }
        $answer = [0, 0, 0];
        $bestTotal = -1;
        for ($mid = $k; $mid < $windows - $k; $mid++) {
            $l = $left[$mid - $k];
            $r = $right[$mid + $k];
            $cur = $sums[$l] + $sums[$mid] + $sums[$r];
            if ($cur > $bestTotal) {
                $bestTotal = $cur;
                $answer = [$l, $mid, $r];
            }
        }
        return $answer;
    }
}
