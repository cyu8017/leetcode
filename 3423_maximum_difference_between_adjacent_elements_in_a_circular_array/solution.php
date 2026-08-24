<?php
// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution {
    function maxAdjacentDistance($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $d = abs($nums[$i] - $nums[($i + 1) % $n]);
            if ($d > $ans) $ans = $d;
        }
        return $ans;
    }
}
