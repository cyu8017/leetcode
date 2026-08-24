<?php
// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution {
    function smallestTrimmedNumbers($nums, $queries) {
        $n = count($nums);
        $m = count($queries);
        $ans = array_fill(0, $m, 0);
        for ($qi = 0; $qi < $m; $qi++) {
            $k = $queries[$qi][0];
            $trim = $queries[$qi][1];
            $arr = [];
            for ($i = 0; $i < $n; $i++) {
                $s = $nums[$i];
                $arr[] = [substr($s, -$trim), $i];
            }
            usort($arr, function($a, $b) {
                if ($a[0] !== $b[0]) return $a[0] < $b[0] ? -1 : 1;
                return $a[1] - $b[1];
            });
            $ans[$qi] = $arr[$k - 1][1];
        }
        return $ans;
    }
}
