<?php
// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function largestSubarray($nums, $k) {
        $start = 0;
        $n = count($nums);
        for ($i = 1; $i + $k <= $n; $i++) {
            if ($nums[$i] > $nums[$start]) {
                $start = $i;
            }
        }
        return array_slice($nums, $start, $k);
    }
}
