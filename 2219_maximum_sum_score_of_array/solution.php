<?php
// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution {
    function solve($nums) {
        $total = 0;
        $pref = 0;
        foreach ($nums as $x) $total += $x;
        $ans = PHP_INT_MIN;
        foreach ($nums as $x) {
            $pref += $x;
            $ans = max($ans, max($pref, $total - $pref + $x));
        }
        return $ans;
    }
}
