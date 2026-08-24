<?php
// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumDifference($nums) {
        $ans = -1;
        $mn = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $mn) $ans = max($ans, $nums[$i] - $mn);
            else $mn = $nums[$i];
        }
        return $ans;
    }
}
