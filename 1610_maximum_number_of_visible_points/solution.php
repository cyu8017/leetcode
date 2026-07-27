<?php
// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

class Solution {
    /**
     * @param Integer[][] $points
     * @param Integer $angle
     * @param Integer[] $location
     * @return Integer
     */
    function visiblePoints($points, $angle, $location) {
        $same = 0;
        $a = [];
        foreach ($points as $p) {
            $dx = $p[0] - $location[0];
            $dy = $p[1] - $location[1];
            if ($dx === 0 && $dy === 0) {
                $same++;
            } else {
                $a[] = atan2($dy, $dx);
            }
        }
        sort($a);
        $ext = $a;
        foreach ($a as $x) {
            $ext[] = $x + 2 * M_PI;
        }
        $width = deg2rad($angle) + 1e-12;
        $left = $best = 0;
        $lenA = count($a);
        foreach ($ext as $right => $value) {
            while ($value - $ext[$left] > $width) {
                $left++;
            }
            $best = max($best, min($lenA, $right - $left + 1));
        }
        return $best + $same;
    }
}
