<?php
// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxWidthOfVerticalArea($points) {
        $xs = array_map(fn($p) => $p[0], $points);
        sort($xs);
        $ans = 0;
        for ($i = 1; $i < count($xs); $i++) {
            $ans = max($ans, $xs[$i] - $xs[$i - 1]);
        }
        return $ans;
    }
}
