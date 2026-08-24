<?php
// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    function leftRightDifference($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $left = 0;
        for ($i = 0; $i < $n; $i++) {
            $right = $total - $left - $nums[$i];
            $ans[$i] = abs($left - $right);
            $left += $nums[$i];
        }
        return $ans;
    }
}
