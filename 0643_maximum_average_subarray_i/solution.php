<?php
// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

class Solution {
    function findMaxAverage($nums, $k) {
        $window = 0;
        for ($i = 0; $i < $k; ++$i) $window += $nums[$i];
        $best = $window;
        for ($i = $k; $i < count($nums); ++$i) {
            $window += $nums[$i] - $nums[$i - $k];
            $best = max($best, $window);
        }
        return $best / $k;
    }
}
