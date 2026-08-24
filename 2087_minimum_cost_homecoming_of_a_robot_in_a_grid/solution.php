<?php
// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution {
    /**
     * @param Integer[] $startPos
     * @param Integer[] $homePos
     * @param Integer[] $rowCosts
     * @param Integer[] $colCosts
     * @return Integer
     */
    function minCost($startPos, $homePos, $rowCosts, $colCosts) {
        $ans = 0;
        $sr = $startPos[0];
        $sc = $startPos[1];
        $hr = $homePos[0];
        $hc = $homePos[1];
        if ($sr < $hr) for ($r = $sr + 1; $r <= $hr; $r++) $ans += $rowCosts[$r];
        else for ($r = $sr - 1; $r >= $hr; $r--) $ans += $rowCosts[$r];
        if ($sc < $hc) for ($c = $sc + 1; $c <= $hc; $c++) $ans += $colCosts[$c];
        else for ($c = $sc - 1; $c >= $hc; $c--) $ans += $colCosts[$c];
        return $ans;
    }
}
