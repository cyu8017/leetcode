<?php
// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function subArrayRanges($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $mn = $nums[$i];
            $mx = $nums[$i];
            for ($j = $i; $j < $n; $j++) {
                $mn = min($mn, $nums[$j]);
                $mx = max($mx, $nums[$j]);
                $ans += $mx - $mn;
            }
        }
        return $ans;
    }
}
