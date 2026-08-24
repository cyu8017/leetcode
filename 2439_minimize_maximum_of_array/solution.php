<?php
// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
    function minimizeArrayValue($nums) {
        $sum = 0;
        $ans = 0;
        for ($i = 0; $i < count($nums); $i++) {
            $sum += $nums[$i];
            $avg = intdiv($sum + $i, $i + 1);
            if ($avg > $ans) $ans = $avg;
        }
        return $ans;
    }
}
