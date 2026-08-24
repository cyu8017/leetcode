<?php
// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution {
    function maxSubarrayLength($nums, $k) {
        $freq = [];
        $ans = 0;
        $left = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $freq[$nums[$right]] = ($freq[$nums[$right]] ?? 0) + 1;
            while ($freq[$nums[$right]] > $k) {
                $freq[$nums[$left]]--;
                $left++;
            }
            if ($right - $left + 1 > $ans) $ans = $right - $left + 1;
        }
        return $ans;
    }
}
