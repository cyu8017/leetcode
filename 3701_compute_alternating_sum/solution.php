<?php
// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

class Solution {
    function alternatingSum($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $ans += $nums[$i];
            else $ans -= $nums[$i];
        }
        return $ans;
    }
}
