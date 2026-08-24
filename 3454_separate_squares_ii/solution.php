<?php
// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

class Solution {
    function separateSquares($squares) {
        $total = 0;
        foreach ($squares as $sq) {
            $l = $sq[2];
            $total += $l * $l;
        }
        $areaBelow = function($y) use ($squares) {
            $below = 0;
            foreach ($squares as $sq) {
                $yi = $sq[1];
                $l = $sq[2];
                $top = $yi + $l;
                if ($y <= $yi) continue;
                else if ($y >= $top) $below += $l * $l;
                else $below += $l * ($y - $yi);
            }
            return $below;
        };
        $lo = 0.0;
        $hi = 2e9;
        for ($it = 0; $it < 60; $it++) {
            $mid = ($lo + $hi) / 2;
            if ($areaBelow($mid) * 2 < $total) $lo = $mid;
            else $hi = $mid;
        }
        return $hi;
    }
}
