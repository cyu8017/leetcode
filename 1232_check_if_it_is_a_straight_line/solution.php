<?php
// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution {
    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function checkStraightLine($coordinates) {
        [$x0, $y0] = $coordinates[0];
        $dx = $coordinates[1][0] - $x0;
        $dy = $coordinates[1][1] - $y0;
        $n = count($coordinates);
        for ($i = 2; $i < $n; $i++) {
            [$x, $y] = $coordinates[$i];
            if (($x - $x0) * $dy !== ($y - $y0) * $dx) return false;
        }
        return true;
    }
}
