<?php
// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution {
    function largestSquareArea($bottomLeft, $topRight) {
        $ans = 0;
        $n = count($bottomLeft);
        for ($i = 0; $i < $n; $i++) {
            $x1 = $bottomLeft[$i][0];
            $y1 = $bottomLeft[$i][1];
            $x2 = $topRight[$i][0];
            $y2 = $topRight[$i][1];
            for ($j = $i + 1; $j < $n; $j++) {
                $x3 = $bottomLeft[$j][0];
                $y3 = $bottomLeft[$j][1];
                $x4 = $topRight[$j][0];
                $y4 = $topRight[$j][1];
                $ww = min($x2, $x4) - max($x1, $x3);
                $h = min($y2, $y4) - max($y1, $y3);
                $e = min($ww, $h);
                if ($e > 0) $ans = max($ans, $e * $e);
            }
        }
        return $ans;
    }
}
