<?php
// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution {
    function minRectanglesToCoverPoints($points, $w) {
        usort($points, function ($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $x1 = -1;
        foreach ($points as $p) {
            if ($p[0] > $x1) {
                $ans++;
                $x1 = $p[0] + $w;
            }
        }
        return $ans;
    }
}
