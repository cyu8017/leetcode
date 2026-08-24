<?php
// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

class Solution {
    function matrixMedian($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $lo = 1;
        $hi = 1000000;
        $need = intdiv($m * $n, 2) + 1;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->countLE($grid, $n, $mid) >= $need) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }

    private function countLE($grid, $n, $x) {
        $cnt = 0;
        foreach ($grid as $row) {
            $l = 0;
            $r = $n;
            while ($l < $r) {
                $mid = ($l + $r) >> 1;
                if ($row[$mid] <= $x) $l = $mid + 1;
                else $r = $mid;
            }
            $cnt += $l;
        }
        return $cnt;
    }
}
