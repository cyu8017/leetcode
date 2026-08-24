<?php
// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    function minCost($nums, $x) {
        $n = count($nums);
        $best = $nums;
        $ans = 0;
        foreach ($nums as $v) $ans += $v;
        for ($rot = 1; $rot < $n; $rot++) {
            $cur = $rot * $x;
            for ($i = 0; $i < $n; $i++) {
                $best[$i] = min($best[$i], $nums[($i + $rot) % $n]);
                $cur += $best[$i];
            }
            $ans = min($ans, $cur);
        }
        return $ans;
    }
}
