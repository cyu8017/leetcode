<?php
// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution {
    function zeroFilledSubarray($nums) {
        $ans = 0;
        $streak = 0;
        foreach ($nums as $x) {
            if ($x === 0) { $streak++; $ans += $streak; }
            else $streak = 0;
        }
        return $ans;
    }
}
