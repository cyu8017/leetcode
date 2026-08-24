<?php
// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
    function maxIncreasingGroups($usageLimits) {
        $arr = $usageLimits;
        sort($arr);
        $ans = 0;
        $sum = 0;
        foreach ($arr as $v) {
            $sum += $v;
            $need = intdiv(($ans + 1) * ($ans + 2), 2);
            if ($sum >= $need) $ans++;
        }
        return $ans;
    }
}
