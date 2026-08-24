<?php
// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution {
    function inc($nums, $start, $k) {
        for ($i = $start; $i + 1 < $start + $k; $i++) {
            if ($nums[$i] >= $nums[$i + 1]) return false;
        }
        return true;
    }

    function hasIncreasingSubarrays($nums, $k) {
        $n = count($nums);
        for ($i = 0; $i + 2 * $k <= $n; $i++) {
            if ($this->inc($nums, $i, $k) && $this->inc($nums, $i + $k, $k)) return true;
        }
        return false;
    }
}
