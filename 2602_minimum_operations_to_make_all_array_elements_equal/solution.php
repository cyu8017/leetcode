<?php
// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution {
    function minOperations($nums, $queries) {
        sort($nums);
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $lowerBound = function($x) use ($nums, $n) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($nums[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = [];
        foreach ($queries as $q) {
            $i = $lowerBound($q);
            $left = $q * $i - $pref[$i];
            $right = $pref[$n] - $pref[$i] - $q * ($n - $i);
            $ans[] = $left + $right;
        }
        return $ans;
    }
}
