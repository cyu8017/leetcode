<?php
// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

class Solution {
    /**
     * @param String[] $timePoints
     * @return Integer
     */
    function findMinDifference($timePoints) {
        return $this->find_min_difference($timePoints);
    }

    /**
     * @param String[] $timePoints
     * @return Integer
     */
    function find_min_difference($timePoints) {
        $minutes = [];
        foreach ($timePoints as $time) {
            $parts = explode(":", $time);
            $minutes[] = ((int)$parts[0]) * 60 + (int)$parts[1];
        }
        sort($minutes);

        $best = $minutes[count($minutes) - 1] - $minutes[0];
        for ($i = 1; $i < count($minutes); $i++) {
            $best = min($best, $minutes[$i] - $minutes[$i - 1]);
        }
        return min($best, 24 * 60 - $minutes[count($minutes) - 1] + $minutes[0]);
    }
}
