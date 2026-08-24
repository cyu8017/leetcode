<?php
// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution {
    function maxTotalValue($nums, $k) {
        $mn = $nums[0];
        $mx = $nums[0];
        foreach ($nums as $x) {
            $mn = min($mn, $x);
            $mx = max($mx, $x);
        }
        return $k * ($mx - $mn);
    }
}
