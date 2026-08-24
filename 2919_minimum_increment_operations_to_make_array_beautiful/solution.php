<?php
// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution {
    function minIncrementOperations($nums, $k) {
        $dp0 = 0;
        $dp1 = 0;
        $dp2 = 0;
        foreach ($nums as $v) {
            $cost = $v < $k ? $k - $v : 0;
            $nd0 = $cost + min($dp0, $dp1, $dp2);
            $dp0 = $dp1;
            $dp1 = $dp2;
            $dp2 = $nd0;
        }
        return min($dp0, $dp1, $dp2);
    }
}
