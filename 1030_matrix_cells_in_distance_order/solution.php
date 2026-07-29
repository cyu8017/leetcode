<?php
// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution {
    /**
     * @param Integer $rows
     * @param Integer $cols
     * @param Integer $rCenter
     * @param Integer $cCenter
     * @return Integer[][]
     */
    function allCellsDistOrder($rows, $cols, $rCenter, $cCenter) {
        $cells = [];
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                $cells[] = [$r, $c];
            }
        }
        usort($cells, function ($a, $b) use ($rCenter, $cCenter) {
            return (abs($a[0] - $rCenter) + abs($a[1] - $cCenter))
                - (abs($b[0] - $rCenter) + abs($b[1] - $cCenter));
        });
        return $cells;
    }
}
