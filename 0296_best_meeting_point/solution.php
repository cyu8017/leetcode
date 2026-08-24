<?php
// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minTotalDistance($grid) {
        $rows = [];
        $cols = [];
        foreach ($grid as $rowIndex => $row) {
            foreach ($row as $colIndex => $value) {
                if ($value === 1) {
                    $rows[] = $rowIndex;
                    $cols[] = $colIndex;
                }
            }
        }
        sort($cols);
        $rowMedian = $rows[intdiv(count($rows), 2)];
        $colMedian = $cols[intdiv(count($cols), 2)];
        $total = 0;
        foreach ($rows as $row) {
            $total += abs($row - $rowMedian);
        }
        foreach ($cols as $col) {
            $total += abs($col - $colMedian);
        }
        return $total;
    }
}
