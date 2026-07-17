<?php
// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution {
    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer[][] $points
     * @return Integer
     */
    function nearestValidPoint($x, $y, $points) {
        $best = PHP_INT_MAX;
        $ans = -1;
        foreach ($points as $i => $point) {
            $px = $point[0];
            $py = $point[1];
            if ($px !== $x && $py !== $y) {
                continue;
            }
            $dist = abs($px - $x) + abs($py - $y);
            if ($dist < $best) {
                $best = $dist;
                $ans = $i;
            }
        }
        return $ans;
    }
}
