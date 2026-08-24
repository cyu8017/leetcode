<?php
// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

class Solution {
    function smallestRangeII($nums, $k) {
        sort($nums);
        $n = count($nums);
        $ans = $nums[$n - 1] - $nums[0];
        for ($i = 0; $i + 1 < $n; $i++) {
            $lo = min($nums[0] + $k, $nums[$i + 1] - $k);
            $hi = max($nums[$n - 1] - $k, $nums[$i] + $k);
            $ans = min($ans, $hi - $lo);
        }
        return $ans;
    }
}
