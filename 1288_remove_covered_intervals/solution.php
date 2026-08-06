<?php
// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        usort($intervals, function ($a, $b) {
            if ($a[0] === $b[0]) return $b[1] <=> $a[1];
            return $a[0] <=> $b[0];
        });
        $answer = 0;
        $farthest = -1;
        foreach ($intervals as [, $end]) {
            if ($end > $farthest) {
                $answer++;
                $farthest = $end;
            }
        }
        return $answer;
    }
}
