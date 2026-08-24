<?php
// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

class Solution {
    function solve($nums) {
        $mn = $nums[0];
        $mx = $nums[0];
        $seen = [];
        foreach ($nums as $x) {
            if (isset($seen[$x])) return false;
            $seen[$x] = true;
            $mn = min($mn, $x);
            $mx = max($mx, $x);
        }
        return $mx - $mn + 1 === count($nums);
    }
}
