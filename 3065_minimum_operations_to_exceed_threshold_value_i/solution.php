<?php
// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution {
    function minOperations($nums, $k) {
        $ans = 0;
        foreach ($nums as $x) if ($x < $k) $ans++;
        return $ans;
    }
}
