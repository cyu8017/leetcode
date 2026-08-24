<?php
// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution {
    private function maxGap($bars) {
        if (count($bars) === 0) return 1;
        sort($bars);
        $best = 1;
        $cur = 1;
        for ($i = 1; $i < count($bars); $i++) {
            if ($bars[$i] === $bars[$i - 1] + 1) $cur++;
            else $cur = 1;
            if ($cur > $best) $best = $cur;
        }
        return $best + 1;
    }

    function maximizeSquareHoleArea($n, $m, $hBars, $vBars) {
        $side = $this->maxGap($hBars);
        $vs = $this->maxGap($vBars);
        if ($vs < $side) $side = $vs;
        return $side * $side;
    }
}
