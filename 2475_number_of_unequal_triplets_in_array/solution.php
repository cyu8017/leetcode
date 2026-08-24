<?php
// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution {
    function unequalTriplets($nums) {
        $cnt = [];
        foreach ($nums as $x) {
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
        }
        $ans = 0;
        $left = 0;
        $n = count($nums);
        foreach ($cnt as $c) {
            $right = $n - $left - $c;
            $ans += $left * $c * $right;
            $left += $c;
        }
        return $ans;
    }
}
