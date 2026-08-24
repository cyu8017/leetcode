<?php
// LeetCode 3914 - Minimum Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    function minOperations($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $ans += max(0, $nums[$i - 1] - $nums[$i]);
        }
        return $ans;
    }
}
