<?php
// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

class Solution {
    function checkCut($rects, $axis) {
        $arr = [];
        foreach ($rects as $r) $arr[] = $axis === 0 ? [$r[0], $r[2]] : [$r[1], $r[3]];
        usort($arr, function($x, $y) {
            if ($x[0] === $y[0]) return $x[1] <=> $y[1];
            return $x[0] <=> $y[0];
        });
        $cuts = 0;
        $end = $arr[0][1];
        for ($i = 1; $i < count($arr); $i++) {
            if ($arr[$i][0] >= $end) {
                $cuts++;
                $end = $arr[$i][1];
                if ($cuts >= 2) return true;
            } else if ($arr[$i][1] > $end) {
                $end = $arr[$i][1];
            }
        }
        return false;
    }

    function checkValidCuts($n, $rectangles) {
        return $this->checkCut($rectangles, 0) || $this->checkCut($rectangles, 1);
    }
}
