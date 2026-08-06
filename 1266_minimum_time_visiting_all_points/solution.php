<?php
// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $ans = 0;
        $n = count($points);
        for ($i = 0; $i < $n - 1; $i++) {
            $ans += max(abs($points[$i][0] - $points[$i + 1][0]), abs($points[$i][1] - $points[$i + 1][1]));
        }
        return $ans;
    }
}
