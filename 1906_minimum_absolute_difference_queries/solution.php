<?php
// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution {
    function minDifference($nums, $queries) {
        $n = count($nums);
        $pref = [];
        for ($i = 0; $i <= $n; $i++) {
            $pref[$i] = array_fill(0, 101, 0);
        }
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i];
            $pref[$i + 1][$nums[$i]]++;
        }
        $ans = [];
        foreach ($queries as $q) {
            $left = $q[0];
            $right = $q[1];
            $prev = -1;
            $best = PHP_INT_MAX;
            for ($value = 1; $value <= 100; $value++) {
                if ($pref[$right + 1][$value] - $pref[$left][$value] > 0) {
                    if ($prev !== -1) {
                        $best = min($best, $value - $prev);
                    }
                    $prev = $value;
                }
            }
            $ans[] = $best === PHP_INT_MAX ? -1 : $best;
        }
        return $ans;
    }
}
