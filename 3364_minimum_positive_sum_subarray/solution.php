<?php
// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution {
    function minimumSumSubarray($nums, $l, $r) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 2147483647;
        $found = false;
        for ($i = 0; $i < $n; $i++) {
            for ($length = $l; $length <= $r && $i + $length <= $n; $length++) {
                $s = $pref[$i + $length] - $pref[$i];
                if ($s > 0 && $s < $ans) {
                    $ans = $s;
                    $found = true;
                }
            }
        }
        return $found ? $ans : -1;
    }
}
