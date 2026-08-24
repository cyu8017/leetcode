<?php
// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
    function distinctDifferenceArray($nums) {
        $n = count($nums);
        $suf = array_fill(0, $n + 1, 0);
        $seen = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            $seen[$nums[$i]] = true;
            $suf[$i] = count($seen);
        }
        $seen = [];
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $seen[$nums[$i]] = true;
            $ans[$i] = count($seen) - $suf[$i + 1];
        }
        return $ans;
    }
}
