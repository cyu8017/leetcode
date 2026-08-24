<?php
// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

class Solution {
    function maxValidPairSum($nums, $k) {
        $ans = 0;
        $x = 0;
        for ($j = $k; $j < count($nums); $j++) {
            $y = $nums[$j];
            $x = max($x, $nums[$j - $k]);
            $ans = max($ans, $x + $y);
        }
        return $ans;
    }
}
