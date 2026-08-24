<?php
// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution {
    function minOperations($nums, $k) {
        $ans = 0;
        foreach ($nums as $x) $ans = ($ans + $x) % $k;
        return $ans;
    }
}
