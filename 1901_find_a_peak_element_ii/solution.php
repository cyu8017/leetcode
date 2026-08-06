<?php
// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

class Solution {
    function findPeakGrid($mat) {
        $rows = count($mat);
        $cols = count($mat[0]);
        $lo = 0;
        $hi = $cols - 1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $maxRow = 0;
            for ($r = 1; $r < $rows; $r++) {
                if ($mat[$r][$mid] > $mat[$maxRow][$mid]) {
                    $maxRow = $r;
                }
            }
            $left = $mid > 0 ? $mat[$maxRow][$mid - 1] : -1;
            $right = $mid + 1 < $cols ? $mat[$maxRow][$mid + 1] : -1;
            if ($mat[$maxRow][$mid] >= $left && $mat[$maxRow][$mid] >= $right) {
                return [$maxRow, $mid];
            }
            if ($left > $mat[$maxRow][$mid]) {
                $hi = $mid - 1;
            } else {
                $lo = $mid + 1;
            }
        }
        return [0, 0];
    }
}
