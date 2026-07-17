<?php
// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $altitude = 0;
        $best = 0;
        foreach ($gain as $change) {
            $altitude += $change;
            $best = max($best, $altitude);
        }
        return $best;
    }
}
