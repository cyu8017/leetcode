<?php
// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution {
    function ok($up, $n, $k) {
        for ($i = 0; $i + 2 * $k <= $n; $i++) {
            if ($up[$i] >= $k && $up[$i + $k] >= $k) return true;
        }
        return false;
    }

    function maxIncreasingSubarrays($nums) {
        $n = count($nums);
        $up = [];
        $up[$n - 1] = 1;
        for ($i = $n - 2; $i >= 0; $i--) {
            $up[$i] = ($nums[$i] < $nums[$i + 1]) ? $up[$i + 1] + 1 : 1;
        }
        $lo = 1;
        $hi = intdiv($n, 2);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->ok($up, $n, $mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
