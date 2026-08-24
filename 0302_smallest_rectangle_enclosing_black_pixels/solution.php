<?php
// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

class Solution {
    /**
     * @param String[][] $image
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function minArea($image, $x, $y) {
        $rows = count($image);
        $cols = count($image[0]);

        $columnHasBlack = function ($col) use ($image, $rows) {
            for ($row = 0; $row < $rows; $row++) {
                if ($image[$row][$col] === "1") {
                    return true;
                }
            }
            return false;
        };

        $rowHasBlack = function ($row) use ($image, $cols) {
            for ($col = 0; $col < $cols; $col++) {
                if ($image[$row][$col] === "1") {
                    return true;
                }
            }
            return false;
        };

        $left = 0;
        $right = $y;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($columnHasBlack($mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        $leftBound = $left;

        $left = $y;
        $right = $cols - 1;
        while ($left < $right) {
            $mid = intdiv($left + $right + 1, 2);
            if ($columnHasBlack($mid)) {
                $left = $mid;
            } else {
                $right = $mid - 1;
            }
        }
        $rightBound = $left;

        $top = 0;
        $bottom = $x;
        while ($top < $bottom) {
            $mid = intdiv($top + $bottom, 2);
            if ($rowHasBlack($mid)) {
                $bottom = $mid;
            } else {
                $top = $mid + 1;
            }
        }
        $topBound = $top;

        $top = $x;
        $bottom = $rows - 1;
        while ($top < $bottom) {
            $mid = intdiv($top + $bottom + 1, 2);
            if ($rowHasBlack($mid)) {
                $top = $mid;
            } else {
                $bottom = $mid - 1;
            }
        }
        $bottomBound = $top;

        return ($rightBound - $leftBound + 1) * ($bottomBound - $topBound + 1);
    }
}
